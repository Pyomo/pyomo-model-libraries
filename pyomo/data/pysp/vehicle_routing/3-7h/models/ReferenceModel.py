#
# Stochastic Optimization PS#3 Problem 7
# Vehicle Routing Problem
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

model = Model()

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
model.X_WS = Param(model.S)
model.X_EV = Param(model.S)
model.X_RP = Param(model.S)
model.X = Var(model.S, bounds=(0.0, model.B))
model.Y = Var(model.I, model.J, bounds=(0.0, model.B))
model.Z = Var(model.I, model.J, bounds=(0.0, None))

model.FirstStageProfit = Var()
model.SecondStageProfit = Var()


#
# Constraints
#

def vehicle_num_cap_rule(model):
    return sum(model.X[s] for s in model.S) <= model.B
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

#NOTE: (Part H) We have added a constraint to fix X at RP
def x_fix_rule(model,s):   
    return model.X[s] == model.X_RP[s]
model.XFixRule = Constraint(model.S, rule=x_fix_rule)

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



# Solve WS for given number of sample realizations with fixed X at X_WS
numSamples=50
numX=5
optVal=numpy.array([0 for i in range(numSamples)])

for i in range(numSamples):
    datafile = '../scenariodata/Scenario' + str(i+1) + '.dat'
    instance = model.create(datafile)
    opt = SolverFactory('glpk')
    results = opt.solve(instance)
    optVal[i] = results.solution.objective.f.value
    
# Calculate point est / interval est of objective value
z_val = 1.96
ERP = optVal[:].mean()
ERP_var = optVal[:].var()*numSamples/(numSamples-1)
ERP_halfwidth = z_val*sqrt(ERP_var/numSamples)
ERP_CI_lo = ERP - ERP_halfwidth
ERP_CI_hi = ERP + ERP_halfwidth
  
print ERP
print ERP_CI_lo, ERP_CI_hi
