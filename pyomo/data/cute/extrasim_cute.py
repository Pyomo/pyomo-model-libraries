#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, and Brandon C. Barrera
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
#   A.Conn, N. Gould, Ph. Toint
#   "LANCELOT, a Fortran package for large-scale nonlinear optimization"
#   Springer Verlag, 1992

#   SIF input: Ph. Toint, Dec 1991.

#   classification LLR2-AN-2-1

from pyomo.core import *
model = AbstractModel()

model.x = Var(bounds=(0,None))
model.y = Var()

def f(model):
    return model.x + 1
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return model.x+2*model.y-2.0 == 0
model.cons1 = Constraint(rule=cons1)
