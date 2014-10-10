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
#   D. Shanno,
#   " On Variable Metric Methods for Sparse Hessians II: the New
#   Method",
#   MIS Tech report 27, University of Arizona (Tucson, UK), 1978.

#   See also Buckley #37 (p. 76) and Toint #15.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = AbstractModel()
model.N = Param(initialize=10)

model.S = RangeSet(1,model.N)
model.x = Var(model.S, initialize=-1.0)

model.SS = RangeSet(2,model.N)
def f(model):
    return sum( 100*(model.x[1]-model.x[i-1]**2)**2 for i in model.SS ) + (model.x[1]-1)**2
model.f = Objective(rule=f, sense=minimize)
