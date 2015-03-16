#
#  Pyomo Python Optimization Modeling Objects
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

#   Source:
#   Hans Mittelmann, private communication.

#   SIF input: N. Gould, Jan 1998

#   classification OOR2-AY-V-0

from pyomo.core import *
model = ConcreteModel()

n = 250

model.x = Var(RangeSet(1,n), initialize=1.0)

def f_rule(model):
    return sum(exp(model.x[j]-model.x[i]) for i in range(1,n) for j in range(i+1,n+1))
model.f = Objective(rule=f_rule)

    
def cons1_rule(model,i):
    return model.x[i]+model.x[i+1] >= 0.0
model.cons1 = Constraint(RangeSet(1,n-1),rule=cons1_rule)

def cons2_rule(model,i):
    return exp(model.x[i])+exp(model.x[i+1]) <= 20.0
model.cons2 = Constraint(RangeSet(1,n-1),rule=cons2_rule)
