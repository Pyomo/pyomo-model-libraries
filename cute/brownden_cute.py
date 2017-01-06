#  _________________________________________________________________________                                                                                \
#                                                                                                                                                           \
#  Pyomo: Python Optimization Modeling Objects                                                                                                           \
#  Copyright (c) 2010 Sandia Corporation.                                                                                                                   \
#  This software is distributed under the BSD License.                                                                                                      \
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,                                                                                   \
#  the U.S. Government retains certain rights in this software.                                                                                             \
#  For more information, see the Pyomo README.txt file.                                                                                                     \
#  _________________________________________________________________________                                                                                \

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

#   Source: Problem 16 in
#   J.J. More', B.S. Garbow and K.E. Hillstrom,
#   "Testing Unconstrained Optimization Software",
#   ACM Transactions on Mathematical Software, vol. 7(1), pp. 17-41, 1981.

#   See also Buckley#30
#   SIF input: Ph. Toint, Dec 1989.

#   classification SUR2-AN-4-0


from pyomo.environ import *
model = AbstractModel()

model.M = Param(initialize=20)
model.N = Param(initialize=4)

model.S = RangeSet(1,4)
model.x_init = Param(model.S)
def xint(model, i):
    return model.x_init[i]
model.x = Var(model.S, initialize=xint)

model.St = RangeSet(1,model.M)

def Sti(model, i):
    return i/5.0
model.t = Param(model.St, initialize=Sti)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    expa = sum ([( (model.x[1]+model.t[i]*model.x[2]-exp(value(model.t[i])))**2 \
    + (model.x[3]+model.x[4]*sin(value(model.t[i]))-cos(value(model.t[i])))**2 )**2 for i in model.St])
    return expa
model.f = Objective(rule=f,sense=minimize)
