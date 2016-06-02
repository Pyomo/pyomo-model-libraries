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
#  Taken from:

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

#   Source:  Problem 29 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   SIF input: Ph. Toint, Feb 1990.

#   classification NOR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()
N = 100
h = 1.0/(N+1)
model.M = RangeSet(1,N)
model.L = RangeSet(0,N+1)
def t_rule(model,i):
    return i*h
model.t = Param(model.M,initialize=t_rule)
def x_init_rule(model,i):
    if (i >= 1) and (i <= N):
        return model.t[i]*(model.t[i]-1.0)
    else:
        return 0.0
model.x = Var(model.L,initialize=x_init_rule)
model.x[0] = 0.0
model.x[0].fixed=True
model.x[N+1] = 0.0
model.x[N+1].fixed=True

model.f = Objective(expr=0)

def cons_rule(model,i):
    return ( model.x[i]+h*((1-model.t[i])*sum(model.t[j]*(model.x[j]+model.t[j]+1.0)**3 for j in range(1,i+1)) + model.t[i]*sum((1.0-model.t[j])*(model.x[j]+model.t[j]+1.0)**3 for j in range(i+1,N+1)))/2.0 ) == 0
model.cons = Constraint(model.M,rule=cons_rule)
