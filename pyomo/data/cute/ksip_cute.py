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

#   Source: problem from Kortanek and No
#   The problem is really a semi-infinite QP
#   to appear in SIAM J. Optimization.

#   The structure is the following :


#     min  "Sum"{ Xj^2/(2j) + Xj/j  ;  j=1,...,n }   subject to

#      "Sum"{ t^(j-1)#Xj } ; j=1,...,n  >=  b(t) for all t in [0 1].


# Four examples are considered for n = 20, corresponding to the RHS
# function, b(t) : sin(t), 1/(2-t), exp(t), and tan(t).

# The interval [0 1] is dicretized via steps of 1/1000

#   SIF input: A.R. Conn, May 1993

#   classification QLR2-AN-20-1001

from pyomo.core import *
model = ConcreteModel()
n = 20.0
m = 1000.0
model.N = RangeSet(1,n)
model.M = RangeSet(0,m)
model.x = Var(model.N,initialize=2.0)

model.obj = Objective(expr=sum((model.x[j]**2/(2.0*j) + model.x[j]/float(j)) for j in model.N))

def cons1_rule(model,i):
    return sum((i/m)**(j-1)*model.x[j] for j in model.N) >= sin(i/m)
model.c = Constraint(model.M,rule=cons1_rule)
