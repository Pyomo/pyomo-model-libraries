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

#   classification OLR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()

n = 1000
nx = 5
ny = 10

model.S1 = RangeSet(1,ny)
model.S2 = RangeSet(1,nx)

def b_rule(model, i, j):
    return float(i-j)/float(nx+ny)
model.b = Param(model.S1,model.S2,initialize=b_rule)

model.S3 = RangeSet(1,n-1)
model.S4 = RangeSet(1,n)
model.S5 = RangeSet(2,ny-1)

model.x = Var(model.S3,model.S2)
model.y = Var(model.S4,model.S1)

def f(model):
    sum1 = sum((model.x[t,i] + 0.5)**4 for t in model.S3 for i in model.S2)
    sum2 = sum((model.y[t,i] + 0.25)**4 for t in model.S4 for i in model.S1)
    return sum1 + sum2
model.f = Objective(rule=f,sense=minimize)

def cons1(model, t):
    sc1 = sum(value(model.b[1,i])*model.x[t,i] for i in model.S2)
    return 0.5*model.y[t,1] + 0.25*model.y[t,2] - model.y[t+1,1] + sc1 == 0
model.cons1 = Constraint(model.S3,rule=cons1)
def cons2(model, t, j):
    sc2 = sum(value(model.b[j,i])*model.x[t,i] for i in model.S2)
    return -model.y[t+1,j] + 0.5*model.y[t,j] - 0.25*model.y[t,j-1] + 0.25*model.y[t,j+1] + sc2 == 0
model.cons2 = Constraint(model.S3,model.S5,rule=cons2)
def cons3(model, t):
    sc3 = sum(model.b[ny,i]*model.x[t,i] for i in model.S2)
    return 0.5*model.y[t,ny] - 0.25*model.y[t,ny-1] - model.y[t+1,ny] + sc3 == 0
model.cons3 = Constraint(model.S3,rule=cons3)

for idx in model.S1:
    model.y[1,idx] = 0.0
    model.y[1,idx].fixed = True

