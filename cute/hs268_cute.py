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
#  Formulated in pyomo by Logan Barnes. 
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
#   K. Schittkowski
#   "More Test Examples for Nonlinear Programming Codes"
#   Springer Verlag, Berlin, Lecture notes in economics and 
#   mathematical systems, volume 282, 1987

#   SIF input: Michel Bierlaire and Annick Sartenaer, October 1992.
#              minor correction by Ph. Shott, Jan 1995.

#   classification QLR2-AN-5-5

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,5)
model.D = Param(model.N,model.N)
model.B = Param(model.N)
model.x = Var(model.N,initialize=1.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return 14463.0 + sum(model.D[i,j]*model.x[i]*model.x[j] for i in model.N for j in model.N) + -2*sum(model.B[i]*model.x[i] for i in model.N)
model.f = Objective(rule=f_rule,sense=minimize)

def cons1_rule(model):
    return -sum(model.x[i] for i in model.N) + 5 >= 0
model.cons1 = Constraint(rule=cons1_rule)
def cons2_rule(model):
    return 10*model.x[1]+10*model.x[2]-3*model.x[3]+5*model.x[4]+4*model.x[5]-20>=0
model.cons2 = Constraint(rule=cons2_rule)
def cons3_rule(model):
    return -8*model.x[1]+model.x[2]-2*model.x[3]-5*model.x[4]+3*model.x[5]+40>=0
model.cons3 = Constraint(rule=cons3_rule)
def cons4_rule(model):
    return 8*model.x[1]-model.x[2]+2*model.x[3]+5*model.x[4]-3*model.x[5]-11>=0
model.cons4 = Constraint(rule=cons4_rule)
def cons5_rule(model):
    return -4*model.x[1]-2*model.x[2]+3*model.x[3]-5*model.x[4]+model.x[5]+30>=0
model.cons5 = Constraint(rule=cons5_rule)
