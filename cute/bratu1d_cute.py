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

#   Source: Problem 121 (p. 99) in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification OXR2-MN-V-0

from pyomo.core import *
model = ConcreteModel()

N = 1001
L = -3.4
h = 1.0/(N+1.0)

def x(model,i):
    if (i==0) or (i==N+1):
        return 0.0
    else:
        return -0.1*h*(i**2)
model.x = Var(RangeSet(0,N+1),initialize=x)

def f_rule(model):
    return 2*L*h*(exp(model.x[1])-exp(model.x[0]))/(model.x[1]-model.x[0])\
    + sum (2.0*model.x[i]**2/h for i in range(1,N+1))\
    - sum (2.0*model.x[i]*model.x[i-1]/h for i in range(1,N+1))\
    + sum (2.0*L*h*(exp(model.x[i+1])-exp(model.x[i]))/(model.x[i+1]-model.x[i]) for i in range(1,N+1)) 
model.f = Objective(rule=f_rule)

model.x[0] = 0.0
model.x[0].fixed = True
model.x[N+1] = 0.0
model.x[N+1].fixed = True
