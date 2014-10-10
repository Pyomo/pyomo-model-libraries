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

#   Source: problem 3 in
#   W. Hock and K. Schittkowski,
#   "Test examples for nonlinear programming codes",
#   Lectures Notes in Economics and Mathematical Systems 187, Springer
#   Verlag, Heidelberg, 1981.

#   SIF input: A.R. Conn March 1990

#   classification QBR2-AN-2-0

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,2)
model.x_init = Param(model.N,mutable=True)
model.x_init[1] = 10.0
model.x_init[2] = 1.0
def x_init(model,i):
    return model.x_init[i]
model.x = Var(model.N,initialize=x_init)

model.f = Objective(expr=model.x[2]+(-model.x[1]+model.x[2])**2)

model.cons1 = Constraint(expr=model.x[2]>=0.0)
