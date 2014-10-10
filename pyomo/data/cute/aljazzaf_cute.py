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
#   M. Aljazzaf,
#   "Multiplier methods with partial elimination of constraints for
#   nonlinear programming",
#   PhD Thesis, North Carolina State University, Raleigh, 1990.

#   SDIF input: Ph. Toint, May 1990.

#   classification QQR2-AN-3-1

from pyomo.core import *
model = AbstractModel()

model.N = Param(initialize=3)
model.N1 = Param(initialize=2)
model.Biga = Param(initialize=100.0)
def F_rule(model):
    return (value(model.Biga)**2-1.0)/(value(model.N)-1)
model.F = Param(initialize=F_rule)
def F2_rule(model):
    return (value(model.Biga)**2-1.0)/(value(model.Biga)*(value(model.N)-1))
model.F2 = Param(initialize=F2_rule)
model.S = RangeSet(1,model.N)
def A_rule(model, i):
    return value(model.Biga)-(i-1)*value(model.F2)
model.A = Param(model.S, initialize=A_rule)
def B_rule(model, i):
    return (i-1)*value(model.F)+1.0
model.B = Param(model.S, initialize=B_rule)

model.x = Var(model.S, bounds=(0,None), initialize=0.0)

model.SS1 = RangeSet(2,model.N1)
model.SS2 = RangeSet(model.N1+1,model.N)
def f(model):
    return model.A[1]*(model.x[1]-0.5)**2 +\
           sum(value(model.A[i])*(model.x[i]+1.0)**2 for i in model.SS1) +\
           sum(value(model.A[i])*(model.x[i]-1.0)**2 for i in model.SS2)
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return -model.B[1]*model.x[1]+model.B[1] +\
           sum(value(model.B[i])*(model.x[i]-0.0)**2 for i in model.SS1) +\
           sum(value(model.B[i])*(model.x[i]-1.0)**2 for i in model.SS2) == 0
model.cons1 = Constraint(rule=cons1)
