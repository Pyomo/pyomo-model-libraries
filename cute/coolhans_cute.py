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
#   S. Ceria, private communication, 1995.

#   SIF input: Ph. Toint, Feb 1995.

#   classification NQR2-RN-9-9

from pyomo.environ import *
model = AbstractModel()

model.N = RangeSet(1,3)

model.A = Param(model.N,model.N)
model.B = Param(model.N,model.N)
model.C = Param(model.N,model.N)

model.X = Var(model.N,model.N,initialize=0.0)

def _AXX(model,i,j):
    return sum(sum(model.A[i,k]*model.X[k,m] for k in range(1,4)) *model.X[m,j] for m in range(1,4))
model.AXX = Expression(model.N, model.N, rule=_AXX)

def _BX(model,i,j):
    return sum(model.B[i,k]*model.X[k,j] for k in range(1,4))
model.BX = Expression(model.N, model.N, rule=_BX)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    return 0.0
model.f = Objective(rule=f)
    
def con1(model,i,j):
    return (model.AXX[i,j] + model.BX[i,j] + model.C[i,j]) == 0
model.matrix = Constraint(model.N,model.N,rule=con1)
    
