import pyomo.environ
from pyomo.opt import SolverFactory
from concrete2 import model

instance = model.create()

opt = SolverFactory("glpk")
results = opt.solve(instance)
instance.load(results)

# @loop1:
from pyomo.core import Var
for name, var in instance.active_components(Var).iteritems():
    for key in var:
        print("%s %s %s" % (name, key, str(var[key].value)))
# @:loop1

# @loop2:
for index in instance.x:
    print("%s %s" % (str(instance.x[index]), str(instance.x[index].value)))
# @:loop2

# @loop3:
from pyomo.core import Var
for var in instance.active_components(Var):
    print("Variable "+str(var))
    obj = getattr(instance, var)
    for index in obj:
        print("%s %s" % (str(obj[index]), str(obj[index].value)))
# @:loop3
