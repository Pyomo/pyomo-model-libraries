import os

import pyomo.common.unittest as unittest

from pyomo.common.timing import TicTocTimer
from pyomo.environ import *
from pyomo.dae import *

_dir = os.path.dirname(__file__)

@unittest.pytest.mark.performance
class TestStochPDEgas(unittest.TestCase):

    def recordData(self, name, value):
        """A method for recording data associated with a test.  This method is only
           meaningful when running this TestCase with 'nose', using the TestData plugin.
        """
        tmp = getattr(self, 'testdata', None)
        if not tmp is None:
            tmp[name] = value

    def test_stochpdegas_automatic(self):
        timer = TicTocTimer()
        from .distill_DAE import create_instance
        instance = create_instance()
        self.recordData('create_instance', timer.toc('create_instance'))


if __name__ == '__main__':
    import sys
    from pyomo.common.fileutils import this_file_dir
    sys.path.insert(0, os.path.dirname(this_file_dir()))
    __package__ = os.path.basename(this_file_dir())
    unittest.main()
