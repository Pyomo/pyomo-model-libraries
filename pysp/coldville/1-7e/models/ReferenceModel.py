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
# Stochastic Optimization PS#1 Problem 7
# Coldville snow removal
#


#
# Imports
#

from pyomo.core import *

#
# Model
#

model = Model()

#
# Parameters
#

# Define sets
model.MATERIALS = Set()
model.METHODS = Set()

# Data_deterministic
model.SummerMaterialCost = Param(model.MATERIALS, within=PositiveReals)
model.MaterialSalvagePrice = Param(model.MATERIALS, within=PositiveReals)
model.FleetCapacity = Param(within=PositiveReals)
model.MaterialRequirement = Param(model.MATERIALS, model.METHODS)

#Data_stochastic
model.WinterMaterialCost = Param(model.MATERIALS, within=PositiveReals)
model.TruckCost = Param(within=PositiveReals)
model.Efficiency = Param(model.METHODS, within=PositiveReals)
model.TruckdayRequirement = Param(within=PositiveReals)



#
# Variables
#

model.SummerMaterialPurchase = Var(model.MATERIALS, bounds=(0.0, None))
model.WinterMaterialPurchase = Var(model.MATERIALS, bounds=(0.0, None))
model.SalvagedMaterial = Var(model.MATERIALS, bounds=(0.0, None))
model.TruckdayUsedinMethod = Var(model.METHODS, bounds=(0.0, None))

model.FirstStageCost = Var()
model.SecondStageCost = Var()

#
# Constraints
#

def total_truckday_rule(model):
    return sum(model.TruckdayUsedinMethod[j] for j in model.METHODS) <= model.FleetCapacity

model.TotalTruckdayRule = Constraint(rule=total_truckday_rule)

def demand_rule(model):
    return sum(model.Efficiency[j]*model.TruckdayUsedinMethod[j] for j in model.METHODS) >= model.TruckdayRequirement

model.DemandRule = Constraint(rule=demand_rule)

def balance_rule(model,i):
    return model.SummerMaterialPurchase[i] + model.WinterMaterialPurchase[i] - (sum(model.MaterialRequirement[i,j] * model.TruckdayUsedinMethod[j] for j in model.METHODS))\
    - model.SalvagedMaterial[i] == 0

model.BalanceRule = Constraint(model.MATERIALS, rule=balance_rule)


#
# Stage-specific cost computations
#

def first_stage_cost_rule(model):
    return (model.FirstStageCost - sum(model.SummerMaterialCost[i]*model.SummerMaterialPurchase[i] for i in model.MATERIALS)) == 0.0
 
model.ComputeFirstStageCost = Constraint(rule=first_stage_cost_rule)


def second_stage_cost_rule(model):
    expcost = sum(model.WinterMaterialCost[i] * model.WinterMaterialPurchase[i] for i in model.MATERIALS)
    expcost += model.TruckCost * ( sum(model.TruckdayUsedinMethod[j] for j in model.METHODS) ) 
    expcost -= sum(model.MaterialSalvagePrice[i]*model.SalvagedMaterial[i] for i in model.MATERIALS)
    return (model.SecondStageCost - expcost) == 0.0
 
model.ComputeSecondStageCost = Constraint(rule=second_stage_cost_rule)

#
# Objective
#

def total_cost_rule(model):
    return (model.FirstStageCost + model.SecondStageCost)

model.Total_Cost_Objective = Objective(rule=total_cost_rule, sense=minimize)
