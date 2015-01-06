from pyomo.core import *

model = AbstractModel()

model.c1 = Set(dimen=3)
model.Z = Param(model.c1)

instance = model.create('example1.csv.dat')

print('c1 '+str(sorted(list(instance.c1.data()))))
print('Z')
keys = instance.Z.keys()
for key in sorted(keys):
    print(str(key)+" "+str(value(instance.Z[key])))
