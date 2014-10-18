# iterative1.py
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
print results

# Iterate to eliminate the previously found solution
for i in range(5):
    instance.load(results)

    expr = 0
    for j in instance.x:
        if instance.x[j].value == 0:
            expr += instance.x[j]
        else:
            expr += (1-instance.x[j])
    instance.c.add( expr >= 1 )

    instance.preprocess()
    results = opt.solve(instance)
    print results
