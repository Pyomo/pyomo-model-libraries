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

#   Source:
#   A. R. Conn, N. I. M. Gould and Ph. L. Toint,
#   "LANCELOT: a Fortran package for large-scale nonlinear optimization
#    (Release A)", Springer Series in Computational Mathematics 17,
#   Springer Verlag, 1992

#   SIF input: A. R. Conn, Nick Gould and Ph. L. Toint, June 1994.

#   classification OOR2-AY-V-V

from pyomo.core import *

model = AbstractModel()

model.n = Param(initialize=100)
model.S = RangeSet(1,model.n)

model.y = Var()
def bounds(model,i):
    return (-1,i)
model.x = Var(model.S,initialize=0.5,bounds=bounds)

def f(m):
    expr = 0.5*( (m.x[1] - m.x[value(m.n)]) * m.x[2] + m.y )**2
    return expr
model.f = Objective(rule=f,sense=minimize)

def consq(m,i):
    expr = m.y + m.x[1]*m.x[i+1] + (1+float(2)/float(i))*m.x[i]*m.x[value(m.n)]
    return (None,expr,0.0)
model.consq = Constraint(RangeSet(1,model.n-1),rule=consq)

def conss(m,i):
    expr = (sin(m.x[i]))**2
    return (None,expr,0.5)
model.conss = Constraint(model.S,rule=conss)

def eq(m):
    return (1.0, (m.x[1]+m.x[value(m.n)])**2)
model.eq = Constraint(rule=eq)
