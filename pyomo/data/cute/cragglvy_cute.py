#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

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

#   Source:  problem 32 in
#   Ph. L. Toint,
#   "Test problems for partially separable optimization and results
#   for the routine PSPMIN",
#   Report 83/4, Department of Mathematics, FUNDP (Namur, B), 1983.

#   See  also Buckley#18
#   SIF input: Ph. Toint, Dec 1989.

#   classification OUR2-AY-V-0

from pyomo.core import *
model = ConcreteModel()

m = 2499
n = 2*m+2

def x(model,i):
    if i==1:
        return 1.0
    else:
        return 2.0
model.x = Var(RangeSet(1,n),initialize=x)

def f(model):
    return sum((exp(model.x[2*i-1])-model.x[2*i])**4 +\
    100*(model.x[2*i]-model.x[2*i+1])**6 +\
    (tan(model.x[2*i+1]-model.x[2*i+2])+model.x[2*i+1]-model.x[2*i+2])**4 +\
    (model.x[2*i-1])**8 +\
    (model.x[2*i+2]-1.0)**2 for i in range(1,m+1))
model.f = Objective(rule=f)
