#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

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

#   Source: Problem 9 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   See also Buckley#28
#   SIF input: Ph. Toint, Dec 1989.

#   classification NOR2-AN-3-15
from pyomo.environ import *
model = AbstractModel()

x_init =  {}
x_init[1] = 0.4
x_init[2] = 1
x_init[3] = 0

def x_init_rule(model,i):
    return x_init[i]
model.x = Var(RangeSet(1,3),initialize = x_init_rule)
model.rhs = Param(RangeSet(1,15))

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return 0
model.f = Objective(rule=f_rule)

def cons_rule(model,i):
    return (model.x[1]*exp(-0.5*model.x[2]*(0.5*(8-i)-model.x[3])**2) == model.rhs[i])
model.cons = Constraint(RangeSet(1,15),rule=cons_rule)

