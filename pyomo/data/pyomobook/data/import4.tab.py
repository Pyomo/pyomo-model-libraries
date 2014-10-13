import pyomo.environ
from pyomo.core import *

model = AbstractModel()

model.C = Set(dimen=2)

instance = model.create('import4.tab.dat')

print('C '+str(sorted(list(instance.C.data()))))
