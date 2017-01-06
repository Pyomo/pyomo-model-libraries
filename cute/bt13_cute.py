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

#   Source: problem 13 in
#   P.T. Boggs and J.W. Tolle,
#   "A strategy for global convergence in a sequential
#    quadratic programming algorithm",
#   SINUM 26(3), pp. 600-623, 1989.

#   The problem has been modified by adding a lower bound of 0.0 on x5
#   in order to make it bounded below.

#   The problem is not convex.

#   SIF input: Ph. Toint, June 1993.

#   classification LQR2-AY-5-1

from pyomo.environ import *
model = AbstractModel()

model.N = Param()
model.S = RangeSet(1,model.N)
model.x_init = Param(model.S)
def xinit(model, i):
    return value(model.x_init[i])
model.x = Var(model.S, initialize=xinit)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    return model.x[5]
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return model.x[1]**2+(model.x[1]-2*model.x[2])**2 + (model.x[2]-3*model.x[3])**2+(model.x[3]-4*model.x[4])**2-model.x[5]**2 == 0
model.cons1 = Constraint(rule=cons1)

def cons2(model):
    return model.x[5] >= 0
model.cons2 = Constraint(rule=cons2)
