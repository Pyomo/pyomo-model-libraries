import pyomo.modeling
from pyomo.core import *

model = AbstractModel()

model.Z = Set(dimen=4)

instance = model.create('ABCD1.dat')

print(sorted(list(instance.Z.data())))
