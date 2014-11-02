from pyomo.environ import *

model = AbstractModel()

# @decl:
model.A = Set(dimen=3)
# @:decl

instance = model.create('set2a.dat')

print sorted(list(instance.A.data()))
