# Register custom pytest plugin

import gc
import logging
import os
import platform
import sys
import time
try:
    import ujson as json
except ImportError:
    import json

from collections import OrderedDict

import pyomo
import pyomo.common.unittest as unittest
from pyomo.common.timing import TicTocTimer, report_timing
from pyomo.version import version_info as pyomo_version


def getRunInfo(pytestconfig):
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
    if pytestconfig.getoption('--with-cython'):
        import Cython
        info['cython'] = tuple(int(x) for x in Cython.__version__.split('.'))
    info.update(getPyomoInfo())
    return info

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
    return { 'branch': branch, 'sha': sha, 'diffs': diffs,
             'pyomo_version': pyomo_version }


class TimingHandler(logging.Handler):
    def __init__(self):
        super().__init__()
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


def pytest_addoption(parser):
    """
    Add another parser option to specify suite of solver tests to run
    """
    group = parser.getgroup('performance', 'Report performance tests results.')
    group.addoption(
        '--json',
        action='store',
        dest='json_path',
        default=None,
        help='Save test results in a JSON at specified path.'
    )
    group.addoption(
        '--replicates',
        action='store',
        dest='replicates',
        type=int,
        default=1,
        help='Number of replicates to run.'
    )
    group.addoption(
        '--with-cython',
        action='store_true',
        dest='cython',
        help='Cythonization enabled.'
    )

def pytest_configure(config):
    """
    Register additional solver marker, as applicable.
    This stops pytest from printing a warning about unregistered solver options.
    """
    config.addinivalue_line(
        "markers", "performance(name): mark performance test category"
    )
