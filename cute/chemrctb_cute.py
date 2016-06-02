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

#   Source:  problem 8, eqs (8.10)--(8.11) in
#   J.J. More',
#   "A collection of nonlinear model problems"
#   Proceedings of the AMS-SIAM Summer seminar on the Computational
#   Solution of Nonlinear Systems of Equations, Colorado, 1988.
#   Argonne National Laboratory MCS-P60-0289, 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification NOR2-MN-V-V

from pyomo.core import *
model = AbstractModel()

n = 1000
model.n = Param(initialize=n)

model.pe = Param(initialize=5.0)
model.d = Param(initialize=0.135)
model.b = Param(initialize=0.5)
model.gamma = Param(initialize=25.0)

def h_rule(model):
    return 1/(float(n)-1)
model.h = Param(initialize=h_rule)
def ct1_rule(model):
    return -value(model.h)*value(model.pe)
model.ct1 = Param(initialize=ct1_rule)
def cti1_rule(model):
    return 1/value(model.h) + 1/((value(model.h)**2)*value(model.pe))
model.cti1 = Param(initialize=cti1_rule)
def cti_rule(model):
    return -1/value(model.h)-2/((value(model.h)**2)*value(model.pe))
model.cti = Param(initialize=cti_rule)

model.S = RangeSet(1,n)
model.t = Var(model.S, bounds=(0.0000001,None), initialize=1.0)

def f(model):
    return 0
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return (value(model.ct1)*model.t[2]-model.t[1]+value(model.h)*value(model.pe)) == 0
model.cons1 = Constraint(rule=cons1)

model.SS = RangeSet(2,model.n-1)
def cons2(model, i):
    return (value(model.d)*(value(model.b)+1-model.t[i])*exp(value(model.gamma)-value(model.gamma)/model.t[i])+value(model.cti1)*model.t[i-1]\
    +value(model.cti)*model.t[i]+model.t[i+1]/(value(model.h)**2*value(model.pe))) == 0
model.cons2 = Constraint(model.SS,rule=cons2)

def cons3(model):
    return (model.t[value(model.n)]-model.t[value(model.n)-1]) == 0
model.cons3 = Constraint(rule=cons3)
