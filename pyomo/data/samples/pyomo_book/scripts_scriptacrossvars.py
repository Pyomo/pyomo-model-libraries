from pyomo.opt import SolverFactory
from concrete2 import model

instance = model.create()

opt = SolverFactory("glpk")
results = opt.solve(instance)
instance.load(results)

for index in instance.x:
    print instance.x[index], instance.x[index].value

from pyomo.core import Var
for var in instance.component_objects(Var, active=True):
    print "Variable",var
    obj = getattr(instance, var)
    for index in obj:
        print obj[index], obj[index].value
