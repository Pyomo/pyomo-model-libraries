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
#   P.N. Brown and Y. Saad,
#   "Hybrid Krylov Methods for Nonlinear Systems of Equations",
#   SIAM J. Sci. Stat. Comput. 11, pp. 450-481, 1990.
#   The boundary conditions have been set according to
#   I.E. Kaporin and O. Axelsson,
#   "On a class of nonlinear equation solvers based on the residual norm
#   reduction over a sequence of affine subspaces",
#   SIAM J, Sci. Comput. 16(1), 1995.

#   SIF input: Ph. Toint, Jan 1995.

#   classification NQR2-MY-V-V

from pyomo.core import *
model = ConcreteModel()
M = 100
model.M = Param(initialize=M)
model.H = Param(initialize=1.0/(M+2.0))
model.RE = Param(initialize=4500.0)

model.S1 = RangeSet(-1,M+2)
model.S2 = RangeSet(1,M)

model.y = Var(model.S1,model.S1,initialize=0.0)

def f(model):
    return 0
model.f = Objective(rule=f,sense=minimize)

def cons(model, i, j):
    return (20*model.y[i,j]-8*model.y[i-1,j]-8*model.y[i+1,j]\
    -8*model.y[i,j-1]-8*model.y[i,j+1]+2*model.y[i-1,j+1]+2*model.y[i+1,j-1]+2*model.y[i-1,j-1]+2*model.y[i+1,j+1] +\
    model.y[i-2,j] + model.y[i+2,j] + model.y[i,j-2] + model.y[i,j+2] + (model.RE/4.0)*(model.y[i,j+1]-model.y[i,j-1])\
    *(model.y[i-2,j]+model.y[i-1,j-1]+model.y[i-1,j+1]-4*model.y[i-1,j]-4*model.y[i+1,j]-model.y[i+1,j-1] \
    -model.y[i+1,j+1] - model.y[i+2,j]) - (model.RE/4.0)*(model.y[i+1,j]-model.y[i-1,j])*\
    (model.y[i,j-2]+model.y[i-1,j-1]+model.y[i+1,j-1]-4*model.y[i,j-1]-4*model.y[i,j+1]-model.y[i-1,j+1]-model.y[i+1,j+1] - model.y[i,j+2])) == 0
model.cons = Constraint(model.S2,model.S2,rule=cons)

for j in model.S1:
    model.y[-1,j] = 0.0
    model.y[-1,j].fixed = True

    model.y[0,j] = 0.0
    model.y[0,j].fixed = True

for i in model.S2:
    model.y[i,-1] = 0.0
    model.y[i,-1].fixed = True

    model.y[i,0] = 0.0
    model.y[i,0].fixed = True

    model.y[i,value(model.M)+1] = 0.0
    model.y[i,value(model.M)+1].fixed = True

    model.y[i,value(model.M)+2] = 0.0
    model.y[i,value(model.M)+2].fixed = True

for j in model.S1:
    model.y[value(model.M)+1,j] = -value(model.H)/2.0
    model.y[value(model.M)+1,j].fixed = True

    model.y[value(model.M)+2,j] = value(model.H)/2.0
    model.y[value(model.M)+2,j].fixed = True

