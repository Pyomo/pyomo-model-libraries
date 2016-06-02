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

#   Source: Problem 11 in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SXR2-AN-3-0

from pyomo.core import *
model = ConcreteModel()

model.M = 10

model.xinit = {}
model.xinit[1] = 0.0
model.xinit[2] = 10.0
model.xinit[3] = 1.0

def xinit(model,i):
    return model.xinit[i]
model.x = Var(RangeSet(1,3),initialize=xinit)

def t(model,i):
    return 0.1*i
model.t = Param(RangeSet(1,model.M),initialize=t)
    
def f_rule(model):
    return sum((exp(-model.t[i]*model.x[1])-exp(-model.t[i]*model.x[2])-model.x[3]\
    *exp(-model.t[i])+model.x[3]*exp(-i))**2 for i in range(1,model.M+1))
model.f = Objective(rule=f_rule)

def cons1(model):
    return model.x[3]==1.0
model.cons1 = Constraint(rule=cons1)
