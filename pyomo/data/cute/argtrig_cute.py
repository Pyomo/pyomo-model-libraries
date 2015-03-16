# _________________________________________________________________________
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

#   Source:  Problem 26 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   SIF input: Ph. Toint, Dec 1989.

#   classification NOR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()

N = 100
model.x = Var(RangeSet(1,N),initialize=1.0/N)

def f_rule(model):
    return 0
model.f = Objective(rule=f_rule)

def cons1_rule(model,i):
    return i*(cos(model.x[i])+sin(model.x[i])) + sum(cos(model.x[j]) for j in range(1,N+1)) - (N+i) == 0
model.cons = Constraint(RangeSet(1,N),rule=cons1_rule)
    
    
    
