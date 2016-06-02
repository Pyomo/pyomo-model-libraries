
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
model.N = RangeSet(1,9)
model.x = Var(model.N,initialize=1.0)

model.obj = Objective(expr=-.5*(model.x[1]*model.x[4]-model.x[2]*model.x[3]+model.x[3]*model.x[9]-model.x[5]*model.x[9]+model.x[5]*model.x[8]-model.x[6]*model.x[7]))

model.c1 = Constraint(expr=1-model.x[3]**2-model.x[4]**2>=0)
model.c2 = Constraint(expr=1-model.x[5]**2-model.x[6]**2>=0)
model.c3 = Constraint(expr=1-model.x[9]**2>=0)
model.c4 = Constraint(expr=1-model.x[1]**2-(model.x[2]-model.x[9])**2>=0)
model.c5 = Constraint(expr=1-(model.x[1]-model.x[5])**2-(model.x[2]-model.x[6])**2>=0)
model.c6 = Constraint(expr=1-(model.x[1]-model.x[7])**2-(model.x[2]-model.x[8])**2>=0)
model.c7 = Constraint(expr=1-(model.x[3]-model.x[7])**2-(model.x[4]-model.x[8])**2>=0)
model.c8 = Constraint(expr=1-(model.x[3]-model.x[5])**2-(model.x[4]-model.x[6])**2>=0)
model.c9 = Constraint(expr=1-model.x[7]**2-(model.x[8]-model.x[9])**2>=0)
model.c10= Constraint(expr=model.x[1]*model.x[4]-model.x[2]*model.x[3]>=0)
model.c11= Constraint(expr=model.x[3]*model.x[9]>=0)
model.c12= Constraint(expr=-model.x[5]*model.x[9]>=0)
model.c13= Constraint(expr=model.x[5]*model.x[8]-model.x[6]*model.x[7]>=0)
model.c14= Constraint(expr=model.x[9]>=0)
