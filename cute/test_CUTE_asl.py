#
# Test the NL writer on a subset of the CUTE test cases
#

import shutil
import sys
import subprocess
import os
import warnings
import json

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


# https://github.com/ghackebeil/gjh_asl_json
has_gjh_asl_json = False
if os.system(['gjh_asl_json', '-v']) == 0:
    has_gjh_asl_json = True


class Tests(unittest.TestCase):
    # These two lines can be removed after we finish the PyUtilib divorce
    pyutilib_th = 1
    pyomo_unittest = 1
    def pyomo(self, cmd):
        os.chdir(currdir)
        output = main.main(['convert', '--logging=quiet', '-c']+cmd)
        return output

    def pyomo_asl(self, name):
        if name in CUTE.asl_skipped_models:
            self.skipTest('Ignoring test ' + name)
            return
        if not has_gjh_asl_json:
            self.skipTest("'gjh_asl_json' executable not available")
            return

        with TempfileManager:
            tmpdir = TempfileManager.create_tempdir()
            self._pyomo_asl_impl(name, tmpdir)

    def _pyomo_asl_impl(self, name, tmpdir):
        source = os.path.join(currdir, name + '_cute.py')
        nl = os.path.join(tmpdir, name + '.test.nl')
        main.main([
            'convert', '--logging=quiet', '-c',
            '--output=' + nl,
            '--symbolic-solver-labels',
            source,
        ])

        # obtain the pyomo-generated nl file summary information for
        # comparison with ampl
        cmd = [
            'gjh_asl_json', nl,
            'rows=' + os.path.join(tmpdir, name + '.test.row'),
            'cols=' + os.path.join(tmpdir, name + '.test.col'),
        ]
        p = subprocess.run(
            cmd,
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(p.returncode, 0, msg=p.stdout)

        # obtain the ampl-generated nl file summary information for
        # comparison with pyomo
        #
        # Note: gjh_asl_json writes the JSON to the same directory as
        # the source.  We will copy the sources into the temporary
        # directory before running it (in case the source dir is not
        # writable).
        for ext in ('nl', 'row', 'col'):
            shutil.copyfile(os.path.join(currdir, name + '.ampl.' + ext),
                            os.path.join(tmpdir, name + '.ampl.' + ext))
        cmd = [
            'gjh_asl_json',
            os.path.join(tmpdir, name + '.ampl.nl'),
            'rows=' + os.path.join(tmpdir, name + '.ampl.row'),
            'cols=' + os.path.join(tmpdir, name + '.ampl.col'),
        ]
        p = subprocess.run(
            cmd,
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(p.returncode, 0, msg=p.stdout)
        with open(os.path.join(tmpdir, name + '.test.json'), 'r') as f:
            pyomo_res = json.load(f)
        with open(os.path.join(tmpdir, name + '.ampl.json'), 'r') as f:
            ampl_res = json.load(f)
        try:
            self.assertStructuredAlmostEqual(
                pyomo_res, ampl_res, abstol=1e-14, reltol=1e-7)
            return
        except AssertionError:
            pass

        # Make sure this is not a simple case of Pyomo/AMPL moving
        # constants in the constraint body to the upper/lower bound
        del ampl_res["constraint bounds"]
        del pyomo_res["constraint bounds"]
        del ampl_res["initial evaluations"]["constraints"]
        del pyomo_res["initial evaluations"]["constraints"]
        self.assertStructuredAlmostEqual(
            pyomo_res, ampl_res, abstol=1e-14, reltol=1e-7)
        # If the json files match at this point, it is
        # almost entirely certain that the difference had to
        # do with one of AMPL or Pyomo moving a fixed part
        # of the constraint body from the body to the bounds
        warnings.warn('asl comparison was relaxed for model '+name)


class SmokeASLTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)

    @parameterized.parameterized.expand(input=smoke)
    def test_pyomo_asl_smoke(self, name):
        self.pyomo_asl(name)


@unittest.pytest.mark.expensive
class ExpensiveASLTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)

    #
    # The following test calls the gjh_asl_json executable to
    # generate JSON files corresponding to both the
    # AMPL-generated nl file and the Pyomo-generated nl
    # file. The JSON files are then diffed using the pyutilib.th
    # test class method assertMatchesJsonBaseline()
    #
    @parameterized.parameterized.expand(input=expensive)
    def test_pyomo_asl_expensive(self, name):
        self.pyomo_asl(name)


if __name__ == "__main__":
    unittest.main()
