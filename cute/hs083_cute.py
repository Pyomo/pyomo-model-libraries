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
#   Taken from cute suite. Formulated in pyomo by Logan Barnes.

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,5)
model.M = RangeSet(1,12)
model.a = Param(model.M)
model.l = Param(model.N)
model.u = Param(model.N)

x_init={}
x_init[1] = 78.0
x_init[2] = 33.0
x_init[3] = 27.0
x_init[4] = 27.0
x_init[5] = 27.0

def x_init_rule(model,i):
    return x_init[i]

def x_bounds_rule(model,i):
    return (value(model.l[i]),value(model.u[i]))
model.x = Var(model.N,bounds=x_bounds_rule,initialize=x_init_rule)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return 5.3578547*model.x[3]**2 + 0.8356891*model.x[1]*model.x[5] + 37.293239*model.x[1] - 40792.141
model.obj = Objective(rule=obj_rule, sense=minimize)

def cons1_rule(model):
    return 0 <= model.a[1] + model.a[2]*model.x[2]*model.x[5] + model.a[3]*model.x[1]*model.x[4]\
         - model.a[4]*model.x[3]*model.x[5] <= 92
model.constr1 = Constraint(rule=cons1_rule)

def cons2_rule(model):
    return 0 <= model.a[5] + model.a[6]*model.x[2]*model.x[5] + model.a[7]*model.x[1]*model.x[2]\
         + model.a[8]*model.x[3]**2 - 90 <= 20
model.constr2 = Constraint(rule=cons2_rule)

def cons3_rule(model):
    return 0 <= model.a[9] + model.a[10]*model.x[3]*model.x[5] + model.a[11]*model.x[1]*model.x[3]\
         + model.a[12]*model.x[3]*model.x[4] -20 <= 5
model.constr3 = Constraint(rule=cons3_rule)
