import os

import pyomo.common.unittest as unittest

from pyomo.common.timing import TicTocTimer
from pyomo.environ import *
from pyomo.dae import *

_dir = os.path.dirname(__file__)

from pyomo.contrib.pynumero.algorithms.solvers.cyipopt_solver import (
    cyipopt_available,
)

@unittest.pytest.mark.performance
@unittest.skipUnless(cyipopt_available, "CyIpopt is not available")
class TestImplicitDistill(unittest.TestCase):

    _predicted_results = {
        "u1[1]": 3.0,
        "u1[2]": 1.0,
        "u1[3]": 1.0,
        "u1[4]": 1.0,
        "u1[5]": 1.0,
        "u1[6]": 1.0,
        "u1[7]": 1.000000000894782,
        "u1[8]": 1.0000001521950732,
        "u1[9]": 1.1623645619362053,
        "u1[10]": 1.3172203610288866,
        "u1[11]": 1.4501249165622068,
        "u1[12]": 1.5616919180444544,
        "u1[13]": 1.6535269384632936,
        "u1[14]": 1.7279135986010443,
        "u1[15]": 1.7874071166551058,
        "u1[16]": 1.8345254556710076,
        "u1[17]": 1.8715664136378687,
        "u1[18]": 1.900524442000351,
        "u1[19]": 1.9230723526888294,
        "u1[20]": 1.9405795753127466,
        "u1[21]": 1.954147687752178,
        "u1[22]": 1.9646514781090727,
        "u1[23]": 1.9727790642832834,
        "u1[24]": 1.9790679419304176,
        "u1[25]": 1.9839358036166106,
        "u1[26]": 1.987706049586084,
        "u1[27]": 1.990628440391752,
        "u1[28]": 1.9928955539673907,
        "u1[29]": 1.9946557490664876,
        "u1[30]": 1.9960232900793193,
        "u1[31]": 1.9970862048604325,
        "u1[32]": 1.997912354477815,
        "u1[33]": 1.9985541054206861,
        "u1[34]": 1.999051916788678,
        "u1[35]": 1.9994370891585196,
        "u1[36]": 1.9997338678771428,
        "u1[37]": 1.9999610501879141,
        "u1[38]": 2.000133211258838,
        "u1[39]": 2.0002616372545323,
        "u1[40]": 2.0003550326522737,
        "u1[41]": 2.0004200528631024,
        "u1[42]": 2.0004617009821075,
        "u1[43]": 2.0004836185973205,
        "u1[44]": 2.0004882949451854,
        "u1[45]": 2.000477217021499,
        "u1[46]": 2.0004509878661367,
        "u1[47]": 2.000409457215106,
        "u1[48]": 2.0003519538618404,
        "u1[49]": 2.000277826301352,
        "u1[50]": 2.0001878222716396,
        "u1[51]": 2.000087833075182,
    }

    def recordData(self, name, value):
        """A method for recording data associated with a test.  This method is only
           meaningful when running this TestCase with 'nose', using the TestData plugin.
        """
        tmp = getattr(self, 'testdata', None)
        if not tmp is None:
            tmp[name] = value

    def test_implicit_distill(self):
        timer = TicTocTimer()
        from .distill_DAE import (
            create_instance,
            setup_implicit,
            solve,
        )
        instance = create_instance()
        self.recordData('create_instance', timer.toc('create_instance'))
        implicit_instance = setup_implicit(instance)
        self.recordData('setup_implicit', timer.toc('setup_implicit'))
        results = solve(implicit_instance)
        self.recordData('solve', timer.toc('solve'))

        sol_data = {
            name: instance.find_component(name).value
            for name in self._predicted_results
        }
        self.assertStructuredAlmostEqual(
            self._predicted_results,
            sol_data,
            delta=1e-5,
        )
        self.recordData('check_results', timer.toc('check_results'))


if __name__ == '__main__':
    import sys
    from pyomo.common.fileutils import this_file_dir
    sys.path.insert(0, os.path.dirname(this_file_dir()))
    __package__ = os.path.basename(this_file_dir())
    unittest.main()
