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

#   classification  QOR2-AY-6-2
from pyomo.core import *
model = AbstractModel()

model.x11 = Var(bounds=(0,None),initialize=1)
model.x12 = Var(initialize=1)
model.x22 = Var(bounds=(0,None),initialize=1)
model.y11 = Var(bounds=(None,0),initialize=1)
model.y12 = Var(initialize=1)
model.y22 = Var(bounds=(None,0),initialize=1)

def f(model):
    return ((model.x11-model.y11)**2 + 2*(model.x12-model.y12)**2 + (model.x22-model.y22)**2)
model.f = Objective(rule=f, sense=minimize)

def cons1(model):
    return (0, (model.x11*model.x22 - model.x12**2), None)
model.cons1 = Constraint(rule=cons1)
def cons2(model):
    return (None, (model.y11*model.y22 - model.y12**2), 0)
model.cons2 = Constraint(rule=cons2)
