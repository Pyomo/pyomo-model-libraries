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
#   R. Fletcher
#   "Practical Methods of Optimization",
#   second edition, Wiley, 1987.

#   SIF input: Ph. Toint, March 1994.

#   classification QOR2-AN-4-4

from pyomo.core import *
model = AbstractModel()

model.S1 = RangeSet(1,4)
model.x = Var(model.S1,initialize=1)

def f(model):
    return model.x[1]*model.x[2]
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return (model.x[1]*model.x[3]+model.x[2]*model.x[4])**2/(model.x[1]**2+model.x[2]**2) - model.x[3]**2 - model.x[4]**2 + 1 == 0
model.cons1 = Constraint(rule=cons1)
def cons2(model):
    return model.x[1]-model.x[3]-1 >= 0
model.cons2 = Constraint(rule=cons2)
def cons3(model):
    return model.x[2]-model.x[4]-1 >= 0
model.cons3 = Constraint(rule=cons3)
def cons4(model):
    return model.x[3]-model.x[4] >= 0
model.cons4 = Constraint(rule=cons4)
def cons5(model):
    return model.x[4] >= 1
model.cons5 = Constraint(rule=cons5)
