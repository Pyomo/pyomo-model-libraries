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

#   Source:  problem 8 in
#   A.R.Conn,N.I.M.Gould and Ph.L.Toint,
#   "Testing a class of methods for solving minimization 
#   problems with simple bounds on their variables, 
#   Mathematics of Computation 50, pp 399-430, 1988.

#   SIF input: Nick Gould and Ph. Toint, Dec 1995.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()

ns = 499.0
n = 2*ns +2.0

model.N = RangeSet(1,n)


def x_init_rule(model,i):
    if i == 1:
        return  -3.0
    elif i == 2:
        return -1.0
    elif i == 3:
        return -3.0
    elif i == 4:
        return -1.0
    else: 
        return -2.0
model.x = Var(model.N,initialize=x_init_rule)

def f(model):
    return  1.0+sum(100*(model.x[2*i]-model.x[2*i-1]**2)**2 +\
    (1.0-model.x[2*i-1])**2 +90*(model.x[2*i+2]-model.x[2*i+1]**2)**2 +\
    (1.0-model.x[2*i+1])**2 +\
    10*(model.x[2*i]+model.x[2*i+2]-2.0)**2 +\
    (model.x[2*i]-model.x[2*i+2])**2/10 for i in range(1,int(ns)+1))
model.f = Objective(rule=f)
    
