from pyomo.environ import *
from simple import model

import logging

logger = logging.getLogger('pyomo.opt')
logger.setLevel(50)

# @load:
solver = SolverFactory('glpk')

# check final basis using exact arithmetic
#   --steep
solver.options.steep=None
# set glpk random number seed
#   --seed=1357908642
solver.options.seed=1357908642
# Run GLPK with the steep and seed solver options
results = solver.solve(model)

# Rerun GLPK with a new seed solver option
# This overrides the solver.options values
results = solver.solve(model, tee=True, options={'seed':1234567890})

# Rerun GLPK with another new seed solver option
# This does NOT override the solver.options values
results = solver.solve(model, tee=True, solver_options={'seed':1020304})

# Do we think this should work?
# It doesn't right now
results = solver.solve(model, tee=True, seed=13579)
# @:load
print(solver.options.seed)

model.solutions.store_to(results)
print(results)
