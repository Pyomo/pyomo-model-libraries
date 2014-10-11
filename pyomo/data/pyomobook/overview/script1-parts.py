import pyomo.modeling
from pyomo.opt import SolverFactory
from concrete1 import model

# @pprint:
model.pprint()
# @:pprint

# @create:
instance = model.create()
instance.pprint()
# @:create

# @opt:
opt = SolverFactory("glpk")
results = opt.solve(instance)
# @:opt

# @write:
results.write()
# @:write
