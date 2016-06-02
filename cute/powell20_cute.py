
#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, Brandon C. Barrera and Saumyajyoti Chaudhuri
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

#   Source: a generalization of problem 20 in
#   M. J. D. Powell
#   "On the quadratic progamming algorithm of Goldfarb and Idnani",
#   Mathematical Programmimg Study 25 (1985) 46-61.

#   SIF input: Nick Gould, August 1994.

#   classification QLR2-AN-V-V

from pyomo.core import *
model = AbstractModel()

model.N = Param(initialize=10)

model.Rx = RangeSet(1,model.N)
def x(model, i):
    if (i%2==1):
        return 0
    else:
        return -0.5-i
model.x = Var(model.Rx,initialize=x)

def f(model):
    return  0.5*sum( model.x[i]**2 for i in model.Rx )
model.f = Objective(rule=f,sense=minimize)

model.Rc1 = RangeSet(1,model.N-1)
def cons1(model,k):
    return model.x[k+1]-model.x[k] >= -0.5+(-1)**k*k
model.cons1 = Constraint(model.Rc1,rule=cons1)

def cons2(model):
    return model.x[1]-model.x[value(model.N)] >= model.N - 0.5
model.cons2 = Constraint(rule=cons2)
