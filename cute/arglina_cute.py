#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

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

#   Source: Problem 32 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.
#   See also Buckley#80 (with different N and M)
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-V-0


from pyomo.core import *
model = ConcreteModel()


N = 100.0
M = 200.0

model.x = Var(RangeSet(1,N),initialize=1.0)

def f_rule(model):
    return sum((sum(-2.0*model.x[j]/M for j in range(1,i)) + \
             model.x[i]*(1.0-2.0/M) + \
             sum(-2.0*model.x[j]/M for j in range(i+1,int(N)+1)) - \
             1.0)**2 for i in range(1,int(N)+1) )+ \
           sum( (sum(-2.0*model.x[j]/M for j in range(1,int(N)+1)) -1.0 )**2 \
             for i in range(int(N)+1,int(M)+1) )
model.f = Objective(rule=f_rule)


