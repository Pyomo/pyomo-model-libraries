from pyomo.core import *

model = AbstractModel()

# @decl:
model.A = Set(dimen=2)
model.B = Param(model.A)
model.C = Param(model.A)
model.D = Param(model.A)
# @:decl

instance = model.create('param6a.dat')

keys = instance.B.keys()
print('B')
for key in sorted(keys):
    print(str(key)+" "+str(value(instance.B[key])))
print('C')
keys = instance.C.keys()
for key in sorted(keys):
    print(str(key)+" "+str(value(instance.C[key])))
print('D')
keys = instance.D.keys()
for key in sorted(keys):
    print(str(key)+" "+str(value(instance.D[key])))
