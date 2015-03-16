#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Juan Lopez and Gabe Hackebeil
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
#   M.C. Pinar and S.A. Zenios,
#   "Approximately Exact Smoothing Functions for Exact Penalty Methods",
#   Institute for Numerical Analysis, TUD, Lyngby, Denmark.

#   SIF input: Ph. Toint, August 1993.

#   classification LQR2-AN-3-5

from pyomo.core import *
model = ConcreteModel()

model.x = Var(RangeSet(1,2),initialize=2.0)
model.z = Var(initialize=2.0)

def f(model):
    return model.z
model.f = Objective(rule=f)

def con1(model):
    return model.z+5*model.x[1]-model.x[2] >= 0
model.cons1 = Constraint(rule=con1)

def con2(model):
    return model.z-4*model.x[2]-model.x[1]**2-model.x[2]**2 >= 0
model.cons2 = Constraint(rule=con2)

def con3(model):
    return model.z-5*model.x[1]-model.x[2] >= 0
model.cons3 = Constraint(rule=con3)

def con4(model):
    return model.x[1]+model.x[2]+10.0 <= 0
model.cons4 = Constraint(rule=con4)

def con5(model):
    return 2*model.x[1]**2-model.x[2]**2+4.0 <= 0
model.cons5 = Constraint(rule=con5)
