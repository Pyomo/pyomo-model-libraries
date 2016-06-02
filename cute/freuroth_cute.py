#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
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

#   Source: problem 2 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   See also Toint#33, Buckley#24
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()


n = 5000
ngs = n-1

model.x = Var(RangeSet(1,n))

def f_rule(model):
    return sum(((5.0-model.x[i+1])*model.x[i+1]**2+model.x[i]-2*model.x[i+1]-13.0)**2 for i in range(1,ngs+1))+\
    sum(((1.0+model.x[i+1])*model.x[i+1]**2+model.x[i]-14*model.x[i+1]-29.0)**2 for i in range(1,ngs+1))
model.f = Objective(rule=f_rule)

model.x[1] = 0.5
model.x[2] = -2.0

for i in range(3,n+1):
    model.x[i] = 0.0
