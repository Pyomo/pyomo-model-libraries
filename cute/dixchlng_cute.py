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

#   Source:
#   L.C.W. Dixon, personnal communication, Jan 1991.

#   SIF input: Ph. Toint, Feb 1991.

#   classification SOR2-AN-10-5

from pyomo.environ import *
model = AbstractModel()

model.S = RangeSet(1,10)
model.x_init = Param(model.S)
def xit(model, i):
    return value(model.x_init[i])
model.x = Var(model.S, initialize=xit)

model.SS = RangeSet(1,7)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    es1 = sum ([100*(model.x[i+1]-model.x[i]**2)**2 for i in model.SS])
    es2 = sum ([(model.x[i]-1)**2 for i in model.SS])
    es3 = sum ([90*(model.x[i+3]-model.x[i+2]**2)**2 for i in model.SS])
    es4 = sum ([(model.x[i+2]-1)**2 for i in model.SS])
    es5 = sum ([10.1*(model.x[i+1]-1)**2 for i in model.SS])
    es6 = sum ([10.1*(model.x[i+3]-1)**2 for i in model.SS])
    es7 = sum ([19.8*(model.x[i+1]-1)*(model.x[i+3]-1) for i in model.SS])
    return es1 + es2 + es3 + es4 + es5 + es6 + es7
model.f = Objective(rule=f,sense=minimize)


def cons1_rule(model,i):
    expr = 1.0
    for j in range(1,i+1):
        expr *= model.x[j]
    return expr-1.0 == 0
model.cons1 = Constraint([2,4,6,8,10],rule=cons1_rule)
"""
def cons1(model):
    ep1 = model.x[1] * model.x[2] - 1
    return ep1 == 0
model.cons1 = Constraint(rule=cons1)
def cons2(model):
    ep2 = model.x[1] * model.x[2] * model.x[3] * model.x[4]
    return ep2 - 1 == 0
model.cons2 = Constraint(rule=cons2)
def cons3(model):
    ep3 = model.x[1] * model.x[2] * model.x[3] * model.x[4] * model.x[5] * model.x[6]
    return ep3 - 1 == 0
model.cons3 = Constraint(rule=cons3)
def cons4(model):
    ep4 = model.x[1] * model.x[2] * model.x[3] * model.x[4] * model.x[5] * model.x[6] * model.x[7] * model.x[8]
    return ep4 - 1 == 0
model.cons4 = Constraint(rule=cons4)
def cons5(model):
    ep5 = model.x[1] * model.x[2] * model.x[3] * model.x[4] * model.x[5] * model.x[6] * model.x[7] * model.x[8] * model.x[9] * model.x[10]
    return ep5 - 1 == 0
model.cons5 = Constraint(rule=cons5)
"""
