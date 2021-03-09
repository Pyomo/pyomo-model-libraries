from pyomo.environ import *

def create_model(N):
    model = ConcreteModel()

    model.A = RangeSet(N)
    model.x = Var(model.A)

    expr=sum(i*model.x[i] for i in model.A)
    model.obj = Objective(expr=expr)

    def c_rule(model, i):
        return (N-i+1)*model.x[i] >= N
    model.c = Constraint(model.A, rule=c_rule)

    return model
