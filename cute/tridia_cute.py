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

#   Source: problem 8 in
#   Ph.L. Toint,
#   "Test problems for partially separable optimization and results
#   for the routine PSPMIN",
#   Report 83/4, Department of Mathematics, FUNDP (Namur, B), 1983.

#   See also Buckley#40 (p.96)

#   SIF input: Ph. Toint, Dec 1989.

#   classification QUR2-AN-V-0
from pyomo.environ import *
model = AbstractModel()

model.N = Param()
model.alpha = Param()
model.beta = Param()
model.gamma = Param()
model.delta = Param()

model.R1 = RangeSet(1,model.N)
model.x = Var(model.R1,initialize=1.0)

model.R2 = RangeSet(2,model.N)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))


def f(model):
    return model.gamma*(model.x[1]*model.delta-1.0)**2 + sum( i*(-model.beta*model.x[i-1]+model.alpha*model.x[i])**2 for i in model.R2 )
model.f = Objective(rule=f,sense=minimize)
