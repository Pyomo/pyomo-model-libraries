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
#
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
#   P. Wolfe,
#   "Explicit solution of an optimization problem",
#   Mathematical Programming 2, 258-260, 1972.

#   SIF input: Nick Gould, Oct 1992.

#   See also Schittkowski #368 (for N = 8)

#   classification OBR2-MN-V-0

from pyomo.core import *
model = AbstractModel()

model.n = Param(initialize=10)
model.Rx = RangeSet(1,model.n)
model.x = Var(model.Rx, bounds=(0.0,1.0))

def f(model):
    return sum( -model.x[i]**2*model.x[j]**4 for i in model.Rx for j in model.Rx ) +\
           sum( model.x[i]**3*model.x[j]**3 for i in model.Rx for j in model.Rx )
model.f = Objective(rule=f,sense=minimize)
