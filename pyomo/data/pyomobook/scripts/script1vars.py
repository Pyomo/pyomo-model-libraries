import pyomo.environ
from pyomo.opt import SolverFactory
from concrete1 import model as model1
from concrete2 import model as model2

opt = SolverFactory("glpk")

# @load1:
instance1 = model1
results1 = opt.solve(instance1)
# @:load1

instance2 = model2
results2 = opt.solve(instance2)

# @value1:
from pyomo.core import value

print("x_2  value: "+str(instance1.x_2.value))
print("x_2  value: "+str(value(instance1.x_2)))
print("x[2] value: "+str(instance2.x[2].value))
print("x[2] value: "+str(value(instance2.x[2])))
# @:value1

# @value2:
print("x_2  object: "+str(instance1.x_2))
print("x[2] object: "+str(instance2.x[2]))
# @:value2

# @comparison1:
if value(instance1.x_2) == value(instance2.x[2]):
# @:comparison1
    print("x_2 == x[2]")
else:
    print("x_2 != x[2]")

# @comparison2:
if instance1.x_2 == instance2.x[2]:
# @:comparison2
    print("x_2 == x[2]")
else:
    print("x_2 != x[2]")
