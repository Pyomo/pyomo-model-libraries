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

model.n = Param(initialize=1000)
model.b = Param(initialize=5)

model.Sn = RangeSet(1,model.n)
model.Sb = RangeSet(1,model.b)

model.x = Var(model.Sn, bounds=(-1,1), initialize=0.99)
model.y = Var(model.Sn, bounds=(-1,1), initialize=-0.99)
model.z = Var(model.Sb, bounds=(0,2), initialize=0.5)

def f(model):
    sum_expr_1 = 0
    sum_expr_2 = 0
    for i in model.Sn:
        sum_expr_1 += model.x[i]*model.y[i]
    for j in model.Sb:
        sum_expr_2 += 0.5*model.z[j]**2
    exp = sum_expr_1 + sum_expr_2
    return exp
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    sum_cexpr_1 = 0
    sum_cexpr_2 = 0
    for i in model.Sn:
        sum_cexpr_1 += model.x[i] + model.y[i]
    for j in model.Sb:
        sum_cexpr_2 += model.z[j]
    cexp = sum_cexpr_1 + sum_cexpr_2
    return (value(model.b)+ 1, cexp, None)
model.cons1 = Constraint(rule=cons1)

def cons2(model, i):
    csum = 0
    for j in model.Sb:
        csum += model.z[j]
    return model.x[i] - model.y[i] + csum == value(model.b)
model.cons2 = Constraint(model.Sn, rule=cons2)
