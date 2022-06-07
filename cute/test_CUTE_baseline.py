#
# Test the NL writer on a subset of the CUTE test cases
#

from itertools import zip_longest
import sys
import os

import pyomo.common.unittest as unittest
import pyomo.scripting.pyomo_main as main
from pyomo.common.dependencies import attempt_import
from pyomo.common.fileutils import this_file_dir
from pyomo.common.tempfiles import TempfileManager

# Ensure plugins are registered
import pyomo.environ

parameterized, param_available = attempt_import('parameterized')
if not param_available:
    raise unittest.SkipTest('Parameterized is not available.')

currdir = this_file_dir()

try:
    from pyomo.repn.tests.ampl.nl_diff import load_and_compare_nl_baseline
except ImportError:
    # Backwards compatibility: fallback to the previous differ
    # TODO: This can be removed after the NL Writer v2 has been merged
    def load_and_compare_nl_baseline(base, test):
        # Check that the pyomo nl file matches its own baseline
        with open(test, 'r') as f1, open(base, 'r') as f2:
            f1_contents = list(
                filter(None, f1.read().replace('n', 'n ').split()))
            f2_contents = list(
                filter(None, f2.read().replace('n', 'n ').split()))
            for item1, item2 in zip_longest(f1_contents, f2_contents):
                try:
                    self.assertAlmostEqual(
                        float(item1.strip()), float(item2.strip()))
                except:
                    self.assertEqual(item1, item2)

try:
    sys.path.insert(0, currdir)
    import CUTE_classifications as CUTE
finally:
    sys.path.remove(currdir)

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
        return main.main(['convert', '--logging=quiet', '-c'] + cmd)

    def pyomo_baseline(self, name):
        if name in CUTE.baseline_skipped_models:
            self.skipTest('Ignoring test '+name)
            return

        source = os.path.join(currdir, name + '_cute.py')
        with TempfileManager:
            result = TempfileManager.create_tempfile(suffix='.test.nl')
            self.pyomo(['--output=' + result, source])

            self.assertEqual(*load_and_compare_nl_baseline(
                os.path.join(currdir, name + '.pyomo.nl'),
                result))


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
    unittest.main()
