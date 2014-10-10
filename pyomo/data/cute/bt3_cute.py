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

#   Source: problem 3 in
#   P.T. Boggs and J.W. Tolle,
#   "A strategy for global convergence in a sequential
#    quadratic programming algorithm",
#   SINUM 26(3), pp. 600-623, 1989.

#   The problem is convex.

#   SIF input: Ph. Toint, June 1993.

#   classification SLR2-AY-5-3

from pyomo.core import *
model = AbstractModel()

model.S = RangeSet(1,5)
model.x = Var(model.S, initialize=20.0)

def f(model):
    return (model.x[1]-model.x[2])**2+(model.x[2]+model.x[3]-2)**2+(model.x[4]-1)**2+(model.x[5]-1)**2
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return model.x[1]+3*model.x[2] == 0
def cons2(model):
    return model.x[3]+model.x[4]-2*model.x[5] == 0
def cons3(model):
    return model.x[2]-model.x[5] == 0
model.cons1 = Constraint(rule=cons1)
model.cons2 = Constraint(rule=cons2)
model.cons3 = Constraint(rule=cons3)
