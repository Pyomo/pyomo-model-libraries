#
# Tests driven by test_baselines.yml
#

import os
import sys
from os.path import abspath, dirname
currdir = dirname(abspath(__file__))+os.sep

import pyutilib.th as unittest
import pyutilib.autotest
import pyomo.modeling

pyutilib.autotest.create_test_suites(filename=currdir+'test_baselines.yml', _globals=globals())

if __name__ == "__main__":
    unittest.main()
