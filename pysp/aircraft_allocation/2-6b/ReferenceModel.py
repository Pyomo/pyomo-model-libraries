#
# Stochastic Optimization PS#2 Problem 6b
# Aircraft allocation
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
model.TYPES = Set() #j
model.ROUTES = Set() #r
model.SCENARIOS = Set() #u

# Data_deterministic
model.C = Param(model.TYPES, model.ROUTES)
model.Q = Param(model.ROUTES)
model.K = Param(model.TYPES, model.ROUTES)
model.B = Param(model.TYPES)
model.D = Param(model.ROUTES, model.SCENARIOS)
model.PROB = Param(model.ROUTES, model.SCENARIOS)
model.Zbounds = Param(model.ROUTES, model.SCENARIOS)


#
# Variables
#
model.X = Var(model.TYPES, model.ROUTES, bounds=(0.0, None))
model.Z = Var(model.ROUTES, model.SCENARIOS, bounds=(0.0, None))

model.FirstStageCost = Var()
model.SecondStageCost = Var()

#
# Constraints
#
def aircraft_avail_rule(model,j):
    return sum(model.X[j,r] for r in model.ROUTES) <= model.B[j]
model.AircraftAvailRule = Constraint(model.TYPES, rule=aircraft_avail_rule)

def equiv_capacity_rule(model,r):
    return sum(model.K[j,r] * model.X[j,r] for j in model.TYPES) >= sum(model.Z[r,u] for u in model.SCENARIOS)
model.EquivCapacityRule = Constraint(model.ROUTES, rule=equiv_capacity_rule)

def z_rule(model,r,u):
    return (0, model.Z[r,u], model.Zbounds[r,u])
model.ZRule = Constraint(model.ROUTES, model.SCENARIOS, rule=z_rule)
   
#
# Stage-specific cost computations
#
def first_stage_cost_rule(model):
    return (model.FirstStageCost \
            - sum(sum(model.C[j,r] * model.X[j,r] for r in model.ROUTES) for j in model.TYPES) \
            - sum(sum(model.PROB[r,u] * model.Q[r] * (model.D[r,u] - sum(model.Z[r,w] for w in model.SCENARIOS if w <= u )) for u in model.SCENARIOS) for r in model.ROUTES)) == 0.0
model.ComputeFirstStageCost = Constraint(rule=first_stage_cost_rule)

def second_stage_cost_rule(model):
    return model.SecondStageCost == 0.0
model.ComputeSecondStageCost = Constraint(rule=second_stage_cost_rule)

#
# Objective
#
def total_cost_rule(model):
    return (model.FirstStageCost + model.SecondStageCost)
model.Total_Cost_Objective = Objective(rule=total_cost_rule, sense=minimize)

#
# Solve and print
#
instance = model.create('ReferenceModel.dat')
opt = SolverFactory('glpk')
PartBresults = opt.solve(instance)

print PartBresults.solution.objective
