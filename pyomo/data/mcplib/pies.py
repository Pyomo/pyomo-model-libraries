# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
# A linear program with a variable rhs in the constraint system
# is expressed as a complementarity problem.
#
# LP:   min     <c,x>
#               Ax = q(p),
#       s.t.    Bx = b,
#               x >= 0
#
# where the prices p are the duals to the first constraint.
#
# MCP:	           A'p + B'v + c >= 0, x >= 0, comp.
#           -Ax + q(p)           =  0, p free, comp.
#           -Bx              + b =  0, v free, comp.
#
# Of course, the variables x and v are going to be
# split up further in the model.
#
# References:
# William W. Hogan, Energy Policy Models for Project Independence,
# Computers \& Operations Research (2), 1975.
# 
# N. Josephy, A Newton Method for the PIES energy model,
# Tech Report, Mathematics Research Center, UW-Madison, 1979.
# 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

from pyomo.environ import *
from pyomo.mpec import *

model = ConcreteModel()

model.comod = Set(ordered=True)         # coal and light and heavy oil
model.R = Set()                         # resources
model.creg = Set(initialize=[1,2])      # coal producing regions
model.oreg = Set(initialize=[1,2])      # crude oil producing regions
model.ctyp = Set(initialize=[1,2,3])    # increments of coal production
model.otyp = Set(initialize=[1,2])      # increments of oil production
model.refin = Set(initialize[1,2])      # refineries
model.users = Set(initialize[1,2])      # consumption regions

model.rmax = Param(model.R)                 # maximum resource usage
model.cmax = Param(model.creg,model.ctyp)   # coal prod. limits
model.omax = Param(model.oreg,model.otyp)   # oil prod. limits
model.rcost = Param(model.refin)            # refining cost
model.q0 = Param(model.comod)               # base demand for commodities
model.p0 = Param(model.comod)               # base prices for commodities
model.demand = Param(model.comod,model.users)   # computed at optimality
model.output = Param(model.refin,model.comod)   # % output of light/heavy oil
model.esub = Param(model.comod,model.comod) # cross-elasticities of substitution
model.cruse = Param(model.R,model.creg,model.ctyp)  # resource use in coal prod
model.oruse = Param(model.R,model.oreg,model.otyp)  # resource use in oil prod
model.ccost = Param(model.creg,model.ctyp)  # coal prod. cost
model.ocost = Param(model.oreg,model.otyp)  # oil prod. cost
model.ctcost = Param(model.creg,model.users)
model.otcost = Param(model.oreg,model.refin)
model.ltcost = Param(model.refin,model.users)   # light oil trans costs
model.htcost = Param(model.refin,model.users)   # heavy oil trans costs

model.i_c = Param(model.creg,model.ctyp)
model.i_o = Param(model.oreg,model.otyp)
model.i_ct = Param(model.creg,model.users)      # initial trans
model.i_ot = Param(model.oreg,model.refin)      # initial trans
model.i_lt = Param(model.refin,model.users)     # initial trans
model.i_ht = Param(model.refin,model.users)     # initial trans
model.iprice = Param(model.comod,model.users)   # initial price estimate

def c_init(model, cr, ct):
    return model.i_c[cr,ct]
model.c = Var(model.creg, model.ctyp, initialize=c_init)    # coal production

def o_init(model, r, ot):
    return model.i_o[r,ot]
model.o = Var(model.oreg, model.otyp, initialize=o_init)    # oil production

def ct_init(model, cr, u):
    return model.i_ct[cr,u]
model.ct = Var(model.creg, model.users, initialize=ct_init) # coal transportation levels

def ot_init(model, Or, r):
    return model.i_ot[Or,r]
model.ot = Var(model.oreg, model.refin, initialize=ot_init) # crude oil transportation levels

def lt_init(model, r, u):
    return model.i_lt[r,u]
model.lt = Var(model.refin, model.users, initialize=lt_init)    # light transportation levels

def ht_init(model, r, u):
    return model.i_ht[r,u]
model.ht = Var(model.refin, model.users, initialize=ht_init)    # heavy transportation levels

def p_init(model, co, u):
    return model.iprice[co,u]
model.p = Var(model.comod, model.users, initialize=p_init)      # commodity prices

model.mu = Var(model.R, initialize=1)       # dual to ruse cons.; marginal utility
model.cv = Var(model.creg, initialize=1)    # dual to cmbal
model.ov = Var(model.oreg, initialize=1)
model.lv = Var(model.refin, initialize=1)
model.hv = Var(model.refin, initialize=1)

def delc_rule(model, cr, t):
    return complements(
            0 <= model.c[cr,t] <= model.cmax[cr,t],
	        model.ccost[cr,t] - model.cv[cr] + 
                sum(model.cruse[res,cr,t]*model.mu[res] for res in model.R)
            )
model.delc = Complementarity(model.creg, model.ctyp, rule=delc_rule)

def delo_rule(model, r, t):
    return complements(
            0 <= model.o[r,t] <= model.omax[r,t],
            model.ocost[r,t] - model.ov[r] + 
                sum(model.oruse[res,r,t]*model.mu[res] for res in model.R)
            )
model.delo = Complementarity(model.oreg, model.otyp, rule=delo_rule)

def delct_rule(model, cr, u):
    return complements(
            0 <= model.ct[cr,u],
            model.ctcost[cr,u] + model.cv[cr] >= model.p["C",u]
            )
model.delct = Complementarity(model.creg, model.users, rule=delct_rule)

def delot_rule(model, Or, r):
    return complements(
            0 <= model.ot[Or,r],
            model.otcost[Or,r] + model.rcost[r] + model.ov[Or] >=
                model.output[r,"L"] * model.lv[r] + model.output[r,"H"] * model.hv[r]
            )
model.delot = Complementarity(model.oreg, model.refin, rule=delot_rule)

def dellt_rule(model, r, u):
    return complements(
            0 <= model.lt[r,u],
            model.ltcost[r,u] + model.lv[r] >= model.p["L",u]
            )
model.dellt = Complementarity(model.refin, model.users, rule=dellt_rule)

def delht_rule(model, r, u):
    return complements(
            0 <= model.ht[r,u],
            model.htcost[r,u] + model.hv[r] >= model.p["H",u]
            )
model.delht = Complementarity(model.refin, model.users, rule=delht_rule)

# excess supply of product
def dembal_init(model, co, u):
    if model.comod.ord(co) == 1:
        lhs = sum(model.ct[r,u] for r in model.creg)
    elif model.comod.ord(co) == 2:
        lhs = sum(model.lt[r,u] for r in model.refin)
    elif model.comod.ord(co) == 3:
        lhs = sum(model.ht[r,u] for r in model.refin)
    return complements(
            0.1 <= model.p[co,u],
            lhs >= model.q0[co] * 
                   prod(model.p[cc,u]/model.p0[cc])**model.esub[co,cc] for cc in model.comod)
            )
model.dembal = Complementarity(model.comod, model.users, rule=dembal_init)

# coal material balance
def cmbal_rule(model, cr)
    return complements(
            model.cv[cr],
            sum(model.c[cr,t] for t in model.ctyp) == sum(model.ct[cr,u] for u in model.users)
            )
model.cmbal = Complementarity(model.creg, rule=creg_rule)
  
# oil material balance
def ombal_rule(model, Or)
    return complements(
            model.ov[Or],
            sum(model.o[Or,t] for t in model.otyp) == sum(model.ot[Or,r] for r in model.refin)
            )
model.ombal = Complementarity(model.oreg, rule=ombal_rule)

# light material balance
def lmbal_rule(model, r):
    return complements(
            model.lv[r],
            sum(model.ot[Or,r] * model.output[r,"L"] for Or in model.oreg) == 
                    sum(model.lt[r,u] for u in model.users)
            )
model.lmbal = Complementarity(model.refin, rule=lmbal_rule)

# heavy material balance
def hmbal_rule(model, r):
    return complements(
            model.hv[r],
            sum(model.ot[Or,r] * model.output[r,"H"] for Or in model.oreg) ==
                    sum(model.ht[r,u] for u in model.users)
            )
model.hmbal = Complementarity(model.refin, rule=hmbal_rule)

# resource use constraints
def ruse_rule(model, res):
    return complements(
            0 <= model.mu[res],
            model.rmax[res] >=
                sum(model.c[cr,t]*model.cruse[res,cr,t] for cr in model.creg for t in model.ctyp) +
                sum(model.o[Or,t]*model.oruse[res,Or,t] for Or in model.oreg for t in model.otyp)
            )
model.ruse = Complementarity(model.R, rule=ruse_rule)

