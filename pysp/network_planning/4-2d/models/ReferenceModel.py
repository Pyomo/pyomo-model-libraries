#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2025
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

#
# Stochastic Optimization PS#4 Problem 2
# Telecommunication Network Design
#


#
# Imports
#

from pyomo.core import *
from pyomo.opt import SolverFactory
import scipy
import numpy

#
# Model
#

model = AbstractModel()

#
# Parameters
#

# Define sets
model.I = Set()
model.K = Set()
model.P = Set()

# Data_deterministic
model.aa = Param(model.K, model.P)
model.dd = Param(model.I, model.P)
model.Cost = Param(model.K)
model.B = Param()

#Data_stochastic
model.ppDemand = Param(model.I)
model.R = Param(model.K)


#
# Variables
#
model.X_EV = Param(model.K)
model.X_WS = Param(model.K)
model.X = Var(model.K, bounds=(0.0, None))
model.Y = Var(model.I, model.P, bounds=(0.0, None))
model.Z = Var(model.I, bounds=(0.0, None))

model.FirstStageCost = Var()
model.SecondStageCost = Var()


#
# Constraints
#

def budget_rule(model):
    return sum(model.X[k] * model.Cost[k] for k in model.K) <= model.B
model.BudgetRule = Constraint(rule=budget_rule)

def required_demand_rule(model,i):
    return sum(model.Y[i,p] for p in model.P if model.dd[i,p]==1) + model.Z[i] >= model.ppDemand[i]
model.RequiredDemandRule = Constraint(model.I, rule=required_demand_rule)

def capacity_rule(model,k):
    return sum(sum(model.Y[i,p] for i in model.I if model.aa[k,p]==1 and model.dd[i,p]==1) for p in model.P) <= model.X[k]*model.R[k]
model.CapacityRule = Constraint(model.K, rule=capacity_rule)

#NOTE: (Part E) We have added a constraint to fix X at EV (or WS) solution
def x_fix_rule(model,k):  
    return model.X[k] == model.X_EV[k] 
    #return model.X[k] == model.X_WS[k]
model.XFixRule = Constraint(model.K, rule=x_fix_rule)

#
# Stage-specific cost computations
#

def first_stage_cost_rule(model):
    return model.FirstStageCost == 0.0
model.ComputeFirstStageCost = Constraint(rule=first_stage_cost_rule)


def second_stage_cost_rule(model):
    return model.SecondStageCost - sum(model.Z[i] for i in model.I) == 0.0
model.ComputeSecondStageCost = Constraint(rule=second_stage_cost_rule)

#
# Objective
#

def total_cost_rule(model):
    return (model.FirstStageCost + model.SecondStageCost)

model.Total_Cost_Objective = Objective(rule=total_cost_rule, sense=minimize)

# Solve WS for given number of sample realizations
numSamples=50
numX=7
optVal=numpy.array([0 for i in range(numSamples)])

for i in range(numSamples):
    datafile = '../scenariodata/Scenario' + str(i+1) + '.dat'
    instance = model.create(datafile)
    opt = SolverFactory('gurobi')
    results = opt.solve(instance)
    optVal[i] = results.solution.objective.f.value

#Calculate point est / interval est of objective value, point estimate of solution
z_val = 1.96
EEV = optVal[:].mean()
EEV_var = optVal[:].var()*numSamples/(numSamples-1)
EEV_halfwidth = z_val*sqrt(EEV_var/numSamples)
EEV_CI_lo = EEV - EEV_halfwidth
EEV_CI_hi = EEV + EEV_halfwidth

    
print EEV
print EEV_CI_lo, EEV_CI_hi
