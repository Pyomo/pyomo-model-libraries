from pyomo.environ import *

model = AbstractModel()

# @decl1:
model.x = Var()
# @:decl1

# @decl2:
model.A = Set(initialize=[1,2,3])
model.y = Var(within=model.A)
model.r = Var(domain=Reals)
model.w = Var(within=Boolean)
# @:decl2

# @decl3:
B = [1.5, 2.5, 3.5]
model.u = Var(B)
model.C = Set()
model.t = Var(B, model.C)
# @:decl3

# @decl4:
model.a = Var(bounds=(0.0,None))

lower = {1:2, 2:4, 3:6}
upper = {1:3, 2:4, 3:7}
def f(model, i):
    return (lower[i], upper[i])
model.b = Var(model.A, bounds=f)
# @:decl4

# @decl5:
model.za = Var(initialize=9, within=NonNegativeReals)
model.zb = Var(model.A, initialize={1:1, 2:4, 3:9})
model.zc = Var(model.A, initialize=2)
# @:decl5

# @decl6:
def g(model, i):
    return 3*i
model.m = Var(model.A, initialize=g)
# @:decl6


model = model.create_instance('var_declaration.dat')

# @decl7a:
model.za = 8.5
print(model.za.value)        # 8.5
model.za.reset()
print(model.za.value)        # 9
# @:decl7a

# @decl7:
model.za = 8.5
model.zb[2] = 7
# @:decl7

# @decl8:
print(float(model.za))       # 8.5
print(float(model.zb[2]))    # 7.0
# @:decl8

# @decl9:
print(value(model.za))       # 8.5
print(value(model.zb[2]))    # 7
# @:decl9

# @decl10:
print(len(model.za))         # 1
print(len(model.zb))         # 3
# @:decl10

# @decl11:
print(model.zb[2].value)     # 7
print(model.zb[2].initial)   # 4
print(model.za.lb)           # 0
print(model.za.ub)           # None
print(model.zb[2].fixed)     # False
# @:decl11
model.pprint()
