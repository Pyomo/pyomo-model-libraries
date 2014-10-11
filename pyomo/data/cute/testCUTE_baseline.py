#
# Test the NL writer on a subset of the CUTE test cases
#

import os
from os.path import abspath, dirname

import pyutilib.th as unittest
import pyutilib.subprocess
import pyomo.scripting.pyomo_command as main
from pyomo.core.base import expr as Expr
from pyomo.opt import ProblemFormat
from pyomo.core import *

from pyomo.data.cute import CUTE_classifications as CUTE

currdir = dirname(abspath(__file__))+os.sep

class Tests(unittest.TestCase):
    def pyomo(self, cmd):
        os.chdir(currdir)
        output = main.run(['-q', '-c']+cmd)
        return output

class SmokeBaselineTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)
SmokeBaselineTests = unittest.category('smoke','nightly','expensive')(SmokeBaselineTests)

class ExpensiveBaselineTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)
ExpensiveBaselineTests = unittest.category('expensive')(ExpensiveBaselineTests)

"""
The following test generates an nl file for the test case
and checks that it matches the current pyomo baseline nl file.
"""
@unittest.nottest
def pyomo_baseline_test(self, name):
    if name in CUTE.baseline_skipped_models:
        self.skipTest('Ignoring test '+name)
        return

    self.pyomo(['--save-model='+currdir+name+'.test.nl',
                '--skip-canonical-repn',
                currdir+name+'_cute.py'])

    # Check that the pyomo nl file matches its own baseline    
    self.assertFileEqualsBaseline(currdir+name+'.test.nl', currdir+name+'.pyomo.nl', tolerance=(1e-8, False))

for name in CUTE.smoke_models:
    SmokeBaselineTests.add_fn_test(fn=pyomo_baseline_test, name=name)
for name in CUTE.moderate_models:
    ExpensiveBaselineTests.add_fn_test(fn=pyomo_baseline_test, name=name)
for name in CUTE.expensive_models:
    ExpensiveBaselineTests.add_fn_test(fn=pyomo_baseline_test, name=name)

if __name__ == "__main__":
    unittest.main()
