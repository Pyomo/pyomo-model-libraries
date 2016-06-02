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

#   Source: a variant on a problem of optimal knot placement in a
#   scheme for ordinary differential equations with boundary values
#   suggested by J. R. Kightley, see N. I. M. Gould, "An algorithm for
#   large-scale quadratic programming", IMA J. Num. Anal (1991),
#   11, 299-324, problem class 3. Note that the optimal solution values
#   given in that paper are incorrect.

#   SIF input: Nick Gould, December 1991

#   classification QLR2-MN-V-V

from pyomo.core import *
model = ConcreteModel()

K = 350

def alpha_rule(model,i):
    if i>1:
        return 1.0+1.01**i
    else:
        return 2.0
model.alpha = Param(RangeSet(1,K+1),initialize=alpha_rule)

def knot_init_rule(model,i):
    return model.alpha[i]
def knot_bounds_rule(model,i):
    return (model.alpha[i],model.alpha[i+1])
model.knot = Var(RangeSet(1,K),initialize=knot_init_rule,bounds=knot_bounds_rule)

def space_init_rule(model,i):
    return model.alpha[i+1]-model.alpha[i]
def space_bounds_rule(model,i):
    return (0.4*(model.alpha[i+2]-model.alpha[i]),0.6*(model.alpha[i+2]-model.alpha[i]))
model.space = Var(RangeSet(1,K-1),initialize=space_init_rule,bounds=space_bounds_rule)

def f_rule(model):
    return sum (.5*(model.space[i+1]-model.space[i])**2 for i in range(1,K-1))+\
    sum(0.5*(model.knot[K-i]+model.space[i]-model.alpha[K+1-i])**2 for i in range(1,K))
model.f = Objective(rule=f_rule)

def cons1_rule(model,i):
    return model.space[i]-model.knot[i+1]+model.knot[i] == 0
model.cons1 = Constraint(RangeSet(1,K-1),rule=cons1_rule)
