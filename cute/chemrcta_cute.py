#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

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

#   Source: Problem 8, eqs (8.6)--(8.9) in
#   J.J. More',
#   "A collection of nonlinear model problems"
#   Proceedings of the AMS-SIAM Summer seminar on the Computational
#   Solution of Nonlinear Systems of Equations, Colorado, 1988.
#   Argonne National Laboratory MCS-P60-0289, 1989.

#   SIF input: Ph. Toint, Dec 1989.
#              minor correction by Ph. Shott, Jan 1995 and F Ruediger, Mar 1997.

#   classification NOR2-MN-V-V

from pyomo.core import *
model = ConcreteModel()

n = 2500.0
pem = 1.0
peh = 5.0
d = 0.135
b = 0.5
beta = 2.0
gamma = 25.0
h = 1/(n-1)
cu1 = -h*pem
cui1 = 1/(h**2*pem)+1/h
cui = -1/h-2/(h**2*pem)
ct1 = -h*peh
cti1 = 1/(h**2*peh)+1/h
cti = -beta-1/h-2/(h**2*peh)

model.t = Var(RangeSet(1,n),initialize=1.0,bounds=(0.0000001,None))
model.u = Var(RangeSet(1,n),initialize=1.0,bounds=(0.0,None))

def f(model):
    return 0
model.f = Objective(rule=f)

def con1(model):
    return (cu1*model.u[2]-model.u[1]+h*pem) == 0
model.cons1 = Constraint(rule=con1)

def con2(model):
    return (ct1*model.t[2]-model.t[1]+h*peh) == 0
model.cons2 = Constraint(rule=con2)

def con3(model,i):
    return (-d*model.u[i]*exp(gamma-gamma/model.t[i])+(cui1)*model.u[i-1] + cui*model.u[i] + model.u[i+1]/(h**2*pem)) == 0
model.cons3 = Constraint(RangeSet(2,n-1),rule=con3)

def con4(model,i):
    return (b*d*model.u[i]*exp(gamma-gamma/model.t[i])+(cti1)*model.t[i-1] + cti*model.t[i] +\
    model.t[i+1]/(h**2*peh)) == 0
model.cons4 = Constraint(RangeSet(2,n-1),rule=con4)

def con5(model):
    return (model.u[n]-model.u[n-1]) == 0
model.cons5 = Constraint(rule=con5)

def con6(model):
    return (model.t[n]-model.t[n-1]) == 0
model.cons6 = Constraint(rule=con6)

