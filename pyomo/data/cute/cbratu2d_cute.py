#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil
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

#   Source: problem 3 in
#   J.J. More',
#   "A collection of nonlinear model problems"
#   Proceedings of the AMS-SIAM Summer seminar on the Computational
#   Solution of Nonlinear Systems of Equations, Colorado, 1988.
#   Argonne National Laboratory MCS-P60-0289, 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification NOR2-MN-V-V

from pyomo.core import*
model = ConcreteModel()

p = 23
l = 5.0
h = 1.0/(p-1.0)
c = h**2/l

model.u = Var(RangeSet(1,p),RangeSet(1,p),initialize=0.0)
model.x = Var(RangeSet(1,p),RangeSet(1,p),initialize=0.0)

model.f = Objective(expr=0.0)

def con1(model,i,j):
    return (4*model.u[i,j]-model.u[i+1,j]-model.u[i-1,j]-model.u[i,j+1]-\
    model.u[i,j-1]-c*exp(model.u[i,j])*cos(model.x[i,j])) == 0
model.cons1 = Constraint(RangeSet(2,p-1),RangeSet(2,p-1),rule=con1)

def con2(model,i,j):
    return (4*model.x[i,j]-model.x[i+1,j]-model.x[i-1,j]-model.x[i,j+1]-\
    model.x[i,j-1]-c*exp(model.u[i,j])*sin(model.x[i,j])) == 0
model.cons2 = Constraint(RangeSet(2,p-1),RangeSet(2,p-1),rule=con2)

for j in range(1,p+1):
    model.u[1,j].fix(0.0)
    model.u[p,j].fix(0.0)
    model.x[1,j].fix(0.0)
    model.x[p,j].fix(0.0)

for i in range(2,p):
    model.u[i,p].fix(0.0)
    model.u[i,1].fix(0.0)
    model.x[i,p].fix(0.0)
    model.x[i,1].fix(0.0)
