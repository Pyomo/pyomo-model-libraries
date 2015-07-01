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
c = (48.4/50.176)*sin(.25)
d = (48.4/50.176)*cos(.25)
model.N = RangeSet(1,9)
model.x = Var(model.N)
model.x[1] = 0.8
model.x[2] = 0.8
model.x[3] = 0.2
model.x[4] = 0.2
model.x[5] = 1.0454
model.x[6] = 1.0454
model.x[7] = 0.0
model.x[8] = 0.0

def _y1(model):
    return sin(model.x[8])
model.y1 = Expression(rule=_y1)
def _y2(model):
    return cos(model.x[8])
model.y2 = Expression(rule=_y2)
def _y3(model):
    return sin(model.x[9])
model.y3 = Expression(rule=_y3)
def _y4(model):
    return cos(model.x[9])
model.y4 = Expression(rule=_y4)
def _y5(model):
    return sin(model.x[8] - model.x[9])
model.y5 = Expression(rule=_y5)
def _y6(model):
    return cos(model.x[8] - model.x[9])
model.y6 = Expression(rule=_y6)

model.obj = Objective(expr=3000*model.x[1]+1000*model.x[1]**3+2000*model.x[2]+666.667*model.x[2]**3)

model.c1 = Constraint(expr=0.4-model.x[1]+2*c*model.x[5]**2-model.x[5]*model.x[6]\
    *(d*model.y1+c*model.y2)-model.x[5]*model.x[7]*(d*model.y3+c*model.y4)==0)
model.c2 = Constraint(expr=0.4-model.x[2]+2*c*model.x[6]**2+model.x[5]*model.x[6]\
    *(d*model.y1-c*model.y2)+model.x[6]*model.x[7]*(d*model.y5-c*model.y6)==0)
model.c3 = Constraint(expr=0.8+2*c*model.x[7]**2+model.x[5]*model.x[7]*(d*model.y3\
    -c*model.y4)-model.x[6]*model.x[7]*(d*model.y5+c*model.y6)==0)
model.c4 = Constraint(expr=0.2-model.x[3]+2*d*model.x[5]**2+model.x[5]*model.x[6]\
    *(c*model.y1-d*model.y2)+model.x[5]*model.x[7]*(c*model.y3-d*model.y4)==0)
model.c5 = Constraint(expr=0.2-model.x[4]+2*d*model.x[6]**2-model.x[5]*model.x[6]\
    *(c*model.y1+d*model.y2)-model.x[6]*model.x[7]*(c*model.y5+d*model.y6)==0)
model.c6 = Constraint(expr=-.337+2*d*model.x[7]**2-model.x[5]*model.x[7]\
    *(c*model.y3+d*model.y4)+model.x[6]*model.x[7]*(c*model.y5-d*model.y6)==0)
model.c7 = Constraint(expr=model.x[1]>=0)
model.c8 = Constraint(expr=model.x[2]>=0)
model.c9 = Constraint(expr=model.x[5]>=.90909)
model.c10 = Constraint(expr=model.x[6]>=.90909)
model.c11 = Constraint(expr=model.x[7]>=.90909)
model.c12 = Constraint(expr=model.x[5]<=1.0909)
model.c13 = Constraint(expr=model.x[6]<=1.0909)
model.c14 = Constraint(expr=model.x[7]<=1.0909)

