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

#   Source: Problem 3 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   See also Buckley#16.
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-3-0


from pyomo.environ import *
model = AbstractModel()

model.N = Param(initialize=3)
model.M = Param(initialize=15)

model.S = RangeSet(1,model.M)
model.y = Param(model.S)
def u_rule(model, i):
    return i
model.u = Param(model.S,initialize=u_rule)
def v_rule(model, i):
    return 16-i
model.v = Param(model.S,initialize=v_rule)
def w_rule(model, i):
    return min([value(model.u[i]),value(model.v[i])])
model.w = Param(model.S,initialize=w_rule)

model.SS = RangeSet(1,model.N)
model.x = Var(model.SS, initialize=1.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    return sum ([( value(model.y[i])-(model.x[1]+value(model.u[i])/(value(model.v[i])*model.x[2]+value(model.w[i])*model.x[3])) )**2 for i in model.S])
model.f = Objective(rule=f,sense=minimize)
