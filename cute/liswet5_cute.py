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
#  Formulated in pyomo by Logan Barnes. Taken from:

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
#   W. Li and J. Swetits,
#   "A Newton method for convex regression, data smoothing and
#   quadratic programming with bounded constraints",
#   SIAM J. Optimization 3 (3) pp 466-488, 1993.

#   SIF input: Nick Gould, August 1994.

#   classification QLR2-AN-V-V

from pyomo.core import *
model = AbstractModel()

K = 2
N = 10000

model.S = RangeSet(0,K)
model.R = RangeSet(1,N+K)
model.Q = RangeSet(1,N)

def B_rule(model,i):
    if i == 0:
        return 1.0
    else:
        return model.B[i-1]*i
model.B = Param(model.S,initialize=B_rule)

def C_rule(model,i):
    if i == 0:
        return 1.0
    else:
        return (-1.0)**i*model.B[K]/(model.B[i]*model.B[K-i])
model.C = Param(model.S,initialize=C_rule)

def T_rule(model,i):
    return (i-1.0)/(N+K-1.0)
model.T = Param(model.R,initialize=T_rule)

model.x = Var(model.R)

def f_rule(model):
    return sum(-(exp(model.T[i])+0.1*sin(i))*model.x[i] for i in model.R) +\
           sum(0.5*(exp(model.T[i])+0.1*sin(i))**2  for i in model.R) +\
           sum(0.5*model.x[i]**2 for i in model.R)
model.f = Objective(rule=f_rule,sense=minimize)

def cons1_rule(model,j):
    return sum(model.C[i]*model.x[j+K-i] for i in model.S) >= 0
model.cons1 = Constraint(model.Q,rule=cons1_rule)
