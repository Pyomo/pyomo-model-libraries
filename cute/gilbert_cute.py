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

#   Source: 
#   J.Ch. Gilbert,
#   "On the Realization of the Wolfe Conditions in Reduced Quasi-Newton
#   Methods for Equality Constrained Optimization",
#   RR-2127, INRIA (F), 1993.

#   SIF input: Ph. Toint, April 1994

#   classification QQR2-AN-V-1

from pyomo.core import *
model = ConcreteModel()

n = 1000

def x_init_rule(model,i):
    return (-1.0)**(i+1)*10.0
model.x = Var(RangeSet(1,n),initialize=x_init_rule)

def f_rule(model):
    return sum(((n+1-i)*model.x[i]/n-1.0)**2 for i in range(1,n+1))/2.0
model.f = Objective(rule=f_rule)

def cons1_rule(model):
    return (sum(model.x[i]**2 for i in range(1,n+1)) - 1.0 )/2.0 == 0.0
model.cons1 = Constraint(rule=cons1_rule)
    
    
    
