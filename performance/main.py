import argparse
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
from six import iteritems

import pyutilib.th as unittest
import pyomo
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
        if cat not in self._testRecord:
            self._testRecord[cat] = OrderedDict()
        try:
            name = record.msg.obj.name
        except AttributeError:
            name = record.msg.obj.__class__.__name__
        self._testRecord[cat][name] = record.msg.timer


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
        for cat, req in iteritems(self._category):
            if getattr(test.test, cat, 0):
                setattr(test.test, cat, req)
        self._timer.tic("")

    def afterTest(self, test):
        test.test.testdata['test_time'] = self._timer.toc("")
        test.test.testdata = None
        self._timingHandler.clearTest()


def getPyomoInfo():
    cwd = os.getcwd()
    try:
        os.chdir(os.path.dirname(pyomo.__file__))
        sha = os.popen('git rev-parse HEAD').read().strip()
        diffs = os.popen('git diff-index --name-only HEAD').read()
        diffs = diffs.strip().split()
        branch = os.popen('git symbolic-ref -q --short HEAD').read().strip()
    finally:
        os.chdir(cwd)
    return {'branch':branch, 'sha':sha, 'diffs':diffs}


def getRunInfo():
    info = {
        'time': time.time(),
        'python': [platform.python_implementation()] + list(sys.version_info),
        'platform': platform.system(),
        'hostname': platform.node(),
    }
    info.update(getPyomoInfo())
    return info


def run_tests(argv):
    results = ( getRunInfo(), OrderedDict() )
    recorder = DataRecorder(results[1])
    nose.core.run(argv=argv, addplugins=[recorder])
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
        help='Store the test results to the specified file'
    )
    parser.add_argument(
        '-n', '--replicates',
        action='store',
        dest='replicates',
        type=int,
        default=1,
        help='Number of replicates to run'
    )

    options, argv = parser.parse_known_args(argv)
    if options.output:
        ostream = open(options.output, 'w')
        close_ostream = True
    else:
        ostream = sys.stdout
        close_ostream = False

    try:
        results = tuple(run_tests(argv) for i in range(options.replicates))
        results = (results[0][0],) + tuple(r[1] for r in results)
        # Note: explicitly specify sort_keys=False so that ujson
        # preserves the OrderedDict keys in the JSON
        json.dump(results, ostream, indent=2, sort_keys=False)
    finally:
        if close_ostream:
            ostream.close()


if __name__ == '__main__':
    main(sys.argv)
