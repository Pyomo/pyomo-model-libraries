from pyomo.core import *

model = AbstractModel()

model.Z = Set(dimen=3)
model.Y = Param(model.Z)

instance = model.create('ABCD4.dat')

print('Z '+str(sorted(list(instance.Z.data()))))
print('Y')
for key in sorted(instance.Y.keys()):
    print(cname(instance.Y,key)+" "+str(value(instance.Y[key])))
