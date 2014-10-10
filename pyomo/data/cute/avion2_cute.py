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

model.SR = Var(initialize=27.452)
model.SR.setlb(10)
model.SR.setub(150)

model.LR = Var(initialize=1.5000)
model.LR.setlb(0)
model.LR.setub(10)

model.PK = Var(initialize=10.000)
model.PK.setlb(0)
model.PK.setub(10)

model.EF = Var(initialize=0.000)
model.EF.setlb(0)
model.EF.setub(5)

model.SX = Var(initialize=19.217)
model.SX.setlb(7)
model.SX.setub(120)

model.LX = Var(initialize=1.5000)
model.LX.setlb(1.5)
model.LX.setub(8)

model.SD = Var(initialize=3.5688)
model.SD.setlb(2)
model.SD.setub(20)

model.SK = Var(initialize=4.0696)
model.SK.setlb(2)
model.SK.setub(30)

model.ST = Var(initialize=34.315)
model.ST.setlb(30)
model.ST.setub(500)

model.SF = Var(initialize=88.025)
model.SF.setlb(20)
model.SF.setub(200)

model.LF = Var(initialize=5.1306)
model.LF.setlb(0.01)
model.LF.setub(20)

model.AM = Var(initialize=0.0000)
model.AM.setlb(0)
model.AM.setub(10)

model.CA = Var(initialize=-0.14809)
model.CA.setlb(-0.2)
model.CA.setub(-0.001)

model.CB = Var(initialize=0.75980)
model.CB.setlb(0.1)
model.CB.setub(2)

model.SO = Var(initialize=0.0000)
model.SO.setlb(0)
model.SO.setub(1)

model.SS = Var(initialize=0.0000)
model.SS.setlb(0)
model.SS.setub(2)

model.IMPDER = Var(initialize=114.7)
model.IMPDER.setlb(100)
model.IMPDER.setub(1000)

model.IMPK = Var(initialize=500.00)
model.IMPK.setlb(500)
model.IMPK.setub(5000)

model.IMPFUS = Var(initialize=1760.5)
model.IMPFUS.setlb(500)
model.IMPFUS.setub(5000)

model.QI = Var(initialize=2325.6)
model.QI.setlb(1000)
model.QI.setub(20000)

model.PT = Var(initialize=5.6788)
model.PT.setlb(2)
model.PT.setub(30)

model.MV = Var(initialize=14197.0)
model.MV.setlb(2000)
model.MV.setub(20000)

model.MC = Var(initialize=12589.0)
model.MC.setlb(3000)
model.MC.setub(30000)

model.MD = Var(initialize=28394.0)
model.MD.setlb(5000)
model.MD.setub(50000)

model.PD = Var(initialize=0.2000)
model.PD.setlb(0.2)
model.PD.setub(0.8)

model.NS = Var(initialize=1.0000)
model.NS.setlb(1)
model.NS.setub(5)

model.VS = Var(initialize=0.0000)
model.VS.setlb(0)
model.VS.setub(20)

model.CR = Var(initialize=100.00)
model.CR.setlb(100)
model.CR.setub(400)

model.PM = Var(initialize=15.000)
model.PM.setlb(4)
model.PM.setub(15)

model.DV = Var(initialize=0.0000)
model.DV.setlb(0)
model.DV.setub(10)

model.MZ = Var(initialize=500.00)
model.MZ.setlb(500)
model.MZ.setub(10000)

model.VN = Var(initialize=10.000)
model.VN.setlb(10)
model.VN.setub(50)

model.QV = Var(initialize=814.90)
model.QV.setlb(250)
model.QV.setub(5000)

model.QF = Var(initialize=3140.5)
model.QF.setlb(750)
model.QF.setub(15000)

model.IMPTRAIN = Var(initialize=1945.0)
model.IMPTRAIN.setlb(250)
model.IMPTRAIN.setub(3000)

model.IMPMOT = Var(initialize=190.85)
model.IMPMOT.setlb(10)
model.IMPMOT.setub(5000)

model.IMPNMOT = Var(initialize=35.000)
model.IMPNMOT.setlb(35)
model.IMPNMOT.setub(70)

model.IMPPET = Var(initialize=100.00)
model.IMPPET.setlb(100)
model.IMPPET.setub(3000)

model.IMPPIL = Var(initialize=200.00)
model.IMPPIL.setlb(200)
model.IMPPIL.setub(400)

model.IMPCAN = Var(initialize=120.00)
model.IMPCAN.setlb(120)
model.IMPCAN.setub(240)

model.IMPSNA = Var(initialize=700.00)
model.IMPSNA.setlb(700)
model.IMPSNA.setub(1900)

model.MS = Var(initialize=1000.0)
model.MS.setlb(100)
model.MS.setub(1000)

model.EL = Var(initialize=4.9367)
model.EL.setlb(2)
model.EL.setub(20)

model.DE = Var(initialize=0.0000)
model.DE.setlb(0)
model.DE.setub(1)

model.DS = Var(initialize=0.0000)
model.DS.setlb(0)
model.DS.setub(2)

model.IMPVOIL = Var(initialize=5000.0)
model.IMPVOIL.setlb(500)
model.IMPVOIL.setub(5000)

model.NM = Var(initialize=1.0)
model.NM.setlb(1)
model.NM.setub(2)

model.NP = Var(initialize=1.0)
model.NP.setlb(1)
model.NP.setub(2)

model.NG = Var(initialize=1.0)
model.NG.setlb(1)
model.NG.setub(2)

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
