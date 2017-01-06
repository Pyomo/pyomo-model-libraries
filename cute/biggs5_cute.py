#  _________________________________________________________________________
#                                                                           
#  Pyomo: Python Optimization Modeling Objects                           
#  Copyright (c) 2010 Sandia Corporation.                                   
#  This software is distributed under the BSD License.                      
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,   
#  the U.S. Government retains certain rights in this software.             
#  For more information, see the Pyomo README.txt file.                     
#  _________________________________________________________________________

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

#   Source: Problem 74 in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SXR2-AN-6-0

from pyomo.environ import *
model = AbstractModel()

model.N = Param(initialize=6)
model.M = Param(initialize=13)
model.S = RangeSet(1,model.N)
model.SS = RangeSet(1,model.M)
model.xinit = Param(model.S)
def init1(model, i):
    return value(model.xinit[i])
model.x = Var(model.S, initialize=init1)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    sum1 = 0
    for i in model.SS:
        sum1 += (-exp(-0.1*i)+5*exp(-i)-3*exp(-0.4*i)+ model.x[3]*exp(-0.1*i*model.x[1])\
        - model.x[4]*exp(-0.1*i*model.x[2]) + model.x[6]*exp(-0.1*i*model.x[5]))**2
    return sum1
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return model.x[6] == 3
model.cons1 = Constraint(rule=cons1)
