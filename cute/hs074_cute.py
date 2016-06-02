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
model.a = 0.55
model.N = RangeSet(1,4)
model.x = Var(model.N,initialize=0.0)
model.x[1].setub(1200)
model.x[1].setlb(0)
model.x[2].setub(1200)
model.x[2].setlb(0)
model.x[3].setub(model.a)
model.x[3].setlb(-model.a)
model.x[4].setub(model.a)
model.x[4].setlb(-model.a)

model.obj = Objective(expr = 3.0*model.x[1] + 1.0e-6*model.x[1]**3 + 2*model.x[2] + 2.0e-6*model.x[2]**3/3)

model.constr1 = Constraint(expr = -model.a <= model.x[4] - model.x[3] <= model.a)
model.constr2 = Constraint(expr = model.x[1] == 1000*sin(-model.x[3] - 0.25) + 1000*sin(-model.x[4] - 0.25) + 894.8)
model.constr3 = Constraint(expr = model.x[2] == 1000*sin(model.x[3] - 0.25) + 1000*sin(model.x[3] - model.x[4] - 0.25) + 894.8)
model.constr4 = Constraint(expr = 0.0 == 1000*sin(model.x[4] - 0.25) + 1000*sin(model.x[4] - model.x[3] - 0.25) + 1294.8)
