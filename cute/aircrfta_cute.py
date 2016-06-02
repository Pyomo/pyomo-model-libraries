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

#   Source: Problem 9 in
#   J.J. More',"A collection of nonlinear model problems"
#   Proceedings of the AMS-SIAM Summer Seminar on the Computational
#   Solution of Nonlinear Systems of Equations, Colorado, 1988.
#   Argonne National Laboratory MCS-P60-0289, 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification NOR2-RN-8-5

from pyomo.core import *
model = ConcreteModel()

model.rollrate = Var(initialize=0.0)
model.pitchrat = Var(initialize=0.0)
model.yawrate = Var(initialize=0.0)
model.attckang = Var(initialize=0.0)
model.sslipang = Var(initialize=0.0)
model.elevator = Var(initialize=0.0)
model.aileron = Var(initialize=0.0)
model.rudderdf = Var(initialize=0.0)

model.elevator = 0.1
model.elevator.fixed=True
model.aileron = 0
model.aileron.fixed=True
model.rudderdf = 0
model.rudderdf.fixed=True

def f(model):
    return 0
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    exp1 = -3.933*model.rollrate+0.107*model.pitchrat+0.126*model.yawrate-9.99*model.sslipang\
    - 45.83*model.aileron-7.64*model.rudderdf-0.727*model.pitchrat*model.yawrate+8.39*model.yawrate*model.attckang\
    - 684.4*model.attckang*model.sslipang+63.5*model.pitchrat*model.attckang
    return (0,exp1)
def cons2(model):
    exp2 = -0.987*model.pitchrat-22.95*model.attckang-28.37*model.elevator+0.949*model.rollrate*model.yawrate\
    + 0.173*model.rollrate*model.sslipang
    return (0,exp2)
def cons3(model):
    exp3 = 0.002*model.rollrate-0.235*model.yawrate+5.67*model.sslipang-0.921*model.aileron-6.51*model.rudderdf\
    - 0.716*model.rollrate*model.pitchrat-1.578*model.rollrate*model.attckang+1.132*model.pitchrat*model.attckang
    return (0,exp3)
def cons4(model):
    exp4 = model.pitchrat- model.attckang-1.168*model.elevator-model.rollrate*model.sslipang
    return (0,exp4)
def cons5(model):
    exp5 = -model.yawrate-0.196*model.sslipang-0.0071*model.aileron+model.rollrate*model.attckang
    return (0,exp5)

model.cons1 = Constraint(rule=cons1)
model.cons2 = Constraint(rule=cons2)
model.cons3 = Constraint(rule=cons3)
model.cons4 = Constraint(rule=cons4)
model.cons5 = Constraint(rule=cons5)
