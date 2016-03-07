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
#   Ph. Toint, private communication.

#   SIF input: Ph. Toint, April 1991.

#   classification SOR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()

model.t = Param(initialize=1000)
model.xt = Param(initialize=10.0)
model.mass = Param(initialize=0.37)
model.tol = Param(initialize=0.1)

def h_rule(model):
    return value(model.xt)/value(model.t)
model.h = Param(initialize=h_rule)
def w_rule(model):
    return value(model.xt)*(value(model.t)+1.0)/2.0
model.w = Param(initialize=w_rule)

def fmax_rule(model):
    return value(model.xt)/value(model.t)
model.fmax = Param(initialize=fmax_rule)

model.S = RangeSet(0,model.t)
model.SS = RangeSet(1,model.t)

def x_rule(model, i):
    return i*value(model.h)
def x_bound(model, i):
    l = 0.0
    u = value(model.xt)
    return (l,u)
model.x = Var(model.S, bounds=x_bound, initialize=x_rule)
model.y = Var(model.S)
model.z = Var(model.S)
model.vx = Var(model.S, initialize=1.0)
model.vy = Var(model.S)
model.vz = Var(model.S)

def u_bound(model, i):
    l = -value(model.fmax)
    u = value(model.fmax)
    return (l,u)
model.ux = Var(model.SS, bounds=u_bound)
model.uy = Var(model.SS, bounds=u_bound)
model.uz = Var(model.SS, bounds=u_bound)

model.x[0] = 0.0
model.x[0].fixed=True
model.y[0] = 0.0
model.y[0].fixed=True
model.z[0] = 1.0
model.z[0].fixed=True
model.vx[0] = 0.0
model.vx[0].fixed=True
model.vy[0] = 0.0
model.vy[0].fixed=True
model.vz[0] = 0.0
model.vz[0].fixed=True
model.vx[value(model.t)] = 0.0
model.vx[value(model.t)].fixed=True
model.vy[value(model.t)] = 0.0
model.vy[value(model.t)].fixed=True
model.vz[value(model.t)] = 0.0
model.vz[value(model.t)].fixed=True

def f(model):
    return sum ([(i*value(model.h)/value(model.w))*(model.x[i] - value(model.xt))**2 for i in model.SS])
model.f = Objective(rule=f,sense=minimize)

def acx(model, i):
    return value(model.mass)*(model.vx[i]-model.vx[i-1])/value(model.h) - model.ux[i] == 0
model.acx = Constraint(model.SS, rule=acx)
def acy(model, i):
    return value(model.mass)*(model.vy[i]-model.vy[i-1])/value(model.h) - model.uy[i] == 0
model.acy = Constraint(model.SS, rule=acy)
def acz(model, i):
    return value(model.mass)*(model.vz[i]-model.vz[i-1])/value(model.h) - model.uz[i] == 0
model.acz = Constraint(model.SS, rule=acz)
def psx(model, i):
    return (model.x[i]-model.x[i-1])/value(model.h) - model.vx[i] == 0
model.psx = Constraint(model.SS, rule=psx)
def psy(model, i):
    return (model.y[i]-model.y[i-1])/value(model.h) - model.vy[i] == 0
model.psy = Constraint(model.SS, rule=psy)
def psz(model, i):
    return (model.z[i]-model.z[i-1])/value(model.h) - model.vz[i] == 0
model.psz = Constraint(model.SS, rule=psz)
def sc(model, i):
    return (model.y[i] - sin(model.x[i]))**2 + (model.z[i] - cos(model.x[i]))**2 - value(model.tol)**2 <= 0
model.sc = Constraint(model.SS, rule=sc)
