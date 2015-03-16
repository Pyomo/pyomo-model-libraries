#
#  Pyomo Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil, Juan Lopez
# Taken from

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

#   Source a multi-dimensional extension of problem 28 in
#   W. Hock and K. Schittkowski,
#   "Test examples for nonlinear programming codes",
#   Lectures Notes in Economics and Mathematical Systems 187, Springer
#   Verlag, Heidelberg, 1981.

#   SIF input Nick Gould, December 1991
#              minor correction by Ph. Shott, Jan 1995.

#   classification QLR2-AY-10-8

from pyomo.core import *
model = ConcreteModel()

N=10

def x_init_rule(model,i):
    if i==1:
        return -4.0
    else:
        return 1.0
model.x = Var(RangeSet(1,N),initialize=x_init_rule)

def f_rule(model):
    return sum ((model.x[i]+model.x[i+1])**2 for i in range(1,N))
model.f = Objective(rule=f_rule)
    
def cons_rule(model,i):
    return -1.0+model.x[i]+2*model.x[i+1]+3*model.x[i+2] == 0
model.cons = Constraint(RangeSet(1,N-2),rule=cons_rule)
