#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, and Brandon C. Barrera
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

#   Source:  The first problem given by
#   R. Fletcher,
#   "An optimal positive definite update for sparse Hessian matrices"
#   Numerical Analysis report NA/145, University of Dundee, 1992.

#   N.B. This formulation is incorrect. See FLETCBV2.SIF for
#        the correct version.

#   SIF input: Nick Gould, Oct 1992.

#   classification OUR2-AN-V-0

from pyomo.core import *
model = AbstractModel()

model.n = Param(initialize=10)
model.kappa = Param(initialize=1.0)
model.objscale = Param(initialize=1.0e0)
def h_rule(model):
    return 1/(value(model.n)+1.0)
model.h = Param(initialize=h_rule)
def p_rule(model):
    return 1/value(model.objscale)
model.p = Param(initialize=p_rule)

model.S = RangeSet(1,model.n)
model.SS = RangeSet(1,model.n-1)

def x_int(model, i):
    return i*value(model.h)
model.x = Var(model.S, initialize=x_int)

def f(model):
    exp1 = 0.5*value(model.p)*(model.x[1])**2
    exp2 = 0.5*value(model.p)*(model.x[value(model.n)])**2
    sum1 = sum ([0.5*value(model.p)*(model.x[i]-model.x[i+1])**2 for i in model.SS])
    sum2 = sum ([(value(model.p)*(-1-2/value(model.h)**2)*model.x[i]) for i in model.S])
    sum3 = sum ([(-value(model.kappa)*value(model.p)*cos(model.x[i])/value(model.h)**2) for i in model.S])
    return (exp1 + sum1 + exp2 + sum2 + sum3)
model.f = Objective(rule=f,sense=minimize)
