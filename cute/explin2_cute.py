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

#   classification OBR2-AN-V-V

from pyomo.core import *
model = AbstractModel()

model.n = Param(initialize=120)
model.m = Param(initialize=10)

model.S = RangeSet(1,model.n)
model.x = Var(model.S,bounds=(0,10.0),initialize=0.0)

model.SS = RangeSet(1,model.m)
def f(model):
    sum1 = sum ([exp(0.1*i*model.x[i]*model.x[i+1]/value(model.m))  for i in model.SS])
    sum2 = sum ([(-10.0*i*model.x[i]) for i in model.S])
    return sum1 + sum2
model.f = Objective(rule=f,sense=minimize)
