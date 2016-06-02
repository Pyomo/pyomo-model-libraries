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

#   Source: Nick Gould

#   SIF input: Nick Gould, September 1997.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()

N = 10000
K = 20

model.x = Var(RangeSet(1,N),initialize=0.0001/(N+1))

def Q(model,i):
    if i<=N-K:
        return sum(model.x[j] for j in range(i,i+K+1))
    else:
        return sum(model.x[j] for j in range(i,N+1))

def f(model):
    return sum(Q(model,i)*(Q(model,i)*(Q(model,i)**2-20)-0.1) for i in range(1,N+1))
model.f = Objective(rule=f)
