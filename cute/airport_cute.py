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
#   Contribution from a LANCELOT user.

#   SIF input : Rodrigo de Barros Nabholz & Maria Aparecida Diniz Ehrhardt
#               November 1994, DMA - IMECC- UNICAMP
#   Adaptation for CUTE: Ph. Toint, November 1994.

#   classification SQR2-MN-84-42

from pyomo.environ import *
model=AbstractModel()

model.N = 42
model.x = Var(RangeSet(1,42),bounds=(-10,10))
model.y = Var(RangeSet(1,42),bounds=(-10,10))
model.r = Param(RangeSet(1,model.N))
model.cx = Param(RangeSet(1,model.N))
model.cy = Param(RangeSet(1,model.N))

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_obj_rule(model):
    return sum((model.x[i]-model.x[j])**2+(model.y[i]-model.y[j])**2 for i in range(1,model.N) for j in range(i+1,model.N+1))
model.f = Objective(rule=f_obj_rule)

def cons1_rule(model,i):
    return (model.x[i]-model.cx[i])**2 + (model.y[i]-model.cy[i])**2 - model.r[i] <= 0
model.cons1 = Constraint(RangeSet(1,42),rule=cons1_rule)
