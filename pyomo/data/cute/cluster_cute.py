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

#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   Source:  problem 207 in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.
#   SIF input: Ph. Toint, Dec 1989.
#   classification NOR2-AN-2-2
#   Solution

from pyomo.core import *
model = ConcreteModel()

model.x1 = Var()
model.x2 = Var()

def obj_rule(model):
    return 0
model.obj = Objective(rule=obj_rule)

def con1(model):
    return ((model.x1-model.x2*model.x2) * (model.x1-sin(model.x2))) == 0
model.cons1 = Constraint(rule=con1)

def con2(model):
    return (((cos(model.x2))-model.x1) * (model.x2-cos(model.x1))) == 0
model.cons2 = Constraint(rule=con2)
