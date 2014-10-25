from pyomo.environ import *

model = ConcreteModel()

model.x = Var([1,2], initialize=1.0)

# @decl1:
model.a = Objective()
# @:decl1

# @decl2:
model.b = Objective()
model.c = Objective([1,2,3])
# @:decl2

# @decl3:
model.d = Objective(expr=model.x[1] + 2*model.x[2])
# @:decl3

# @decl4:
model.e = Objective(expr=model.x[1], sense=maximize)
# @:decl4

# @decl5:
model.f = Objective(expr=model.x[1] + 2*model.x[2])

def TheObjective(model):
    return model.x[1] + 2*model.x[2]
model.g = Objective(rule=TheObjective)

def gg_rule(model):
    return model.x[1] + 2*model.x[2]
model.gg = Objective()
# @:decl5

# @decl6:
def h_rule(model, i):
    return i*model.x[1] + i*i*model.x[2]
model.h = Objective([1, 2, 3, 4])
# @:decl6

# @decl7:
def m_rule(model):
    expr = model.x[1]
    expr += 2*model.x[2]
    return expr
model.m = Objective()
# @:decl7

# @decl8:
p = 0.6
def n_rule(model):
    if p > 0.5:
        return model.x[1] + 2*model.x[2]
    else:
        return model.x[1] + 3*model.x[2]
    return expr
model.n = Objective()
# @:decl8

# @decl9:
p = 0.6
if p > 0.5:
    model.p = Objective(expr=model.x[1] + 2*model.x[2])
else:
    model.p = Objective(expr=model.x[1] + 3*model.x[2])
# @:decl9

model.display()
