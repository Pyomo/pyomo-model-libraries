# noiteration1.py
from __future__ import division
from pyomo.core import *
from pyomo.opt import SolverFactory

# Create a solver
opt = SolverFactory('glpk')

#
# A simple model with binary variables and
# an empty constraint list.
#
model = AbstractModel()
model.n = Param(default=4)
model.x = Var(RangeSet(model.n), within=Binary)
def o_rule(model):
    return summation(model.x)
model.o = Objective(rule=o_rule)
model.c = ConstraintList()

# Create a model instance and optimize
instance = model.create()
results = opt.solve(instance)
instance.load(results)

if instance.x[2].value == 0:
    print "The second index has a zero"
else:
    print "x[2]=",instance.x[2].value

