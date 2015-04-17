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
model.x = Var(model.N,bounds=(0,1))
model.x[1] = 0.7
model.x[2] = 0.2
model.x[3] = 0.1

model.obj = Objective(expr=-32.174*(255*log((model.x[1]+model.x[2]+model.x[3]+0.03)/(0.09*model.x[1] + model.x[2] + model.x[3] + 0.03))\
      +280*log((model.x[2]+model.x[3]+0.03)/(0.07*model.x[2] + model.x[3] + 0.03))\
      +290*log((model.x[3]+0.03)/(0.13*model.x[3] + 0.03))))
     
model.constr1 = Constraint(expr = model.x[1] + model.x[2] + model.x[3] == 1)
