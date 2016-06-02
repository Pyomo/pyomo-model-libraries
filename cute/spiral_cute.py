#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, Brandon C. Barrera and Saumyajyoti Chaudhuri
#Taken from:
##
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   A nonlinear minmax problem.
#   Source:
#   E. Polak, J.E. Higgins and D. Mayne,
#   "A barrier function for minmax problems",
#   Mathematical Programming, vol.54(2), pp. 155-176, 1992.
#   SIF input: Ph. Toint, April 1992.
#   classification LOR2-AN-3-2
#   Solution

from pyomo.core import *
model = AbstractModel()

model.x1 = Var(initialize=1.41831)
model.x2 = Var(initialize=-4.79462)
model.u = Var (initialize = 1.0)

def obj(model):
    return model.u
model.obj = Objective(rule=obj,sense=minimize)

def c1(model):
    return 0 <= -(model.x1-(sqrt((model.x1*model.x1)+(model.x2*model.x2)))*cos((sqrt((model.x1*model.x1)+(model.x2*model.x2))))) * (model.x1\
    -(sqrt((model.x1*model.x1)+(model.x2*model.x2)))*cos((sqrt((model.x1*model.x1)+(model.x2*model.x2))))) - 0.0050*model.x1 * model.x1 - \
    0.0050*model.x2 * model.x2 + model.u
model.c1 = Constraint(rule=c1)

def c2(model):
    return 0 <= -(model.x2-(sqrt((model.x1*model.x1)+(model.x2*model.x2)))*sin((sqrt((model.x1*model.x1)+(model.x2*model.x2))))) * \
    (model.x2-(sqrt((model.x1*model.x1)+(model.x2*model.x2)))*sin((sqrt((model.x1*model.x1)+(model.x2*model.x2))))) - 0.0050*model.x1 * model.x1 - \
    0.0050*model.x2 * model.x2 + model.u
model.c2 = Constraint(rule=c2)
