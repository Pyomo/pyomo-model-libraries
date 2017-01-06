#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Formulated in pyomo by Logan Barnes. Taken from:

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
#   A partial specification of problem SPANHYD.

#   SIF input: Ph. Toint, Sept 1990.

#   classification LNR2-MN-97-33

from pyomo.environ import *
model = AbstractModel()
model.N = RangeSet(1,97)

model.l  = Param(model.N)
model.u  = Param(model.N)
model.x0 = Param(model.N)

def x_bounds_rule(model,i):
    return [value(model.l[i]),value(model.u[i])]
def x_init_rule(model,i):
    return model.x0[i]

model.x = Var(model.N,bounds=x_bounds_rule,initialize=x_init_rule)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return -model.x[1]
model.obj = Objective(rule=obj_rule,sense=minimize)

def n1_rule(model): 
    return model.x[1] - model.x[11] - model.x[21] - model.x[30] + 51.38 == 0
model.n1 = Constraint(rule=n1_rule)
def n2_rule(model):
    return model.x[2] + model.x[11] - model.x[12] + model.x[21] - model.x[22] - model.x[31] + 13.84 == 0
model.n2 = Constraint(rule=n2_rule)
def n3_rule(model):
    return model.x[3] + model.x[12] - model.x[13] + model.x[22] - model.x[23] - model.x[32] + 2.58 == 0
model.n3 = Constraint(rule=n3_rule)
def n4_rule(model):
    return model.x[4] - model.x[14] - model.x[24] - model.x[33] + 21.91 == 0
model.n4 = Constraint(rule=n4_rule)
def n5_rule(model):
    return model.x[5] + model.x[13] + model.x[14] - model.x[15] - model.x[34] == 0
model.n5 = Constraint(rule=n5_rule)
def n6_rule(model):
    return model.x[6] - model.x[16] - model.x[25] - model.x[35] + 12.97 == 0
model.n6 = Constraint(rule=n6_rule)
def n7_rule(model):
    return model.x[7] + model.x[16] - model.x[17] + model.x[25] - model.x[26] - model.x[36] == 0
model.n7 = Constraint(rule=n7_rule)
def n8_rule(model):
    return model.x[8] + model.x[17] - model.x[18] + model.x[26] - model.x[27] - model.x[37] + 2.89 == 0
model.n8 = Constraint(rule=n8_rule)
def n9_rule(model):
    return model.x[9] + model.x[15] + model.x[18] - model.x[19] + model.x[23] + model.x[24] + model.x[27] - model.x[28] - model.x[38] + 20.84 == 0
model.n9 = Constraint(rule=n9_rule)
def n10_rule(model):
    return model.x[10] + model.x[19] - model.x[20] + model.x[28] - model.x[29] - model.x[39] + 17.14 == 0
model.n10 = Constraint(rule=n10_rule)
def n11_rule(model):
    return model.x[30] - model.x[40] - model.x[50] - model.x[59] + 32.06 == 0
model.n11 = Constraint(rule=n11_rule)
def n12_rule(model):
    return model.x[31] + model.x[40] - model.x[41] + model.x[50] - model.x[51] - model.x[60] + 0.28 == 0
model.n12 = Constraint(rule=n12_rule)
def n13_rule(model):
    return model.x[32] + model.x[41] - model.x[42] + model.x[51] - model.x[52] - model.x[61] + 4.2 == 0
model.n13 = Constraint(rule=n13_rule)
def n14_rule(model):
    return model.x[33] - model.x[43] - model.x[53] - model.x[62] + 48.37 == 0
model.n14 = Constraint(rule=n14_rule)
def n15_rule(model):
    return model.x[34] + model.x[42] + model.x[43] - model.x[44] - model.x[63] == 0
model.n15 = Constraint(rule=n15_rule)
def n16_rule(model):
    return model.x[35] - model.x[45] - model.x[54] - model.x[64] + 18.13 == 0
model.n16 = Constraint(rule=n16_rule)
def n17_rule(model):
    return model.x[36] + model.x[45] - model.x[46] + model.x[54] - model.x[55] - model.x[65] == 0
model.n17 = Constraint(rule=n17_rule)
def n18_rule(model):
    return model.x[37] + model.x[46] - model.x[47] + model.x[55] - model.x[56] - model.x[66] - 1.61 == 0
model.n18 = Constraint(rule=n18_rule)
def n19_rule(model):
    return model.x[38] + model.x[44] + model.x[47] - model.x[48] + model.x[52] + model.x[53] + model.x[56] - model.x[57] - model.x[67] + 26.6 == 0
model.n19 = Constraint(rule=n19_rule)
def n20_rule(model):
    return model.x[39] + model.x[48] - model.x[49] + model.x[57] - model.x[58] - model.x[68] + 18.76 == 0
model.n20 = Constraint(rule=n20_rule)
def n21_rule(model):
    return model.x[59] - model.x[69] - model.x[79] - model.x[88] + 18.13 == 0
model.n21 = Constraint(rule=n21_rule)
def n22_rule(model):
    return model.x[60] + model.x[69] - model.x[70] + model.x[79] - model.x[80] - model.x[89] == 0
model.n22 = Constraint(rule=n22_rule)
def n23_rule(model):
    return model.x[61] + model.x[70] - model.x[71] + model.x[80] - model.x[81] - model.x[90] == 0
model.n23 = Constraint(rule=n23_rule)
def n24_rule(model):
    return model.x[62] - model.x[72] - model.x[82] - model.x[91] + 18.13 == 0
model.n24 = Constraint(rule=n24_rule)
def n25_rule(model):
    return model.x[63] + model.x[71] + model.x[72] - model.x[73] - model.x[92] == 0
model.n25 = Constraint(rule=n25_rule)
def n26_rule(model):
    return model.x[64] - model.x[74] - model.x[83] - model.x[93] + 9.1 == 0
model.n26 = Constraint(rule=n26_rule)
def n27_rule(model):
    return model.x[65] + model.x[74] - model.x[75] + model.x[83] - model.x[84] - model.x[94] == 0
model.n27 = Constraint(rule=n27_rule)
def n28_rule(model):
    return model.x[66] + model.x[75] - model.x[76] + model.x[84] - model.x[85] - model.x[95] - 5.81 == 0
model.n28 = Constraint(rule=n28_rule)
def n29_rule(model):
    return model.x[67] + model.x[73] + model.x[76] - model.x[77] + model.x[81] + model.x[82] + model.x[85] - model.x[86] - model.x[96] + 9.1 == 0
model.n29 = Constraint(rule=n29_rule)
def n30_rule(model):
    return model.x[68] + model.x[77] - model.x[78] + model.x[86] - model.x[87] - model.x[97] + 6.02 == 0
model.n30 = Constraint(rule=n30_rule)
def n31_rule(model):
    return model.x[20] + model.x[29] + model.x[49] + model.x[58] + model.x[78] + model.x[87] - 608.35 == 0
model.n31 = Constraint(rule=n31_rule)
def n32_rule(model):
    return -model.x[1] - model.x[2] - model.x[3] - model.x[4] - model.x[5] - model.x[6] - model.x[7] - model.x[8] - model.x[9] - model.x[10] + 4626.34 == 0
model.n32 = Constraint(rule=n32_rule)
def n33_rule(model):
    return model.x[88] + model.x[89] + model.x[90] + model.x[91] + model.x[92] + model.x[93] + model.x[94] + model.x[95] + model.x[96] + model.x[97] - 4363.0 == 0
model.n33 = Constraint(rule=n33_rule)
