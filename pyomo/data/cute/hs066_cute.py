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
model.N = RangeSet(1,3)
model.x = Var(model.N)
model.x[1] = 0
model.x[2] = 1.05
model.x[3] = 2.9

model.obj = Objective(expr =0.2*model.x[3] - 0.8*model.x[1])

model.constr1 = Constraint(expr =model.x[2] - exp(model.x[1]) >= 0)
model.constr2 = Constraint(expr =model.x[3] - exp(model.x[2]) >= 0)
model.constr3 = Constraint(expr =   0 <= model.x[1] <= 100)
model.constr4 = Constraint(expr =   0 <= model.x[2] <= 100)
model.constr5 = Constraint(expr =   0 <= model.x[3] <=  10)
