#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil
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
#   A.R. Conn, N. Gould and Ph.L. Toint,
#   "The LANCELOT User's Manual",
#   Dept of Maths, FUNDP, 1991.

#   SIF input:  Ph. Toint, Jan 1991.

#   classification OOR2-AN-2-1

from pyomo.core import *
model = ConcreteModel()

model.x = Var()
model.y = Var()


model.f = Objective (expr=exp(model.x-2*model.y))

model.cons1 = Constraint(expr=sin(-model.x+model.y-1)==0)
model.cons2 = Constraint (expr=-2<=model.x<=2)
model.cons3 = Constraint(expr=-1.5<=model.y<=1.5)
