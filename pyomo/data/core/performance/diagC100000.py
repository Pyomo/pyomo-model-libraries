import pyomo.modeling
from pyomo.core import *


model = ConcreteModel()

def f(model, N):
    model.A = RangeSet(N)
    def domain_rule(model, i):
        return Reals
    model.x = Var(model.A, domain=domain_rule)

    expr=sum(i*model.x[i] for i in model.A)
    model.obj = Objective(expr=expr)

    def c_rule(model, i):
        return (N-i+1)*model.x[i] >= N
    model.c = Constraint(model.A)

    return model
   
model = f(model, 100000)
