import pyomo.modeling
from pyomo.core import *


model = ConcreteModel()

def f(model, N):
    model.A = RangeSet(N)
    model.x = Var(model.A, bounds=(1,2))

    expr=sum(2*model.x[i]*model.x[i+1] for i in model.A if (i+1) in model.A)
    model.obj = Objective(expr=expr)

    return model
   
model = f(model, 100000)
