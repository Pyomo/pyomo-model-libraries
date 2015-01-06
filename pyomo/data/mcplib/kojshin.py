# ****************************************************************
#
# This simple four-variable problem was given by:
# M. Kojima and S. Shindo, "Extensions of Newton and Quasi-Newton
# Method to PC^1 equations", Journal of Operations Research Society of
# Japan (29) p352-374.
# 
# Two solutions: x1 = (1.2247, 0, 0, 0.5), x2 = (1, 0, 3, 0).
# 
# *******************************************************************

from pyomo.core import *
from pyomo.mpec import *

model = AbstractModel()

model.Rn = Rangeset(1,4)
model.initpoint = RangeSet(1,8)

model.x = Var(model.Rn)
model.sx = Var([1,2], initialize={1:1, 2:4})

def f_rule(model, j):
    if j == 1: 
        rhs = 3*model.sx[1]+2*model.x[1]*model.x[2]+2*model.sx[2]+model.x[3]+3*model.x[4]-6
	elif j == 2:
        rhs = 2*model.sx[1]+model.x[1]+model.sx[2]+10*model.x[3]+2*model.x[4]-2
	elif j == 3:
        rhs = 3*model.sx[1]+model.x[1]*model.x[2]+2*model.sx[2]+2*model.x[3]+9*model.x[4]-9
    elif j == 4:
	    rhs = model.sx[1]+3*model.sx[2]+2*model.x[3]+3*model.x[4]-3
    return complements( 0 <= model.x[j], rhs)
model.f = Complementarity(model.Rn, rule=f_rule)

model.xinit = Param(model.Rn, model.initpoint, within=NonNegativeReals)

