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
#  Formulated in pyomo by Logan Barnes and Gabe Hackebeil. Taken from:

# hs114.mod QOR2-MY-10-31
# Original AMPL coding by Elena Bobrovnikova (summer 1996 at Bell Labs).

# Alkylation process

# Ref.: W. Hock and K. Schittkowski, Test Examples for Nonlinear Programming
# Codes.  Lecture Notes in Economics and Mathematical Systems, v. 187,
# Springer-Verlag, New York, 1981, p. 123.

# Number of variables:  10
# Number of constraints:  31
# Objective separable
# Objective nonconvex
# Nonlinear constraints

from pyomo.environ import *
model = AbstractModel()
n = 10
model.I = RangeSet(1,n)
model.lb = Param(model.I)
model.ub = Param(model.I)
model.x0 = Param(model.I)
a = .99
b = .90

def x_bounds_rule(model,i):
    return (value(model.lb[i]),value(model.ub[i]))
def x_init_rule(model,i):
    return model.x0[i]
model.x = Var(model.I,bounds=x_bounds_rule,initialize=x_init_rule)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return 5.04*model.x[1] + .035*model.x[2] + 10.0*model.x[3] + 3.36*model.x[5] - .063*model.x[4]*model.x[7]
model.obj = Objective(rule=obj_rule,sense=minimize)

def _G1(model):
    return 35.82 - 0.222*model.x[10] - b*model.x[9]
model.G1 = Expression(rule=_G1)
def _G2(model):
    return -133 + 3*model.x[7] - a*model.x[10]
model.G2 = Expression(rule=_G2)
def _G5(model):
    return 1.12*model.x[1] + .13167*model.x[1]*model.x[8] - .00667*model.x[1]*model.x[8]**2 - a*model.x[4]
model.G5 = Expression(rule=_G5)
def _G6(model):
    return 57.425 + 1.098*model.x[8] - .038*model.x[8]**2 + .325*model.x[6] - a*model.x[7]
model.G6 = Expression(rule=_G6)

def cons1_rule(model):
    return model.G1 >= 0 
model.g1 = Constraint(rule=cons1_rule)
def cons2_rule(model):
    return model.G2 >= 0
model.g2 = Constraint(rule=cons2_rule)
def cons3_rule(model):
    return -model.G1 + model.x[9]*(1/b - b) >= 0
model.g3 = Constraint(rule=cons3_rule)
def cons4_rule(model):
    return -model.G2 + (1/a - a)*model.x[10] >= 0
model.g4 = Constraint(rule=cons4_rule)
def cons5_rule(model):
    return model.G5 >= 0
model.g5 = Constraint(rule=cons5_rule)
def cons6_rule(model):
    return model.G6 >= 0
model.g6 = Constraint(rule=cons6_rule)
def cons7_rule(model):
    return -model.G5 + (1/a - a)*model.x[4] >= 0
model.g7 = Constraint(rule=cons7_rule)
def cons8_rule(model):
    return -model.G6 + (1/a - a)*model.x[7] >= 0
model.g8 = Constraint(rule=cons8_rule)
def cons9_rule(model):
    return 1.22*model.x[4] - model.x[1] - model.x[5] == 0
model.g9 = Constraint(rule=cons9_rule)
def cons10_rule(model):
    return 98000.0*model.x[3]/(model.x[4]*model.x[9] + 1000*model.x[3]) - model.x[6] == 0
model.g10= Constraint(rule=cons10_rule)
def cons11_rule(model):
    return (model.x[2] + model.x[5])/model.x[1] - model.x[8] == 0
model.g11= Constraint(rule=cons11_rule)
