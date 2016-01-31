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
#   A.R. Conn, N. Gould and Ph.L. Toint,
#   "The LANCELOT User's Manual",
#   Dept of Maths, FUNDP, 1991.

#   SIF input: Ph. Toint, Jan 1991.

#   classification QLR2-AN-2-1

from pyomo.core import *
model = AbstractModel()

model.x = Var(bounds=(0.0,None))
model.y = Var(bounds=(0.0,None))

def f(model):
    return (model.x-model.y)**2
model.f = Objective(rule=f, sense=minimize)

def cons1(model):
    return (0, model.x+model.y-1)
model.cons1 = Constraint(rule=cons1)
