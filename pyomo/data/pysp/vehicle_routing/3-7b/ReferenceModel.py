#
# Stochastic Optimization PS#3 Problem 7
# Vehicle Routing Problem
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
model.I = Set() #node
model.J = Set()
model.S = Set() #source node
model.D = Set() #demand node

# Data_deterministic
model.Arc = Param(model.I, model.J) #arc available
model.Rev = Param(model.I, model.J) #arc revenue
model.Cost = Param(model.I, model.J) #arc cost
model.B = Param()

#Data_stochastic
model.ArcDemand = Param(model.I, model.J) #arc demand

#
# Variables
#
model.X = Var(model.S, bounds=(0.0, model.B))
model.Y = Var(model.I, model.J, bounds=(0.0, model.B))
model.Z = Var(model.I, model.J, bounds=(0.0, None))

model.FirstStageProfit = Var()
model.SecondStageProfit = Var()

#
# Constraints
#
def vehicle_num_cap_rule(model):
    return sum(model.X[s] for s in model.S) == model.B
model.VehicleNumCapRule = Constraint(rule=vehicle_num_cap_rule)

def vehicle_assigned_cap_rule(model,s):
    return sum(model.Y[s,j] for j in model.J if model.Arc[s,j]>=1) == model.X[s]
model.RequiredDemandRule = Constraint(model.S, rule=vehicle_assigned_cap_rule)

def flow_balance_rule(model,d):
    return (sum(model.Y[i,d] for i in model.I if model.Arc[i,d]>=1) - sum(model.Y[d,i] for i in model.I if model.Arc[d,i]>=1)) == 0.0
model.FlowBalanceRule = Constraint(model.D, rule=flow_balance_rule)

def overage_rule(model,i,j):
    return model.Y[i,j] - model.ArcDemand[i,j] <= model.Z[i,j]
model.OverageRule = Constraint(model.I, model.J, rule=overage_rule)

def y_rule(model,i,j):
    return (0.0, model.Y[i,j], model.Arc[i,j]*51)
model.YRule = Constraint(model.I, model.J, rule=y_rule)

#
# Stage-specific cost computations
#
def first_stage_profit_rule(model):
    return model.FirstStageProfit == 0.0
model.ComputeFirstStageProfit = Constraint(rule=first_stage_profit_rule)

def second_stage_profit_rule(model):
    return model.SecondStageProfit - sum(sum(model.Rev[i,j] * model.Y[i,j] - (model.Rev[i,j] + model.Cost[i,j])* model.Z[i,j] \
                                           for i in model.I) for j in model.J) == 0.0
model.ComputeSecondStageProfit = Constraint(rule=second_stage_profit_rule)

#
# Objective
#
def total_profit_rule(model):
    return (model.FirstStageProfit + model.SecondStageProfit)
model.Total_Profit_Objective = Objective(rule=total_profit_rule, sense=maximize)

# Solve and print
EV_model = model.create('ReferenceModel.dat')
opt = SolverFactory('glpk')
results_EV = opt.solve(EV_model)
EV = results_EV.solution.objective.f.value
print('EV = ' + str(EV) + '\n')
print results_EV.solution.variable.X
