#  _________________________________________________________________________
#                                                                           
#  Pyomo: Python Optimization Modeling Objects                           
#  Copyright (c) 2010 Sandia Corporation.                                   
#  This software is distributed under the BSD License.                      
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,   
#  the U.S. Government retains certain rights in this software.             
#  For more information, see the Pyomo README.txt file.                     
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird and Daniel P. Word
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

#   Source: problem P4 in
#   W.W. Hager,
#   "Multiplier Methods for Nonlinear Optimal Control",
#   SIAM J. on Numercal Analysis 27(4): 1061-1080, 1990.

#   SIF input: Ph. Toint, April 1991.

#   classification OLR2-AN-V-V

from pyomo.core import *

model = ConcreteModel()

def t_rule(m,i):
    return i*value(m.h)
def z_rule(m,i):
    return exp(-2*value(m.t[i]))
def a_rule(m,i):
    return -0.5*value(m.z[i])
def b_rule(m,i):
    return value(m.a[i])*(value(m.t[i])+0.5)
def c_rule(m,i):
    return value(m.a[i])*(value(m.t[i])**2 + value(m.t[i])+ 0.5)
def scda_rule(m):
    return (value(m.a[1])-value(m.a[0]))/2
def scdb_rule(m):
    return (value(m.b[1])- value(m.b[0]))*value(m.n)
def scdc_rule(m):
    return (value(m.c[1])- value(m.c[0]))*value(m.n)*value(m.n)*0.5
def xx0_rule(m):
    return (1+3*value(m.e))/(2-2*value(m.e))

model.n = Param(initialize=5000)
model.h = Param(initialize=1.0/5000.0)
model.one = Param(initialize=1)

model.Sx = RangeSet(0,model.n)
model.Su = RangeSet(1,model.n)
model.S = RangeSet(0,model.one)

model.t = Param(model.Sx, initialize=t_rule)
model.z = Param(model.Sx, initialize=z_rule)
model.a = Param(model.S, initialize=a_rule)
model.b = Param(model.S, initialize=b_rule)
model.c = Param(model.S, initialize=c_rule)
model.scda = Param(initialize=scda_rule)
model.scdb = Param(initialize=scdb_rule)
model.scdc = Param(initialize=scdc_rule)
model.e = Param(initialize = exp(1))
model.xx0 = Param(initialize=xx0_rule)

def u_bounds(m, i):
    return (None,1.0)

model.x = Var(model.Sx, initialize=0.0)
model.u = Var(model.Su, bounds=u_bounds, initialize=0.0)


def f(m):
    sum_expr_1 = 0
    sum_expr_2 = 0
    for i in m.Su:
        sum_expr_1 += (value(m.scda)*m.z[i-1]*m.x[i]**2 + value(m.scdb)*m.z[i-1]*m.x[i]*(m.x[i-1]-m.x[i]) + value(m.scdc)*m.z[i-1]*(m.x[i-1]-m.x[i])**2)
        sum_expr_2 += ((value(m.h))*(m.u[i])**2)*0.5
    exp = sum_expr_1 + sum_expr_2
    return exp
model.f = Objective(rule=f,sense=minimize)

def cons1(m, i):
    return (0,(value(m.n)-1)*m.x[i] - value(m.n)*m.x[i-1] - exp(value(m.t[i]))*m.u[i])
model.cons1 = Constraint(model.Su,rule=cons1)

model.x[0].fix(value(model.xx0))
