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
#   R.  Wommersley and R. Fletcher,
#   "An algorithm for composite nonsmooth optimization problems"
#   JOTA, vol.48, pp.493-523, 1986

#   SIF input: Ph. Toint, April 1992.

#   classification LOR2-AN-3-3

from pyomo.core import *
model = AbstractModel()

model.S = RangeSet(1,2)
model.x = Var(model.S, initialize=2.0)
model.u = Var(initialize=1.0)

def f(model):
    return model.u
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return model.u-model.x[1]**2-model.x[2]**4 >= 0
model.cons1 = Constraint(rule=cons1)

def cons2(model):
    return model.u-(2.0-model.x[1])**2-(2.0-model.x[2])**2 >= 0
model.cons2 = Constraint(rule=cons2)

def cons3(model):
    return model.u-2*exp(model.x[2]-model.x[1]) >= 0
model.cons3 = Constraint(rule=cons3)
