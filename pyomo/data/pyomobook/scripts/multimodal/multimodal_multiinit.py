from pyomo.core import *
from pyutilib.misc import Options
from math import pi

model = ConcreteModel()

model.x = Var(bounds=(0,4))
model.y = Var(bounds=(0,4))

def multimodal(m):
    return (2-cos(pi*m.x)-cos(pi*m.y)) * (m.x**2) * (m.y**2)
model.obj = Objective(rule=multimodal, sense=minimize)

instance = model.create();

options = Options()
options.solver = 'ipopt'
options.quiet = True

instance.x = 0.25
instance.y = 0.25
print "x0=", instance.x.value, " y0=", instance.y.value,
results, opt = scripting.util.apply_optimizer(options, instance)
instance.load(results)
print "x*=", instance.x.value, " y*=", instance.y.value

instance.x = 2.5
instance.y = 2.5
print "x0=", instance.x.value, " y0=", instance.y.value,
results, opt = scripting.util.apply_optimizer(options, instance)
instance.load(results)
print "x*=", instance.x.value, " y*=", instance.y.value
