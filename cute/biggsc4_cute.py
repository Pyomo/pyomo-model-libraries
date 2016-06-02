#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

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

#   classification QLR2-AN-4-7

from pyomo.core import *
model = ConcreteModel()

model.x = Var(RangeSet(1,4),bounds=(0,5),initialize=0)

def f_rule(model):
    return (-model.x[1]*model.x[3]-model.x[2]*model.x[4])
model.f = Objective(rule=f_rule)

def con1(model):
    return 0 <= model.x[1]+model.x[2] -2.5 <= 5.0

def con2(model):
    return 0 <= model.x[1]+model.x[3] -2.5 <= 5.0

def con3(model):
    return 0 <= model.x[1]+model.x[4] -2.5 <= 5.0

def con4(model):
    return 0 <= model.x[2]+model.x[3] -2.0 <= 5.0
    
def con5(model):
    return 0 <= model.x[2]+model.x[4] -2.0 <= 5.0
    
def con6(model):
    return 0 <= model.x[3]+model.x[4] -1.5 <= 5.0
    
def con7(model):
    return model.x[1]+model.x[2]+model.x[3]+model.x[4]-5.0 >= 0

model.cons1 = Constraint(rule=con1)
model.cons2 = Constraint(rule=con2)
model.cons3 = Constraint(rule=con3)
model.cons4 = Constraint(rule=con4)
model.cons5 = Constraint(rule=con5)
model.cons6 = Constraint(rule=con6)
model.cons7 = Constraint(rule=con7)
