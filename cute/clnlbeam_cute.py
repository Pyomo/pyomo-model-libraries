#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Juan Lopez and Gabe Hackebeil
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
#   H. Maurer and H.D. Mittelman,
#   "The non-linear beam via optimal control with bound state variables",
#   Optimal Control Applications and Methods 12, pp. 19-31, 1991.

#   SIF input: Ph. Toint, Nov 1993.

#   classification  OOR2-MN-V-V

from pyomo.core import*
model = ConcreteModel()

ni = 500
alpha = 350.0
h = 1.0/ni

def t_init(model,i):
    return 0.05*cos(i*h)
model.t = Var(RangeSet(0,ni),initialize=t_init,bounds=(-1.0,1.0))

def x_init(model,i):
    return 0.05*cos(i*h)
model.x = Var(RangeSet(0,ni),initialize=x_init,bounds=(-0.05,0.05))

model.u = Var(RangeSet(0,ni))

def f(model):
    return sum((0.5*h*(model.u[i+1]**2 + model.u[i]**2) + 0.5*alpha*h*(cos(model.t[i+1]) +\
    cos(model.t[i])))for i in range(0,ni))
model.f = Objective(rule=f)

def con1(model,i):
    return model.x[i+1] - model.x[i] - 0.5*h*(sin(model.t[i+1]) + sin(model.t[i]))== 0
model.cons1 = Constraint(RangeSet(0,ni-1),rule=con1)

def con2(model,i):
    return model.t[i+1] - model.t[i] - 0.5*h*model.u[i+1] - 0.5*h*model.u[i] == 0
model.cons2 = Constraint(RangeSet(0,ni-1),rule=con2)

model.x[0] = 0.0
model.x[0].fixed = True
model.x[ni] = 0.0
model.x[ni].fixed = True
model.t[0] = 0.0
model.t[0].fixed = True
model.t[ni] = 0.0
model.t[ni].fixed = True
