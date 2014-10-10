import pyomo.environ
from pyomo.opt import SolverFactory
from concrete1 import model

#model.pprint()

instance = model.create()
#instance.pprint()

#from pyutilib.misc import Options
#options=Options()
#options.debug=1
#options.expansion_factor = 2
# @cmd:
opt = SolverFactory('coliny', solver='sco:ps')
print(opt.options)
# @:cmd
#opt.keepfiles = True
results = opt.solve(instance)

results.write()
