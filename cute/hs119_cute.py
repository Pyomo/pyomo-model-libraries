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
#

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,16)
model.M = RangeSet(1,8)
model.a = Param(model.N,model.N,default=0)
model.b = Param(model.M,model.N,default=0)
model.c = Param(model.M,default=0)
model.x = Var(model.N,bounds=(0,5),initialize=10.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))


def obj_rule(model):
    return sum(model.a[i,j]*(model.x[i]**2+model.x[i]+1)*(model.x[j]**2+model.x[j]+1) for i in model.N for j in model.N)
model.obj = Objective(rule=obj_rule,sense=minimize)

def cons1_rule(model,i):
    return sum(model.b[i,j]*model.x[j] for j in model.N) == model.c[i]
model.constr1 = Constraint(model.M,rule=cons1_rule)
