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
#   M.M. Makela,
#   "Nonsmooth optimization",
#   Ph.D. thesis, Jyvaskyla University, 1990

#   SIF input: Ph. Toint, Nov 1993.

#   classification  LLR2-AN-51-50

from pyomo.core import *
model = ConcreteModel()

ri = 50
t = -25.5 + (50)

def x_init_rule(model,j):
    return -25.5+j
model.x = Var(RangeSet(1,ri),initialize=x_init_rule)

model.u = Var() 

model.obj = Objective(expr=model.u)

def f_rule(model,i):
    return model.u >= 50*model.x[i] - summation(model.x)
model.f = Constraint(RangeSet(1,ri),rule=f_rule)
