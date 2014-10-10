import pyomo.environ
from pyomo.core import *

model = AbstractModel()

# @decl:
model.z = Param()
# @:decl

instance = model.create('ex.dat')

print(value(instance.z))
