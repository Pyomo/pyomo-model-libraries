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
#   Taken from cute suite. Formulated in pyomo by Logan Barnes.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,5)
model.x = Var(model.N)
model.x[1] = -2
model.x[2] = 1.5
model.x[3] = 2
model.x[4] = -1
model.x[5] = -1

def obj_rule(model):
    expr = 1.0
    for i in model.N:
        expr *= model.x[i]
    return expr
model.obj = Objective(rule=obj_rule)

model.constr1 = Constraint(expr = sum(model.x[j]**2 for j in model.N) == 10)
model.constr2 = Constraint(expr = model.x[2]*model.x[3] - 5*model.x[4]*model.x[5] == 0)
model.constr3 = Constraint(expr = model.x[1]**3 + model.x[2]**3 == -1)
