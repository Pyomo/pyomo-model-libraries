
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

#   Source: an exercize for L. Watson course on LANCELOT in the Spring 1993.
#   B.Benhabib, R.G.Fenton and A.A.Goldberg,
#   "Analytical trajectory optimization of seven degrees of freedom redundant
#   robot",
#   Transactions of the Canadian Society for Mechanical Engineering,
#   vol.11(4), 1987, pp 197-200.

#   SIF input: Manish Sabu at Virginia Tech., Spring 1993.
#              Minor modifications by Ph. L. Toint, April 1993.

#   classification QOR2-MY-14-2
from pyomo.core import *
model = AbstractModel()

model.XPOS = Param(initialize=4);
model.YPOS = Param(initialize=4);
model.HIGH = Param(initialize=2.356194);
model.DOWN = Param(initialize=-2.356194);
model.R1 = RangeSet(1,7)
model.R2 = RangeSet(1,6)
model.THIN = Param(model.R1,initialize=0.0)


model.TH = Var(model.R1)
model.THI = Var(model.R1)

def f(model):
    return sum( (model.TH[i]-model.THI[i])**2 for i in model.R1 )
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return ( 0, sum( cos(model.TH[i]) for i in model.R2 ) + 0.5*cos(model.TH[7]) - model.XPOS )
model.cons1 = Constraint(rule=cons1)

def cons2(model):
    return ( 0, sum([sin(model.TH[i]) for i in model.R2]) + 0.5*sin(model.TH[7]) - model.YPOS )
model.cons2 = Constraint(rule=cons2)
def cons3(model, i):
    return model.THI[i] == model.THIN[i]
model.cons3 = Constraint(model.R1,rule=cons3)

