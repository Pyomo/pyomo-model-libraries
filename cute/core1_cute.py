#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, and Brandon C. Barrera
# Taken from:

# AMPL Model by Hande Y. Benson
#
# Copyright (C) 2001 Princeton University
# All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that the copyright notice and this
# permission notice appear in all supporting documentation.

#   classification LQI2-RN-65-59

from pyomo.environ import *
model = AbstractModel()

Flow_init = {1:5.797, 2:5.797, 3:9.997, 4:9.997, 5:16.076, 6:4.8, 7:0.766, \
             8:-4.49, 9:11.586, 10:17.2404, 11:2.10363, 12:17.2404, 13:2.10363, \
             14:11.5676, 15:1.41145, 16:10.838, 17:8.718, 18:9.918, 19:22.464, \
             20:15.616, 21:2.141, 22:2.141, 23:2.141, 24:1.919}

model.SF = RangeSet(1,24)
model.SP = RangeSet(1,6)
model.SD = RangeSet(1,9)
model.SPi = RangeSet(1,20)

model.Flow = Var(model.SF,initialize=Flow_init)
model.Prod = Var(model.SP)
model.Supply = Var(model.SP)
model.Demand = Var(model.SD)
model.Pi = Var(model.SPi)

model.Region = Param(model.SD)
model.loflows = Param(model.SF)
model.hiflows = Param()
model.hisupply = Param(model.SP)
model.loprods = Param(model.SP)
model.hiprods = Param(model.SP)
model.lopi = Param(model.SPi)
model.hipi = Param(model.SPi)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def cost(model):
    exp = 2.28*model.Prod[1] + 2.28*model.Prod[2] + 2.28*model.Prod[3] + 1.68*model.Prod[4] + 1.68*model.Prod[5] + 1.68*model.Prod[6]
    return exp
model.cost = Objective(rule=cost,sense=minimize)

def node1(model):
    return model.Flow[1] + model.Flow[2] - model.Supply[1] == 0
def node2(model):
    return -1*model.Flow[1] - model.Flow[2] + model.Flow[3] + model.Flow[4] - model.Supply[2] == 0
def node3(model):
    return  -1*model.Flow[3] - model.Flow[4] + model.Flow[5] + model.Demand[1] == 0
def node4(model):
    return -1*model.Flow[5] - model.Flow[8] + model.Flow[9] == 0
def node5(model):
    return model.Flow[6] - model.Supply[3] == 0
def node6(model):
    return -1*model.Flow[6] + model.Flow[7] + model.Demand[2] == 0
def node7(model):
    return -1*model.Flow[7] + model.Flow[8] + model.Demand[3] == 0
def node8(model):
    return model.Flow[10] + model.Flow[11] - model.Supply[4] == 0
def node9(model):
    return -1*model.Flow[10] - model.Flow[11] + model.Flow[12] + model.Flow[13] == 0
def node10(model):
    return -1*model.Flow[12] - model.Flow[13] + model.Flow[14] + model.Flow[15] + model.Demand[4] == 0
def node11(model):
    return -1*model.Flow[14] - model.Flow[15] + model.Flow[16] + model.Flow[21] == 0
def node12(model):
    return -1*model.Flow[16] + model.Flow[17] + model.Demand[5] == 0
def node13(model):
    return -1*model.Flow[17] + model.Flow[18] - model.Supply[5] == 0
def node14(model):
    return -1*model.Flow[9] - model.Flow[18] + model.Flow[19] - model.Supply[6] == 0
def node15(model):
    return -1*model.Flow[19] + model.Flow[20] + model.Demand[6] == 0
def node16(model):
    return -1*model.Flow[20] + model.Demand[7] == 0
def node17(model):
    return -1*model.Flow[21] + model.Flow[22] == 0
def node18(model):
    return -1*model.Flow[22] + model.Flow[23] == 0
def node19(model):
    return -1*model.Flow[23] + model.Flow[24] + model.Demand[8] == 0
def node20(model):
    return -1*model.Flow[24] + model.Demand[9] == 0
def region1(model):
    return -1*model.Demand[1] <= model.Region[1]
def region2(model):
    return -1*model.Demand[2] <= model.Region[2]
def region3(model):
    return -1*model.Demand[3] <= model.Region[3]
def region4(model):
    return -1*model.Demand[4] <= model.Region[4]
def region5(model):
    return -1*model.Demand[5] <= model.Region[5]
def region6(model):
    return -1*model.Demand[6] <= model.Region[6]
def region7(model):
    return -1*model.Demand[7] <= model.Region[7]
def region8(model):
    return -1*model.Demand[8] <= model.Region[8]
def region9(model):
    return -1*model.Demand[9] <= model.Region[9]
def prod1(model):
    return model.Supply[1] <= model.Prod[1]
def prod2(model):
    return model.Supply[2] <= model.Prod[2]
def prod3(model):
    return model.Supply[3] <= model.Prod[3]
def prod4(model):
    return model.Supply[4] <= model.Prod[4]
def prod5(model):
    return model.Supply[5] <= model.Prod[5]
def prod6(model):
    return model.Supply[6] <= model.Prod[6]
def arc1(model):
    return (model.Flow[1]**2) -9.07027*(model.Pi[1] - model.Pi[2]) == 0
def arc2(model):
    return (model.Flow[2]**2) -9.07027*(model.Pi[1] - model.Pi[2]) == 0
def arc3(model):
    return (model.Flow[3]**2) -6.04685*(model.Pi[2] - model.Pi[3])  == 0
def arc4(model):
    return (model.Flow[4]**2) -6.04685*(model.Pi[2] - model.Pi[3]) == 0
def arc5(model):
    return (model.Flow[5]**2) -1.39543*(model.Pi[3] - model.Pi[4]) == 0
def arc6(model):
    return (model.Flow[6]**2) -0.100256*(model.Pi[5] - model.Pi[6]) == 0
def arc7(model):
    return (model.Flow[7]**2) -0.148655*(model.Pi[6] - model.Pi[7]) == 0
def arc8(model):
    return (model.Flow[8]**2) +0.226895*(model.Pi[4] - model.Pi[7]) == 0
def arc9(model):
    return (model.Flow[9]**2) -0.659656*(model.Pi[4] - model.Pi[14]) == 0
def arc10(model):
    return (model.Flow[10]**2) -7.25622*(model.Pi[8] - model.Pi[9]) >= 0
def arc11(model):
    return (model.Flow[11]**2) -0.10803*(model.Pi[8] - model.Pi[9]) >= 0
def arc12(model):
    return (model.Flow[12]**2) -1.81405*(model.Pi[9] - model.Pi[10]) == 0
def arc13(model):
    return (model.Flow[13]**2) -0.0270084*(model.Pi[9] - model.Pi[10]) == 0
def arc14(model):
    return (model.Flow[14]**2) -1.45124*(model.Pi[10] - model.Pi[11]) == 0
def arc15(model):
    return (model.Flow[15]**2) -0.0216067*(model.Pi[10] - model.Pi[11]) == 0
def arc16(model):
    return (model.Flow[16]**2) -0.863836*(model.Pi[11] - model.Pi[12]) == 0
def arc17(model):
    return (model.Flow[17]**2) -0.907027*(model.Pi[12] - model.Pi[13]) == 0
def arc18(model):
    return (model.Flow[18]**2) -7.25622*(model.Pi[13] - model.Pi[14]) == 0
def arc19(model):
    return (model.Flow[19]**2) -3.62811*(model.Pi[14] - model.Pi[15]) == 0
def arc20(model):
    return (model.Flow[20]**2) -1.45124*(model.Pi[15] - model.Pi[16]) == 0
def arc21(model):
    return (model.Flow[21]**2) -0.0514445*(model.Pi[11] - model.Pi[17]) == 0
def arc22(model):
    return (model.Flow[22]**2) -0.00641977*(model.Pi[17] - model.Pi[18]) >= 0
def arc23(model):
    return (model.Flow[23]**2) -0.00170320*(model.Pi[18] - model.Pi[19]) == 0
def arc24(model):
    return (model.Flow[24]**2) -0.0278190*(model.Pi[19] - model.Pi[20]) == 0
model.node1 = Constraint(rule=node1)
model.node2 = Constraint(rule=node2)
model.node3 = Constraint(rule=node3)
model.node4 = Constraint(rule=node4)
model.node5 = Constraint(rule=node5)
model.node6 = Constraint(rule=node6)
model.node7 = Constraint(rule=node7)
model.node8 = Constraint(rule=node8)
model.node9 = Constraint(rule=node9)
model.node10 = Constraint(rule=node10)
model.node11 = Constraint(rule=node11)
model.node12 = Constraint(rule=node12)
model.node13 = Constraint(rule=node13)
model.node14 = Constraint(rule=node14)
model.node15 = Constraint(rule=node15)
model.node16 = Constraint(rule=node16)
model.node17 = Constraint(rule=node17)
model.node18 = Constraint(rule=node18)
model.node19 = Constraint(rule=node19)
model.node20 = Constraint(rule=node20)
model.region1 = Constraint(rule=region1)
model.region2 = Constraint(rule=region2)
model.region3 = Constraint(rule=region3)
model.region4 = Constraint(rule=region4)
model.region5 = Constraint(rule=region5)
model.region6 = Constraint(rule=region6)
model.region7 = Constraint(rule=region7)
model.region8 = Constraint(rule=region8)
model.region9 = Constraint(rule=region9)
model.prod1 = Constraint(rule=prod1)
model.prod2 = Constraint(rule=prod2)
model.prod3 = Constraint(rule=prod3)
model.prod4 = Constraint(rule=prod4)
model.prod5 = Constraint(rule=prod5)
model.prod6 = Constraint(rule=prod6)
model.arc1 = Constraint(rule=arc1)
model.arc2 = Constraint(rule=arc2)
model.arc3 = Constraint(rule=arc3)
model.arc4 = Constraint(rule=arc4)
model.arc5 = Constraint(rule=arc5)
model.arc6 = Constraint(rule=arc6)
model.arc7 = Constraint(rule=arc7)
model.arc8 = Constraint(rule=arc8)
model.arc9 = Constraint(rule=arc9)
model.arc10 = Constraint(rule=arc10)
model.arc11 = Constraint(rule=arc11)
model.arc12 = Constraint(rule=arc12)
model.arc13 = Constraint(rule=arc13)
model.arc14 = Constraint(rule=arc14)
model.arc15 = Constraint(rule=arc15)
model.arc16 = Constraint(rule=arc16)
model.arc17 = Constraint(rule=arc17)
model.arc18 = Constraint(rule=arc18)
model.arc19 = Constraint(rule=arc19)
model.arc20 = Constraint(rule=arc20)
model.arc21 = Constraint(rule=arc21)
model.arc22 = Constraint(rule=arc22)
model.arc23 = Constraint(rule=arc23)
model.arc24 = Constraint(rule=arc24)

def f(model, i):
    return (model.loflows[i], model.Flow[i], model.hiflows)
model.f = Constraint(model.SF, rule=f)

def s(model, i):
    return model.Supply[i] <= model.hisupply[i]
model.s = Constraint(model.SP, rule=s)

def pr(model, i):
    return (model.loprods[i], model.Prod[i], model.hiprods[i])
model.pr = Constraint(model.SP, rule=pr)

def pi(model, i):
    return (model.lopi[i], model.Pi[i], model.hipi[i])
model.pi = Constraint(model.SPi, rule=pi)
