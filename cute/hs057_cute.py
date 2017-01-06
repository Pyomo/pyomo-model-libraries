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
#   Taken from cute suite. Formulated in Pyomo by Logan Barnes and Gabriel Hackebeil.

x_init = {}
x_init[1] = 0.42
x_init[2] = 5.0

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,44)
model.M = RangeSet(1,2)
def x_init_rule(model,i):
    return x_init[i]
model.x = Var(model.M,initialize=x_init_rule)
model.b = Param(model.N)
model.a = Param(model.N)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj(model):
    return sum((model.b[i] - model.x[1] - (0.49 - model.x[1])*exp(-model.x[2]*(model.a[i]-8)))**2 for i in model.N)
model.obj = Objective(rule=obj,sense=minimize)

def cons1(model):
    return (0.09,(0.49*model.x[2] - model.x[1]*model.x[2]),None)
model.constr1 = Constraint(rule=cons1)
def cons2(model):
    return (0.4,model.x[1],None)
model.constr2 = Constraint(rule=cons2)
def cons3(model):
    return (-4,model.x[2],None)
model.constr3 = Constraint(rule=cons3) 
