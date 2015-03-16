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
#   Ph.L. Toint,
#   "Some numerical results using a sparse matrix updating formula in
#   unconstrained optimization",
#   Mathematics of Computation, vol. 32(114), pp. 839-852, 1978.

#   See also Buckley#84
#   SIF input: Ph. Toint, Dec 1989.

#   classification OUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()

N = 1000

model.x = Var(RangeSet(1,N),initialize=1.0)

def f_rule(model):
    return (abs(-2*model.x[2]+1+(3-2*model.x[1])*model.x[1]))**(7/3.0) +\
    sum((abs(1-model.x[i-1]-2*model.x[i+1]+(3-2*model.x[i])*model.x[i]))**(7/3.0) for i in range(2,N))+\
    (abs(-model.x[N-1]+1 +(3-2*model.x[N])*model.x[N]))**(7/3.0) +\
    sum((abs(model.x[i]+model.x[i+N/2]))**(7/3.0) for i in range(1,int(N/2)+1))
model.f = Objective(rule=f_rule)



