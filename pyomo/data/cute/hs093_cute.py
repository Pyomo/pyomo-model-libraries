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
model.N = RangeSet(1,6)
model.x = Var(model.N,bounds=(0,None))
model.x[1] = 5.54
model.x[2] = 4.4
model.x[3] = 12.02
model.x[4] = 11.82
model.x[5] = 0.702
model.x[6] = 0.852

model.obj = Objective(expr=0.0204*model.x[1]*model.x[4]*(model.x[1] + model.x[2] + model.x[3]) +\
  0.0187*model.x[2]*model.x[3]*(model.x[1] + 1.57*model.x[2] + model.x[4]) +\
  0.0607*model.x[1]*model.x[4]*model.x[5]**2*(model.x[1] + model.x[2] + model.x[3]) +\
  0.0437*model.x[2]*model.x[3]*model.x[6]**2*(model.x[1] + 1.57*model.x[2] + model.x[4]))
 
def prod(model):
    expr = 1.0
    for j in model.N:
        expr *= model.x[j]
    return expr

model.constr1 = Constraint(expr=0.001*prod(model)>=2.07)
model.constr2 = Constraint(expr=0.00062*model.x[1]*model.x[4]*model.x[5]**2\
                                *(model.x[1] + model.x[2] + model.x[3])\
                                + 0.00058*model.x[2]*model.x[3]*model.x[6]**2*(model.x[1] + 1.57*model.x[2] + model.x[4])<= 1)
