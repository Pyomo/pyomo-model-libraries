import os

import pyutilib.th as unittest

from pyomo.common.timing import TicTocTimer
from pyomo.environ import *
from pyomo.opt import WriterFactory
from pyomo.dae import *

_dir = os.path.dirname(__file__)

@unittest.category('performance', 'short', 'nl', 'bar', 'gams')
class TestStochPDEgas(unittest.TestCase):
    def test_stochpdegas_automatic(self):
        timer = TicTocTimer()
        from .stochpdegas_automatic import model
        instance = model.create_instance(
            os.path.join(_dir,'stochpdegas_automatic.dat'))
        self.recordTestData('create_instance', timer.toc(''))

        # discretize model
        discretizer = TransformationFactory('dae.finite_difference')
        discretizer.apply_to(instance,nfe=1,wrt=instance.DIS,scheme='FORWARD')
        discretizer.apply_to(instance,nfe=47,wrt=instance.TIME,scheme='BACKWARD')
        self.recordTestData('discretize', timer.toc(''))

        # What it should be to match description in paper
        #discretizer.apply_to(instance,nfe=48,wrt=instance.TIME,scheme='BACKWARD')
        
        TimeStep = instance.TIME[2]-instance.TIME[1]
        
        def supcost_rule(m,k):
            return sum(m.cs*m.s[k,j,t]*(TimeStep) for j in m.SUP for t in m.TIME.get_finite_elements())
        instance.supcost = Expression(instance.SCEN,rule=supcost_rule)
        
        def boostcost_rule(m,k):
            return sum(m.ce*m.pow[k,j,t]*(TimeStep) for j in m.LINK_A for t in m.TIME.get_finite_elements())
        instance.boostcost = Expression(instance.SCEN,rule=boostcost_rule)
        
        def trackcost_rule(m,k):
            return sum(m.cd*(m.dem[k,j,t]-m.stochd[k,j,t])**2.0 for j in m.DEM for t in m.TIME.get_finite_elements())
        instance.trackcost = Expression(instance.SCEN,rule=trackcost_rule)
        
        def sspcost_rule(m,k):
            return sum(m.cT*(m.px[k,i,m.TIME.last(),j]-m.px[k,i,m.TIME.first(),j])**2.0 for i in m.LINK for j in m.DIS)
        instance.sspcost = Expression(instance.SCEN,rule=sspcost_rule)
        
        def ssfcost_rule(m,k):
            return sum(m.cT*(m.fx[k,i,m.TIME.last(),j]-m.fx[k,i,m.TIME.first(),j])**2.0 for i in m.LINK for j in m.DIS)
        instance.ssfcost = Expression(instance.SCEN,rule=ssfcost_rule)
        
        def cost_rule(m,k):
            return 1e-6*(m.supcost[k] + m.boostcost[k] + m.trackcost[k] + m.sspcost[k] + m.ssfcost[k])   
        instance.cost = Expression(instance.SCEN,rule=cost_rule)
        
        def mcost_rule(m):
            return (1.0/m.S)*sum(m.cost[k] for k in m.SCEN)
        instance.mcost = Expression(rule=mcost_rule)
        
        def eqcvar_rule(m,k):
            return m.cost[k] - m.nu <= m.phi[k];
        instance.eqcvar = Constraint(instance.SCEN,rule=eqcvar_rule)
        
        def obj_rule(m):
            return (1.0-m.cvar_lambda)*m.mcost + m.cvar_lambda*m.cvarcost
        instance.obj = Objective(rule=obj_rule)
        
        self.recordTestData('postprocessing', timer.toc(''))
        

        for fmt in ('nl', 'bar','gams'):
            if not getattr(self, fmt, 0):
                continue
            writer = WriterFactory(fmt)
            fname = 'tmp.test.'+fmt
            self.assertFalse(os.path.exists(fname))
            try:
                timer.tic('')
                writer(instance, fname, lambda x:True, {})
                _time = timer.toc('')
                self.assertTrue(os.path.exists(fname))
                self.recordTestData(fmt, _time)
            finally:
                try:
                    os.remove(fname)
                except:
                    pass
