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

#   Source: 
#   K.C. Kiwiel,
#   "Methods of Descent for Nondifferentiable Optimization"
#   Lectures Notes in Mathematics 1133, Springer Verlag, 1985.

#   SIF input: Ph. Toint, Nov 1993.

#   classification  LQR2-AN-3-2

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,2)
model.x = Var(model.N)
model.x[1] = -1.5
model.x[2] =  2.0
model.u = Var()

model.f = Objective(expr=model.u)

model.cons1 = Constraint(expr=-model.u+model.x[2]-1+model.x[1]**2+(model.x[2]-1.0)**2<=0.0)
model.cons2 = Constraint(expr=-model.u+model.x[2]+1-model.x[1]**2-(model.x[2]-1.0)**2<=0.0)
