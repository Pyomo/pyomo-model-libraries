
#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, Brandon C. Barrera and Saumyajyoti Chaudhuri
# Taken from:
#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   A mistake in writing Hock and Schittkowski problem 108.
#   Source:
#   Ph. Toint.
#   classification QQR2-AY-9-13
#   SIF input: Ph. Toint, Apr 1990.
#   Number of variables
#   Parameters
#   Objective Function
#   Constraint function
#   Solution

from pyomo.core import *
model = AbstractModel()

model.n = Param(initialize=9)
model.x1 = Var(initialize=1.0)
model.x2 = Var(initialize=1.0)
model.x3 = Var(initialize=1.0)
model.x4 = Var(initialize=1.0)
model.x5 = Var(initialize=1.0)
model.x6 = Var(initialize=1.0)
model.x7 = Var(initialize=1.0)
model.x8 = Var(initialize=1.0)
model.x9 = Var(bounds=(0,None),initialize=1.0)

def obj(model):
    return -0.5*model.x1 * model.x4 + 0.5*model.x2 * model.x3 - \
    0.5*model.x3 * model.x9 + 0.5*model.x5 * model.x9 - 0.5*model.x5 * \
    model.x8 + 0.5*model.x6 * model.x7
model.obj = Objective(rule=obj, sense=minimize)

def c1(model):
    return (None, model.x3*model.x3 + model.x4*model.x4 - 1.0, 0)
model.c1 = Constraint(rule=c1)
def c2(model):
    return (None, model.x5*model.x5 + model.x6*model.x6 - 1.0, 0)
model.c2 = Constraint(rule=c2)
def c3(model):
    return (None, model.x9*model.x9 - 1.0, 0)
model.c3 = Constraint(rule=c3)
def c4(model):
    return (None, model.x1*model.x1 + (model.x2-model.x9)*(model.x2-model.x9) - 1.0, 0)
model.c4 = Constraint(rule=c4)
def c5(model):
    return (None, (model.x1-model.x5)*(model.x1-model.x5) + (model.x2-model.x6)*(model.x2-model.x6) - 1.0, 0)
model.c5 = Constraint(rule=c5)
def c6(model):
    return (None, (model.x1-model.x7)*(model.x1-model.x7) + (model.x2-model.x8)*(model.x2-model.x8) - 1.0, 0)
model.c6 = Constraint(rule=c6)
def c7(model):
    return (None, (model.x3-model.x5)*(model.x3-model.x5) + (model.x4-model.x6)*(model.x4-model.x6) - 1.0, 0)
model.c7 = Constraint(rule=c7)
def c8(model):
    return (None, (model.x3-model.x7)*(model.x3-model.x7) + (model.x4-model.x8)*(model.x4-model.x8) - 1.0, 0)
model.c8 = Constraint(rule=c8)
def c9(model):
    return (None, model.x7*model.x7 + model.x8*model.x9 - 1.0, 0)
model.c9 = Constraint(rule=c9)
def c10(model):
    return (0, model.x8*model.x9, None)
model.c10 = Constraint(rule=c10)
def c11(model):
    return (0, model.x5*model.x8 - model.x6*model.x7, None)
model.c11 = Constraint(rule=c11)
def c12(model):
    return (0, model.x1*model.x4 - model.x2*model.x3, None)
model.c12 = Constraint(rule=c12)
def c13(model):
    return (None, -model.x5*model.x9, 0)
model.c13 = Constraint(rule=c13)
