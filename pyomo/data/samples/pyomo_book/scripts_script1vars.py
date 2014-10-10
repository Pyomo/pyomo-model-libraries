from pyomo.opt import SolverFactory
from concrete1 import model as model1
from concrete2 import model as model2

opt = SolverFactory("glpk")

instance1 = model1.create()
results1 = opt.solve(instance1)
instance1.load(results1)

instance2 = model2.create()
results2 = opt.solve(instance2)
instance2.load(results2)

from pyomo.core import value

print "x_2  value:", instance1.x_2.value
print "x_2  value:", value(instance1.x_2)
print "x[2] value:", instance2.x[2].value
print "x[2] value:", value(instance2.x[2])

print "x_2  object:", instance1.x_2
print "x[2] object:", instance2.x[2]

if value(instance1.x_2) == value(instance2.x[2]):
    print "x_2 == x[2]"
else:
    print "x_2 != x[2]"

if instance1.x_2 == instance2.x[2]:
    print "x_2 == x[2]"
else:
    print "x_2 != x[2]"
