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
#   C. Gigola and S. Gomez,
#   "A Regularization Method for Solving the Finite Convex Min-Max Problem",
#   SINUM 27(6), pp. 1621-1634, 1990.

#   SIF input: Ph. Toint, August 1993.

#   classification LQR2-AN-3-3

from pyomo.core import *
model = ConcreteModel()

model.x = Var([1,2], initialize=2.0)
model.z = Var(initialize=2.0)

model.f = Objective(expr=model.z)

model.cons1 = Constraint(expr=model.z+5.0*model.x[1]-model.x[2] >= 0)
model.cons2 = Constraint(expr=model.z-4.0*model.x[2]-model.x[1]**2-model.x[2]**2 >= 0)
model.cons3 = Constraint(expr=model.z-5.0*model.x[1]-model.x[2] >= 0)
