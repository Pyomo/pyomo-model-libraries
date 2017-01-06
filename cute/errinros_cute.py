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
#   An error in specifying problem CHNROSNB.
#   SIF input: Ph. Toint, Sept 1990.

#   classification SUR2-AN-V-0

from pyomo.environ import *
model = AbstractModel()

model.N = Param(initialize=50)
model.S = RangeSet(1,model.N)
model.alpha = Param(model.S)
model.x = Var(model.S,initialize=-1.0)

model.SS = RangeSet(2,model.N)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    sum1 = sum ([(model.x[i-1]-16*value(model.alpha[i])**2*model.x[i]**2)**2 for i in model.SS])
    sum2 = sum ([(model.x[i]-1.0)**2 for i in model.SS])
    return sum1 + sum2
model.f = Objective(rule=f,sense=minimize)
