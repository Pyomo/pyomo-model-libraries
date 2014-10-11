import pyomo.modeling
from pyomo.opt import SolverFactory
from concrete1 import model

model.pprint()

instance = model.create()
instance.pprint()

# @cmd:
opt = SolverFactory('ipopt')
# @:cmd
results = opt.solve(instance)

results.write()
