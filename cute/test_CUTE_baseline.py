#
# Test the NL writer on a subset of the CUTE test cases
#

from itertools import zip_longest
import sys
import os
from os.path import abspath, dirname, join

import pyomo.common.unittest as unittest
import pyomo.scripting.pyomo_main as main
import pyomo.core.expr.current as Expr
from pyomo.opt import ProblemFormat
from pyomo.core import *
import pyomo.common

currdir = dirname(abspath(__file__))+os.sep

parameterized, param_available = pyomo.common.dependencies.attempt_import('parameterized')
if not param_available:
    raise unittest.SkipTest('Parameterized is not available.')

sys.path.append(currdir)
#from pyomo.data.cute import CUTE_classifications as CUTE
import CUTE_classifications as CUTE
sys.path.pop()

smoke = []
for name in CUTE.smoke_models:
    smoke.append(name)

expensive = []
for name in CUTE.moderate_models:
    expensive.append(name)
for name in CUTE.expensive_models:
    expensive.append(name)


class Tests(unittest.TestCase):
    def pyomo(self, cmd):
        os.chdir(currdir)
        output = main.main(['convert', '--logging=quiet', '-c']+cmd)
        return output
    def pyomo_baseline(self, name):
        if name in CUTE.baseline_skipped_models:
            self.skipTest('Ignoring test '+name)
            return

        self.pyomo(['--output='+currdir+name+'.test.nl',
                    currdir+name+'_cute.py'])

        # Check that the pyomo nl file matches its own baseline
        test, base = join(currdir, name+'.test.nl'), join(currdir, name+'.pyomo.nl')
        with open(test, 'r') as f1, open(base, 'r') as f2:
            f1_contents = list(filter(None, f1.read().replace('n', 'n ').split()))
            f2_contents = list(filter(None, f2.read().replace('n', 'n ').split()))
            for item1, item2 in zip_longest(f1_contents, f2_contents):
                try:
                    self.assertAlmostEqual(float(item1.strip()), float(item2.strip()))
                except:
                    self.assertEqual(item1, item2)


class SmokeBaselineTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)

    @parameterized.parameterized.expand(input=smoke)
    def test_pyomo_baseline_smoke(self, name):
        self.pyomo_baseline(name)


@unittest.pytest.mark.expensive
class ExpensiveBaselineTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)

    """
    The following test generates an nl file for the test case
    and checks that it matches the current pyomo baseline nl file.
    """
    @parameterized.parameterized.expand(input=expensive)
    def test_pyomo_baseline_expensive(self, name):
        self.pyomo_baseline(name)


if __name__ == "__main__":
    import pyomo.environ
    unittest.main()
