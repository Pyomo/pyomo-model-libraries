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

from pyomo.core import *
model = AbstractModel()
model.N = RangeSet(1,10)
model.x = Var(model.N,bounds=(2.001,9.999),initialize=9.0)

def prod(model):
    expr = 1.0
    for j in model.N:
        expr *= model.x[j]
    return expr

def obj_rule(model):
    return sum(log(model.x[j]-2.0)**2 + log(10.0 - model.x[j])**2 for j in model.N) - (prod(model))**0.2
model.obj = Objective(rule=obj_rule,sense=minimize)
