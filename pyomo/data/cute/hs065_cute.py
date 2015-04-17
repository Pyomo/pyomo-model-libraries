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
model.x[1] = -5
model.x[2] = 5
model.x[3] = 0

model.obj = Objective(expr =(model.x[1] - model.x[2])**2 + (model.x[1] + model.x[2] - 10.0)**2/9.0\
    + (model.x[3] - 5)**2)

model.constr1 = Constraint(expr=model.x[1]**2 + model.x[2]**2 + model.x[3]**2 <= 48)
model.constr2 = Constraint(expr=-4.5 <= model.x[1] <= 4.5)
model.constr3 = Constraint(expr=-4.5 <= model.x[2] <= 4.5)
model.constr4 = Constraint(expr= -5 <= model.x[3] <=   5)
