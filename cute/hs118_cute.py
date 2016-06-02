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
#  Formulated in pyomo by Logan Barnes.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,15)
model.M = RangeSet(1,4)
model.L = RangeSet(0,4)
model.P = RangeSet(4,15)

model.l = Param(model.N,mutable=True)
model.l[1] =  8.0
model.l[2] = 43.0
model.l[3] =  3.0
for j in model.P:
    model.l[j] = 0.0

model.u = Param(model.N,mutable=True)
model.u[1] = 21.0
model.u[2] = 57.0
model.u[3] = 16.0
for k in model.M:
    model.u[3*k+1] = 90.0
    model.u[3*k+2] = 120.0
    model.u[3*k+3] = 60.0

def x_bound_rule(model,i):
    return (value(model.l[i]),value(model.u[i]))

model.x = Var(model.N,bounds=x_bound_rule)

model.x[1] = 20
model.x[2] = 55
model.x[3] = 15
model.x[4] = 20
model.x[5] = 60
model.x[6] = 20
model.x[7] = 20
model.x[8] = 60
model.x[9] = 20
model.x[10] = 20
model.x[11] = 60
model.x[12] = 20
model.x[13] = 20
model.x[14] = 60
model.x[15] = 20

model.obj = Objective(expr=sum((2.3*model.x[3*k+1] + 0.0001*model.x[3*k+1]**2 + 1.7*model.x[3*k+2] + 0.0001*model.x[3*k+2]**2 + 2.2*model.x[3*k+3] + 0.00015*model.x[3*k+3]**2) for k in model.L))

def cons1_rule(model,j):
    return 0 <= model.x[3*j+1] - model.x[3*j-2] + 7 <= 13
model.constr1 = Constraint(model.M,rule=cons1_rule)
def cons2_rule(model,j):
    return 0 <= model.x[3*j+2] - model.x[3*j-1] + 7 <= 14
model.constr2 = Constraint(model.M,rule=cons2_rule)
def cons3_rule(model,j):
    return 0 <= model.x[3*j+3] - model.x[3*j] + 7 <= 13
model.constr3 = Constraint(model.M,rule=cons3_rule)

model.constr4 = Constraint(expr= model.x[1] + model.x[2] + model.x[3] >= 60)
model.constr5 = Constraint(expr= model.x[4] + model.x[5] + model.x[6] >= 50)
model.constr6 = Constraint(expr= model.x[7] + model.x[8] + model.x[9] >= 70)
model.constr7 = Constraint(expr= model.x[10] + model.x[11] + model.x[12] >= 85)
model.constr8 = Constraint(expr= model.x[13] + model.x[14] + model.x[15] >= 100)

