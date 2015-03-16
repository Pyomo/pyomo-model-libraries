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
#  Formulated in pyomo by Logan Barnes and Gabe Hackebeil.
#
#  Taken from CUTE models

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,7)
model.l = Param(model.N, mutable=True)
model.a = Param(initialize=-0.25)
model.l[1] = 0.1
model.l[2] = 0.1
model.l[3] = 0.1
model.l[4] = 0.1
model.l[5] = 0.1
model.l[6] = 0.1
model.l[7] = 0.001

def x_bound_rule(model,j):
    return(value(model.l[j]),10.0)
model.x = Var(model.N,bounds=x_bound_rule,initialize=6.0)

model.obj = Objective(expr=10.0*model.x[1]*model.x[4]**2*model.x[7]**model.a/(model.x[2]*model.x[6]**3)+15.0*model.x[3]\
         *model.x[4]/(model.x[1]*model.x[2]**2*model.x[5]*model.x[7]**0.5)+20.0*model.x[2]*model.x[6]/(model.x[1]**2*model.x[4]*model.x[5]**2)\
         +25.0*model.x[1]**2*model.x[2]**2*model.x[5]**0.5*model.x[7]/(model.x[3]*model.x[6]**2))

model.c1 = Constraint(expr=1.0-.5*model.x[1]**0.5*model.x[7]/(model.x[3]*model.x[6]**2)-.7*model.x[1]**3*model.x[2]*model.x[6]*model.x[7]**.5/model.x[3]**2\
         -.2*model.x[3]*model.x[6]**(2.0/3.0)*model.x[7]**.25/(model.x[2]*model.x[4]**.5)>=0)
         
model.c2 = Constraint(expr=1.0-1.3*model.x[2]*model.x[6]/(model.x[1]**.5*model.x[3]*model.x[5])-.8*model.x[3]*model.x[6]**2/(model.x[4]*model.x[5])
         -3.1*model.x[2]**.5*model.x[6]**(1.0/3.0)/(model.x[1]*model.x[4]**2*model.x[5])>=0)

model.c3 = Constraint(expr=1.0-2.0*model.x[1]*model.x[5]*model.x[7]**(1.0/3.0)/(model.x[3]**1.5*model.x[6])-.1*model.x[2]*model.x[5]/\
         (model.x[3]**.5*model.x[6]*model.x[7]**.5)-model.x[2]*model.x[3]**.5*model.x[5]/model.x[1]-\
         .65*model.x[3]*model.x[5]*model.x[7]/(model.x[2]**2*model.x[6])>=0)

model.c4 = Constraint(expr=1.0-.2*model.x[2]*model.x[5]**.5*model.x[7]**(1.0/3.0)/(model.x[1]**2*model.x[4])-.3*model.x[1]**.5*model.x[2]**2\
         *model.x[3]*model.x[4]**(1.0/3.0)*model.x[7]**.25/model.x[5]**(2.0/3.0)-.4*model.x[3]*model.x[5]*model.x[7]**.75/\
         (model.x[1]**3*model.x[2]**2)-.5*model.x[4]*model.x[7]**.5/model.x[3]**2>=0)
         
model.c5 = Constraint(expr=10.0*model.x[1]*model.x[4]**2*model.x[7]**model.a/(model.x[2]*model.x[6]**3)+15*model.x[3]\
         *model.x[4]/(model.x[1]*model.x[2]**2*model.x[5]*model.x[7]**0.5)+20*model.x[2]*model.x[6]/(model.x[1]**2*model.x[4]*model.x[5]**2)\
         +25.0*model.x[1]**2*model.x[2]**2*model.x[5]**0.5*model.x[7]/(model.x[3]*model.x[6]**2)>=100.0)

model.c6 = Constraint(expr=10*model.x[1]*model.x[4]**2*model.x[7]**model.a/(model.x[2]*model.x[6]**3)+15*model.x[3]
         *model.x[4]/(model.x[1]*model.x[2]**2*model.x[5]*model.x[7]**0.5)+20*model.x[2]*model.x[6]/(model.x[1]**2*model.x[4]*model.x[5]**2)
         +25.0*model.x[1]**2*model.x[2]**2*model.x[5]**0.5*model.x[7]/(model.x[3]*model.x[6]**2)<=3000.0)
