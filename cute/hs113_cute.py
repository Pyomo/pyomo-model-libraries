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
model.N = RangeSet(1,10)
model.x = Var(model.N)
model.x[1] = 2.0
model.x[2] = 3.0
model.x[3] = 5.0
model.x[4] = 5.0
model.x[5] = 1.0
model.x[6] = 2.0
model.x[7] = 7.0
model.x[8] = 3.0
model.x[9] = 6.0
model.x[10]=10.0

model.obj = Objective(expr=model.x[1]**2+model.x[2]**2+model.x[1]*model.x[2]-14*model.x[1]-16*model.x[2]+(model.x[3]-10)**2+4*(model.x[4]-5)**2 +(model.x[5]-3)**2+2*(model.x[6]-1)**2+5*model.x[7]**2+7*(model.x[8]-11)**2+2*(model.x[9]-10)**2+(model.x[10]-7)**2+45)

model.c1 = Constraint(expr=105-4*model.x[1]-5*model.x[2]+3*model.x[7]-9*model.x[8]>=0)
model.c2 = Constraint(expr=-10*model.x[1]+8*model.x[2]+17*model.x[7]-2*model.x[8]>=0)
model.c3 = Constraint(expr=8*model.x[1]-2*model.x[2]-5*model.x[9]+2*model.x[10]+12>=0)
model.c4 = Constraint(expr=-3*(model.x[1]-2)**2-4*(model.x[2]-3)**2-2*model.x[3]**2+7*model.x[4]+120>=0)
model.c5 = Constraint(expr=-5*model.x[1]**2-8*model.x[2]-(model.x[3]-6)**2+2*model.x[4]+40>=0)
model.c6 = Constraint(expr=-.5*(model.x[1]-8)**2-2*(model.x[2]-4)**2-3*model.x[5]**2+model.x[6]+30>=0)
model.c7 = Constraint(expr=-model.x[1]**2-2*(model.x[2]-2)**2+2*model.x[1]*model.x[2]-14*model.x[5]+6*model.x[6]>=0)
model.c8 = Constraint(expr=3*model.x[1]-6*model.x[2]-12*(model.x[9]-8)**2+7*model.x[10]>=0) 

