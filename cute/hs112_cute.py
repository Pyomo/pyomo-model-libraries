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
model.x = Var(model.N,bounds=(.000001,None),initialize=0.1)
model.c = Param(model.N)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return sum(model.x[j]*(model.c[j] + log(model.x[j]/sum(model.x[k] for k in model.N))) for j in model.N)
model.obj = Objective(rule=obj_rule,sense=minimize)

def cons1_rule(model):
    return model.x[1] + 2.0*model.x[2] + 2.0*model.x[3] + model.x[6] + model.x[10] == 2.0
model.cons1 = Constraint(rule=cons1_rule)

def cons2_rule(model):
    return model.x[4] + 2.0*model.x[5] + model.x[6] + model.x[7] == 1.0
model.cons2 = Constraint(rule=cons2_rule)

def cons3_rule(model):
    return model.x[3] + model.x[7] + model.x[8] + 2.0*model.x[9] + model.x[10] == 1.0
model.cons3 = Constraint(rule=cons3_rule)
