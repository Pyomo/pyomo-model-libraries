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
model.N = RangeSet(1,8)
model.x = Var(model.N,bounds=(0.1,10.0))
model.x[1] = 6.0
model.x[2] = 3.0
model.x[3] = 0.4
model.x[4] = 0.2
model.x[5] = 6.0
model.x[6] = 6.0
model.x[7] = 1.0
model.x[8] = 0.5

model.obj = Objective(expr=(0.4*model.x[1]**0.67) * (model.x[7]**-0.67) + (0.4*model.x[2]**0.67)\
    * (model.x[8]**-0.67) + 10 - model.x[1] - model.x[2])

model.c1 = Constraint(expr=1-0.0588*model.x[5]*model.x[7]-.1*model.x[1]>=0)
model.c2 = Constraint(expr=1-0.0588*model.x[6]*model.x[8]-.1*model.x[1]-.1*model.x[2]>=0)
model.c3 = Constraint(expr=1-(4.0*model.x[3]/model.x[5])-\
    (2.0/(model.x[3]**0.71*model.x[5]))-(0.0588*model.x[7]/(model.x[3]**1.3))>=0)
model.c4 = Constraint(expr=1-4.0*model.x[4]/model.x[6]-\
    (2.0/(model.x[4]**0.71*model.x[6]))-(0.0588*model.x[8]/(model.x[4]**1.3))>=0)
model.c5 = Constraint(expr=0.4*(model.x[1]**0.67)*(model.x[7]**(-0.67))\
    +.4*(model.x[2]**0.67)*(model.x[8]**(-0.67))+10-model.x[1]-model.x[2]>=0.1)
model.c6 = Constraint(expr=0.4*(model.x[1]**0.67)*(model.x[7]**(-0.67))\
    +.4*(model.x[2]**0.67)*(model.x[8]**(-0.67))+10-model.x[1]-model.x[2]<=4.2)
