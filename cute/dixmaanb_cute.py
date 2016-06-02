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
#   L.C.W. Dixon and Z. Maany,
#   "A family of test problems with sparse Hessians for unconstrained
#   optimization",
#   TR 206, Numerical Optimization Centre, Hatfield Polytechnic, 1988.

#   See also Buckley#221 (p. 49)
#   SIF input: Ph. Toint, Dec 1989.
#              correction by Ph. Shott, January 1995.

#   classification OUR2-AN-V-0

from pyomo.core import *
model = AbstractModel()
M = 1000
model.M = Param(initialize=M)
model.N = Param(initialize=3*M)

model.alpha = Param(initialize=1.0)
model.beta = Param(initialize=0.0625)
model.gamma = Param(initialize=0.0625)
model.delta = Param(initialize=0.0625)

model.S1 = RangeSet(1,4)
model.S2 = RangeSet(1,model.N)
model.K = Param(model.S1, initialize=0)
model.x = Var(model.S2, initialize=2.0)

model.S3 = RangeSet(1,model.N-1)
model.S4 = RangeSet(1,2*model.M)
model.S5 = RangeSet(1,model.M)

def f(model):
    exp1 = sum ([value(model.alpha)*model.x[i]**2*(i/value(model.N))**value(model.K[1]) for i in model.S2])
    exp2 = sum ([value(model.beta)*model.x[i]**2*(model.x[i+1]+model.x[i+1]**2)**2*(i/value(model.N))**value(model.K[2]) for i in model.S3])
    exp3 = sum ([value(model.gamma)*model.x[i]**2*model.x[i+value(model.M)]**4*(i/value(model.N))**value(model.K[3]) for i in model.S4])
    exp4 = sum ([value(model.delta)*model.x[i]*model.x[i+2*value(model.M)]*(i/value(model.N))**value(model.K[4]) for i in model.S5])
    return 1.0 + exp1 + exp2 + exp3 + exp4
model.f = Objective(rule=f,sense=minimize)
