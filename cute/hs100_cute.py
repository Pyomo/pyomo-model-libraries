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
model.N = RangeSet(1,7)
model.x = Var(model.N)
model.x[1] = 1.0
model.x[2] = 2.0
model.x[3] = 0.0
model.x[4] = 4.0
model.x[5] = 0.0
model.x[6] = 1.0
model.x[7] = 1.0

model.obj = Objective(expr=(model.x[1]-10)**2 + 5.0*(model.x[2]-12)**2 + model.x[3]**4\
     + 3.0*(model.x[4]-11)**2 + 10.0*model.x[5]**6 + 7.0*model.x[6]**2 + model.x[7]**4\
     - 4.0*model.x[6]*model.x[7] - 10.0*model.x[6] - 8.0*model.x[7])
     
model.constr1 = Constraint(expr=2*model.x[1]**2 + 3*model.x[2]**4 + model.x[3] + 4*model.x[4]**2 + 5*model.x[5] <= 127.0)
model.constr2 = Constraint(expr=7*model.x[1] + 3*model.x[2] + 10*model.x[3]**2 + model.x[4] - model.x[5] <= 282.0)
model.constr3 = Constraint(expr=23*model.x[1] + model.x[2]**2 + 6*model.x[6]**2 - 8*model.x[7] <= 196.0)
model.constr4 = Constraint(expr=-4*model.x[1]**2 - model.x[2]**2 + 3*model.x[1]*model.x[2]\
        -2*model.x[3]**2 - 5*model.x[6] + 11*model.x[7] >= 0)
