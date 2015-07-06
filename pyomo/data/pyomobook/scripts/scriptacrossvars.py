import pyomo.environ
from pyomo.opt import SolverFactory
from concrete2 import model

instance = model

opt = SolverFactory("glpk")
results = opt.solve(instance)
#instance.load(results)

# @loop1:
from pyomo.core import Var
for (name, key), var in instance.component_data_iterindex(Var, active=True):
    print("%s %s %s" % (name, key, str(var.value)))
# @:loop1

# @loop2:
for index in instance.x:
    print("%s %s" % (str(instance.x[index]), str(instance.x[index].value)))
# @:loop2

# @loop3:
from pyomo.core import Var
for var in instance.component_objects(Var, active=True):
    print("Variable "+str(var))
    for index in var:
        print("%s %s" % (str(var[index]), str(var[index].value)))
# @:loop3
