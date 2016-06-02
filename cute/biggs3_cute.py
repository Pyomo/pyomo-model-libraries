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

#   Source: Problem 152 in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SXR2-AN-6-0

from pyomo.core import *
model = ConcreteModel()

model.N = Param(initialize=6)
model.M = Param(initialize=13)
model.S = RangeSet(1,model.N)
model.SS = RangeSet(1,model.M)

model.x = Var(model.S)
model.x[1] = 1.0
model.x[2] = 2.0
model.x[3] = 1.0
model.x[4] = 1.0
model.x[5] = 4.0
model.x[6] = 3.0

def f_rule(model):
    sum1 = 0.0  
    for i in model.SS:  
        sum1 +=(-exp(-0.1*i)+5*exp(-i)-3*exp(-0.4*i)+model.x[3]*exp(-0.1*i*model.x[1])\
        -model.x[4]*exp(-0.1*i*model.x[2])+model.x[6]*exp(-0.1*i*model.x[5]))**2
    return sum1
model.f = Objective(rule=f_rule)
    
def cons1(model):
    return model.x[3]==1
model.cons1 = Constraint(rule=cons1)

def cons2(model):
    return model.x[5]==4
model.cons2 = Constraint(rule=cons2)

def cons3(model):
    return model.x[6]==3
model.cons3 = Constraint(rule=cons3)


