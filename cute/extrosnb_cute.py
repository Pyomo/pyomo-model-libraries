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

#   Source: problem 10 in
#   Ph.L. Toint,
#   "Test problems for partially separable optimization and results
#   for the routine PSPMIN",
#   Report 83/4, Department of Mathematics, FUNDP (Namur, B), 1983.

#   See also Buckley#116.  Note that MGH#21 is the separable version.
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = AbstractModel()

model.N = Param(initialize=10)
model.S = RangeSet(1,model.N)
model.x = Var(model.S,initialize=1)

model.Sf = RangeSet(2,model.N)
def f(model):
    sumexp = sum ([100*(model.x[i]-model.x[i-1]**2)**2 for i in model.Sf])
    return (model.x[1]-1)**2 + sumexp
model.f = Objective(rule=f,sense=minimize)
