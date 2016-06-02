# ******************************************************
#
# A non-cooperative game example; a Nash equilibrium is sought;
# 
# References:
# F.H. Murphy, H.D. Sherali, and A.L. Soyster, "A mathematical
# programming approach for determining oligopolistic market
# equilibrium", Mathematical Programming 24 (1986) 92-106
# P.T. Harker, "Accelerating the convergence . . .", Mathematical
# Programming 41 (1988) 29 - 59.
# 
# **********************************************************

from pyomo.environ import *
from pyomo.mpec import *


model = AbstractModel()

model.Rn = RangeSet(1, 10)

model.gamma = Param(initialize=1.2)

model.c = Param(model.Rn)
model.beta = Param(model.Rn)
model.L = Param(model.Rn, initialize=10)

model.q = Var(model.Rn, within=NonNegativeReals) # production vector

def Q_init(model):
    return sum(model.q[i] for i in model.Rn)
model.Q = Var(initialize=Q_init)

def divQ_init(model):
    return (5000.0/model.Q)**(1/model.gamma)
model.divQ = Var(initialize=divQ_init)

# delf - p - q(I)*delp
def feas_rule(model, i):
    return complements(
	        model.q[i],
	        0 <= model.c[i] + (model.L[i] * model.q[i])**(1/model.beta[i]) - 
                    model.divQ - model.q[i] * (-1/model.gamma) * model.divQ / model.Q
            )
model.feas = Complementarity(model.Rn, rule=feas_rule)

model.initpoint = RangeSet(1,4)

model.initval = Param(model.Rn, model.initpoint, within=NonNegativeReals)
