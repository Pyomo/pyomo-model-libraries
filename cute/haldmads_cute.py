#  This software is distributed under the BSD License.
#  under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil, Juan Lopez
# Taken from:

# AMPL Model by Hande Y. Benson
#
# Copyright (C) 2001 Princeton University
# All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that the copyright notice and this
# permission notice appear in all supporting documentation.                     

#   Source: 
#   J. Hald and K. Madsen,
#   "Combined LP and quasi-Newton methods for minimax optimization",
#   Mathematical Programming 20, pp. 49-62, 1981.

#   SIF input: Ph. Toint, Nov 1993.

#   classification  LOR2-AN-6-42


from pyomo.core import *
model = ConcreteModel()

def y_rule(model,i):
    return -1.0+0.1*(i-1)
model.y = Param(RangeSet(1,21),initialize=y_rule)

def ey_rule(model,i):
    return exp(model.y[i])
model.ey = Param(RangeSet(1,21),initialize=ey_rule)

def x_init_rule(model,i):
    if i==1:
        return 0.5
    else:
        return 0.0
model.x = Var(RangeSet(1,5),initialize=x_init_rule)

model.u = Var(initialize=0.0)

model.f = Objective(expr=model.u)

def cons1_rule(model,i):
    return (model.x[1]+model.y[i]*model.x[2])/(1.0+model.x[3]*model.y[i]+\
    model.x[4]*model.y[i]**2+model.x[5]*model.y[i]**3)-model.u <= model.ey[i]
model.cons1 = Constraint(RangeSet(1,21),rule=cons1_rule)

def cons2_rule(model,i):
    return -(model.x[1]+model.y[i]*model.x[2])/(1.0+model.x[3]*model.y[i]+model.x[4]*model.y[i]**2+\
    model.x[5]*model.y[i]**3)-model.u <= -model.ey[i]
model.cons2 = Constraint(RangeSet(1,21),rule=cons2_rule)
