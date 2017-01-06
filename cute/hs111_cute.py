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
#  Formulated in pyomo by Logan Barnes. Taken from:

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

#   Source: problem 111 in
#   W. Hock and K. Schittkowski,
#   "Test examples for nonlinear programming codes",
#   Lectures Notes in Economics and Mathematical Systems 187, Springer
#   Verlag, Heidelberg, 1981.
#   This problem has been modified on 20 Oct 92 by Todd Plantenga as follows.
#   The bound constraints, which are inactive at the solution,
#   are removed.

#   SIF input: Nick Gould, August 1991 and T. Plantenga, October 1992.

#   classification OOR2-AN-10-3

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,10)
model.x = Var(model.N,bounds=(-100,100),initialize=-2.3)
model.c = Param(model.N)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return sum(exp(model.x[j])*(model.c[j] + model.x[j] - log(sum(exp(model.x[k]) for k in model.N))) for j in model.N)
model.obj = Objective(rule=obj_rule,sense=minimize)

def cons1_rule(model):
    return exp(model.x[1]) + 2*exp(model.x[2]) + 2*exp(model.x[3]) + exp(model.x[6]) + exp(model.x[10]) == 2.0
model.cons1 = Constraint(rule=cons1_rule)
def cons2_rule(model):
    return exp(model.x[4]) + 2*exp(model.x[5]) + exp(model.x[6]) + exp(model.x[7]) == 1
model.cons2 = Constraint(rule=cons2_rule)
def cons3_rule(model):
    return exp(model.x[3]) + exp(model.x[7]) + exp(model.x[8]) + 2*exp(model.x[9]) + exp(model.x[10]) == 1
model.cons3 = Constraint(rule=cons3_rule)
