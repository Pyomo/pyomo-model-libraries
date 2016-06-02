#
#  Pyomo Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
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

#   Source problem 5 in
#   S. Nash,
#   "Newton-type minimization via the Lanczos process",
#   SIAM J. Num. Anal. 21, 1984, 770-788.

#   SIF input Nick Gould, Oct 1992.
#              minor correction by Ph. Shott, Jan 1995.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()

n = 500

model.x = Var(RangeSet(1,n),initialize=1.0/(n+1.0))

def f_rule(model):
    return 1.0 + sum(100*(model.x[i]-model.x[i-1]**2)**2 for i in range(2,n+1))+\
    sum((model.x[i]-1.0)**2 for i in range(2,n+1))
model.f = Objective(rule=f_rule)
    
    
    
    
