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

#   Source: problem 9 in
#   J.J. More',"A collection of nonlinear model problems"
#   Proceedings of the AMS-SIAM Summer Seminar on the Computational
#   Solution of Nonlinear Systems of Equations, Colorado, 1988.
#   Argonne National Laboratory MCS-P60-0289, 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification SXR2-RN-8-0

from pyomo.environ import *
model = AbstractModel()

X_init = {}
X_init[1] = 0
X_init[2] = 0
X_init[3] = 0
X_init[4] = 0
X_init[5] = 0
X_init[6] = -0.05
X_init[7] = 0.1
X_init[8] = 0.0

n = 8
m = 5

model.N = RangeSet(1,n)
model.M = RangeSet(1,m)

model.A = Param(model.M,model.N)

def X_init_rule(model,i):
    return X_init[i]
model.X = Var(model.N,initialize=X_init_rule)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))


def _AX(model,i):
    return sum(model.A[i,j]*model.X[j] for j in model.N)
model.AX = Expression(model.M, rule=_AX)
model.P1 = Expression(initialize=(-0.727*model.X[2]*model.X[3])+(8.39*model.X[3]*model.X[4])-(684.4*model.X[4]*model.X[5])+(63.5*model.X[4]*model.X[2]))
model.P2 = Expression(initialize=(0.949*model.X[1]*model.X[3])+(0.173*model.X[1]*model.X[5]))
model.P3 = Expression(initialize=(-0.716*model.X[1]*model.X[2])-(1.578*model.X[1]*model.X[4])+(1.132*model.X[4]*model.X[2]))
model.P4 = Expression(initialize=-1*model.X[1]*model.X[5])
model.P5 = Expression(initialize=model.X[1]*model.X[4])

def L2force_rule(model):
    return (model.AX[1]+model.P1)**2 \
          +(model.AX[2]+model.P2)**2 \
          +(model.AX[3]+model.P3)**2 \
          +(model.AX[4]+model.P4)**2 \
          +(model.AX[5]+model.P5)**2 
model.L2force = Objective(rule=L2force_rule)

def elevator_rule(model):
    return model.X[6] == -0.05
model.elevator = Constraint(rule=elevator_rule)

def aileron_rule(model):
    return model.X[7] == 0.1; 
model.aileron = Constraint(rule=aileron_rule)

def rudder_rule(model):
    return model.X[8] == 0.0;
model.rudder = Constraint(rule=rudder_rule)
