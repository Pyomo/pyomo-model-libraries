#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Formulated in pyomo by Logan Barnes and Gabe Hackebeil.
#
#  Take from CUTE test models

from pyomo.environ import *
model = AbstractModel()
PI = 4 * atan(1)
model.I = RangeSet(1,235)
model.N = RangeSet(1,8)
model.M = RangeSet(6,8)

x_init = {}
x_init[1] =   0.1
x_init[2] =   0.2
x_init[3] = 100.0
x_init[4] = 125.0
x_init[5] = 175.0
x_init[6] =  11.2
x_init[7] =  13.2
x_init[8] =  15.8

model.y = Param(model.I)

def x_init_rule(model,i):
    return x_init[i]
model.x = Var(model.N,initialize=x_init_rule)

def _a(model,i):
    return (model.x[1]/model.x[6]) * exp(-(model.y[i] - model.x[3])**2 / (2 * model.x[6]**2))
model.a = Expression(model.I, rule=_a)

def _b(model,i):
    return (model.x[2]/model.x[7]) * exp(-(model.y[i] - model.x[4])**2 / (2 * model.x[7]**2))
model.b = Expression(model.I, rule=_b)

def _c(model,i):
    return ((1 - model.x[2] - model.x[1]) / model.x[8]) * exp(-(model.y[i] - model.x[5])**2 / (2 * model.x[8]**2))
model.c = Expression(model.I, rule=_c)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj(model):
    return -sum(log((model.a[i] + model.b[i] + model.c[i]) / sqrt(2 * PI)) for i in model.I)
model.obj = Objective(rule=obj,sense=minimize)

def cons1(model):
    return 1 - model.x[1] - model.x[2] >= 0
model.C1 = Constraint(rule=cons1)
def bound1(model):
    return .001 <= model.x[1] <= .499
model.B1 = Constraint(rule=bound1)
def bound2(model):
    return .001 <= model.x[2] <= .449
model.B2 = Constraint(rule=bound2)
def bound3(model):
    return 100 <= model.x[3] <= 180
model.B3 = Constraint(rule=bound3)
def bound4(model):
    return 130 <= model.x[4] <= 210
model.B4 = Constraint(rule=bound4)
def bound5(model):
    return 170 <= model.x[5] <= 240
model.B5 = Constraint(rule=bound5)
def bound6(model):
    return 5 <= model.x[6] <= 25
model.B6 = Constraint(rule=bound6)
def bound7(model):
    return 5 <= model.x[7] <= 25
model.B7 = Constraint(rule=bound7)
def bound8(model):
    return 5 <= model.x[8] <= 25
model.B8 = Constraint(rule=bound8)
