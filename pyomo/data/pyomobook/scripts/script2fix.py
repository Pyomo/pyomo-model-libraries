import sys
import os
currdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/nonlinear/multimodal/'

import pyomo.environ
from pyomo.opt import SolverFactory
sys.path.append(currdir)
from multimodal import model
sys.path.remove(currdir)

#opt = SolverFactory("coliny", solver='sco:ps') # TODO - remove when ipopt is working...
opt = SolverFactory("ipopt")
instance = model

# @value:
instance.y = 3.5
instance.x = 3.5
# @:value
# @fixed:
instance.y.fixed = True
# @:fixed

results = opt.solve(instance)
instance.load(results)

xval = instance.x.value
print("First   x was "+str(instance.x.value)+\
        " and y was "+str(instance.y.value))

instance.x.fixed = True
instance.y.fixed = False

results = opt.solve(instance)
instance.load(results)

print("Next    x was "+str(instance.x.value)+\
        " and y was "+str(instance.y.value))

instance.x.fixed = False
instance.y.fixed = True

results = opt.solve(instance)
instance.load(results)

print("Finally x was "+str(instance.x.value)+\
        " and y was "+str(instance.y.value))
