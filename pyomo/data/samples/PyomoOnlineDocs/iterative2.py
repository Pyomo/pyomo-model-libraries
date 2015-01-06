# iterative2.py

from pyomo.core import *
from pyomo.opt import SolverFactory

# Create a solver
opt = SolverFactory('cplex')

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
print(results)

# "flip" the value of x[2] (it is binary)
# then solve again
instance.load(results)

if instance.x[2] == 0:
    instance.x[2] = 1
else:
    instance.x[2] = 0
instance.x[2].fixed = True
instance.preprocess()
results = opt.solve(instance)
print(results)
