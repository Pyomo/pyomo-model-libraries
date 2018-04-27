#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Formulated in pyomo by Logan Barnes and Gabe Hackebeil.
#
#  Taken from:

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
#   A.R. Conn, N. Gould and Ph.L. Toint,
#   "The LANCELOT User's Manual",
#   Dept of Maths, FUNDP, 1991.

#   SIF input: Ph. Toint, Jan 1991.

#   classification OLR2-AN-2-1

from pyomo.environ import *
from pyomo.core.expr.current import Expr_if

model = AbstractModel()
model.N = RangeSet(1,5)
model.x = Param(model.N)
model.y = Param(model.N)
c = 0.85
model.a = Var(bounds=(0,None))
model.b = Var()

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return sum(0.5*Expr_if(IF=abs(model.a*model.x[i]+model.b-model.y[i])>15,
                               THEN=1.5*abs(model.a*model.x[i]+model.b-model.y[i])-0.5*1.5**2,
                               ELSE=0.5*abs(model.a*model.x[i]+model.b-model.y[i])**2) \
                   for i in range(1,6))
model.f = Objective(rule=f_rule,sense=minimize)

def cons1_rule(model):
    return model.a+model.b-c <= 0.0
model.cons1 = Constraint(rule=cons1_rule)
