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
#  Formulated in pyomo by Logan Barnes. Taken from:

# hs116.mod LQR2-MN-13-41
# Original AMPL coding by Elena Bobrovnikova (summer 1996 at Bell Labs).

# 3-stage membrane separation

# Ref.: W. Hock and K. Schittkowski, Test Examples for Nonlinear Programming
# Codes.  Lecture Notes in Economics and Mathematical Systems, v. 187,
# Springer-Verlag, New York, 1981, p. 124.

# Number of variables: 13
# Number of constraints: 41
# Objective linear
# Nonlinear constraints

from pyomo.core import *
model = ConcreteModel()
N = 13
model.I = RangeSet(1,N)
a = 0.002
b = 1.262626
c = 1.231059
d = 0.03475
e = 0.975
f = 0.00975

model.x = Var(model.I,bounds=(0,None))
model.x[1] = 0.5
model.x[2] = 0.8
model.x[3] = 0.9
model.x[4] = 0.1
model.x[5] = 0.14
model.x[6] = 0.5
model.x[7] = 489.0
model.x[8] = 80.0
model.x[9] = 650.0
model.x[10]= 450.0
model.x[11]= 150.0
model.x[12]= 150.0
model.x[13]= 150.0

model.obj = Objective(expr=model.x[11]+model.x[12]+model.x[13])

model.c1 = Constraint(expr=model.x[3]-model.x[2] >= 0)
model.c2 = Constraint(expr=model.x[2]-model.x[1] >= 0)
model.c3 = Constraint(expr=1-a*model.x[7]+a*model.x[8] >= 0)
model.c4 = Constraint(expr=model.x[11]+model.x[12]+model.x[13] >= 50)
model.c5 = Constraint(expr=model.x[13] - b * model.x[10] + c * model.x[3] * model.x[10] >= 0)
model.c6 = Constraint(expr=model.x[5] - d * model.x[2] - e * model.x[2] * model.x[5] + f * model.x[2]**2 >= 0)
model.c7 = Constraint(expr=model.x[6] - d * model.x[3] - e * model.x[3] * model.x[6] + f * model.x[3]**2 >= 0)
model.c8 = Constraint(expr=model.x[4] - d * model.x[1] - e * model.x[1] * model.x[4] + f * model.x[1]**2 >= 0)
model.c9 = Constraint(expr=model.x[12] - b * model.x[9] + c * model.x[2] * model.x[9] >= 0)
model.c10= Constraint(expr=model.x[11] - b * model.x[8] + c * model.x[1] * model.x[8] >= 0)
model.c11= Constraint(expr=model.x[5] * model.x[7] - model.x[1] * model.x[8] - model.x[4] * model.x[7] + model.x[4] * model.x[8] >= 0)
model.c12= Constraint(expr=1 - a * (model.x[2] * model.x[9] + model.x[5] * model.x[8] - model.x[1] * model.x[8] - model.x[6] * model.x[9]) - model.x[5] - model.x[6] >= 0)
model.c13= Constraint(expr=model.x[2] * model.x[9] - model.x[3] * model.x[10] - model.x[6] * model.x[9] - 500 * model.x[2] + 500 * model.x[6] + model.x[2] * model.x[10] >= 0)
model.c14= Constraint(expr=model.x[2] - 0.9 - a * (model.x[2] * model.x[10] - model.x[3] * model.x[10]) >= 0)
model.c15= Constraint(expr=model.x[11] + model.x[12] + model.x[13] <= 250)

model.b1=Constraint(expr= 0.1 <= model.x[1] <= 1)
model.b2=Constraint(expr= 0.1 <= model.x[2] <= 1)
model.b3=Constraint(expr= 0.1 <= model.x[3] <= 1)
model.b4=Constraint(expr= 0.0001 <= model.x[4] <= 0.1)
model.b5=Constraint(expr= 0.1 <= model.x[5] <= 0.9)
model.b6=Constraint(expr= 0.1 <= model.x[6] <= 0.9)
model.b7=Constraint(expr= 0.1 <= model.x[7] <= 1000)
model.b8=Constraint(expr= 0.1 <= model.x[8] <= 1000)
model.b9=Constraint(expr= 500 <= model.x[9] <= 1000)
model.b10=Constraint(expr= 0.1 <= model.x[10] <= 500)
model.b11=Constraint(expr= 1 <= model.x[11] <= 150)
model.b12=Constraint(expr= 0.0001 <= model.x[12] <= 150)
model.b13=Constraint(expr= 0.0001 <= model.x[13] <= 150)

