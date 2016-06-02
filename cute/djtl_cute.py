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

#   Source: modified version of problem 19 in
#   W. Hock and K. Schittkowski,
#   "Test examples for nonlinear programming codes",
#   Lectures Notes in Economics and Mathematical Systems 187, Springer
#   Verlag, Heidelberg, 1981.
#   that is meant to simulate the Lagrangian barrier objective function
#   for particular values of the shifts and multipliers

#   SIF input: A.R. Conn August 1993

#   classification OUR2-AN-2-0
from __future__ import division
from pyomo.core import *
model = ConcreteModel()

model.x1 = Var(initialize=15.0)
model.x2 = Var(initialize=-1.0)

def f_rule(model):
    if (-(value(model.x1)-5)**2-(value(model.x2)-5)**2+200+1 <= 0.0):
        obj1=(1E10*(-(model.x1-5)**2-(model.x2-5)**2+200)**2) 
    else:
        obj1=(-log(-(model.x1-5)**2-(model.x2-5)**2+200+1))
    if ((value(model.x1)-5)**2+(value(model.x2)-5)**2-100+1 <= 0.0):
        obj2=(1E10*((model.x1-5)**2+(model.x2-5)**2-100)**2) 
    else:
        obj2=( -log((model.x1-5)**2+(model.x2-5)**2-100+1))
    if ((value(model.x2)-5)**2+(value(model.x1)-6)**2+1 <= 0.0):
        obj3=( 1E10*((model.x2-5)**2+(model.x1-6)**2)**2) 
    else:
        obj3=( -log((model.x2-5)**2+(model.x1-6)**2+1))
    if (-(value(model.x2)-5)**2-(value(model.x1)-6)**2+82.81+1 <= 0.0):
        obj4=( 1E10*(-(model.x2-5)**2-(model.x1-6)**2+82.81)**2)
    else:
        obj4=( -log(-(model.x2-5)**2-(model.x1-6)**2+82.81+1))
    if (100-value(model.x1)+1 <= 0.0):
        obj5=( 1E10*(100-model.x1)**2)
    else:
        obj5=( -log(100-model.x1+1))
    if (value(model.x1)-13+1 <= 0.0):
        obj6=( 1E10*(model.x1-13)**2)
    else:
        obj6=( -log(model.x1-13+1))
    if (100-value(model.x2)+1 <= 0.0):
        obj7=( 1E10*(100-model.x2)**2)
    else:
        obj7=( -log(100-model.x2+1))
    if (value(model.x2)+1<= 0.0):
        obj8=(1E10*(model.x2)**2)
    else:
        obj8=( -log(model.x2+1))
    return (model.x1-10)**3+(model.x2-20)**3+obj1+obj2+obj3+obj4+obj5+obj6+obj7+obj8
model.f = Objective(rule=f_rule)
