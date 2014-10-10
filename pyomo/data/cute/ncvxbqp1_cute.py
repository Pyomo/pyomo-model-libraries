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

#   classification QBR2-AN-V-0
from pyomo.core import *
model = ConcreteModel()

model.N = Param(initialize=100)
model.M = Param(initialize=model.N/2.0)
model.Nplus = Param(initialize=model.N/4.0)

model.Rx = RangeSet(1,model.N)
model.x = Var(model.Rx,bounds=(0.1,10.0),initialize=0.5)

model.Rsum1 = RangeSet(1,model.Nplus)
model.Rsum2 = RangeSet(model.Nplus+1,model.N)
def f(model):
    return sum( 0.5*i*(model.x[i]+model.x[ ((2*i-1) % value(model.N)) + 1] + model.x[ ((3*i-1) % value(model.N)) +1 ] )**2 for i in model.Rsum1 ) -\
           sum( 0.5*i*(model.x[i]+model.x[ ((2*i-1) % value(model.N)) + 1] + model.x[ ((3*i-1) % value(model.N)) +1 ] )**2 for i in model.Rsum2 )
model.f = Objective(rule=f,sense=minimize)
