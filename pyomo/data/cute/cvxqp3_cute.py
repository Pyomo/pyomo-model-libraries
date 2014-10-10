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

#   classification QLR2-AN-V-V

from pyomo.core import *
model = AbstractModel()
N = 10000
model.N = Param(initialize=N)
model.M = Param(initialize=3*N/4)

model.S = RangeSet(1,model.N)
model.SS = RangeSet(1,model.M)
model.x = Var(model.S, bounds=(0.1,10.0), initialize=0.5)

def f(model):
    return sum ([(model.x[i]+model.x[((2*i-1) % value(model.N))+1]+model.x[((3*i-1) % value(model.N))+1])**2*i/2.0 for i in model.S])
model.f = Objective(rule=f,sense=minimize)
def cons1(model, i):
    return model.x[i]+2*model.x[((4*i-1) % value(model.N))+1] + 3*model.x[((5*i-1)  % value(model.N))+1] - 6.0 == 0
model.cons1 = Constraint(model.SS, rule=cons1)
