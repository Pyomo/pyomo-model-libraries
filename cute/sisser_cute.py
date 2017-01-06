
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

#   Source:
#   F.S. Sisser,
#   "Elimination of bounds in optimization problems by transforming
#   variables",
#   Mathematical Programming 20:110-121, 1981.

#   See also Buckley#216 (p. 91)

#   SIF input: Ph. Toint, Dec 1989.

#   classification OUR2-AN-2-0

from pyomo.environ import *
model = AbstractModel()

model.N = RangeSet(1,2)
model.xinit = Param(model.N)

def fa(model, i):
    return value(model.xinit[i])
model.x = Var(model.N,initialize=fa)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))


def f(model):
    return 3*model.x[1]**4 - 2*(model.x[1]*model.x[2])**2 + 3*model.x[2]**4
model.f = Objective(rule=f,sense=minimize)
