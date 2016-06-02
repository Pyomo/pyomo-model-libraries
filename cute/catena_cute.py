#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, and Brandon C. Barrera
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
#   K. Veselic,
#   "De forma catenarum in campo gravitatis pendentium",
#   Klasicna Gimnazija u Zagrebu, Zagreb, 1987.

#   SIF input: Ph. L. Toint, May 1993.
#              correction by F. Ruediger, Mar 1997.

#   classification LQR2-AY-V-V


from pyomo.core import *
model = ConcreteModel()

model.N = Param(initialize=10)

model.gamma = Param(initialize=9.81)
model.tmass = Param(initialize=500.0)
model.bl = Param(initialize=1.0)
model.fract = Param(initialize=0.6)

def len_rule(model):
    return value(model.bl)*(value(model.N)+1)*value(model.fract)
def mass_rule(model):
    return value(model.tmass)/(value(model.N)+1.0)
def mg_rule(model):
    return value(model.mass)*value(model.gamma)
model.length = Param(initialize=len_rule)
model.mass = Param(initialize=mass_rule)
model.mg = Param(initialize=mg_rule)

model.Sv = RangeSet(0,model.N+1)
model.So = RangeSet(1,model.N)
model.Sc = RangeSet(1,model.N+1)

def x_rule(model, i):
    return i*value(model.length)/(value(model.N)+1.0)
def y_rule(model, i):
    return -i*value(model.length)/(value(model.N)+1.0)
#def fix1(model, i):
#       if i == 0:
#               return (0,0)
#       else:
#               return (None,None)
#def fix2(model, i):
#       if i == model.N+1:
#               return (model.length,modell.ength)
#       if i == 0:
#               return (0,0)
#       else:
#               return (None,None)

model.x = Var(model.Sv, initialize=x_rule)
model.y = Var(model.Sv, initialize=y_rule)
model.z = Var(model.Sv, initialize=0.0)

def f(model):
    obsum = 0
    for i in model.So:
        obsum += value(model.mg)*model.y[i]
    obsum +=  value(model.mg)*model.y[value(model.N)+1]/2.0
    expr = value(model.mg)*model.y[0]/2.0 + obsum
    return expr
model.f = Objective(rule=f,sense=minimize)

def cons1(model, i):
    expr = (model.x[i]-model.x[i-1])**2 + (model.y[i]-model.y[i-1])**2 + (model.z[i]-model.z[i-1])**2
    return expr == value(model.bl)**2
model.cons1 = Constraint(model.Sc, rule=cons1)


model.x[0] = 0.0
model.x[0].fixed = True
model.y[0] = 0.0
model.y[0].fixed = True
model.z[0] = 0.0
model.z[0].fixed = True
model.x[value(model.N)+1] = value(model.length)
model.x[value(model.N)+1].fixed = True
