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

#   classification  LQR2-AN-3-2

from pyomo.core import *
model = AbstractModel()
model.N = RangeSet(1,2)
model.x = Var(model.N,initialize=-1.0)
model.u = Var()

def f(model):
    return model.u
model.f = Objective(rule=f, sense=minimize)

def cons1(model):
    return (None,(-model.u - model.x[1] - 3.75 + 3.75*(model.x[1]**2 + model.x[2]**2)),0)
model.cons1 = Constraint(rule=cons1)
def cons2(model):
    return (None,(-model.u - model.x[1] - 0.25 + 0.25*(model.x[1]**2 + model.x[2]**2)),0)
model.cons2 = Constraint(rule=cons2)
