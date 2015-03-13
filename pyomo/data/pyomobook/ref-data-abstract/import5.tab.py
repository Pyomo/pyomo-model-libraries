from pyomo.environ import *

model = AbstractModel()

model.B = Set(dimen=2)

instance = model.create('import5.tab.dat')

print('B '+str(list(sorted(instance.B.data()))))
