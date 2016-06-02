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
#  Formulated in pyomo by Logan Barnes. Taken from:

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

#   Source: problem 44 in
#   W. Hock and K. Schittkowski,
#   "Test examples for nonlinear programming codes",
#   Lectures Notes in Economics and Mathematical Systems 187, Springer
#   Verlag, Heidelberg, 1981.

#   SIF input: Ph.L. Toint, October 1990.

#   classification QLR2-AN-4-6

from pyomo.core import *
model = ConcreteModel()
N = 4
model.M = RangeSet(1,4)
model.x = Var(model.M,bounds=(0.0,None),initialize=1.0)

model.f = Objective(expr=model.x[1]-model.x[2]-model.x[3]-model.x[1]*model.x[3]+model.x[1]*model.x[4]+model.x[2]*model.x[3]-model.x[2]*model.x[4])

model.cons1 = Constraint(expr=-model.x[1]-model.x[2]+8>=0)
model.cons2 = Constraint(expr=-4*model.x[1]-model.x[2]+12>=0)
model.cons3 = Constraint(expr=-3*model.x[1]-4*model.x[2]+12>=0)
model.cons4 = Constraint(expr=-2*model.x[3]-model.x[4]+8>=0)
model.cons5 = Constraint(expr=-model.x[3]-2*model.x[4]+8>=0)
model.cons6 = Constraint(expr=-model.x[3]-model.x[4]+5>=0)
