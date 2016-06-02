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
model.x = Var(model.N,initialize=2.0)

model.obj = Objective(expr = (model.x[1]-1)**2 + (model.x[1] - model.x[2])**2\
                                 + (model.x[3]-1)**2 + (model.x[4]-1)**4 + (model.x[5]-1)**6)
                                 
model.constr1 = Constraint(expr = model.x[1]**2*model.x[4] + sin(model.x[4]-model.x[5]) == 2*sqrt(2))
model.constr2 = Constraint(expr = model.x[2] + model.x[3]**4*model.x[4]**2 == 8 + sqrt(2))
