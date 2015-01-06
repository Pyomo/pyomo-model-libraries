from pyomo.core import *

model = AbstractModel()

# @decl1:
model.A = Set(ordered=True)
# @:decl1

instance = model.create('set_options.dat')
instance.pprint()
