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

#   Source:
#   L.C.W. Dixon and Z. Maany,
#   "A family of test problems with sparse Hessians for unconstrained
#   optimization",
#   TR 206, Numerical Optimization Centre, Hatfield Polytechnic, 1988.

#   See also Buckley#221 (p. 49)
#   SIF input: Ph. Toint, Dec 1989.
#              correction by Ph. Shott, January 1995.

#   classification OUR2-AN-V-0

from pyomo.environ import *
model = AbstractModel()

M =1000
N =3*M

alpha = 1.0
beta = 0.0625
gamma = 0.0625
delta = 0.0625

model.K = Param(RangeSet(1,4))
model.x = Var(RangeSet(1,N),initialize=2.0)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return 1.0 + sum(alpha*model.x[i]**2*(i/float(N))**model.K[1] for i in range(1,N+1))+\
    sum(beta*model.x[i]**2*(model.x[i+1]+model.x[i+1]**2)**2*(i/float(N))**model.K[2] for i in range(1,N))+\
    sum(gamma*model.x[i]**2*model.x[i+M]**4*(i/float(N))**model.K[3] for i in range(1,2*M+1)) +\
    sum(delta*model.x[i]*model.x[i+2*M]*(i/float(N))**model.K[4] for i in range(1,M+1))
model.f = Objective(rule=f_rule)
