import pyomo.modeling
from pyomo.core import *

model = AbstractModel()

model.A = Set()
model.B = Set(ordered=Set.InsertionOrder)
model.C = Set(ordered=Set.InsertionOrder)

instance = model.create('set1.dat')

print(sorted(list(instance.A.data())))
print(list(instance.B))
print(list(instance.C))
