import os
import six

import pyomo.common.unittest as unittest

try:
    from pyomo.common.dependencies import numpy_available
except ImportError:
    try:
        import numpy
        numpy_available = True
    except ImportError:
        numpy_available = False

from pyomo.common.timing import TicTocTimer
from pyomo.opt import WriterFactory

from .models.misc import (
    pmedian, pmedian_quicksum, pmedian_tuple,
    bilinear, bilinear_nlcontext,
    diag_sum, diag_quicksum,
)
from .models.jump import (
    lqcp, lqcp_quicksum,
    facility, facility_quicksum,
    opf, opf_quicksum,
    clnlbeam,
)
from .models.devel import (
    osarwar_github_issue_691,
)

CWD = os.getcwd()

class TestModel(unittest.TestCase):
    # These two lines can be removed after we finish the PyUtilib divorce
    pyutilib_th = 1
    pyomo_unittest = 1
    def _run_test(self, model_lib, data):
        timer = TicTocTimer()
        if isinstance(data, six.string_types) and data.endswith('.dat'):
            model = model_lib()
            modeldir = os.path.dirname(model_lib.__code__.co_filename)
            dat_file = os.path.join(modeldir, data)
            model = model.create_instance(dat_file)
        elif data is None:
            model = model_lib()
        elif type(data) is tuple:
            model = model_lib(*data)
        else:
            model = model_lib(data)
        if not model.is_constructed():
            model = model.create_instance()
        self.recordTestData('create_instance', timer.toc(''))

        for fmt in ('nl', 'lp','bar','gams'):
            if not getattr(self, fmt, 0):
                continue
            writer = WriterFactory(fmt)
            fname = os.path.join(CWD, 'tmp.test.'+fmt)
            self.assertFalse(os.path.exists(fname))
            try:
                timer.tic('')
                writer(model, fname, lambda x:True, {})
                _time = timer.toc('')
                self.assertTrue(os.path.exists(fname))
                self.recordTestData(fmt, _time)
            finally:
                try:
                    os.remove(fname)
                except:
                    pass

@unittest.category('performance', 'nl', 'lp', 'bar', 'gams')
class TestMisc(TestModel):

    @unittest.category('short')
    def test_pmedian_sum_test4(self):
        self._run_test(pmedian.create_model, 'pmedian.test4.dat')

    @unittest.category('short')
    def test_pmedian_quicksum_test4(self):
        self._run_test(pmedian_quicksum.create_model, 'pmedian.test4.dat')

    @unittest.category('short')
    def test_pmedian_tuple_test4(self):
        self._run_test(pmedian_tuple.create_model, 'pmedian.test4.dat')

    @unittest.category('long')
    def test_pmedian_sum_test8(self):
        self._run_test(pmedian.create_model, 'pmedian.test8.dat')

    @unittest.category('long')
    def test_pmedian_quicksum_test8(self):
        self._run_test(pmedian_quicksum.create_model, 'pmedian.test8.dat')

    @unittest.category('long')
    def test_pmedian_tuple_test8(self):
        self._run_test(pmedian_tuple.create_model, 'pmedian.test8.dat')

    @unittest.category('short')
    def test_bilinear_100(self):
        self._run_test(bilinear.create_model, 100)

    @unittest.category('short')
    def test_bilinear_nlcontext_100(self):
        self._run_test(bilinear_nlcontext.create_model, 100)

    @unittest.category('long')
    def test_bilinear_100000(self):
        self._run_test(bilinear.create_model, 100000)

    @unittest.category('long')
    def test_bilinear_nlcontext_100000(self):
        self._run_test(bilinear_nlcontext.create_model, 100000)
        
    @unittest.category('short')
    def test_diag_sum_100(self):
        self._run_test(diag_sum.create_model, 100)

    @unittest.category('short')
    def test_diag_quicksum_100(self):
        self._run_test(diag_quicksum.create_model, 100)

    @unittest.category('long')
    def test_diag_sum_100000(self):
        self._run_test(diag_sum.create_model, 100000)

    @unittest.category('long')
    def test_diag_quicksum_100000(self):
        self._run_test(diag_quicksum.create_model, 100000)


@unittest.category('performance', 'nl', 'gams')
class TestJump(TestModel):

    @unittest.category('short', 'lp', 'bar')
    def test_lqcp_10(self):
        self._run_test(lqcp.create_model, 10)

    @unittest.category('short', 'lp', 'bar')
    def test_lqcp_quicksum_10(self):
        self._run_test(lqcp_quicksum.create_model, 10)

    @unittest.category('long', 'lp', 'bar')
    def test_lqcp_500(self):
        self._run_test(lqcp.create_model, 500)

    @unittest.category('long', 'lp', 'bar')
    def test_lqcp_quicksum_500(self):
        self._run_test(lqcp_quicksum.create_model, 500)

    @unittest.category('short', 'lp', 'bar')
    def test_facility_5(self):
        self._run_test(facility.create_model, 5)

    @unittest.category('short', 'lp', 'bar')
    def test_facility_quicksum_5(self):
        self._run_test(facility_quicksum.create_model, 5)

    @unittest.category('long', 'lp', 'bar')
    def test_facility_25(self):
        self._run_test(facility.create_model, 25)

    @unittest.category('long', 'lp', 'bar')
    def test_facility_quicksum_25(self):
        self._run_test(facility_quicksum.create_model, 25)

    #
    # Note: opf contains cos() and cannot be sent to Baron
    #

    @unittest.category('short')
    def test_opf_662(self):
        _dir = os.path.dirname(opf.__file__)
        self._run_test(opf.create_model, (
            os.path.join(_dir, 'IEEE662.bus'),
            os.path.join(_dir, 'IEEE662.branch') ))

    @unittest.category('short')
    def test_opf_quicksum_662(self):
        _dir = os.path.dirname(opf.__file__)
        self._run_test(opf_quicksum.create_model, (
            os.path.join(_dir, 'IEEE662.bus'),
            os.path.join(_dir, 'IEEE662.branch') ))

    @unittest.category('long')
    def test_opf_6620(self):
        _dir = os.path.dirname(opf.__file__)
        self._run_test(opf.create_model, (
            os.path.join(_dir, 'IEEE6620.bus'),
            os.path.join(_dir, 'IEEE6620.branch') ))

    @unittest.category('long')
    def test_opf_quicksum_6620(self):
        _dir = os.path.dirname(opf.__file__)
        self._run_test(opf_quicksum.create_model, (
            os.path.join(_dir, 'IEEE6620.bus'),
            os.path.join(_dir, 'IEEE6620.branch') ))

    #
    # Note: clnlbean contains cos() and cannot be sent to Baron
    #

    @unittest.category('short')
    def test_clnlbean_5000(self):
        self._run_test(clnlbeam.create_model, 'clnlbeam-5000.dat')

    @unittest.category('long')
    def test_clnlbean_50000(self):
        self._run_test(clnlbeam.create_model, 'clnlbeam-50000.dat')


@unittest.category('performance', 'nl', 'lp', 'bar', 'gams')
class TestDevel(TestModel):

    @unittest.skipIf(not numpy_available, 'numpy is not available')
    @unittest.category('devel')
    def test_issue_691(self):
        self._run_test(osarwar_github_issue_691.create_model, 1000)
