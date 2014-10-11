import pyomo.modeling
from pyomo.core import *


model = ConcreteModel()

def f(model, N):
    model.A = RangeSet(N)
    model.x = Var(model.A, bounds=(1,2))

    expr=0
    for i in model.A:
        if not (i+1) in model.A:
            continue
        expr += 2.0*(model.x[i]*model.x[i+1]+1)
    model.obj = Objective(expr=expr)

    return model
   
model = f(model, 1000000)
