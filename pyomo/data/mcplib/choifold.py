from pyomo.environ import *
from pyomo.mpec import *


model = AbstractModel()

# subjects or consumers
model.M = Param(within=IntegerInterval(1,None), initialize=30)
# brand names
model.N = Param(within=IntegerInterval(1,None), initialize=14)

model.subjects = RangeSet(1, model.M)
model.brands = RangeSet(1, model.N)
model.ingred = Set(initialize=["asp","asub","caff","aing"])

# randomness increases as chi decreases
model.chi = Param(within=NonNegativeReals, initialize=3)
# demand for no drug at all
model.Kdemand = Param()
# constant term in probability function
# representing "no purchase" option
model.K = Param(initialize=1)
# j's amount of ingredient k
model.x = Param(model.brands, model.ingred)
# i's preference for k
model.y = Param(model.subjects, model.ingred)
# i's importance weight for all k
model.v = Param(model.subjects)
# constant in DU eqn
model.w = Param(model.subjects)
# constant in DU eqn
model.b = Param(model.subjects)
# average cost for producing j
model.c = Param(model.brands)
# existing market prices
model.p_current = Param(model.brands)
# initial price iterate
model.p_init = Param(model.brands, initialize=lambda model, j:c[j] + .01)
# soln from Choi, DeSarbo, Harker
model.p_solu = Param(model.brands)
# computed demands
model.demand = Param(model.brands)
# DU is a computed parameter, such that
#   -chi(DU_{ij}) = w_i*p_j + DU[i,j]
def DU_init(model, i, j):
    return -model.chi * (model.v[i] * sum((model.x[j,k]-model.y[i,k])**2 for k in model.ingred) + model.b[i])
model.DU = Param(model.subjects, model.brands, initialize=DU_init)

model.p_lo = Param(model.brands, initialize=lambda M,j:M.c[j] if j != 8 else .199)
model.p_up = Param(model.brands, initialize=lambda M,j:Infinity if j != 8 else .199)

def p_bounds(model, j):
    return (model.p_lo[j], model.p_up[j])
model.p = Var(model.brands, bounds=p_bounds, initialize=p_init)

def dutil_init(model, i, j):
    return exp(model.w[i]*model.p[j]+model.DU[i,j])
model.dutil = Var(model.subjects, model.brands, initialize=dutil_init)

# marginal profit for brand j
def mprofit_rule(model, j):
	return model.p[j] *
(	(-1/model.M) * sum(
	model.dutil[i,j]
	  / ( model.K + sum(model.dutil[i,jj] for jj in model.brands) )
	  * (1 + (model.p[j]-model.c[j]) * model.w[i]
	    * ( model.K + sum(model.dutil[i,jj] for jj in model.brands if jj != j) )
	    / ( model.K + sum(model.dutil[i,jj] for jj in model.brands))
	    )
	for i in model.subjects)
)
	== 0
model.mprofit = Constraint(model.brands, rule=mprofit_rule)
