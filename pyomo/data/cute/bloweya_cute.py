#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Juan Lopez and Gabe Hackebeil
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

#   Source: a simplification of
#   J.F. Blowey and C.M. Elliott,
#   "The Cahn-Hilliard gradient theory for phase separation with 
#   non-smooth free energy Part II: Numerical analysis",
#   European Journal of Applied Mathematics (3) pp 147-179, 1992.

#   SIF input: Nick Gould, August 1996

#   classification QLR2-MN-V-V

from pyomo.core import *
model = ConcreteModel()

N = 1000.0
A = 1/5.0
B = 2/5.0
C = 3/5.0
D = 4/5.0
INT = N*(1+A+B-C-D)

def v_rule(model,i):
    if (0 <= i) and (i <= N*A):
        return 1.0
    elif (N*A+1 <= i) and (i <= N*B):
        return 1 - (i-N*A)*2/(N*(B-A))
    elif (N*B+1 <= i) and (i <= N*C):
        return -1 
    elif (N*C+1 <= i) and (i <= N*D):
        return (-1 + (i-N*C)*2/(N*(D-C)))
    else:
        return 1.0
model.v = Param(RangeSet(0,N),initialize=v_rule)

def u_rule(model,i):
    return model.v[i]
model.u = Var(RangeSet(0,N),bounds=(-1.0,1.0),initialize=u_rule)
model.w = Var(RangeSet(0,N),initialize=0.0)
    
def f_rule(model):
    return -2*model.u[0]*model.u[1] + model.u[0]**2 + \
    sum(-2*model.u[i]*model.u[i+1] + 2*model.u[i]**2 for i in range(1,int(N)))+\
    model.u[N]**2+sum(1/N**2*model.u[i]*model.w[i] for i in range(0,int(N)+1))+\
    sum(-1/N**2*model.v[i]*model.u[i]-2/N**2*model.v[i]*model.w[i] for i in range(0,int(N)+1))+\
    (model.v[1]-model.v[0])*model.u[0]\
    +sum((model.v[i-1]-2*model.v[i]+model.v[i+1])*model.u[i] for i in range(1,int(N))) + (model.v[N-1]-model.v[N])*model.u[N]
model.f = Objective(rule=f_rule)
    
def con1_rule(model):
    return 0.5*model.u[0] + sum(model.u[i] for i in range(1,int(N))) + 0.5*model.u[N] == 0.2*INT
model.cons1 = Constraint(rule=con1_rule)

def con2_rule(model):
    return model.u[0] - model.u[1] - 1/N**2*model.w[0] == 0
model.cons2 = Constraint(rule=con2_rule)

def con3_rule(model,i):
    return 2*model.u[i] - model.u[i+1] - model.u[i-1] - 1/N**2*model.w[i] == 0
model.cons3 = Constraint(RangeSet(1,N-1),rule=con3_rule)

def con4_rule(model):
    return model.u[N] - model.u[N-1] - 1/N**2*model.w[N]== 0
model.cons4 = Constraint(rule=con4_rule)
