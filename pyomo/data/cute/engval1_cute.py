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

#   Source: problem 31 in
#   Ph.L. Toint,
#   "Test problems for partially separable optimization and results
#   for the routine PSPMIN",
#   Report 83/4, Department of Mathematics, FUNDP (Namur, B), 1983.

#   See also Buckley#172 (p. 52)
#   SIF input: Ph. Toint and N. Gould, Dec 1989.

#   classification OUR2-AN-V-0

from pyomo.core import *
model = AbstractModel()

model.N = Param(initialize=5000)
model.S1 = RangeSet(1,model.N)
model.S2 = RangeSet(1,model.N-1)
model.x = Var(model.S1, initialize=2.0)

def f(model):
    sumexp1 = 0
    sumexp2 = 0
    for i in model.S2:
        sumexp1 += -4*model.x[i]+3.0
        sumexp2 += (model.x[i]**2+model.x[i+1]**2)**2
    return sumexp1 + sumexp2
model.f = Objective(rule=f,sense=minimize)
