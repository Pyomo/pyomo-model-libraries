#
#  Pyomo: Python Optimization Modeling Objects
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
#   G. Li,
#   "The secant/finite difference algorithm for solving sparse
#   nonlinear systems of equations",
#   SIAM Journal on Optimization, (to appear), 1990.

#   SIF input: Ph. Toint, Apr 1990.
#              minor correction by Ph. Shott, January 1995.

#   classification OUR2-AN-V-0


from pyomo.core import *
model = ConcreteModel()

N = 2000
model.x = Var(RangeSet(1,N),initialize=0.0)

def f_rule(model):
    return sum((model.x[i]-2)**4 + (model.x[i]*model.x[i+1]-2*model.x[i+1])**2 +\
    (model.x[i+1]+1)**2 for i in range(1,N)) + 16
model.f = Objective(rule=f_rule)
