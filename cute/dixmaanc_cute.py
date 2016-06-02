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

#   classification LQI2-RN-157-134

from pyomo.core import *
model = ConcreteModel()

M =1000
N =3*M

alpha = 1.0
beta = 0.125
gamma = 0.125
delta = 0.125

model.K = Param(RangeSet(1,4),initialize=0)
model.x = Var(RangeSet(1,N),initialize=2.0)

def f_rule(model):
    return 1.0 + sum(alpha*model.x[i]**2*(i/N)**model.K[1] for i in range(1,N+1))+\
    sum(beta*model.x[i]**2*(model.x[i+1]+model.x[i+1]**2)**2*(i/N)**model.K[2] for i in range(1,N))+\
    sum(gamma*model.x[i]**2*model.x[i+M]**4*(i/N)**model.K[3] for i in range(1,2*M+1)) +\
    sum(delta*model.x[i]*model.x[i+2*M]*(i/N)**model.K[4] for i in range(1,M+1))
model.f = Objective(rule=f_rule)
