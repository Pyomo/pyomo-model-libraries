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

#   Source: K. Oettershagen
#   "Ein superlinear konvergenter algorithmus zur losung
#    semi-infiniter optimierungsproblem",
#    Ph.D thesis, Bonn University, 1982

#   SIF input: Nick Gould, February, 1994.

#   classification LLR2-AN-3-V
from pyomo.core import *

model = ConcreteModel()

model.M = Param(initialize=500)
model.lower = Param(initialize=0.0)
model.upper = Param(initialize=2.0)
model.diff = Param(initialize=model.upper-model.lower)
model.h = Param(initialize=(model.diff/model.M))

model.u = Var()
model.S = RangeSet(1,2)
model.x = Var(model.S)

def f(model):
    return model.u
model.f = Objective(rule=f, sense=minimize)

model.OP = RangeSet(0,model.M)
def cons1(model, i):
    return model.u-(i*model.h+model.lower)*model.x[1]-exp(i*model.h+model.lower)*model.x[2] - (i*model.h+model.lower)**2 >= 0
model.cons1 = Constraint(model.OP,rule=cons1)

def cons2(model, i):
    return model.u+(i*model.h+model.lower)*model.x[1]+exp(i*model.h+model.lower)*model.x[2] + (i*model.h+model.lower)**2 >= 0
model.cons2 = Constraint(model.OP,rule=cons2)
