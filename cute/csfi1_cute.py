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

#   Source: problem MAXTPH in
#   Vasko and Stott
#   "Optimizing continuous caster product dimensions:
#    an example of a nonlinear design problem in the steel industry"
#   SIAM Review, Vol 37 No, 1 pp.82-84, 1995

#   SIF input: A.R. Conn April 1995

#   classification LOR2-RN-5-4

from pyomo.core import *
model = ConcreteModel()

density = 0.284
lenmax = 60.0
maxaspr = 2.0
minthick = 7.0
minarea = 200.0
maxarea = 250.0
k = 1.0

model.thick = Var(bounds=(minthick,None),initialize=0.5)
model.wid = Var(bounds=(0.0,None),initialize=0.5)
model.len = Var(bounds=(0.0,lenmax),initialize=0.5)
model.tph = Var(bounds=(0.0,None),initialize=0.5)
model.ipm = Var(bounds=(0.0,None),initialize=0.5)

def f(model):
    return -model.tph
model.f = Objective(rule=f)

def con1(model):
    return 117.370892*model.tph/(model.wid*model.thick)-model.ipm == 0.0
def con2(model):
    return model.thick**2*model.ipm/48.0-model.len == 0.0;
def con3(model):
    return model.wid/model.thick <= maxaspr
def con4(model):
    return 0.0 <= model.thick*model.wid - minarea <= maxarea-minarea
    
model.cons1 = Constraint(rule=con1)
model.cons2 = Constraint(rule=con2)
model.cons3 = Constraint(rule=con3)
model.cons4 = Constraint(rule=con4)
