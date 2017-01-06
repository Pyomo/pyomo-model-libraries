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

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,8)
model.M = RangeSet(1,7)
model.L = RangeSet(2,8)
model.a = Param(model.N)
model.t = Param(model.N)
model.b = Param()
model.x = Var(model.M,bounds=(0,1.58),initialize=0.5)
model.q = Var(model.N)
model.s = Var(model.N)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return -(sum(model.a[j+1]*(model.t[j+1]-model.t[j])*cos(model.x[j]) for j in model.M)**2)
model.obj = Objective(rule=obj_rule,sense=minimize)

def cons1_rule(model):
    return model.q[8] == 1.0e+5
model.constr1 = Constraint(rule=cons1_rule)
def cons2_rule(model):
    return model.s[8] == 1.0e+3
model.constr2 = Constraint(rule=cons2_rule)
def cons3_rule(model):
    return model.q[1] == 0.0
model.constr3 = Constraint(rule=cons3_rule)
def cons4_rule(model):
    return model.s[1] == 0.0
model.constr4 = Constraint(rule=cons4_rule)
def cons5_rule(model,i):
    return model.q[i] == 0.5*(model.t[i]-model.t[i-1])**2*(model.a[i]*sin(model.x[i-1]) - model.b)\
     + (model.t[i]-model.t[i-1])*model.s[i-1] + model.q[i-1]
model.constr5 = Constraint(model.L,rule=cons5_rule)
def cons6_rule(model,i):
    return model.s[i] == (model.t[i]-model.t[i-1])*(model.a[i]*sin(model.x[i-1]) - model.b) + model.s[i-1]
model.constr6 = Constraint(model.L,rule=cons6_rule)

def cons7_rule(model):
    return model.r[1] == 0
#model.constr7 = Constraint(rule=cons7_rule)

def cons8_rule(model,i):
    return model.r[i] == model.a[i]*(model.t[i]-model.t[i-1])*cos(model.x[i-1]) + model.r[i-1];
#model.constr8 = Constraint(range(2,9),rule=cons8_rule)
