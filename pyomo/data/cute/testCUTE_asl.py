#
# Test the NL writer on a subset of the CUTE test cases
#

import os
from os.path import abspath, dirname
import warnings
has_json = False
try:
    import json
    has_json = True
except:
    pass

import pyutilib.th as unittest
import pyutilib.subprocess
import pyomo.scripting.pyomo_main as main
from pyomo.core.base import expr as Expr
from pyomo.opt import ProblemFormat
from pyomo.core import *

from pyomo.data.cute import CUTE_classifications as CUTE

currdir = dirname(abspath(__file__))+os.sep

has_asl_test = False
if os.system('asl_test -v') == 0:
    has_asl_test = True

class Tests(unittest.TestCase):

    def pyomo(self, cmd):
        os.chdir(currdir)
        output = main.main(['convert', '--logging=quiet', '-c']+cmd)
        return output

class SmokeASLTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)
SmokeASLTests = unittest.category('smoke','nightly','expensive')(SmokeASLTests)

class ExpensiveASLTests(Tests):
    def __init__(self, *args, **kwds):
        Tests.__init__(self, *args, **kwds)
ExpensiveASLTests = unittest.category('expensive')(ExpensiveASLTests)

"""
The following test calls the asl_test executable to generate JSON
files corresponding to both the AMPL-generated nl file and the
Pyomo-generated nl file. The JSON files are then diffed using the
pyutilib.th test class method assertMatchesJsonBaseline()
"""
@unittest.nottest
def pyomo_asl_test(self, name):
    if name in CUTE.asl_skipped_models:
        self.skipTest('Ignoring test '+name)
        return
    if has_asl_test is False:
        self.skipTest('asl_test executable not available')
        return
    if has_json is False:
        self.skipTest('JSON module not available')
        return
    self.pyomo(['--output='+currdir+name+'.test.nl',
                '--symbolic-solver-labels',
                '--skip-canonical-repn',
                currdir+name+'_cute.py'])

    # compare AMPL and Pyomo nl file structure
    #########################################
    try:
        os.remove(currdir+'stub.json')
    except Exception:
        pass
    try:
        os.remove(currdir+'stub.test.json')
    except Exception:
        pass

    # obtain the nl file summary information for comparison with ampl
    p = pyutilib.subprocess.run(
        'asl_test '+currdir+name+'.test.nl rows='
        +currdir+name+'.test.row cols='+currdir+name+'.test.col')
    self.assertTrue(p[0] == 0, msg=p[1])
    os.rename(currdir+'stub.json',currdir+'stub.test.json')
    # obtain the nl file summary information for comparison with pyomo
    p = pyutilib.subprocess.run(
        'asl_test '+currdir+name+'.ampl.nl rows='
        +currdir+name+'.ampl.row cols='+currdir+name+'.ampl.col')
    self.assertTrue(p[0] == 0, msg=p[1])
    try:
        self.assertMatchesJsonBaseline(
            currdir+'stub.test.json', currdir+'stub.json', tolerance=1e-6)
    except AssertionError:
        # Make sure this is not a simple case of Pyomo/AMPL moving
        # constants in the constraint body to the upper/lower bound
        f = open(currdir+'stub.json','r')
        ampl_res = json.load(f)
        f.close()
        f = open(currdir+'stub.test.json','r')
        pyomo_res = json.load(f)
        f.close()
        del ampl_res["constraint bounds"]
        del pyomo_res["constraint bounds"]
        del ampl_res["initial evaluations"]["constraints"]
        del pyomo_res["initial evaluations"]["constraints"]
        f = open(currdir+'stub.json','w')
        json.dump(ampl_res,f,indent=2)
        f.close()
        f = open(currdir+'stub.test.json','w')
        json.dump(pyomo_res,f,indent=2)
        f.close()
        self.assertMatchesJsonBaseline(
            currdir+'stub.test.json', currdir+'stub.json', tolerance=1e-6)
        # If the json files match at this point, it is almost entirely
        # certain that the difference had to do with one of AMPL or
        # Pyomo moving constraint body from the body to the constraint
        # bounds
        warnings.warn('asl comparison was relaxed for model '+name)
    os.remove(currdir+'stub.json')

    # delete temporary test files
    os.remove(currdir+name+'.test.col')
    os.remove(currdir+name+'.test.row')
    os.remove(currdir+name+'.test.nl')
    ##########################################

for name in CUTE.smoke_models:
    SmokeASLTests.add_fn_test(fn=pyomo_asl_test, name=name)
for name in CUTE.moderate_models:
    ExpensiveASLTests.add_fn_test(fn=pyomo_asl_test, name=name)
for name in CUTE.expensive_models:
    ExpensiveASLTests.add_fn_test(fn=pyomo_asl_test, name=name)

if __name__ == "__main__":
    import pyomo.environ
    unittest.main()
