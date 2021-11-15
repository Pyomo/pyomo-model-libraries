import argparse
import gc
import logging
import nose
import os
import platform
import sys
import time
try:
    import ujson as json
except ImportError:
    import json

from collections import OrderedDict

import pyomo.common.unittest as unittest
import pyomo
from pyomo.version import version_info as pyomo_version
from pyomo.common.timing import TicTocTimer, report_timing

class TimingHandler(logging.Handler):
    def __init__(self):
        super(TimingHandler, self).__init__()
        self._testRecord = None
        self.enabled = True

    def setTest(self, testRecord):
        self._testRecord = testRecord['timing'] = OrderedDict()

    def clearTest(self):
        self._testRecord = None

    def emit(self, record):
        if self._testRecord is None:
            return
        cat = record.msg.__class__.__name__
        if cat in self._testRecord:
            _cat = self._testRecord[cat]
        else:
            _cat = self._testRecord[cat] = OrderedDict()
        try:
            name = record.msg.obj.name
        except AttributeError:
            name = record.msg.obj.__class__.__name__
        if name in _cat:
            _val = _cat[name]
            if type(_val) is not list:
                _val = [_val]
            _val.append(record.msg.timer)
        else:
            _val = record.msg.timer
        _cat[name] = _val


class DataRecorder(nose.plugins.base.Plugin):
    enabled = True

    def __init__(self, data):
        super(DataRecorder, self).__init__()
        self._data = data
        self._timingHandler = None
        self._timer = TicTocTimer()
        self._category = {}

    def configure(self, options, conf):
        super(DataRecorder, self).configure(options, conf)
        self.attribPlugin = next( x for x in conf.plugins
                                  if hasattr(x, 'validateAttrib') )
        self.enabled = True

    def begin(self):
        # Set up the interception of the timing reports
        self._timingHandler = TimingHandler()
        timing_logger = logging.getLogger('pyomo.common.timing')
        timing_logger.setLevel(logging.INFO)
        timing_logger.addHandler(self._timingHandler)
        # Determine and remember the "status" of all key categories.  If
        # the user did not specify any categories, then they all will
        # remain enabled.  However, if the user specified any
        # categories, then disable the ones that the user did NOT
        # request.
        for cat in ('nl','lp','bar','gams'):
            if not self.attribPlugin.enabled:
                self._category[cat] = True
                continue
            @unittest.category(cat, 'performance', 'long', 'short', 'devel')
            class tmp(unittest.TestCase):
                def test(self):
                    pass
            req = self.attribPlugin.validateAttrib(tmp.test, tmp)
            self._category[cat] = req is not False

    def beforeTest(self, test):
        addr = test.address()
        try:
            addr = addr[1]+":"+addr[2]
        except:
            addr = test.id()
        test.test.testdata = self._data[addr] = OrderedDict()
        self._timingHandler.setTest(test.test.testdata)
        # disable any categories we are not interested in
        for cat, req in self._category.items():
            if getattr(test.test, cat, 0):
                setattr(test.test, cat, req)
        # Trigger garbage collection (try and get a "clean" environment)
        gc.collect()
        gc.collect()
        self._timer.tic("")

    def afterTest(self, test):
        test.test.testdata['test_time'] = self._timer.toc("")
        test.test.testdata = None
        self._timingHandler.clearTest()


def getPyomoInfo():
    cwd = os.getcwd()
    sha = None
    diffs = []
    branch = None
    try:
        os.chdir(os.path.dirname(pyomo.__file__))
        sha = os.popen('git rev-parse HEAD').read().strip()
        diffs = os.popen('git diff-index --name-only HEAD').read()
        diffs = diffs.strip().split()
        branch = os.popen('git symbolic-ref -q --short HEAD').read().strip()
    finally:
        os.chdir(cwd)
    return { 'branch':branch, 'sha':sha, 'diffs':diffs,
             'pyomo_version': pyomo_version }


def getRunInfo(cython):
    info = {
        'time': time.time(),
        'python_implementation': platform.python_implementation(),
        'python_version': tuple(sys.version_info),
        'python_build': platform.python_build(),
        'platform': platform.system(),
        'hostname': platform.node(),
    }
    if info['python_implementation'].lower() == 'pypy':
        info['pypy_version'] = tuple(sys.pypy_version_info)
    if cython:
        import Cython
        info['cython'] = tuple(int(x) for x in Cython.__version__.split('.'))
    info.update(getPyomoInfo())
    return info


def run_tests(cython, argv):
    gc.collect()
    gc.collect()
    results = ( getRunInfo(cython), OrderedDict() )
    recorder = DataRecorder(results[1])
    nose.core.run(argv=argv, addplugins=[recorder])
    gc.collect()
    gc.collect()
    return results


def main(argv):
    parser = argparse.ArgumentParser(
        epilog="Remaining arguments are passed to nosetests"
    )
    parser.add_argument(
        '-o', '--output',
        action='store',
        dest='output',
        default=None,
        help='Store the test results to the specified file.'
    )
    parser.add_argument(
        '-d', '--dir',
        action='store',
        dest='output_dir',
        default=None,
        help='Store the test results in the specified directory.  If -o '
        'is not specified, then a file name is automatically generated '
        'based on the git branch and hash.'
    )
    parser.add_argument(
        '-n', '--replicates',
        action='store',
        dest='replicates',
        type=int,
        default=1,
        help='Number of replicates to run.'
    )
    parser.add_argument(
        '--with-cython',
        action='store_true',
        dest='cython',
        help='Cythonization enabled.'
    )

    options, argv = parser.parse_known_args(argv)
    cython = options.cython
    results = tuple(run_tests(cython, argv) for i in range(options.replicates))
    results = (results[0][0],) + tuple(r[1] for r in results)

    if options.output_dir:
        if not options.output:
            options.output = 'perf-%s-%s-%s-%s.json' % (
                results[0]['branch'],
                results[0]['sha'][:7] + (
                    '_mod' if results[0]['diffs'] else ''),
                results[0]['python_implementation'].lower() + (
                    '.'.join(str(i) for i in results[0]['python_version'][:3])),
                time.strftime('%y%m%d:%H%M', time.gmtime())
            )
        options.output = os.path.join(options.output_dir, options.output)
    if options.output:
        print(f"Writing results to {options.output}")
        ostream = open(options.output, 'w')
        close_ostream = True
    else:
        ostream = sys.stdout
        close_ostream = False
    try:
        # Note: explicitly specify sort_keys=False so that ujson
        # preserves the OrderedDict keys in the JSON
        json.dump(results, ostream, indent=2, sort_keys=False)
    finally:
        if close_ostream:
            ostream.close()
    print("Performance run complete.")

if __name__ == '__main__':
    main(sys.argv)
