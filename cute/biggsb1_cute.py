#  _________________________________________________________________________
#                                                                           
#  Pyomo: Python Optimization Modeling Objects                           
#  Copyright (c) 2010 Sandia Corporation.                                   
#  This software is distributed under the BSD License.                      
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,   
#  the U.S. Government retains certain rights in this software.             
#  For more information, see the Pyomo README.txt file.                     
#  _________________________________________________________________________

# Formulated in Pyomo by Juan Lopez
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
#   M. Batholomew-Biggs and F.G. Hernandez,
#   "Some improvements to the subroutine OPALQP for dealing with large
#    problems",
#   Numerical Optimization Centre, Hatfield, 1992.

#   SIF input: Ph Toint, April 1992.

#   classification QBR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()

model.N = 1000
model.x = Var(RangeSet(1,model.N))

def f_rule(model):
    return (model.x[1]-1)**2 + sum((model.x[i+1]-model.x[i])**2 for i in range(1,model.N)) + (1-model.x[model.N])**2
model.f = Objective(rule=f_rule)

def cons1(model,i):
    return 0.0<=model.x[i]<=0.9
model.cons1 = Constraint(RangeSet(1,model.N-1),rule=cons1)
