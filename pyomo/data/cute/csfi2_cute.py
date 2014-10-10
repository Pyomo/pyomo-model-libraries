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

#   Source: problem MINLEN in
#   Vasko and Stott
#   "Optimizing continuous caster product dimensions:
#    an example of a nonlinear design problem in the steel industry"
#   SIAM Review, Vol 37 No, 1 pp.82-84, 1995

#   SIF input: A.R. Conn April 1995

#   classification LOR2-RN-5-4

from pyomo.core import *
model = AbstractModel()

model.mintph = Param(initialize=45.0)
model.minthick = Param(initialize=7.0)
model.minarea = Param(initialize=200.0)
model.maxarea = Param(initialize=250.0)
model.maxaspr = Param(initialize=2.0)
model.k = Param(initialize=1.0)

def thick_bound(model):
    l = value(model.minthick)
    return (l,None)
model.thick = Var(bounds=thick_bound, initialize=0.5)
model.wid = Var(bounds=(0.0,None), initialize=0.5)
model.len = Var(bounds=(0.0,None), initialize=0.5)
def tph_bound(model):
    l = value(model.mintph)
    return (l,None)
model.tph = Var(bounds=tph_bound, initialize=0.5)
model.ipm = Var(bounds=(0.0,None), initialize=0.5)

def f(model):
    return model.len
model.f = Objective(rule=f,sense=minimize)

def cons1(model):
    return 117.370892*model.tph/(model.wid*model.thick)-model.ipm == 0.0
model.cons1 = Constraint(rule=cons1)
def cons2(model):
    return model.thick**2*model.ipm/48.0-model.len == 0.0
model.cons2 = Constraint(rule=cons2)
def cons3(model):
    return model.wid/model.thick <= value(model.maxaspr)
model.cons3 = Constraint(rule=cons3)
def cons4(model):
    #return 0.0 <= model.thick*model.wid - value(model.minarea) <= value(model.maxarea) - value(model.minarea)
    return (0.0, model.thick*model.wid - value(model.minarea), value(model.maxarea) - value(model.minarea))
model.cons4 = Constraint(rule=cons4)
