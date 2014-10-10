#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Formulated in pyomo by Logan Barnes and Gabe Hackebeil.
#
#  Taken from:

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

#   classification OUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()
n = 1000
model.N = RangeSet(1,n)
model.M = RangeSet(2,n-1)
alpha = 0.5

def x_init_rule(model,i):
    return i/(n+1.0)
model.x = Var(model.N,initialize=x_init_rule)

model.f = Objective(expr=sum(model.x[i] for i in model.N)+sum(alpha*cos(2*model.x[i]-model.x[n]-model.x[1]) for i in model.M))
