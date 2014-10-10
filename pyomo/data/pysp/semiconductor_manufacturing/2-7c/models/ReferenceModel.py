#
# Stochastic Optimization PS#2 Problem 7
# Semiconductor Manufacturer
#


#
# Imports
#

from pyomo.core import *
from pyomo.opt import SolverFactory


#
# Model
#

model = AbstractModel()

#
# Parameters
#

# Define sets
model.MACHINES = Set()
model.WAFERS = Set()
model.WAFERS_sub1 = Set()
model.WAFERS_sub2 = Set()
model.STEPS = Set()
model.STEPS_sub1 = Set()


# Data_deterministic
model.B = Param()
model.Cap = Param(model.MACHINES)

#Data_stochastic
model.ProdTime = Param(model.WAFERS, model.STEPS, model.MACHINES)
model.Demand = Param(model.WAFERS)

#
# Variables
#
model.X_RP = Param(model.MACHINES)
model.X_EV = Param(model.MACHINES)
model.X = Var(model.MACHINES, bounds=(0.0, model.B))
model.Y = Var(model.WAFERS, model.STEPS, model.MACHINES, bounds=(0.0, None))
model.Ytotal = Var(model.WAFERS, bounds=(0.0, None))
model.Z = Var(model.WAFERS, bounds=(0.0, None))

model.FirstStageCost = Var()
model.SecondStageCost = Var()

#
# Constraints
#

def machine_capacity(model,m):
    return sum(sum(model.Y[w,s,m]*model.ProdTime[w,s,m] for s in model.STEPS) for w in model.WAFERS) <= model.Cap[m]*(1+model.X[m])
model.machine_capacity = Constraint(model.MACHINES, rule=machine_capacity)

def finished_wafers_sub1(model,w,s):
    return sum(model.Y[w,s,m] for m in model.MACHINES) == model.Ytotal[w]
model.finished_wafers = Constraint(model.WAFERS_sub1, model.STEPS_sub1, rule=finished_wafers_sub1)

def finished_wafers_sub2(model,w,s):
    return sum(model.Y[w,s,m] for m in model.MACHINES) == model.Ytotal[w]
model.finished_wafers_sub2 = Constraint(model.WAFERS_sub2, model.STEPS, rule=finished_wafers_sub2)

def nonnegZ(model,w):
    return model.Demand[w] - model.Ytotal[w] <= model.Z[w]
model.nonnegZ = Constraint(model.WAFERS, rule=nonnegZ)

def buyMachines(model):
    return sum(model.X[m] for m in model.MACHINES) <= model.B
model.buyMachines = Constraint(rule=buyMachines)

def y_rule(model,w,s,m):
    if model.ProdTime[w,s,m] > 0 :
        return (0.0, model.Y[w,s,m], None)
    else:
        return (0.0, model.Y[w,s,m], 0)
model.YRule = Constraint(model.WAFERS, model.STEPS, model.MACHINES, rule=y_rule)

#NOTE: (Part C) We have added a constraint to fix X at EV (or RP) solution
def x_fix_rule(model,m):  
    #return model.X[m] == model.X_EV[m]
    return model.X[m] == model.X_RP[m]
model.XFixRule = Constraint(model.MACHINES, rule=x_fix_rule)

#
# Stage-specific cost computations
#

def first_stage_cost_rule(model):
    return model.FirstStageCost == 0
model.ComputeFirstStageCost = Constraint(rule=first_stage_cost_rule)


def second_stage_cost_rule(model): 
    return (model.SecondStageCost - sum(model.Z[w] for w in model.WAFERS) ) == 0.0
model.ComputeSecondStageCost = Constraint(rule=second_stage_cost_rule)

#
# Objective
#

def total_cost_rule(model):
    return (model.FirstStageCost + model.SecondStageCost)

model.Total_Cost_Objective = Objective(rule=total_cost_rule, sense=minimize)

#instance = model.create('ReferenceModel.dat')
#opt = SolverFactory('glpk')
#results = opt.solve(instance)
##results.write()
#print results.solution.objective.f.value
