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
#  Taken from cute suite. Formulated in Pyomo by Logan Barnes.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,2)
model.x = Var(model.N,within=NonNegativeReals)
model.x[1].setub(75.0)
model.x[2].setub(65.0)

model.x[1] = 90.0
model.x[2] = 10.0

model.obj = Objective(expr = -75.196 + 3.8112*model.x[1] + 0.0020567*model.x[1]**3 - 1.0345e-5*model.x[1]**4\
  + 6.8306*model.x[2] - 0.030234*model.x[1]*model.x[2] + 1.28134e-3*model.x[2]*model.x[1]**2\
  + 2.266e-7*model.x[1]**4*model.x[2] - 0.25645*model.x[2]**2 + 0.0034604*model.x[2]**3 - 1.3514e-5*model.x[2]**4\
  + 28.106/(model.x[2] + 1.0) + 5.2375e-6*model.x[1]**2*model.x[2]**2 + 6.3e-8*model.x[1]**3*model.x[2]**2\
  - 7e-10*model.x[1]**3*model.x[2]**3 - 3.405e-4*model.x[1]*model.x[2]**2 + 1.6638e-6*model.x[1]*model.x[2]**3\
  + 2.8673*exp(0.0005*model.x[1]*model.x[2]) - 3.5256e-5*model.x[1]**3*model.x[2]\
# the last term appears in CUTE but not in H&S
  -0.12694*model.x[1]**2)
  
model.constr1 = Constraint(expr=model.x[1]*model.x[2] >= 700)
model.constr2 = Constraint(expr=model.x[2] - (model.x[1]**2)/125.0 >= 0)
model.constr3 = Constraint(expr=(model.x[2] - 50)**2 - 5*(model.x[1] - 55) >= 0)
