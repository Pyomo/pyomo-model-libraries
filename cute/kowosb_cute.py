#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Formulated in pyomo by Logan Barnes. Taken from:

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

#   Source:  Problem 15 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-MN-4-0

from pyomo.environ import *
model = AbstractModel()
N = 4
M = 11
model.n = RangeSet(1,N)
model.m = RangeSet(1,M)
model.x_init = {}
model.x_init[1] = 0.25
model.x_init[2] = 0.39
model.x_init[3] = 0.415
model.x_init[4] = 0.39
def x_init_rule(model,i):
    return model.x_init[i]
model.x = Var(model.n,initialize=x_init_rule)
model.y = Param(model.m)
model.u = Param(model.m)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return sum((model.y[i]-model.x[1]*(model.u[i]**2+model.u[i]*model.x[2])/(model.u[i]**2+model.u[i]*model.x[3]+model.x[4]))**2 for i in model.m)

model.f = Objective(rule=f_rule,sense=minimize)
