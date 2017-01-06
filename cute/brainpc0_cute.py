#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

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
#   N. Dautrebande,
#   private communication, 1994.

#   SIF input: Ph. Toint, Oct 1994.

#   classification SOR2-MY-6907-6900

from pyomo.environ import *
model = AbstractModel()

NS = 2.0
NP = 5.0
NO = 26.0
H = 1.0
NT = 3450.0

model.TO = Param(RangeSet(1,NO))
model.U = Param(RangeSet(0,NT))
model.oc_init = Param(RangeSet(1,NO))

model.x = Var(RangeSet(1,NS),RangeSet(0,NT),bounds=(0,None),initialize=0.001)
model.k = Var(RangeSet(1,NP),bounds=(0,None), initialize=0.001)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

model.x[1,0] = 0.0
model.x[1,0].fixed = True
model.x[2,0] = 0.0
model.x[2,0].fixed = True

def f_rule(model):
    return sum(1000*(-(model.x[1,value(model.TO[t])]+model.x[2,value(model.TO[t])])*model.k[1]+model.x[1,value(model.TO[t])]+\
    model.x[2,value(model.TO[t])]+model.U[value(model.TO[t])]*model.k[1]-model.oc_init[t])**2 for t in range(1,int(NO)+1))
model.f = Objective(rule=f_rule)

def cons1_rule(model,t):
    return 1000*(H*(model.k[3]+model.k[4])*model.x[1,t]- H*model.k[5]*model.x[2,t] -\
    H*model.U[t]*model.k[2] + model.x[1,t+1] - model.x[1,t]) == 0
model.cons1 = Constraint(RangeSet(0,int(NT)-1),rule=cons1_rule)

def cons2_rule(model,t):
    return 1000*(H*model.k[5]*model.x[2,t] - H*model.k[4]*model.x[1,t] + model.x[2,t+1] - model.x[2,t]) == 0
model.cons2 = Constraint(RangeSet(0,int(NT)-1),rule=cons2_rule)


