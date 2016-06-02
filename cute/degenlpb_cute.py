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

#   Source:
#   T.C.T. Kotiah and D.I. Steinberg,
#   "Occurences of cycling and other phenomena arising in a class of
#   linear programming models",
#   Communications of the ACM, vol. 20, pp. 107-112, 1977.

#   SIF input: Ph. Toint, Aug 1990.

#   classification LLR2-AN-20-15

from pyomo.core import *
model = AbstractModel()

model.N = Param(initialize=20)
model.M = Param(initialize=15)
model.S = RangeSet(1,model.N)
model.x = Var(model.S, bounds=(0.0,1.0), initialize=1.0)

def f(model):
    return -1*(0.01*model.x[2]+33.333*model.x[3]+100.0*model.x[4]+0.01*model.x[5]+33.343*model.x[6]+100.01*model.x[7]+33.333*model.x[8]+133.33*model.x[9]+100.0*model.x[10])
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return -0.70785+model.x[1]+2*model.x[2]+2*model.x[3]+2*model.x[4]+model.x[5]+2*model.x[6]+2*model.x[7]+model.x[8]+2*model.x[9]+model.x[10] == 0
model.cons1 = Constraint(rule=cons1)
def cons2(model):
    return 0.326*model.x[1]-101*model.x[2]+200*model.x[5]+0.06*model.x[6]+0.02*model.x[7] == 0
model.cons2 = Constraint(rule=cons2)
def cons3(model):
    return 0.0066667*model.x[1]-1.03*model.x[3]+200*model.x[6]+0.06*model.x[8]+0.02*model.x[9] == 0
model.cons3 = Constraint(rule=cons3)
def cons4(model):
    return 0.00066667*model.x[1]-1.01*model.x[4]+200*model.x[7]+0.06*model.x[9]+0.02*model.x[10] == 0
model.cons4 = Constraint(rule=cons4)
def cons5(model):
    return 0.978*model.x[2]-201*model.x[5]+100*model.x[11]+0.03*model.x[12]+0.01*model.x[13] == 0
model.cons5 = Constraint(rule=cons5)
def cons6(model):
    return 0.01*model.x[2]+0.489*model.x[3]-101.03*model.x[6]+100*model.x[12]+0.03*model.x[14]+0.01*model.x[15] == 0
model.cons6 = Constraint(rule=cons6)
def cons7(model):
    return 0.001*model.x[2]+0.489*model.x[4]-101.03*model.x[7]+100*model.x[13]+0.03*model.x[15]+0.01*model.x[16] == 0
model.cons7 = Constraint(rule=cons7)
def cons8(model):
    return 0.001*model.x[3]+0.01*model.x[4]-1.04*model.x[9]+100*model.x[15]+0.03*model.x[18]+0.01*model.x[19] == 0
model.cons8 = Constraint(rule=cons8)
def cons9(model):
    return 0.02*model.x[3]-1.06*model.x[8]+100*model.x[14]+0.03*model.x[17]+0.01*model.x[19] == 0
model.cons9 = Constraint(rule=cons9)
def cons10(model):
    return 0.002*model.x[4]-1.02*model.x[10]+100*model.x[16]+0.03*model.x[19]+0.01*model.x[20] == 0
model.cons10 = Constraint(rule=cons10)
def cons11(model):
    return -2.5742e-6*model.x[11]+0.00252*model.x[13]-0.61975*model.x[16]+1.03*model.x[20] == 0
model.cons11 = Constraint(rule=cons11)
def cons12(model):
    return -0.00257*model.x[11] + 0.25221*model.x[12] - 6.2*model.x[14] + 1.09*model.x[17] == 0
model.cons12 = Constraint(rule=cons12)
def cons13(model):
    return 0.00629*model.x[11]-0.20555*model.x[12]-4.1106*model.x[13]+101.04*model.x[15]+505.1*model.x[16]-256.72*model.x[19] == 0
model.cons13 = Constraint(rule=cons13)
def cons14(model):
    return 0.00841*model.x[12]-0.08406*model.x[13]-0.20667*model.x[14]+20.658*model.x[16]+1.07*model.x[18]-10.5*model.x[19] == 0
model.cons14 = Constraint(rule=cons14)
def cons15(model):
    return -model.x[1]+300*model.x[2]+0.09*model.x[3]+0.03*model.x[4] == 0
model.cons15 = Constraint(rule=cons15)
