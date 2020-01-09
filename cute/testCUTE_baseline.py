#
# Test the NL writer on a subset of the CUTE test cases
#

import sys
import os
from os.path import abspath, dirname

import pyutilib.th as unittest
import pyutilib.subprocess
import pyomo.scripting.pyomo_main as main
import pyomo.core.expr.current as Expr
from pyomo.opt import ProblemFormat
from pyomo.core import *

currdir = dirname(abspath(__file__))+os.sep

sys.path.append(currdir)
#from pyomo.data.cute import CUTE_classifications as CUTE
import CUTE_classifications as CUTE
sys.path.pop()


class Tests(unittest.TestCase):
    def pyomo(self, cmd):
        os.chdir(currdir)
        output = main.main(['convert', '--logging=quiet', '-c']+cmd)
        return output

class SmokeBaselineTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)

@unittest.category('expensive')
class ExpensiveBaselineTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)

"""
The following test generates an nl file for the test case
and checks that it matches the current pyomo baseline nl file.
"""
@unittest.nottest
def pyomo_baseline_test(self, name):
    if name in CUTE.baseline_skipped_models:
        self.skipTest('Ignoring test '+name)
        return

    self.pyomo(['--output='+currdir+name+'.test.nl',
                currdir+name+'_cute.py'])

    # Check that the pyomo nl file matches its own baseline
    self.assertFileEqualsBaseline(
        currdir+name+'.test.nl', currdir+name+'.pyomo.nl', tolerance=(1e-8, False))

for name in CUTE.smoke_models:
    SmokeBaselineTests.add_fn_test(fn=pyomo_baseline_test, name=name)
for name in CUTE.moderate_models:
    ExpensiveBaselineTests.add_fn_test(fn=pyomo_baseline_test, name=name)
for name in CUTE.expensive_models:
    ExpensiveBaselineTests.add_fn_test(fn=pyomo_baseline_test, name=name)

if __name__ == "__main__":
    import pyomo.environ
    unittest.main()
