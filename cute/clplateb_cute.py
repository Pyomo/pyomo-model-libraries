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

#   Source:
#   J. Nocedal,
#   "Solving large nonlinear systems of equations arising in mechanics",
#   Proceedings of the Cocoyoc Numerical Analysis Conference, Mexico,
#   pp. 132-141, 1981.

#   SIF input: Ph. Toint, Dec 1989.

#   classification OXR2-MN-V-0
from pyomo.core import *
model = ConcreteModel()

p = 71
wght = -0.1
disw = wght/(p-1)
hp2 = 0.5*p**2

model.x = Var(RangeSet(1,p),RangeSet(1,p),initialize=0.0)

def f(model):
    return sum(0.5*(model.x[i,j]-model.x[i,j-1])**2+\
    0.5*(model.x[i,j]-model.x[i-1,j])**2+\
    hp2*(model.x[i,j]-model.x[i,j-1])**4+\
    hp2*(model.x[i,j]-model.x[i-1,j])**4\
    for i in range(2,p+1) for j in range(2,p+1)) + sum(wght*model.x[p,j] for j in range(1,p+1))
model.f = Objective(rule=f)

for j in range(1,p+1):
    model.x[1,j] = 0.0
    model.x[1,j].fixed = True


