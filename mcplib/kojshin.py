#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2025
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

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

from pyomo.environ import *
from pyomo.mpec import *

model = ConcreteModel()

model.Rn = RangeSet(1,4)

model.x = Var(model.Rn, initialize=10)

def sx_rule(model, j):
    return model.x[j]*model.x[j]
model.sx = Expression([1,2], rule=sx_rule)

def f_rule(model, j):
    if j == 1: 
        rhs = 3*model.sx[1]+2*model.x[1]*model.x[2]+2*model.sx[2]+model.x[3]+3*model.x[4]-6
    elif j == 2:
        rhs = 2*model.sx[1]+model.x[1]+model.sx[2]+10*model.x[3]+2*model.x[4]-2
    elif j == 3:
        rhs = 3*model.sx[1]+model.x[1]*model.x[2]+2*model.sx[2]+2*model.x[3]+9*model.x[4]-9
    elif j == 4:
        rhs = model.sx[1]+3*model.sx[2]+2*model.x[3]+3*model.x[4]-3
    return complements( 0 <= model.x[j], 0 <= rhs)
model.f = Complementarity(model.Rn, rule=f_rule)

#model.initpoint = RangeSet(1,8)
#model.xinit = Param(model.Rn, model.initpoint, within=NonNegativeReals)

