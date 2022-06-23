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

from pyomo.common.dependencies import attempt_import
from pyomo.common.fileutils import this_file_dir, import_file
from pyomo.common.tempfiles import TempfileManager

# Ensure plugins are registered
import pyomo.environ
from pyomo.opt import WriterFactory

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
        with open(base, 'r') as f1, open(test, 'r') as f2:
            f1_contents = list(
                filter(None, f1.read().replace('n', 'n ').split()))
            f2_contents = list(
                filter(None, f2.read().replace('n', 'n ').split()))
        for i, item1 in enumerate(f1_contents):
            try:
                # mock up assertAlmostEqual:
                if abs(float(item1) - float(f2_contents[i])) <= 1e-7:
                    f2_contents[i] = item1
            except:
                pass
        # for item1, item2 in zip_longest(f1_contents, f2_contents):
        #     try:
        #         self.assertAlmostEqual(
        #             float(item1.strip()), float(item2.strip()))
        #     except:
        #         self.assertEqual(item1, item2)
        return f1_contents, f2_contents

try:
    sys.path.insert(0, currdir)
    import CUTE_classifications as CUTE
finally:
    sys.path.remove(currdir)

smoke = list(CUTE.smoke_models)
expensive = list(CUTE.moderate_models)
expensive.extend(CUTE.expensive_models)

# https://github.com/ghackebeil/gjh_asl_json
has_gjh_asl_json = False
if os.system('gjh_asl_json -v') == 0:
    has_gjh_asl_json = True

# Prevent the module cache from persisting past the end of testing this module
def tearDownModule():
    Driver._model_cache.clear()


class Driver(object):
    # These two lines can be removed after we finish the PyUtilib divorce
    pyutilib_th = 1
    pyomo_unittest = 1

    _nl_version = 'nl' if WriterFactory('nl_v1') is None else 'nl_v1'
    _model_cache = {}

    def create_nl_file(self, source, result, symbolic):
        # This module creates models up to 4 times.  Caching the models
        # saves significant time by avoiding repeated work.
        if source in self._model_cache:
            m = self._model_cache[source]
        else:
            module = import_file(source)
            m = module.model
            if not m.is_constructed():
                m = m.create_instance()
            self._model_cache[source] = m
        
        m.write(
            result,
            format=self._nl_version,
            io_options={
                'symbolic_solver_labels': symbolic,
                'file_determinism': 2 if self._nl_version == 'nl_v2' else 1,
            }
        )

    def pyomo_baseline(self, name):
        """Compare against a cached NL baseline file

        The following test generates an nl file for the test case and
        checks that it matches the current pyomo baseline nl file.

        """
        if name in CUTE.baseline_skipped_models:
            self.skipTest('Ignoring test '+name)
            return

        source = os.path.join(currdir, name + '_cute.py')
        with TempfileManager:
            result = TempfileManager.create_tempfile(suffix='.test.nl')
            self.create_nl_file(source, result, False)
            try:
                baseline = os.path.join(currdir, name + '.pyomo.nl')
                self.assertEqual(*load_and_compare_nl_baseline(
                    baseline, result, self._nl_version
                ))
            except:
                os.system(f"cp {result} {baseline}.new")
                raise

    def pyomo_asl(self, name):
        """Compare NL files using gjh_asl_json

        The following test calls the gjh_asl_json executable to generate
        JSON files corresponding to both the cached AMPL-generated nl
        file and a freshly-generated Pyomo-generated nl file. The JSON
        files are then compared with reasonable numerical tolerances.

        """
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
        self.create_nl_file(source, nl, True)

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
        warnings.warn('asl comparison was relaxed for model ' + name)


class SmokeASLTests_v1(Driver, unittest.TestCase):
    @parameterized.parameterized.expand(input=smoke)
    def test_pyomo_asl_smoke(self, name):
        self.pyomo_asl(name)


@unittest.pytest.mark.expensive
class ExpensiveASLTests_v1(Driver, unittest.TestCase):
    @parameterized.parameterized.expand(input=expensive)
    def test_pyomo_asl_expensive(self, name):
        self.pyomo_asl(name)


class SmokeBaselineTests_v1(Driver, unittest.TestCase):
    @parameterized.parameterized.expand(input=smoke)
    def test_pyomo_baseline_smoke(self, name):
        self.pyomo_baseline(name)


@unittest.pytest.mark.expensive
class ExpensiveBaselineTests_v1(Driver, unittest.TestCase):
    @parameterized.parameterized.expand(input=expensive)
    def test_pyomo_baseline_expensive(self, name):
        self.pyomo_baseline(name)

#
# Explicitly test the NL_v2 writer, if present
#
@unittest.skipIf(WriterFactory('nl_v2') is None, "Requires nl_v2 writer")
class SmokeASLTests_v2(SmokeASLTests_v1):
    _nl_version = 'nl_v2'

@unittest.pytest.mark.expensive
@unittest.skipIf(WriterFactory('nl_v2') is None, "Requires nl_v2 writer")
class ExpensiveASLTests_v2(ExpensiveASLTests_v1):
    _nl_version = 'nl_v2'

@unittest.skipIf(WriterFactory('nl_v2') is None, "Requires nl_v2 writer")
class SmokeBaselineTests_v2(SmokeBaselineTests_v1):
    _nl_version = 'nl_v2'

@unittest.pytest.mark.expensive
@unittest.skipIf(WriterFactory('nl_v2') is None, "Requires nl_v2 writer")
class ExpensiveBaselineTests_v2(ExpensiveBaselineTests_v1):
    _nl_version = 'nl_v2'

if __name__ == "__main__":
    unittest.main()
