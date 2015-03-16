#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Gabe Hackebeil
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

#   classification LQR2-AY-V-V

from pyomo.core import *
model = ConcreteModel()

N = 165

gamma = 9.81
tmass = 500.0
bl = 1.0
fract = 0.6

length = bl*(N+1)*fract
mass = tmass/(N+1)
mg = mass*gamma

def x(model,i):
    return i*length/(N+1)
model.x = Var(RangeSet(0,N+1),initialize=x)

def y(model,i):
    return 0.0
model.y = Var(RangeSet(0,N+1),initialize=y)

model.z = Var(RangeSet(0,N+1),initialize=0.0)

def f_rule(model):
    return mg*model.y[0]/2.0 + sum(mg*model.y[i] for i in range(1,N+1)) + mg*model.y[N+1]/2.0
model.f = Objective(rule=f_rule)

def con1(model,i):
    return (model.x[i]-model.x[i-1])**2 + (model.y[i]-model.y[i-1])**2 + (model.x[i]-model.z[i-1])**2 == bl**2
model.cons1 = Constraint(RangeSet(1,N+1),rule=con1)

model.x[0] = 0.0
model.x[0].fixed = True
model.y[0] = 0.0
model.y[0].fixed = True
model.z[0] = 0.0
model.z[0].fixed = True
model.x[N+1] = length
model.x[N+1].fixed = True
