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
#   Taken from H&S. Formulated in pyomo by Logan Barnes.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,6)
model.u = Param(model.N, mutable=True)
model.u[1] = 0.31
model.u[2] = 0.046
model.u[3] = 0.068
model.u[4] = 0.042
model.u[5] = 0.028
model.u[6] = 0.0134

def x_bounds_rule(model,j):
    return (0,value(model.u[j]))

model.x = Var(model.N,bounds=x_bounds_rule,initialize=0.0)

model.obj = Objective(expr=4.3*model.x[1] + 31.8*model.x[2] + 63.3*model.x[3]\
                     + 15.8*model.x[4] + 68.5*model.x[5] + 4.7*model.x[6])

model.constr1 = Constraint(expr=17.1*model.x[1] + 38.2*model.x[2] + 204.2*model.x[3]\
     + 212.3*model.x[4] + 623.4*model.x[5] + 1495.5*model.x[6]\
    - 169.0*model.x[1]*model.x[3] - 3580.0*model.x[3]*model.x[5]\
    - 3810.0*model.x[4]*model.x[5] - 18500.0*model.x[4]*model.x[6]
    - 24300.0*model.x[5]*model.x[6] >= 4.97)
model.constr2 = Constraint(expr=17.9*model.x[1] + 36.8*model.x[2] + 113.9*model.x[3]\
     + 169.7*model.x[4] + 337.8*model.x[5] + 1385.2*model.x[6]\
    - 139.0*model.x[1]*model.x[3] - 2450.0*model.x[4]*model.x[5] - 16600.0*model.x[4]*model.x[6]\
    - 17200.0*model.x[5]*model.x[6] >= -1.88)
model.constr3 = Constraint(expr=-273.0*model.x[2] - 70.0*model.x[4] - 819.0*model.x[5]\
    + 26000.0*model.x[4]*model.x[5] >= -69.08)
model.constr4 = Constraint(expr=159.9*model.x[1] - 311.0*model.x[2] + 587.0*model.x[4]\
     + 391.0*model.x[5] + 2198.0*model.x[6] - 14000.0*model.x[1]*model.x[6] >= -118.02)
