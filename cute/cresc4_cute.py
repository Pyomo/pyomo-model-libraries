#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Juan Lopez
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

#   classification OOR2-MY-6-8

from pyomo.environ import *
model = AbstractModel()

np = 4
model.x = Param(RangeSet(1,np))
model.y = Param(RangeSet(1,np))

model.v1 = Var(initialize=-40.0)
model.w1 = Var(initialize=5.0)
model.d = Var(bounds=(1e-8,None),initialize=1.0)
model.a = Var(bounds=(1.0,None),initialize=2.0)
model.t = Var(bounds=(0.0,6.2831852),initialize=1.5)
model.r = Var(bounds=(0.39,None),initialize=0.75)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    return(model.d+model.r)**2*acos(-((model.a*model.d)**2 - (model.a*model.d+model.r)**2\
    +(model.d+model.r)**2)/(2*(model.d+model.r)*model.a*model.d))\
    -(model.a*model.d+model.r)**2*acos(((model.a*model.d)**2+(model.a*model.d+model.r)**2-\
    (model.d+model.r)**2)/(2*(model.a*model.d+model.r)*model.a*model.d))\
    +(model.d+model.r)*model.a*model.d*sin(acos(-((model.a*model.d)**2-(model.a*model.d+model.r)**2\
    +(model.d+model.r)**2)/(2*(model.d+model.r)*model.a*model.d)))
model.f = Objective(rule=f)

def con1(model,i):
    return (model.v1+model.a*model.d*cos(model.t)-model.x[i])**2+\
    (model.w1+model.a*model.d*sin(model.t)-model.y[i])**2 - (model.d+model.r)**2<= 0.0
model.cons1 = Constraint(RangeSet(1,np),rule=con1)

def con2(model,i):
    return (model.v1-model.x[i])**2 + (model.w1-model.y[i])**2 - (model.a*model.d+model.r)**2 >= 0.0
model.cons2 = Constraint(RangeSet(1,np),rule=con2)
