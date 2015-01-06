# choi.py

from pyomo.environ import *
from pyomo.mpec import *


model = AbstractModel()

# subjects or consumers
model.M = Param(within=IntegerInterval(1, None))
# brand names
model.N = Param(within=IntegerInterval(1, None))

model.subjects = RangeSet(1, model.M)
model.brands = RangeSet(1, model.N)
model.ingred = Set()

# randomness increases as chi decreases
model.chi = Param(within=NonNegativeReals)
# constant term in probability function
# representing "no purchase" option
model.K = Param()
# amount of ingredients
model.x = Param(model.brands, model.ingred)
# preferences
model.y = Param(model.subjects, model.ingred)
# importance weights
model.v = Param(model.subjects)
# unscaled w values
model.w0 = Param(model.subjects)
# constant in DU eqn
def w_init(model, i):
    return -model.chi * model.w0[i]
model.w = Param(model.subjects, initialize=w_init)
# constant in DU eqn
model.b = Param(model.subjects)
# average cost for producing j
model.c = Param(model.brands)
def DU_init(model, i, j):
    return -model.chi * 
                (model.v[i] * 
                 sum((model.x[j,k]-model.y[i,k])**2 for k in model.ingred) + 
                 model.b[i])
model.DU = Param(model.subjects, model.brands, initialize=DU_init)

model.p_lo = Param(model.brands, default=model.c)
model.p_up = Param(model.brands, default=Infinity)

model.p = Param(model.brands, initialize=lambda model,i:model.c[j] + .01)

# marginal profit for brand j
def mprofit_rule(model, j):
    return complements(
	        model.p_lo[j] <= model.p[j] <= model.p_up[j],

            (-1/model.M) * sum(
                exp(model.w[i]*model.p[j]+model.DU[i,j])
                / ( model.K + sum(exp(model.w[i]*model.p[jj]+model.DU[i,jj]) for jj in model.brands) )
                * (1 + (model.p[j]-model.c[j]) * model.w[i] *
                   ( model.K + sum(exp(model.w[i]*model.p[jj]+model.DU[i,jj]) for jj in model.brands if jj != j) )
                   / ( model.K + sum(exp(model.w[i]*model.p[jj]+model.DU[i,jj]) for jj in model.brands) )
                  ) for i in model.subjects)

            )
model.mprofit = Complementarity(model.brands, rule=mprofit_rule)

