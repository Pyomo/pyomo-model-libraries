#  This software is distributed under the BSD License.
#  under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
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

#   Source: problem 11 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   See also Buckley#27
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-MN-3-0

from pyomo.environ import *
model = ConcreteModel()

N=3
M=99

def t_param_rule(model,i):
    return i/100.0
model.t = Param(RangeSet(1,M),initialize=t_param_rule) 

def y_param_rule(model,i):
    return 25+ (-50*log(value(model.t[i])))**(2.0/3.0)
model.y = Param(RangeSet(1,M),initialize = y_param_rule)

model.x = Var(RangeSet(1,N))
model.x[1] = 5.0;
model.x[2] = 2.5;
model.x[3] = 0.15;

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))
    
def f_rule(model):
    return sum((exp(abs(model.y[i]-model.x[2])**model.x[3]/(-model.x[1]))-model.t[i])**2 for i in range(1,M+1))
model.f = Objective(rule=f_rule)
