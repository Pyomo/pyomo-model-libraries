from pyomo.core import *

model = AbstractModel()

# @decl1:
model.A = Set(initialize=[1,2,3])
model.B = Set(initialize=[(1,1),(2,2),(3,3)])

model.z = Param(model.B, initialize=1.0)
model.y = Param(model.A, model.B, initialize=1.0)
# @:decl1

# @decl2:
model.x = Param(['a','b'], model.B, initialize=1.0)
# @:decl2


# @decl3a:
def C_index(model):
    for k in model.A:
        if k % 2 == 0:
            yield k
model.w = Param(C_index, model.B, initialize=1.0)
# @:decl3a

# @decl3b:
def D_index(model):
    for i in model.B:
        k = sum(i)
        if k % 2 == 0:
            yield (k,k)
D_index.dimen=2
model.v = Param(D_index, model.B, initialize=1.0)
# @:decl3b


instance = model.create()
instance.pprint()
