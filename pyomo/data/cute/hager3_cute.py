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

#   Source: problem P3 in
#   W.W. Hager,
#   "Multiplier Methods for Nonlinear Optimal Control",
#   SIAM J. on Numercal Analysis 27(4): 1061-1080, 1990.

#   SIF input: Ph. Toint, March 1991.

#   classification SLR2-AY-V-V

from pyomo.core import *
model = ConcreteModel()

model.n = Param(initialize=5000.0)
model.h = Param(initialize=1.0/5000.0)

model.Sx = RangeSet(0,model.n)
model.Su = RangeSet(1,model.n)

model.x = Var(model.Sx, initialize=0.0)
model.u = Var(model.Su, initialize=0.0)

def f(m):
    sum_expr_1 = 0
    sum_expr_2 = 0
    for i in m.Su:
        sum_expr_1 += (value(m.h))*(0.625*(m.x[i-1]**2 + m.x[i-1]*m.x[i] + m.x[i]**2) + ((m.x[i-1]+m.x[i])*m.u[i]))/8
        sum_expr_2 += (value(m.h)*(m.u[i])**2)/4
    exp = sum_expr_1 + sum_expr_2
    return exp
model.f = Objective(rule=f,sense=minimize)

def cons1(m,i):
    exp = (value(m.n)-0.25)*m.x[i] - (value(m.n)+0.25)*m.x[i-1] - m.u[i]
    return (0,exp)
model.cons1 = Constraint(model.Su,rule=cons1)

model.x[0] = 1.0
model.x[0].fixed = True
