#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, Brandon C. Barrera and Saumyajyoti Chaudhuri
#Taken from:

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
#   Y. Tanaka, M. Fukushima, T. Ibaraki,
#   "A comparative study of several semi-infinite nonlinear programming
#   algorithms",
#   EJOR, vol. 36, pp. 92-100, 1988.

#   SIF input: Ph. Toint, April 1992.

#   classification LLR2-AN-3-V
from pyomo.core import *
model = AbstractModel()

model.M = Param(initialize=10000)
def h_rule(model):
    return 1.0/value(model.M)
model.h = Param(initialize=h_rule)

model.R1 = RangeSet(1,3)
model.x = Var(model.R1)

def f(model):
    return model.x[1]+0.5*model.x[2]+model.x[3]/3.0;
model.f = Objective(rule=f, sense=minimize)

model.Rc1 = RangeSet(0,model.M)
def cons1(model, i):
    return -model.x[1]-i*value(model.h)*model.x[2]-(i*value(model.h))**2*model.x[3]+tan(i*value(model.h)) <= 0
model.cons1 = Constraint(model.Rc1,rule=cons1)
