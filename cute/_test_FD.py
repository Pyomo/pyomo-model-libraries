#
# Test the conversion to FD
#

import os
from os.path import abspath, dirname

currdir = dirname(abspath(__file__))+os.sep

import pyutilib.th as unittest
from pyomo.core import *
import pyutilib.misc
import pyomo.openopt

from pyomo.data.cute import CUTE_classifications as CUTE

FD_available=False
try:
    import FuncDesigner
    FD_available=True
except:
    pass

@unittest.category('expensive')
class ExpensiveTests(unittest.TestCase):
    pass

@unittest.category('smoke', 'nightly', 'expensive')
class SmokeTests(unittest.TestCase):
    pass


#skip_files = set(['aircrfta', 'artif', 'booth','chemrctb', 'core1','corkscrw', 'eg1','eg2','eg3', 'drcav3lq', 'dtoc1l', 'expfit', 'tfi2','synthes1', 'sosqp1', 's368', 'robot', 'oet1', 'makela3', 'polak1', 'tame', 'mifflin2', 'mifflin1', 'makela4', 'makela2', 'makela1', 'extrasim', 'demymalo', 'chaconn2', 'chaconn1', 'bt1'])
#smoke_files = set( ['bqp1var', 'explin', 'extrasim', 'tame', 'sim2bqp', 'denschna', 'rosenbr', 'bt10', 'sisser', 'denschnb', 'eg1', 'mifflin1', 'makela1', 'bt1', 'denschnc', 'demymalo', 'zy2', 'mifflin2', 'polak1', 'bt9', 'byrdsphr', 'makela2', 'bt2', 'camel6', 'aljazzaf', 'chaconn1', 'chaconn2', 'csfi2', 'bt13', 'cantilvr', 'bt3', 'cb2', 'cb3', 'makela4', 'matrix2'])


@unittest.nottest
def fd_test(self, name):

    if FD_available is False:
        self.skipTest('FuncDesigner module is not available')
        return
    #if name in skip_files:
    #    unittest.skip('Ignoring test '+name)
    #    return

    # all CUTE models implicitly create a concrete instance within the model file
    instance = pyutilib.misc.import_file(currdir+name+'_cute.py').model

    pvals = {}
    for obj in instance.component_data_objects(Objective, active=True):
        fname = obj.name
        pvals[fname] = obj
        break
    #
    S = pyomo.openopt.Pyomo2FuncDesigner(instance)
    oval = S.f(S.initial_point)
    self.assertAlmostEqual(pvals[fname], oval, places=7)

for name in CUTE.smoke_models:
    SmokeTests.add_fn_test(fn=fd_test, name=name)
for name in CUTE.moderate_models:
    ExpensiveTests.add_fn_test(fn=fd_test, name=name)
for name in CUTE.expensive_models:
    ExpensiveTests.add_fn_test(fn=fd_test, name=name)


if __name__ == "__main__":
    unittest.main()
