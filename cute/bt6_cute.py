#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Juan Lopez and Gabe Hackebeil
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

#   Source: problem 6 in
#   P.T. Boggs and J.W. Tolle,
#   "A strategy for global convergence in a sequential 
#    quadratic programming algorithm",
#   SINUM 26(3), pp. 600-623, 1989.

#   The problem is not convex.

#   SIF input: Ph. Toint, June 1993.

#   classification OOR2-AY-5-2

from pyomo.core import *
model = ConcreteModel()

model.x = Var(RangeSet(1,5),initialize=2.0)


def f_rule(model):
    return (model.x[1]-1.0)**2 + (model.x[1]-model.x[2])**2 + (model.x[3]-1.0)**2 +\
    (model.x[4]-1.0)**4 + (model.x[5]-1.0)**6
model.f = Objective(rule=f_rule)

def con1(model):
    return model.x[4]*model.x[1]**2 + sin(model.x[4]-model.x[5]) == 2*(2.0)**0.5
    
def con2(model):
    return model.x[3]**4*model.x[2]**2 + model.x[2] == 8+(2.0)**0.5

model.cons1 = Constraint(rule=con1)
model.cons2 = Constraint(rule=con2)
