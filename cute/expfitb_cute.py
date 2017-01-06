#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
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
#   M.J.D. Powell,
#   "A tolerant algorithm for linearly constrained optimization
#   calculations"'
#   Mathematical Programming 45(3), pp.561--562, 1989.

#   SDIF input: Ph. Toint and N. Gould, May 1990.

#   classification OLR2-AN-5-102

from pyomo.environ import *
model = AbstractModel()

R = 51.0

def T_rule(model,i):
    return 5*(i-1)/(R-1)
model.T = Param(RangeSet(1,R),initialize=T_rule,mutable=True)

def ET_rule(model,i):
    return exp(model.T[i])
model.ET = Param(RangeSet(1,R),initialize=ET_rule)

model.pinit = Param(RangeSet(0,2))

def P_init(model,i):
    return model.pinit[i]
model.P = Var(RangeSet(0,2),initialize=P_init)

model.Q = Var(RangeSet(1,2),initialize=0.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return sum((\
    (model.P[0]+model.P[1]*model.T[i]+model.P[2]*model.T[i]**2)/\
    (model.ET[i]*(1+model.Q[1]*(model.T[i]-5)+model.Q[2]*(model.T[i]-5)**2))\
    -1 )**2 for i in range(1,int(R)+1))
model.f = Objective(rule=f_rule)

def cons1(model,i):
    return model.P[0]+model.P[1]*model.T[i]+model.P[2]*model.T[i]**2-(model.T[i]-5)*model.ET[i]*model.Q[1]-\
        (model.T[i]-5)**2*model.ET[i]*model.Q[2]-model.ET[i]>= 0
model.cons1 = Constraint(RangeSet(1,R),rule=cons1)

def cons2(model,i):
    return (model.T[i]-5)*model.Q[1] + (model.T[i]-5)**2*model.Q[2]+0.99999 >= 0
model.cons2 = Constraint(RangeSet(1,R),rule=cons2)
