#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright 2017 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and 
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain 
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

import os
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.dae import *
from pyomo.util.subsystems import TemporarySubsystemManager
from pyomo.util.calc_var_value import calculate_variable_from_constraint
from pyomo.contrib.pynumero.interfaces.external_pyomo_model import (
    ExternalPyomoModel,
)
from pyomo.contrib.pynumero.interfaces.external_grey_box import (
    ExternalGreyBoxBlock,
)

def make_model(horizon=52, vol=1.6, x_Feed=0.5):

    model = AbstractModel() 
    
    model.Feed = Param(initialize = 24.0/60.0)
    model.x_Feed = Param(initialize = x_Feed)
    model.D = Param(initialize = model.x_Feed*model.Feed)
    model.vol = Param(initialize = vol)
    model.atray = Param(initialize = 0.25)
    model.acond = Param(initialize = 0.5)
    model.areb = Param(initialize = 1.0)
    
    model.S_TRAYS = Set(dimen=1)
    model.S_RECTIFICATION = Set(within = model.S_TRAYS)  
    model.S_STRIPPING = Set(within = model.S_TRAYS)  
    model.x0 = Param(model.S_TRAYS)
    
    model.t = ContinuousSet(initialize=range(1, horizon))
    # Alternatively you could simply specify bounds on the
    # ContinuousSet and let the finite element points be generated
    # automatically.
    # model.t = ContinuousSet(bounds=(1,51))
    
    model.y = Var(model.S_TRAYS, model.t)
    def x_init_rule(m,n,ti):
        return value(m.x0[n])
    model.x = Var(model.S_TRAYS, model.t, initialize=x_init_rule)
    model.dx = DerivativeVar(model.x)
    
    model.rr = Var(model.t,initialize=3.0)
    model.L = Var(model.t,initialize=0.6)
    model.V = Var(model.t,initialize=0.8)
    model.FL = Var(model.t,initialize=1)
    model.u1 = Var(model.t,initialize=3.0, bounds=(1,5))
    
    model.alpha = Param(initialize = 1000)
    model.rho = Param(initialize = 1)
    model.u1_ref = Param(initialize = 2.0)
    model.y1_ref = Param(initialize = 0.895814)
    
    ###                             
    # Model constraints
    ### 
    def reflux_ratio_rule(m,t):
        return m.rr[t] == m.u1[t]
    model.reflux_ratio = Constraint(model.t, rule=reflux_ratio_rule)
    
    def flowrate_rectification_rule(m,t):
        return m.L[t] == m.rr[t]*m.D
    model.flowrate_rectification = Constraint(model.t, rule=flowrate_rectification_rule)
    
    def vapor_column_rule(m,t):
        return m.V[t] == m.L[t]+m.D
    model.vapor_column = Constraint(model.t, rule=vapor_column_rule)
    
    def flowrate_stripping_rule(m,t):
        return m.FL[t] == m.Feed + m.L[t]
    model.flowrate_stripping = Constraint(model.t, rule=flowrate_stripping_rule)
    
    def mole_frac_balance_rule(m,n,t):
        return m.y[n,t] == m.x[n,t]*m.vol/(1+((m.vol-1)*m.x[n,t]))
    model.mole_frac_balance = Constraint(model.S_TRAYS, model.t, rule=mole_frac_balance_rule)
    
    def _diffeq(m,n,t):
        
        if t == 1:
            return Constraint.Skip
        if n == 1:
            return m.dx[n,t] == 1/m.acond*m.V[t]*(m.y[n+1,t]-m.x[n,t])
        elif n in m.S_RECTIFICATION:
            return m.dx[n,t] == 1/m.atray*(m.L[t]*(m.x[n-1,t]-m.x[n,t])-m.V[t]*(m.y[n,t]-m.y[n+1,t]))
        elif n == 17:
            return m.dx[n,t] == 1/m.atray*(m.Feed*m.x_Feed+m.L[t]*m.x[n-1,t]-m.FL[t]*m.x[n,t]-m.V[t]*(m.y[n,t]-m.y[n+1,t]))
        elif n in m.S_STRIPPING:
            return m.dx[n,t] == 1/m.atray*(m.FL[t]*(m.x[n-1,t]-m.x[n,t])-m.V[t]*(m.y[n,t]-m.y[n+1,t]))
        else :
            return m.dx[n,t] == 1/m.areb*(m.FL[t]*m.x[n-1,t]-(m.Feed-m.D)*m.x[n,t]-m.V[t]*m.y[n,t])
    model.diffeq = Constraint(model.S_TRAYS, model.t, rule=_diffeq)
    
    def _init_rule(m,n):
        return m.x[n,1] == m.x0[n]
    model.init_rule = Constraint(model.S_TRAYS, rule=_init_rule)   

    return model


def discretize_model(instance):
    # Discretize using Finite Difference Approach
    discretizer = pyo.TransformationFactory('dae.finite_difference')
    discretizer.apply_to(instance,nfe=50,scheme='BACKWARD')
    
    # Discretize using Orthogonal Collocation
    # discretizer = TransformationFactory('dae.collocation')
    # discretizer.apply_to(instance,nfe=50,ncp=3)
    
    # The objective function in the manually discretized pyomo model
    # iterated over all finite elements and all collocation points.  Since
    # the objective function is not explicitly indexed by a ContinuousSet
    # we add the objective function to the model after it has been
    # discretized to ensure that we include all the discretization points
    # when we take the sum.


def add_objective(instance):
    def obj_rule(m):
        return m.alpha*sum((m.y[1,i] - m.y1_ref)**2 for i in m.t if i != 1) + m.rho*sum((m.u1[i] - m.u1_ref)**2 for i in m.t if i!=1)
    instance.OBJ = pyo.Objective(rule=obj_rule)

    # Calculate setpoint for the reduced space.
    # Reduced space objective must not use algebraic variables.
    t0 = instance.t.first()
    to_reset = [instance.y[1, t0], instance.x[1, t0]]
    with TemporarySubsystemManager(to_reset=to_reset):
        instance.y[1, t0].set_value(pyo.value(instance.y1_ref))
        calculate_variable_from_constraint(
                instance.x[1, t0],
                instance.mole_frac_balance[1, t0],
                )
        instance.x1_ref = pyo.Param(initialize=instance.x[1, t0].value)

    def rs_obj_rule(m):
        return (
                m.alpha*sum((m.x[1,i] - m.x1_ref)**2 for i in m.t if i != 1) +
                m.rho*sum((m.u1[i] - m.u1_ref)**2 for i in m.t if i != 1)
                )
    instance.REDUCED_SPACE_OBJ = pyo.Objective(rule=rs_obj_rule)
    instance.OBJ.deactivate()
    
def create_instance():
    model = make_model()
    file_dir = os.path.dirname(__file__)
    fname = os.path.join(file_dir, "distill.dat")
    instance = model.create_instance(fname)
    discretize_model(instance)
    add_objective(instance)
    return instance
