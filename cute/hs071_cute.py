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
#   Taken from cute suite. Formulated in Pyomo by Logan Barnes.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,4)
model.x = Var(model.N,bounds=(1,5))
model.x[1] = 1
model.x[2] = 5
model.x[3] = 5
model.x[4] = 1

model.obj = Objective(expr=model.x[1]*model.x[4]*(model.x[1] + model.x[2] + model.x[3]) + model.x[3])

def cons1_rule(model):
    expr = 1.0
    for i in range(1,5):
        expr *= model.x[i]
    return expr >= 25
model.constr1 = Constraint(rule=cons1_rule)

#model.constr1 = Constraint(expr=prod {i in 1..4} x[i] >= 25

model.constr2 = Constraint(expr=sum(model.x[i]**2 for i in model.N) == 40)
