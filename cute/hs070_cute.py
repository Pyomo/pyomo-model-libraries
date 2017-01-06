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
#   Taken from cute suite. Formulated in Pyomo by Logan Barnes and Gabe Hackebeil.

from pyomo.environ import *
model = AbstractModel()

X_init = {}
X_init[1] = 2.0
X_init[2] = 4.0
X_init[3] = 0.04
X_init[4] = 2.0

def X_init_rule(model,i):
    return X_init[i]

model.N = RangeSet(1,4)
model.M = RangeSet(1,19)

model.c = Param(model.M)
model.y_obs = Param(model.M)

def x_bounds_rule(model,i):
    if i in [1,2,4]:
        return (0.00001,100.0)
    else:
        return (0.00001,1.0)
model.x = Var(RangeSet(1,4),bounds=x_bounds_rule,initialize=X_init_rule)

def _b(model):
    return model.x[3] + (1-model.x[3])*model.x[4];
model.b = Expression(rule=_b)

def _y_cal(model,i):
    return (1 + 1.0/(12*model.x[2])) \
           * \
           ( \
               model.x[3]*model.b**model.x[2]*(model.x[2]/6.2832)**0.5 * (model.c[i]/7.685)**(model.x[2]-1) \
               * exp(model.x[2] - model.b*model.c[i]*model.x[2]/7.658) \
           ) \
           + \
           (1 + 1.0/(12*model.x[1])) \
           * \
           ( \
               (1-model.x[3])*(model.b/model.x[4])**model.x[1]*(model.x[1]/6.2832)**0.5 * (model.c[i]/7.658)**(model.x[1]-1) \
               * exp(model.x[1] - model.b*model.c[i]*model.x[1]/(7.658*model.x[4])) \
           );
model.y_cal = Expression(model.M, rule=_y_cal)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return sum((model.y_cal[i] - model.y_obs[i])**2 for i in model.M)
model.obj = Objective(rule=obj_rule, sense=minimize)
    
def cons1(model):
    return model.x[3] + (1-model.x[3])*model.x[4] >= 0
model.constr1 = Constraint(rule=cons1)
