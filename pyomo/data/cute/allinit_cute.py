#
#  Pyomo: Python Optimization Modeling Objects
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
#   N. Gould, private communication.

#   SIF input: Nick Gould, June 1990.

#   classification OBR2-AY-4-0

from pyomo.core import *
model = ConcreteModel()

model.x = Var(RangeSet(1,4))

model.f = Objective (expr=  model.x[3]-1 +  model.x[1]**2+model.x[2]**2 + (model.x[3]+model.x[4])**2 +  sin(model.x[3])**2 + model.x[1]**2*model.x[2]**2 + model.x[4]-3 +\
    sin(model.x[3])**2 +    (model.x[4]-1)**2 +(model.x[2]**2)**2+(model.x[3]**2 + (model.x[4]+model.x[1])**2)**2 +\
    (model.x[1]-4 + sin(model.x[4])**2 + model.x[2]**2*model.x[3]**2)**2 +sin(model.x[4])**4)


model.cons1 = Constraint(expr=model.x[2]>=1)

model.cons2 = Constraint(expr=-1e+10<=model.x[3]<=1.0)

model.cons3 = Constraint(expr=model.x[4]==2)



