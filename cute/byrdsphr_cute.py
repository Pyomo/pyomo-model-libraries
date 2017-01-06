#  _________________________________________________________________________
#                                                                           
#  Pyomo: Python Optimization Modeling Objects                           
#  Copyright (c) 2010 Sandia Corporation.                                   
#  This software is distributed under the BSD License.                      
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,   
#  the U.S. Government retains certain rights in this software.             
#  For more information, see the Pyomo README.txt file.                     
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, and Brandon C. Barrera
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
#   R. Byrd,
#   Private communication, Chicago, 1992.

#   SIF input: Ph. Toint, November 1992.

#   classification LQR2-AN-3-2

from pyomo.environ import *
model = AbstractModel()

model.S = RangeSet(1,3)
model.xinit = Param(model.S)
def xin(model, i):
    return value(model.xinit[i])
model.x = Var(model.S, initialize=xin)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    return -model.x[1]-model.x[2]-model.x[3]
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return -9.0+model.x[1]**2+model.x[2]**2+model.x[3]**2 == 0
model.cons1 = Constraint(rule=cons1)

def cons2(model):
    return -9.0+(model.x[1]-1.0)**2+model.x[2]**2+model.x[3]**2 == 0
model.cons2 = Constraint(rule=cons2)
