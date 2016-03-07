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
#   Taken from cute suite. Formulated in Pyomo by Logan Barnes and Gabriel Hackebeil.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,8)
model.M = RangeSet(1,14)
model.x1 = Var(bounds=(1.0e-5,2.0e+3))
model.x2 = Var(bounds=(1.0e-5,1.6e+4))
model.x3 = Var(bounds=(1.0e-5,1.2e+2))
model.y  = Var(model.N,initialize=0.0)
model.a  = Param(model.M,mutable=True)
model.x1 = 1745.0
model.x2 = 12000.0
model.x3 = 110.0
model.a[1]=    0.0
model.a[2]=    0.0
model.a[3]=   85.0
model.a[4]=   90.0
model.a[5]=    3.0
model.a[6]=    0.01
model.a[7]=  145.0
model.a[8]= 5000.0
model.a[9]= 2000.0
model.a[10]=      93.0
model.a[11]=      95.0
model.a[12]=      12.0
model.a[13]=       4.0
model.a[14]=     162.0

model.obj = Objective(expr =-(0.063*model.y[2]*model.y[5] - 5.04*model.x1 - 3.36*model.y[3] - 0.035*model.x2 - 10*model.x3))

model.constr1 = Constraint(RangeSet(1,7),rule=lambda model,i: model.y[i+1] >= model.a[i])
model.constr2 = Constraint(RangeSet(8,14),rule=lambda model,i: model.a[i] >= model.y[i-6])
model.constr3 = Constraint(expr=model.y[3] == 1.22*model.y[2] - model.x1)
model.constr4 = Constraint(expr=model.y[6] == (model.x2+model.y[3])/model.x1)
model.constr5 = Constraint(expr=model.y[2] == 0.01*model.x1*(112 + 13.167*model.y[6] - 0.6667*model.y[6]**2))
model.constr6 = Constraint(expr=model.y[5] == 86.35 + 1.098*model.y[6] - 0.038*model.y[6]**2 + 0.325*(model.y[4]-89))
model.constr7 = Constraint(expr=model.y[8] == 3.0*model.y[5] - 133.0)
model.constr8 = Constraint(expr=model.y[7] == 35.82 - 0.222*model.y[8])
model.constr9 = Constraint(expr=model.y[4] == 98000.0*model.x3/(model.y[2]*model.y[7] + 1000.0*model.x3))

model.y[2] = 1.6*value(model.x1)
while (1):
    y2old = model.y[2].value
    model.y[3] = 1.22 * model.y[2].value - model.x1.value
    model.y[6] = (model.x2.value + model.y[3].value) / model.x1.value
    model.y[2] = 0.01 * model.x1.value * \
                 (112.0 + \
                  13.167 * model.y[6].value - \
                  0.6667 * model.y[6].value**2)
    if abs(y2old - model.y[2].value) < 0.001:
        break

model.y[4] = 93.0
while (1):
    y4old = model.y[4].value
    model.y[5] = 86.35 + \
                 1.098 * model.y[6].value - \
                 0.038 * model.y[6].value**2 + \
                 0.325 * (model.y[4].value - 89)
    model.y[8] = 3 * model.y[5].value - 133
    model.y[7] = 35.82 - 0.222 * model.y[8].value
    model.y[4] = 98000.0 * model.x3.value / \
                 (model.y[2].value * model.y[7].value + 1000 * model.x3.value)
    if abs(y4old - model.y[4].value) < 0.001:
        break
