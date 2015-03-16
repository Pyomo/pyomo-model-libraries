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
#   B. Chen and P. T. Harker,
#   SIMAX 14 (1993) 1168-1190

#   SDIF input: Nick Gould, November 1993.

#   classification QBR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()

n = 1000
nfree = 500
ndegen = 200

def x_p_init(model,i):
    if i<=0:
        return 0.0
    elif i>nfree:
        return 0.0
    else:
        return 1.0
model.x_p = Param(RangeSet(-1,n+2),initialize=x_p_init)

def x_init(model,i):
    return 0.5
model.x = Var(RangeSet(1,n),initialize=x_init,bounds=(0.0,None))

def f(model):
    return sum(0.5*(model.x[i+1]+model.x[i-1] - 2*model.x[i])**2 for i in range(2,n)) +\
    0.5*model.x[1]**2+0.5*(2*model.x[1] - model.x[2])**2 +0.5*(2*model.x[n] - model.x[n-1])**2 +\
    0.5*(model.x[n])**2 +sum(model.x[i]*(-6*model.x_p[i] + \
    4*model.x_p[i+1] + 4*model.x_p[i-1] -model.x_p[i+2] - model.x_p[i-2])for i in range(1,nfree+ndegen+1)) +\
    sum(model.x[i]*(-6*model.x_p[i] + 4*model.x_p[i+1] + 4*model.x_p[i-1] -\
   model.x_p[i+2] - model.x_p[i-2] + 1)for i in range(nfree+ndegen+1,n+1))
model.f = Objective(rule=f)
