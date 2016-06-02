#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Juan Lopez
# Taken from:

#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   A small gas network problem.
#   SIF input: Sybille Schachler, Oxford, August 1992.
#              minor correction by Ph. Shott, Jan 1995.

from pyomo.core import *
model = ConcreteModel()

n = 7
m = 4
demand = -1000.0
pmax1 = 914.73
pmax2 = 904.73
k = -0.597053452

model.p1 = Var(bounds=(None,914.73),initialize=965)
model.p2 = Var(initialize=965)
model.p3 = Var(bounds=(None,904.73),initialize=965)
model.p4 = Var(initialize=965)
model.p5 = Var(bounds=(None,904.73),initialize=965)
model.p6 = Var(initialize=965)
model.p7 = Var(bounds=(None,914.73),initialize=965)
model.q1 = Var(initialize=100.0)
model.f1 = Var(initialize=1000.0)
model.q2 = Var(initialize=100.0)
model.f2 = Var(initialize=1000.0)
model.q3 = Var(initialize=-100.0)
model.f3 = Var(initialize=1000.0)
model.q4 = Var(initialize=-100.0)
model.f4 = Var(bounds=(None,400.0),initialize=1000.0)

def obj_rule(model):
    return - model.p1 - model.p2 - model.p3 - model.p4 - model.p5 - model.p6 - model.p7
model.obj = Objective(rule=obj_rule)

def pan1(model):
    return model.p1 * (abs(model.p1))-model.p2 * (abs (model.p2))  - 0.597053452*model.q1 * (abs(model.q1)) **0.8539 == 0
def pan2(model):
    return model.p3 * (abs(model.p3)) - model.p4 * (abs(model.p4))  - 0.597053452*model.q2 * (abs(model.q2))**0.8539 == 0
def pan3(model):
    return model.p4 * (abs(model.p4))  - model.p5 * (abs(model.p5))  - 0.597053452*model.q3 * (abs(model.q3)) **0.8539 == 0
def pan4(model):
    return model.p6 * (abs(model.p6))  - model.p7 * (abs(model.p7))  - 0.597053452*model.q4 * (abs(model.q4)) **0.8539 == 0
def m1(model):
    return model.q1 - model.f3 == 0
def m2(model):
    return -model.q1 + model.f1 == 0
def m3(model):
    return model.q2 - model.f1 == 0
def m4(model):
    return -model.q2 + model.q3 + 1000.0 == 0
def m5(model):
    return -model.q3 - model.f2 == 0
def m6(model):
    return model.q4 + model.f2 == 0
def m7(model):
    return -model.q4 - model.f4 == 0
    
model.pan1 = Constraint(rule=pan1)
model.pan2 = Constraint(rule=pan2)
model.pan3 = Constraint(rule=pan3)
model.pan4 = Constraint(rule=pan4)
model.mbal1 = Constraint(rule=m1)
model.mbal2 = Constraint(rule=m2)
model.mbal3 = Constraint(rule=m3)
model.mbal4 = Constraint(rule=m4)
model.mbal5 = Constraint(rule=m5)
model.mbal6 = Constraint(rule=m6)
model.mbal7 = Constraint(rule=m7)
