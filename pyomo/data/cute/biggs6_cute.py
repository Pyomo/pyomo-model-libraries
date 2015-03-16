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

#   Source: Problem 21 in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-6-0

from pyomo.core import *
model = ConcreteModel()

model.N = 6
model.M = 13
model.s = RangeSet(1,model.N)

model.xinit = {}
model.xinit[1] = 1
model.xinit[2]  = 2
model.xinit[3]  = 1
model.xinit[4]  = 1
model.xinit[5]  = 4
model.xinit[6]  = 3

def x_init(model,i):
    return model.xinit[i]
model.x = Var(model.s,initialize=x_init)

def f_rule(model):
    return sum((-exp(-0.1*i)+5*exp(-i)-3*exp(-0.4*i)\
    + model.x[3]*exp(-0.1*i*model.x[1]) - model.x[4]*exp(-0.1*i*model.x[2]) +\
    model.x[6]*exp(-0.1*i*model.x[5]))**2 for i in range(1,model.M+1))
model.f = Objective(rule=f_rule)



    
    
    
    
    
