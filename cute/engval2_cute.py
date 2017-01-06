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

#   Source: problem 15 in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-3-0

from pyomo.environ import *
model = AbstractModel()

model.x_init = Param(RangeSet(1,3))

def x_init_rule(model,i):
    return model.x_init[i]
model.x = Var(RangeSet(1,3),initialize= x_init_rule)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return (model.x[1]**2+model.x[2]**2+model.x[3]**2-1)**2\
    + (model.x[1]**2+model.x[2]**2+(model.x[3]-2)**2-1)**2\
    + (model.x[1]+model.x[2]+model.x[3]-1)**2\
    + (model.x[1]+model.x[2]-model.x[3]+1)**2\
    + (3*model.x[2]**2+model.x[1]**3+(5*model.x[3]-model.x[1]+1)**2-36)**2
model.f = Objective(rule=f_rule)
