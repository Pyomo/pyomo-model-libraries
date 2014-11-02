from pyomo.environ import *

model = AbstractModel()

model.A = Set()
model.B = Set()
model.C = Set()

instance = model.create('set1.dat')

print sorted(list(instance.A.data()))
print sorted((instance.B.data()))
print sorted((instance.C.data()))
