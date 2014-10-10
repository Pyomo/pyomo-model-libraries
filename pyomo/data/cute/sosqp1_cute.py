#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, Brandon C. Barrera and Saumyajyoti Chaudhuri
#Taken from:
#
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

#   classification QLR2-AN-V-V

from pyomo.core import *
model = AbstractModel()

model.N = Param(initialize=10)
model.R1 = RangeSet(1,model.N)

model.x = Var(model.R1,bounds=(-1,1))
model.y = Var(model.R1,bounds=(-1,1))

def f(model):
    return sum( model.x[i]*model.y[i] for i in model.R1 )
model.f = Objective(rule=f,sense=minimize)

def cons1(model, i):
    return ( 1, model.x[i]-model.y[i] )
model.cons1 = Constraint(model.R1,rule=cons1)

def cons2(model):
    return ( model.N, sum( model.x[i]+model.y[i] for i in model.R1 ) )
model.cons2 = Constraint(rule=cons2)
