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
#   A.R. Conn, N. Gould and Ph.L. Toint,
#   "LANCELOT, a Fortran package for large-scale nonlinear optimization",
#   Springer Verlag, FUNDP, 1992.

#   SIF input: Ph. Toint, Jan 1991.

#   classification SUR2-AN-2-0

from pyomo.core import *
model = AbstractModel()

model.p = Param(initialize=10)
model.h = Param(initialize=0.25)
model.alpha = Var()
model.beta = Var()
model.S = RangeSet(1,model.p)
def f(model):
    return sum ([(model.alpha*exp(i*value(model.h)*model.beta)-i*value(model.h))**2 for i in model.S])
model.f = Objective(rule=f,sense=minimize)
