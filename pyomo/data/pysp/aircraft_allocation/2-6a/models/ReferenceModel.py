#
# Stochastic Optimization PS#2 Problem 6a
# Aircraft allocation
#

#
# Imports
#
from pyomo.core import *

#
# Model
#
model = AbstractModel()

#
# Parameters
#
# Define sets
model.TYPES = Set()
model.ROUTES = Set()

# Data_deterministic
model.C = Param(model.TYPES, model.ROUTES, within=PositiveReals)
model.Q = Param(model.ROUTES, within=PositiveReals)
model.K = Param(model.TYPES, model.ROUTES, within=PositiveReals)
model.B = Param(model.TYPES, within=PositiveReals)

#Data_stochastic
model.D = Param(model.ROUTES, within=PositiveReals)

#
# Variables
#
model.X = Var(model.TYPES, model.ROUTES, bounds=(0.0, None))
model.Y = Var(model.ROUTES, bounds=(0.0, None))

model.FirstStageCost = Var()
model.SecondStageCost = Var()

#
# Constraints
#
def supply_rule(model, j):
    return sum(model.X[j,r] for r in model.ROUTES) <= model.B[j]
model.SupplyRule = Constraint(model.TYPES, rule=supply_rule)

def y_nonnegtive_rule(model, r):
    return model.Y[r] >= (model.D[r] - sum(model.K[j,r] * model.X[j,r] for j in model.TYPES))
model.YNonnegtiveRule = Constraint(model.ROUTES, rule=y_nonnegtive_rule)

#
# Stage-specific cost computations
#
def first_stage_cost_rule(model):
    return ( model.FirstStageCost - sum(sum(model.C[j,r] * model.X[j,r] for r in model.ROUTES) for j in model.TYPES) ) == 0.0
model.ComputeFirstStageCost = Constraint(rule=first_stage_cost_rule)

def second_stage_cost_rule(model):
    expcost = sum(model.Q[r] * model.Y[r] for r in model.ROUTES)
    return (model.SecondStageCost - expcost) == 0.0
model.ComputeSecondStageCost = Constraint(rule=second_stage_cost_rule)

#
# Objective
#
def total_cost_rule(model):
    return (model.FirstStageCost + model.SecondStageCost)
model.Total_Cost_Objective = Objective(rule=total_cost_rule, sense=minimize)
