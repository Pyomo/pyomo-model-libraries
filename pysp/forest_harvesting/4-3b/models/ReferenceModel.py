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
# Stochastic Optimization PS#4 Problem 3
# MultiPeriod Forest Harvesting Plan
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
model.I = Set()             #timber class
model.IsubFirst = Set()
model.IsubMiddle = Set()
model.IsubLast = Set()
model.J = Set()             #contract levels

# Data_deterministic
model.a = Param(model.I)            #forest yield (cubic feet per acre) 
model.ZBounds = Param(model.J)      #max amount at each contract level (per thousand cubic feet)
model.cost = Param(model.J)         #profit at each contract level (per thousand cubic feet)
model.initTimber = Param(model.I)   #initial acres of each timber class (per thousand cubic feet)

#Data_stochastic
#model.damage = Param(model.T) #forest damage during each time period
model.damage1 = Param()
model.damage2 = Param()
model.damage3 = Param()
model.damage4 = Param()
model.damage5 = Param()


#
# Variables
#

model.X1 = Var(model.I, bounds=(0.0, None))
model.X2 = Var(model.I, bounds=(0.0, None))
model.X3 = Var(model.I, bounds=(0.0, None))
model.X4 = Var(model.I, bounds=(0.0, None))
model.X5 = Var(model.I, bounds=(0.0, None))

model.Y1 = Var(model.I, bounds=(0.0, None))
model.Y2 = Var(model.I, bounds=(0.0, None))
model.Y3 = Var(model.I, bounds=(0.0, None))
model.Y4 = Var(model.I, bounds=(0.0, None))
model.Y5 = Var(model.I, bounds=(0.0, None))

model.Z = Var(model.J, bounds=(0.0, None))

model.FirstStageCost = Var()
model.SecondStageCost = Var()
model.ThirdStageCost = Var()
model.FourthStageCost = Var()
model.FifthStageCost = Var()

#
# Constraints
#

#def harvestFirstClass_rule(model,i,t):
#    return model.Y[i,t+1] == sum((model.Y[i,t] - model.X[i,t])*model.damage[t+1] + model.X[i,t] for i in model.I)   
#model.HarvestFirstClassRule = Constraint(model.IsubFirst, model.TsubNotLast, rule=harvestFirstClass_rule)

def harvestFirstClass_T2_rule(model,i):
    return model.Y2[i] == sum((model.Y1[i] - model.X1[i])*model.damage2 + model.X1[i] for i in model.I)   
model.HarvestFirstClassT2Rule = Constraint(model.IsubFirst, rule=harvestFirstClass_T2_rule)

def harvestFirstClass_T3_rule(model,i):
    return model.Y3[i] == sum((model.Y2[i] - model.X2[i])*model.damage3 + model.X2[i] for i in model.I)   
model.HarvestFirstClassT3Rule = Constraint(model.IsubFirst, rule=harvestFirstClass_T3_rule)

def harvestFirstClass_T4_rule(model,i):
    return model.Y4[i] == sum((model.Y3[i] - model.X3[i])*model.damage4 + model.X3[i] for i in model.I)   
model.HarvestFirstClassT4Rule = Constraint(model.IsubFirst, rule=harvestFirstClass_T4_rule)

def harvestFirstClass_T5_rule(model,i):
    return model.Y5[i] == sum((model.Y4[i] - model.X4[i])*model.damage5 + model.X4[i] for i in model.I)   
model.HarvestFirstClassT5Rule = Constraint(model.IsubFirst, rule=harvestFirstClass_T5_rule)

#######################################################################################################

#def harvestMiddleClasses_rule(model,i,t):
#    return model.Y[i,t+1] == (model.Y[i-1,t] - model.X[i-1,t])*(1-model.damage[t+1])
#model.HarvestMiddleClassesRule = Constraint(model.IsubMiddle, model.TsubNotLast, rule=harvestMiddleClasses_rule)

def harvestMiddleClasses_T2_rule(model,i):
    return model.Y2[i] == (model.Y1[i-1] - model.X1[i-1])*(1-model.damage2)
model.HarvestMiddleClassesT2Rule = Constraint(model.IsubMiddle, rule=harvestMiddleClasses_T2_rule)

def harvestMiddleClasses_T3_rule(model,i):
    return model.Y3[i] == (model.Y2[i-1] - model.X2[i-1])*(1-model.damage3)
model.HarvestMiddleClassesT3Rule = Constraint(model.IsubMiddle, rule=harvestMiddleClasses_T3_rule)

def harvestMiddleClasses_T4_rule(model,i):
    return model.Y4[i] == (model.Y3[i-1] - model.X3[i-1])*(1-model.damage4)
model.HarvestMiddleClassesT4Rule = Constraint(model.IsubMiddle, rule=harvestMiddleClasses_T4_rule)

def harvestMiddleClasses_T5_rule(model,i):
    return model.Y5[i] == (model.Y4[i-1] - model.X4[i-1])*(1-model.damage5)
model.HarvestMiddleClassesT5Rule = Constraint(model.IsubMiddle, rule=harvestMiddleClasses_T5_rule)

##################################################################################################

#def harvestLastClass_rule(model,i,t):
#    return model.Y[i,t+1] == (model.Y[i,t] - model.X[i,t] + model.Y[i-1,t] - model.X[i-1,t])*(1-model.damage[t+1])  
#model.HarvestLastClassRule = Constraint(model.IsubLast, model.TsubNotLast, rule=harvestLastClass_rule)

def harvestLastClass_T2_rule(model,i):
    return model.Y2[i] == (model.Y1[i] - model.X1[i] + model.Y1[i-1] - model.X1[i-1])*(1-model.damage2)  
model.HarvestLastClassT2Rule = Constraint(model.IsubLast, rule=harvestLastClass_T2_rule)

def harvestLastClass_T3_rule(model,i):
    return model.Y3[i] == (model.Y2[i] - model.X2[i] + model.Y2[i-1] - model.X2[i-1])*(1-model.damage3)  
model.HarvestLastClassT3Rule = Constraint(model.IsubLast, rule=harvestLastClass_T3_rule)

def harvestLastClass_T4_rule(model,i):
    return model.Y4[i] == (model.Y3[i] - model.X3[i] + model.Y3[i-1] - model.X3[i-1])*(1-model.damage4)  
model.HarvestLastClassT4Rule = Constraint(model.IsubLast, rule=harvestLastClass_T4_rule)

def harvestLastClass_T5_rule(model,i):
    return model.Y5[i] == (model.Y4[i] - model.X4[i] + model.Y4[i-1] - model.X4[i-1])*(1-model.damage5)  
model.HarvestLastClassT5Rule = Constraint(model.IsubLast, rule=harvestLastClass_T5_rule)

#######################################################################################################

#def contract_rule(model):
#    return sum(sum(model.X[i,t]*model.a[i] for i in model.I) for t in model.T)/1000 == sum(model.Z[j] for j in model.J)
#model.ContractRule = Constraint(rule=contract_rule)

def contract_rule(model):
    return (sum(model.X1[i]*model.a[i] for i in model.I)+ \
            sum(model.X2[i]*model.a[i] for i in model.I)+ \
            sum(model.X3[i]*model.a[i] for i in model.I)+ \
            sum(model.X4[i]*model.a[i] for i in model.I)+ \
            sum(model.X5[i]*model.a[i] for i in model.I) \
            )/1000 == sum(model.Z[j] for j in model.J)
model.ContractRule = Constraint(rule=contract_rule)

#######################################################################################################

#def capacity_rule(model,i,t):
#    return model.X[i,t] <= model.Y[i,t]
#model.Capacity_rule = Constraint(model.I, model.T, rule=capacity_rule)

def capacity_T1_rule(model,i):
    return model.X1[i] <= model.Y1[i]
model.CapacityT1Rule = Constraint(model.I, rule=capacity_T1_rule)

def capacity_T2_rule(model,i):
    return model.X2[i] <= model.Y2[i]
model.CapacityT2Rule = Constraint(model.I, rule=capacity_T2_rule)

def capacity_T3_rule(model,i):
    return model.X3[i] <= model.Y3[i]
model.CapacityT3Rule = Constraint(model.I, rule=capacity_T3_rule)

def capacity_T4_rule(model,i):
    return model.X4[i] <= model.Y4[i]
model.CapacityT4Rule = Constraint(model.I, rule=capacity_T4_rule)

def capacity_T5_rule(model,i):
    return model.X5[i] <= model.Y5[i]
model.CapacityT5Rule = Constraint(model.I, rule=capacity_T5_rule)

########################################################################################################

#def initTimber_rule(model,i,t):
#    return model.Y[i,t] ==  model.initTimber[i]
#model.initTimberRule = Constraint(model.I,model.TsubFirst, rule=initTimber_rule)

def initTimber_rule(model,i):
    return model.Y1[i] ==  model.initTimber[i]
model.initTimberRule = Constraint(model.I, rule=initTimber_rule)

########################################################################################################

def z_rule(model,j):
    return (0.0, model.Z[j], model.ZBounds[j])
model.ZRule = Constraint(model.J, rule=z_rule)

#
# Stage-specific cost computations
#

def first_stage_cost_rule(model):
    return model.FirstStageCost  == 0.0
model.ComputeFirstStageCost = Constraint(rule=first_stage_cost_rule)

def second_stage_cost_rule(model):
    return model.SecondStageCost == 0.0
model.ComputeSecondStageCost = Constraint(rule=second_stage_cost_rule)

def third_stage_cost_rule(model):
    return model.ThirdStageCost == 0.0
model.ComputeThirdStageCost = Constraint(rule=third_stage_cost_rule)

def fourth_stage_cost_rule(model):
    return model.FourthStageCost == 0.0
model.ComputeFourthStageCost = Constraint(rule=fourth_stage_cost_rule)

def fifth_stage_cost_rule(model):
    return ( model.FifthStageCost - sum(model.cost[j]*model.Z[j] for j in model.J) )== 0.0
model.ComputeFifthStageCost = Constraint(rule=fifth_stage_cost_rule)

#
# Objective
#

def total_cost_rule(model):
    return (model.FirstStageCost + model.SecondStageCost + model.ThirdStageCost + model.FourthStageCost + model.FifthStageCost)
model.Total_Cost_Objective = Objective(rule=total_cost_rule, sense=maximize)

#instance = model.create('ReferenceModel.dat')
#opt = SolverFactory('glpk')
#results = opt.solve(instance)
#results.write()
#print results.solution.variable.Y

