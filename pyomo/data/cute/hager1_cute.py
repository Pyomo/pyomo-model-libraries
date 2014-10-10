#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Carl D. Laird and Daniel P. Word
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

#   Source: problem P1 in
#   W.W. Hager,
#   "Multiplier Methods for Nonlinear Optimal Control",
#   SIAM J. on Numerical Analysis 27(4): 1061-1080, 1990.

#   SIF input: Ph. Toint, March 1991.

#   classification SLR2-AN-V-V

from pyomo.core import *
import time

model = AbstractModel()

model.N = Param(initialize=5000)
model.Sx = RangeSet(0,model.N)
model.Sy = RangeSet(1,model.N)
model.x = Var(model.Sx,initialize=0.0)
model.u = Var(model.Sy,initialize=0.0)

def f(m):
    sum_exprs = []
    sum_coefs = []
    for i in m.Sy:
        sum_exprs.append((m.u[i]**2)/(2*value(m.N)))
    expr = 0.5*m.x[value(m.N)]**2 + sum(sum_exprs)
    return expr
model.f = Objective(rule=f,sense=minimize)

def cons1(m,i):
    expr = (value(m.N)-0.5)*m.x[i] + (-value(m.N) - 0.5)*m.x[i-1] - m.u[i]
    return (0,expr)
model.cons1 = Constraint(model.Sy,rule=cons1)

def cons2(m):
    return (1.0,m.x[0])
model.cons2 = Constraint(rule=cons2)
