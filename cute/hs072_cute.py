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
#   Taken from cute suite. Formulated in Pyomo by Logan Barnes.

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,2)
model.M = RangeSet(1,4)
model.x = Var(model.M,bounds=(0.001,None),initialize=1.0)
model.a = Param(model.N,model.M)
model.b = Param(model.N)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return 1 + sum(model.x[j] for j in model.M)
model.obj = Objective(rule=obj_rule, sense=minimize)

def cons_rule(model,i):
    return sum((model.a[i,j]/model.x[j]) for j in model.M) <= model.b[i]
model.constr = Constraint(model.N,rule=cons_rule)

def ub_rule(model,j):
    return model.x[j] <= (5 - j) * 1.0e5
model.ub = Constraint(model.M,rule=ub_rule) 
