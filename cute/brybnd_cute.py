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
# Formulated in Pyomo by Juan Lopez
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

#   Source: problem 31 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   See also Buckley#73 (p. 41) and Toint#18

#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()

N = 5000
ml = 5
mu = 1

model.x = Var(RangeSet(1,N), initialize=-1)

def j_init(model,i):
    return [j for j in range(1,N+1) if (j != i) and (max(1,i-ml) <= j) and (j <= min(N,i+mu))]
model.J = Set(RangeSet(1,N),initialize=j_init)

def f_rule(model):
    return sum((model.x[i]*(2+5*model.x[i]**2) + 1 -\
    sum(model.x[j]*(1+model.x[j]) for j in model.J[i]))**2 for i in range(1,N+1))
model.f = Objective(rule=f_rule)
