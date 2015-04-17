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
#   Taken from cute suite. Formulated in Pyomo by Logan Barnes

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,3)
model.x = Var(model.N,initialize=1.0,bounds=(1.0e-5,None))

model.obj = Objective(expr=5*model.x[1] + 50000.0/model.x[1] + 20*model.x[2] + 72000.0/model.x[2]\
     + 10*model.x[3] + 144000.0/model.x[3])

model.constr1 = Constraint(expr = 4.0/model.x[1] + 32.0/model.x[2] + 120.0/model.x[3] <= 1)
