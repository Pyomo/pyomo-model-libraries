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

#   Source: problem 21 in
#   W. Hock and K. Schittkowski,
#   "Test examples for nonlinear programming codes",
#   Lectures Notes in Economics and Mathematical Systems 187, Springer
#   Verlag, Heidelberg, 1981.

#   SIF input: A.R. Conn, April 1990

#   classification SLR2-AN-7-1


from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,7)
model.x = Var(model.N)

for i in model.N:
    if i <= 2:
        model.x[i] = -1.0
    else:
        model.x[i] = 0.0

model.f = Objective(expr=-100+0.01*(model.x[1]**2+model.x[3]**2+model.x[5]**2+model.x[6]**2) + (model.x[2]**2+model.x[4]**2+model.x[7]**2))

model.cons1 = Constraint(expr=10.0*model.x[1]-model.x[2]-10>=0)
model.cons2 = Constraint(expr=2<=model.x[1]<=50)
model.cons3 = Constraint(expr=-50<=model.x[2]<=50)
model.cons4 = Constraint(expr=model.x[3]<=50)
model.cons5 = Constraint(expr=2<=model.x[4])
model.cons6 = Constraint(expr=model.x[6]<=0)
model.cons7 = Constraint(expr=0<=model.x[7])
