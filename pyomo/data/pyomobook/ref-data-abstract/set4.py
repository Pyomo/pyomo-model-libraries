from pyomo.core import *

model = AbstractModel()

# @decl:
model.A = Set(dimen=2)
# @:decl

instance = model.create('set4.dat')

print sorted(list(instance.A.data()))
