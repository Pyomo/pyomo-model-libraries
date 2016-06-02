#   _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Taken from cute suite. Formulated in pyomo by Gabriel Hackebeil and Logan Barnes.

from pyomo.core import *
model = ConcreteModel()

model.x = Var(range(1,7),within=NonNegativeReals,initialize=0.0)
model.x[1].setub(1)
model.x[4].setub(1)

model.x[1] = 1.0
model.x[2] = 2.0
model.x[6] = 2.0

model.obj = Objective(expr=model.x[1] + 2.0*model.x[2] + 4.0*model.x[5] + exp(model.x[1]*model.x[4]))

model.constr1 = Constraint(expr=model.x[1] + 2*model.x[2] + 5*model.x[5] == 6)
model.constr2 = Constraint(expr=model.x[1] + model.x[2] + model.x[3] == 3)
model.constr3 = Constraint(expr=model.x[4] + model.x[5] + model.x[6] == 2)
model.constr4 = Constraint(expr=model.x[1] + model.x[4] == 1)
model.constr5 = Constraint(expr=model.x[2] + model.x[5] == 2)
model.constr6 = Constraint(expr=model.x[3] + model.x[6] == 2)
#model.constr7 = Constraint(expr=model.x[1] <= 1)
#model.constr8 = Constraint(expr=model.x[4] <= 1)

