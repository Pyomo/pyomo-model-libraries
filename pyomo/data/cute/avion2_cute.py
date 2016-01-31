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

#   classification OLR2-RN-49-15

from pyomo.core import *
model = AbstractModel()

model.SR = Var(initialize=27.452,
               bounds=(10,150))

model.LR = Var(initialize=1.5000,
               bounds=(0,10))

model.PK = Var(initialize=10.000,
               bounds=(0,10))

model.EF = Var(initialize=0.000,
               bounds=(0,5))

model.SX = Var(initialize=19.217,
               bounds=(7,120))

model.LX = Var(initialize=1.5000,
               bounds=(1.5,8))

model.SD = Var(initialize=3.5688,
               bounds=(2,20))

model.SK = Var(initialize=4.0696,
               bounds=(2,30))

model.ST = Var(initialize=34.315,
               bounds=(30,500))

model.SF = Var(initialize=88.025,
               bounds=(20,200))

model.LF = Var(initialize=5.1306,
               bounds=(0.01,20))

model.AM = Var(initialize=0.0000,
               bounds=(0,10))

model.CA = Var(initialize=-0.14809,
               bounds=(-0.2,-0.001))

model.CB = Var(initialize=0.75980,
               bounds=(0.1,2))

model.SO = Var(initialize=0.0000,
               bounds=(0,1))

model.SS = Var(initialize=0.0000,
               bounds=(0,2))

model.IMPDER = Var(initialize=114.7,
                   bounds=(100,1000))

model.IMPK = Var(initialize=500.00,
                 bounds=(500,5000))

model.IMPFUS = Var(initialize=1760.5,
                   bounds=(500,5000))

model.QI = Var(initialize=2325.6,
               bounds=(1000,20000))

model.PT = Var(initialize=5.6788,
               bounds=(2,30))

model.MV = Var(initialize=14197.0,
               bounds=(2000,20000))

model.MC = Var(initialize=12589.0,
               bounds=(3000,30000))

model.MD = Var(initialize=28394.0,
               bounds=(5000,50000))

model.PD = Var(initialize=0.2000,
               bounds=(0.2,0.8))

model.NS = Var(initialize=1.0000,
               bounds=(1,5))

model.VS = Var(initialize=0.0000,
               bounds=(0,20))

model.CR = Var(initialize=100.00,
               bounds=(100,400))

model.PM = Var(initialize=15.000,
               bounds=(4,15))

model.DV = Var(initialize=0.0000,
               bounds=(0,10))

model.MZ = Var(initialize=500.00,
               bounds=(500,10000))

model.VN = Var(initialize=10.000,
               bounds=(10,50))

model.QV = Var(initialize=814.90,
               bounds=(250,5000))

model.QF = Var(initialize=3140.5,
               bounds=(750,15000))

model.IMPTRAIN = Var(initialize=1945.0,
                     bounds=(250,3000))

model.IMPMOT = Var(initialize=190.85,
                   bounds=(10,5000))

model.IMPNMOT = Var(initialize=35.000,
                    bounds=(35,70))

model.IMPPET = Var(initialize=100.00,
                   bounds=(100,3000))

model.IMPPIL = Var(initialize=200.00,
                   bounds=(200,400))

model.IMPCAN = Var(initialize=120.00,
                   bounds=(120,240))

model.IMPSNA = Var(initialize=700.00,
                   bounds=(700,1900))

model.MS = Var(initialize=1000.0,
               bounds=(100,1000))

model.EL = Var(initialize=4.9367,
               bounds=(2,20))

model.DE = Var(initialize=0.0000,
               bounds=(0,1))

model.DS = Var(initialize=0.0000,
               bounds=(0,2))

model.IMPVOIL = Var(initialize=5000.0,
                    bounds=(500,5000))

model.NM = Var(initialize=1.0,
               bounds=(1,2))

model.NP = Var(initialize=1.0,
               bounds=(1,2))

model.NG = Var(initialize=1.0,
               bounds=(1,2))

def f(model):
    expr = (model.SK - 0.01*model.PK*model.SR)**2 \
    + (model.CA - (model.SS-model.SO-model.CB*model.LF)/(model.LF**2) )**2 \
    + (-2*model.AM+model.SO+model.SS + 0.01*model.EF/model.LF)**2 \
    + (model.AM - 0.025*model.SO*model.CB**2/model.CA)**2 \
    + (model.IMPDER - 27.5*model.SD - 1.3*model.SD**2)**2 \
    + (model.IMPK - 70*model.SK + 8.6*model.SK**2)**2 \
    + (model.QI - 1000 + model.MV**2/24000)**2 \
    + (1000*model.PT - model.MD*model.PD)**2 \
    + (model.VN + model.VS +model.QF/790 + 2 - model.MZ/model.CR +model.DV*model.PT)**2 \
    + (model.IMPMOT - 1000*model.PT/(model.PM+20) - 12*sqrt(model.PT))**2 \
    + (model.ST - 1.25*model.SR*model.NM)**2 \
    + (model.SR - model.MD/model.MS)**2 \
    + (model.QV - 2.4*model.SX*sqrt(model.SX)*model.EL/sqrt(model.LX))**2 \
    + (model.SO - 0.785*model.DE**2*model.PT)**2 \
    + (model.SS - 0.785*model.DS**2*model.PT)**2 \
    + (model.CB - 2*(model.VN-model.CA*model.LF**3)/(model.LF**2*(3-model.SO*model.LF)))**2 \
    + (model.IMPVOIL - 1.15*model.SX*(15+0.15*model.SX)*(8+(model.MC*model.LX/(50*model.SR*model.EL))**1.5))**2
    return expr
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return (0, model.SD-0.13*model.SR)
#       return model.SD-0.13*model.SR == 0
model.cons1 = Constraint(rule=cons1)

def cons2(model):
    return (0, model.SX-0.7*model.SR)
#       return model.SX-0.7*model.SR == 0
model.cons2 = Constraint(rule=cons2)

def cons3(model):
    return (0, model.LX-model.LR)
#       return model.LX-model.LR == 0
model.cons3 = Constraint(rule=cons3)

def cons5(model):
    return model.SF - model.ST - 2*model.SD - 2*model.SX - 2*model.SK == 0
model.cons5 = Constraint(rule=cons5)

def cons11(model):
    return model.IMPFUS - 20*model.SF == 0
model.cons11 = Constraint(rule=cons11)

def cons12(model):
    return model.MD - 2*model.MV == 0
model.cons12 = Constraint(rule=cons12)

def cons15(model):
    return model.QF - model.QI - model.QV == 0
model.cons15 = Constraint(rule=cons15)

def cons17(model):
    return model.IMPTRAIN - 0.137*model.MV == 0
model.cons17 = Constraint(rule=cons17)

def cons19(model):
    return model.IMPNMOT - 35*model.NM == 0
model.cons19 = Constraint(rule=cons19)

def cons20(model):
    return model.IMPPET - 0.043*model.QI == 0
model.cons20 = Constraint(rule=cons20)

def cons21(model):
    return model.IMPPIL - 200*model.NP == 0
model.cons21 = Constraint(rule=cons21)

def cons22(model):
    return model.IMPCAN - 120*model.NG == 0
model.cons22 = Constraint(rule=cons22)

def cons23(model):
    return model.IMPSNA - 300*model.NS -400 == 0
model.cons23 = Constraint(rule=cons23)

def cons24(model):
    return model.MC - model.MV + 95*model.NP + 70*model.NG + 660*model.NM + 0.5*model.QI -380 == 0
model.cons24 = Constraint(rule=cons24)

def cons25(model):
    return model.MZ - model.IMPTRAIN + model.IMPNMOT + model.IMPPET + model.IMPPIL + model.IMPCAN + model.IMPSNA + 290 == 0
model.cons25 = Constraint(rule=cons25)
