#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

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

#   Source: Problem 4 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   See also Buckley#25
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-2-0

from pyomo.core import *
model = ConcreteModel()

N = 2

model.x = Var(RangeSet(1,N),initialize=1.0)

    
def f_rule(model):
    return sum((model.x[i]-1000000)**2 for i in range(1,N))+\
    sum((model.x[i+1]-0.000002)**2 for i in range(1,N))+\
    sum((model.x[i]*model.x[i+1]-2.0)**2 for i in range(1,N))
model.f = Objective(rule=f_rule)
