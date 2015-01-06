from pyomo.core import *

model = AbstractModel()

# @decl:
model.A = Set(dimen=3)
# @:decl

instance = model.create('set2.dat')

print sorted(list(instance.A.data()))
