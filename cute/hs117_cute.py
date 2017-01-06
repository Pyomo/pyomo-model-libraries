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

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,10)
model.M = RangeSet(1,5)
model.L = RangeSet(1,15)
model.a = Param(model.N,model.M)
model.b = Param(model.N)
model.c = Param(model.M,model.M)
model.d = Param(model.M)
model.e = Param(model.M)

x_init = {}
x_init[1] =   .001
x_init[2] =   .001
x_init[3] =   .001
x_init[4] =   .001
x_init[5] =   .001
x_init[6] =   .001
x_init[7] = 60.0
x_init[8] =   .001
x_init[9] =   .001
x_init[10]=   .001
x_init[11]=   .001
x_init[12]=   .001
x_init[13]=   .001
x_init[14]=   .001
x_init[15]=   .001

def x_init_rule(model,i):
    return x_init[i]

model.x = Var(model.L,bounds=(0,None),initialize=x_init_rule)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))


def obj_rule(model):
    return sum(-model.b[j]*model.x[j] for j in model.N) + sum(model.c[k,j]*model.x[10+k]*model.x[10+j] for k in model.M for j in model.M) + sum(2*model.d[j]*model.x[10+j]**3 for j in model.M)
model.obj = Objective(rule=obj_rule,sense=minimize)

def cons1_rule(model,j):
    return sum(2*model.c[k,j]*model.x[10+k] for k in model.M) + 3*model.d[j]*model.x[10+j]**2+model.e[j] - sum(model.a[k,j]*model.x[k] for k in model.N) >= 0
model.constr1 = Constraint(model.M,rule=cons1_rule)
