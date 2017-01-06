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
#   an example in a talk by W.K. Zhang and C. Fleury, LLN, 1994.

#   SIF input: Ph. Toint, November 1994

#   classification LOR2-MN-5-1

from pyomo.environ import *
model = AbstractModel()

model.S = RangeSet(1,5)
model.num = Param(model.S)

model.x = Var(model.S, bounds=(0.000001,None), initialize=1.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    se = sum ([model.x[i] for i in model.S])
    return se*0.0624
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    see = sum ([value(model.num[i])/model.x[i]**3 for i in model.S])
    return see - 1.0 <= 0
model.cons1 = Constraint(rule=cons1)
