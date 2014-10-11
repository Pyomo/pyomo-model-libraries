import pyomo.modeling
from pyomo.core import *

model = AbstractModel()

model.p = Param()

instance = model.create('import6.tab.dat')

print('p '+str(value(instance.p)))
