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


def setup_implicit(instance):
    diff_vars = [pyo.Reference(instance.x[i, :]) for i in instance.S_TRAYS]
    deriv_vars = [pyo.Reference(instance.dx[i, :]) for i in instance.S_TRAYS]
    disc_eqns = [pyo.Reference(instance.dx_disc_eq[i, :]) for i in instance.S_TRAYS]
    diff_eqns = [pyo.Reference(instance.diffeq[i, :]) for i in instance.S_TRAYS]

    n_diff = len(diff_vars)
    assert n_diff == len(deriv_vars)
    assert n_diff == len(disc_eqns)
    assert n_diff == len(diff_eqns)

    alg_vars = []
    alg_eqns = []
    alg_vars.extend(pyo.Reference(instance.y[i, :]) for i in instance.S_TRAYS)
    alg_eqns.extend(pyo.Reference(instance.mole_frac_balance[i, :])
            for i in instance.S_TRAYS)
    # Since we are not adding them to the reduced space model, alg vars do not
    # need to be references.
    alg_vars.append(instance.rr)
    alg_vars.append(instance.L)
    alg_vars.append(instance.V)
    alg_vars.append(instance.FL)

    alg_eqns.append(instance.reflux_ratio)
    alg_eqns.append(instance.flowrate_rectification)
    alg_eqns.append(instance.vapor_column)
    alg_eqns.append(instance.flowrate_stripping)

    input_vars = [pyo.Reference(instance.u1[:])]

    # Create a block to hold the reduced space model
    reduced_space = pyo.Block(concrete=True)
    reduced_space.obj = pyo.Reference(instance.REDUCED_SPACE_OBJ)

    n_input = len(input_vars)

    def differential_block_rule(b, i):
        b.state = diff_vars[i]
        b.deriv = deriv_vars[i]
        b.disc = disc_eqns[i]

    def input_block_rule(b, i):
        b.var = input_vars[i]

    reduced_space.differential_block = pyo.Block(
            range(n_diff),
            rule=differential_block_rule,
            )
    reduced_space.input_block = pyo.Block(
            range(n_input),
            rule=input_block_rule,
            )

    reduced_space.external_block = ExternalGreyBoxBlock(instance.t)

    # Add reference to the constraint that specifies the initial conditions
    reduced_space.init_rule = pyo.Reference(instance.init_rule)

    for t in instance.t:
        if t == instance.t.first():
            reduced_space.external_block[t].deactivate()
            continue
        # Create and set external model for every external block
        reduced_space_vars = (
                list(reduced_space.input_block[:].var[t]) +
                list(reduced_space.differential_block[:].state[t]) +
                list(reduced_space.differential_block[:].deriv[t])
                )
        external_vars = [v[t] for v in alg_vars]
        residual_cons = [c[t] for c in diff_eqns]
        external_cons = [c[t] for c in alg_eqns]
        reduced_space.external_block[t].set_external_model(
                ExternalPyomoModel(
                    reduced_space_vars,
                    external_vars,
                    residual_cons,
                    external_cons,
                    ),
                inputs=reduced_space_vars,
                )
    return reduced_space


def solve(reduced_space, tee=False):
    solver = pyo.SolverFactory("cyipopt")
    results = solver.solve(reduced_space, tee=tee)
    return results
