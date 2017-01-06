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

#   Source: problem 1 in
#   P.T. Boggs and J.W. Tolle,
#   "A strategy for global convergence in a sequential 
#    quadratic programming algorithm",
#   SINUM 26(3), pp. 600-623, 1989.
 
#   SIF input: Ph. Toint, June 1993.

#   classification QQR2-AN-2-1

from pyomo.environ import *
model = AbstractModel()

model.xinit = Param(RangeSet(1,2))
model.x = Var(RangeSet(1,2))

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))
    
def f_rule(model):
    return 100*model.x[1]**2+100*model.x[2]**2-model.x[1]-100
model.f = Objective(rule=f_rule)

def con1(model):
    return model.x[1]**2+model.x[2]**2-1.0 == 0
model.cons1 = Constraint(rule=con1)
