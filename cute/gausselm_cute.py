#
#  Pyomo Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil, Juan Lopez
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

#   classification LOR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()

n=16

def x_init_rule(model,k,i,j):
    if i==j:
        return 1.0
    else:
        return 0.01
model.x = Var([(k,i,j) for k in range(1,n+1) for i in range(k,n+1) for j in range(k,n+1)],initialize=x_init_rule)

def f_rule(model):
    return -model.x[n,n,n]
model.f = Objective(rule=f_rule)

conse_index = [(k,i,j) for k in range(1,n-1+1) for i in range(k+1,n+1) for j in range(k+1,n+1)]
def conse_rule(model,k,i,j):
    return model.x[k,i,k]*model.x[k,k,j]/model.x[k,k,k] + model.x[k+1,i,j] - model.x[k,i,j] == 0
model.conse = Constraint(conse_index,rule=conse_rule)

consmikk_index = [(k,i) for k in range(2,n) for i in range(k+1,n+1)]

def consmikk_rule(model,k,i):
    return model.x[k,i,k] - model.x[k,k,k] <= 0
model.consmikk = Constraint(consmikk_index,rule=consmikk_rule)

def consmkik_rule(model,k,i):
    return model.x[k,k,i] - model.x[k,k,k] <= 0
model.consmkik = Constraint(consmikk_index,rule=consmkik_rule)

consmijk_index = [(k,i,j) for k in range(2,n) for i in range(k+1,n+1) for j in range(k+1,n+1)]
def consmijk_rule(model,k,i,j):
    return model.x[k,i,j] - model.x[k,k,k] <= 0
model.consmijk = Constraint(consmijk_index,rule=consmijk_rule)

def conspikk_rule(model,k,i):
    return model.x[k,i,k] + model.x[k,k,k] >= 0
model.conspikk = Constraint(consmikk_index,rule=conspikk_rule)

def conspkik_rule(model,k,i):
    return model.x[k,k,i] + model.x[k,k,k] >= 0
model.conspkik = Constraint(consmikk_index,rule=conspkik_rule)

def conspijk_rule(model,k,i,j):
    return model.x[k,i,j] + model.x[k,k,k] >= 0
model.conspijk = Constraint(consmijk_index,rule=conspijk_rule)

def var_bnd_rule(model,i,j):
    return -1.0 <= model.x[1,i,j] <= 1.0
model.var_bnd = Constraint(RangeSet(1,n),RangeSet(1,n),rule=var_bnd_rule)

def var_bnd_diag_rule(model,k):
    return model.x[k,k,k] >= 0.0
model.var_bnd_diag = Constraint(RangeSet(1,n),rule=var_bnd_diag_rule)

model.x[1,1,1] = 1.0
model.x[1,1,1].fixed = True

