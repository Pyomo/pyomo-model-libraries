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
#   Taken from H&S. Formulated in pyomo by Logan Barnes and Gabe Hackebeil.

from pyomo.core import *
model = ConcreteModel()
N = 8
model.I = RangeSet(1,N)
model.M = RangeSet(2,3)
model.L = RangeSet(4,8)
a = 0.0025
b = 0.01
c = 833.3325
d = 100.0
e = 83333.33
f = 1250.0
g = 1250000.0
h = 2500.0

model.x = Var(model.I)
model.x[1] = 5000.0
model.x[2] = 5000.0
model.x[3] = 5000.0
model.x[4] =  200.0
model.x[5] =  350.0
model.x[6] =  150.0
model.x[7] =  225.0
model.x[8] =  425.0

model.obj = Objective(expr = model.x[1] + model.x[2] + model.x[3])

model.c1 = Constraint(expr=1 - a * (model.x[4] + model.x[6]) >= 0)
model.c2 = Constraint(expr=1 - a * (model.x[5] + model.x[7] - model.x[4]) >= 0)
model.c3 = Constraint(expr=1 - b * (model.x[8] - model.x[5]) >= 0)
model.c4 = Constraint(expr=model.x[1] * model.x[6] - c * model.x[4] - d * model.x[1] + e >= 0)
model.c5 = Constraint(expr=model.x[2] * model.x[7] - f * model.x[5] - model.x[2] * model.x[4] + f *model.x[4] >= 0)
model.c6 = Constraint(expr=model.x[3] * model.x[8] - g - model.x[3] * model.x[5] + h * model.x[5] >= 0)
model.c7 = Constraint(expr=100 <= model.x[1] <= 10000)
def cons8(model,i):
    return 1000 <= model.x[i] <= 10000
model.c8 = Constraint(model.M,rule=cons8)
def cons9(model,i):
    return 10 <= model.x[i] <= 1000
model.c9 = Constraint(model.L,rule=cons9)
    
