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

#   Source: problem 4 in
#   J.J. More',
#   "A collection of nonlinear model problems"
#   Proceedings of the AMS-SIAM Summer seminar on the Computational
#   Solution of Nonlinear Systems of Equations, Colorado, 1988.
#   Argonne National Laboratory MCS-P60-0289, 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification NOR2-RN-V-V

from pyomo.core import *
model = ConcreteModel()

n = 100
c = 1.0

def x_init(model,i):
    return i/float(n)
model.x = Param(RangeSet(1,n),initialize=x_init)

def w_init(model,i):
    return 1.0/float(n)
model.w = Param(RangeSet(1,n),initialize=w_init)

model.h = Var(RangeSet(1,n),initialize=1.0,bounds=(0,None))

model.f = Objective(expr=0.0)
    
def con1(model,i):
    return sum(-0.5*c*model.w[j]*model.x[i]/(model.x[i]+model.x[j])*model.h[i]*model.h[j] for j in range(1,n+1)) + model.h[i] == 1.0
model.cons = Constraint(RangeSet(1,n),rule=con1)

 
