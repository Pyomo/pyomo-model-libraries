#  This software is distributed under the BSD License.
#  under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil, Juan Lopez
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
#   Ph. Toint, private communication,

#   SIF input: Ph. Toint, Dec 1989.

#   classification OUR2-AY-2-0

from pyomo.core import *
model = ConcreteModel()


hlength=30
cslope=100

model.x1 = Var(initialize=-5)
model.x2 = Var(initialize=-7)


def f_rule(model):
    return sin(7*model.x1)**2*cos(7*model.x2)**2*hlength +\
    cslope*sqrt(0.01+(model.x1-model.x2)**2) + cslope*sqrt(0.01+model.x1**2)
model.f = Objective(rule=f_rule)
