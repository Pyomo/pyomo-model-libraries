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
#   W. J. Korchinski, Profimatics, Inc,
#   325 Rolling Oaks Drive, Thousand Oaks, California, USA 91361-1200
#   Telephone: 1-805 496 6661, Fax: 1-805 373 5108

#   SIF input: W. Korchinski, Spring 1993.

#   classification SLR2-MN-19-8

from pyomo.environ import *
model = AbstractModel()

model.S = RangeSet(1,19)
model.w = Param(model.S)
model.m = Param(model.S)

model.Feed = Var(initialize=1)
model.Effluent = Var(initialize=1)
model.MF_ohd = Var(initialize=1)
model.HCN  = Var(initialize=1)
model.LCO = Var(initialize=1)
model.HCO = Var(initialize=1)
model.MF_btms = Var(initialize=1)
model.Decant = Var(initialize=1)
model.Dec_recy = Var(initialize=1)
model.Off_gas = Var(initialize=1)
model.DC4_feed = Var(initialize=1)
model.DC3_feed = Var(initialize=1)
model.DC4_btms = Var(initialize=1)
model.Lean_oil = Var(initialize=1)
model.Propane = Var(initialize=1)
model.Butane = Var(initialize=1)
model.C8spl_fd = Var(initialize=1)
model.LCN = Var(initialize=1)
model.MCN  = Var(initialize=1)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f(model):
    return (model.Feed-value(model.m[1]))**2/value(model.w[1])\
    +(model.Effluent-value(model.m[2]))**2/value(model.w[2])\
    +(model.MF_ohd-value(model.m[3]))**2/value(model.w[3])\
    +(model.HCN-value(model.m[4]))**2/value(model.w[4])\
    +(model.LCO-value(model.m[5]))**2/value(model.w[5])\
    +(model.HCO-value(model.m[6]))**2/value(model.w[6])\
    +(model.MF_btms-value(model.m[7]))**2/value(model.w[7])\
    +(model.Decant-value(model.m[8]))**2/value(model.w[8])\
    +(model.Dec_recy-value(model.m[9]))**2/value(model.w[9])\
    +(model.Off_gas-value(model.m[10]))**2/value(model.w[10])\
    +(model.DC4_feed-value(model.m[11]))**2/value(model.w[11])\
    +(model.DC3_feed-value(model.m[12]))**2/value(model.w[12])\
    +(model.DC4_btms-value(model.m[13]))**2/value(model.w[13])\
    +(model.Lean_oil-value(model.m[14]))**2/value(model.w[14])\
    +(model.Propane-value(model.m[15]))**2/value(model.w[15])\
    +(model.Butane-value(model.m[16]))**2/value(model.w[16])\
    +(model.C8spl_fd-value(model.m[17]))**2/value(model.w[17])\
    +(model.LCN-value(model.m[18]))**2/value(model.w[18])\
    +(model.MCN-value(model.m[19]))**2/value(model.w[19])
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return model.Feed + model.Dec_recy - model.Effluent == 0
model.cons1 = Constraint(rule=cons1)
def cons2(model):
    return model.Effluent - model.MF_ohd - model.HCN - model.LCO - model.HCO - model.MF_btms == 0
model.cons2 = Constraint(rule=cons2)
def cons3(model):
    return model.MF_btms - model.Decant - model.Dec_recy == 0
model.cons3 = Constraint(rule=cons3)
def cons4(model):
    return model.MF_ohd + model.Lean_oil - model.Off_gas - model.DC4_feed == 0
model.cons4 = Constraint(rule=cons4)
def cons5(model):
    return model.DC4_feed - model.DC3_feed - model.DC4_btms == 0
model.cons5 = Constraint(rule=cons5)
def cons6(model):
    return model.DC4_btms - model.Lean_oil - model.C8spl_fd == 0
model.cons6 = Constraint(rule=cons6)
def cons7(model):
    return model.DC3_feed - model.Propane - model.Butane == 0
model.cons7 = Constraint(rule=cons7)
def cons8(model):
    return model.C8spl_fd - model.LCN - model.MCN == 0
model.cons8 = Constraint(rule=cons8)
