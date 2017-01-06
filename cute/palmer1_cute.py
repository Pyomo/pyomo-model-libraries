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
#   M. Palmer, Edinburgh, private communication.

#   SIF input: Nick Gould, 1990.

#   classification SBR2-RN-4-0

from pyomo.environ import *
model = AbstractModel()

model.M = RangeSet(1,31)

model.X = Param(model.M)
model.Y = Param(model.M)

model.A = Var(initialize=1.0)
model.B = Var(bounds=(.00001,None),initialize=1.0)
model.C = Var(bounds=(.00001,None),initialize=1.0)
model.D = Var(bounds=(.00001,None),initialize=1.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def palmer(model):
    return sum( (model.Y[m] - (model.A*(model.X[m]**2) + model.B / (model.C \
    + (model.X[m]**2)/model.D)))**2 for m in model.M )
model.palmer = Objective(rule=palmer,sense=minimize)
