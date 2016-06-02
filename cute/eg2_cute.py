#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Carl D. Laird and Daniel P. Word
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
#   "LANCELOT, A Fortran Package for Large-Scale Nonlinear Optimization
#   (Release A)"
#   Springer Verlag, 1992.

#   SIF input: N. Gould and Ph. Toint, June 1994.

#   classification OBR2-AY-3-0

from pyomo.core import *
model = AbstractModel()
model.N = Param(initialize=1000)
model.S = RangeSet(1,model.N)

model.x = Var(model.S)

def f(m):
    return sum(sin(m.x[1]+m.x[i]**2 - 1.0) for i in range(1,value(m.N))) +\
           0.5*sin(m.x[value(m.N)]**2)

model.f = Objective(rule=f, sense=minimize)
