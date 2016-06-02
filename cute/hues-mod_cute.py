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

#   Source: An inverse problem from astronomy,
#   reformulated as a convex quadratic program by
#   S. P. Hestis, SIAM Review 34 (1992) pp. 642-647.

#   SIF input: Nick Gould, January 1993.
#   improvements by: Ruediger Franke (Ruediger.Franke@RZ.TU-Ilmenau.DE)

#   classification QLR2-MN-V-V

from pyomo.core import *
model = ConcreteModel()
K = 10000
Range = 1.0

def deltax_rule(model):
    return Range/K
model.deltax = Param(initialize=deltax_rule)
model.N = RangeSet(1,K)
model.M = Var(model.N,bounds=(0,None),initialize=1.0)

model.f = Objective(expr=sum((model.M[i]**2)/K for i in model.N))
model.cons1 = Constraint(expr=sum(((i**3)-((i-1)**3))*(model.deltax**3)*model.M[i]/3 for i in model.N) - 1835.2 == 0)
model.cons2 = Constraint(expr=sum(((i**5)-((i-1)**5))*(model.deltax**5)*model.M[i]/5 for i in model.N) - 909.8 == 0)
