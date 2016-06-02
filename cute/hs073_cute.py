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
model.x = Var(model.N,initialize=1.0,within=NonNegativeReals)

model.obj = Objective(expr = 24.55*model.x[1] + 26.75*model.x[2] + 39*model.x[3] + 40.50*model.x[4])

model.constr1 = Constraint(expr = 2.3*model.x[1] + 5.6*model.x[2] + 11.1*model.x[3] + 1.3*model.x[4] >= 5)
model.constr2 = Constraint(expr = -(21.0 + 1.645*sqrt(0.28*model.x[1]**2 + 0.19*model.x[2]**2 + 20.5*model.x[3]**2 + 0.62*model.x[4]**2)) \
                                  +(12.0*model.x[1] + 11.9*model.x[2] + 41.8*model.x[3] + 52.1*model.x[4]) \
                                  >= 0.0)
model.constr3 = Constraint(expr = sum(model.x[j] for j in model.N) == 1)
