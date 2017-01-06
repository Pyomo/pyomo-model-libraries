#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

# Formulated in Pyomo by Juan Lopez
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

#   See also Buckley#46 (n = 25) (p. 45).
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-V-0

from pyomo.environ import *
model = AbstractModel()

n = 50
model.alph = Param(RangeSet(1,n))

model.x = Var(RangeSet(1,n),initialize=-1.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    return sum((model.x[i-1]-model.x[i]**2)**2*16*model.alph[i]**2 +(model.x[i]-1.0)**2 for i in range(2,n+1))
model.f = Objective(rule=f)
