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
#   M.M. Makela,
#   "Nonsmooth optimization",
#   Ph.D. thesis, Jyvaskyla University, 1990

#   SIF input: Ph. Toint, Nov 1993.

#   classification  LLR2-AN-21-40

from pyomo.core import *
model = AbstractModel()

model.N = RangeSet(1,20)
def xrule(model, i):
    if i <= 10:
        return i
    else:
        return -i
model.x = Var(model.N,initialize=xrule)
model.u = Var()

def f(model):
    return model.u
model.f = Objective(rule=f,sense=minimize)

def cons1(model, i):
    return -model.u + model.x[i] <=0
model.cons1 = Constraint(model.N,rule=cons1)

def cons2(model, i):
    return -model.u - model.x[i] <=0
model.cons2 = Constraint(model.N,rule=cons2)
