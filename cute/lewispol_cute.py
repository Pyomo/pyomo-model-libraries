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
#   A. Lewis, private communication.

#   SIF input: A.R. Conn and Ph. Toint, March 1990.

#   classification QOR2-AN-6-9

from pyomo.core import *
model = ConcreteModel()

N = 6
DEG = 3
PEN = 1e4

model.range1 = RangeSet(0,N-1)
model.range2 = RangeSet(0,DEG-1)

def c_index_init(model):
    return [(i,j) for i in range(0,DEG) for j in range(i,N)]
model.c_index = Set(dimen=2,ordered=True,initialize=c_index_init)

def c_rule(model,i,j):
    # This looks cute, but generally doesn't work: you are heavily
    # relying on the order in which the Param indices are constructed.
    #if i == 0:
    #    return 1.0
    #else:
    #    return model.c[i-1,j]*j
    return j**i
model.c = Param(model.c_index,initialize=c_rule)

def ct_rule(model,i):
    # This looks cute, but generally doesn't work: you are heavily
    # relying on the order in which the Param indices are constructed.
    #if i == 0:
    #    return -1.0
    #else:
    #    return model.ct[i-1] * (N-i+1)
    ans = -1.0
    for _i in range(i):
        ans *= N-_i
    return ans
model.ct = Param(model.range2,initialize=ct_rule)

model.a = Var(model.range1,bounds=(-10,10))
model.a[0] = -1.0
model.a[1] = 1.0
model.a[2] = 1.0
model.a[3] = 0.0
model.a[4] = 1.0
model.a[5] = -1.0

model.f = Objective(expr=sum(model.a[j]**2 for j in model.range1))

model.cons1 = Constraint(expr=sum(model.a[j]*model.c[0,j] for j in model.range1) - model.ct[0] == 0)

def cons2_rule(model,i):
    return sum(model.a[j]*model.c[i,j] for j in range(i,N)) - model.ct[i] == 0
model.cons2 = Constraint(range(1,DEG),rule=cons2_rule)

def cons3_rule(model,j):
    return (model.a[j]**3-model.a[j])/PEN == 0
model.cons3 = Constraint(model.range1,rule=cons3_rule)
