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
#
# hs109.mod OOR2-MY-9-26
# Original AMPL coding by Elena Bobrovnikova (summer 1996 at Bell Labs).

# Ref.: W. Hock and K. Schittkowski, Test Examples for Nonlinear Programming
# Codes.  Lecture Notes in Economics and Mathematical Systems, v. 187,
# Springer-Verlag, New York, 1981, p. 118.

# Number of variables:  9
# Number of constraints:  26
# Objective separable
# Objective nonconvex
# Nonlinear constraints


from pyomo.core import *
model = AbstractModel()
model.N = RangeSet(1,9)
model.M = RangeSet(1,2)
model.L = RangeSet(3,9)

a = 50.176
b1 = .25
b = sin(b1)
c = cos(b1)

l_init={}
l_init[1] = 0
l_init[2] = 0
l_init[3] = -0.55
l_init[4] = -0.55
l_init[5] = 196.0
l_init[6] = 196.0
l_init[7] = 196.0
l_init[8] = -400.0
l_init[9] = -400.0

u_init={}
u_init[1] = 0
u_init[2] = 0
u_init[3] = 0.55
u_init[4] = 0.55
u_init[5] = 252.0
u_init[6] = 252.0
u_init[7] = 252.0
u_init[8] = 800.0
u_init[9] = 800.0

def l_init_rule(model,j):
    return l_init[j]
def u_init_rule(model,j):
    return u_init[j]

model.l = Param(model.N,initialize=l_init_rule)
model.u = Param(model.N,initialize=u_init_rule)

def x_bound_rule(model,j):
      if j in model.M:
          return (0,None)
      elif j in model.L:
          return (value(model.l[j]),value(model.u[j]))
model.x = Var(model.N,bounds=x_bound_rule,initialize=0.0)

def obj_rule(model):
    return 3 * model.x[1] + 1e-6 * model.x[1]**3 + 2 * model.x[2] + .522074e-6 * model.x[2]**3
model.obj = Objective(rule=obj_rule,sense=minimize)

def cons1_rule(model):
    return model.x[4] - model.x[3] + .55 >= 0
model.C1 = Constraint(rule=cons1_rule)
def cons2_rule(model):
    return model.x[3] - model.x[4] + .55 >= 0
model.C2 = Constraint(rule=cons2_rule)
def cons3_rule(model):
    return 2250000 - model.x[1]**2 - model.x[8]**2 >= 0
model.C3 = Constraint(rule=cons3_rule)
def cons4_rule(model):
    return 2250000 - model.x[2]**2 - model.x[9]**2 >= 0
model.C4 = Constraint(rule=cons4_rule)
def cons5_rule(model):
    return model.x[5] * model.x[6] * sin(-model.x[3] - .25) + model.x[5] * model.x[7] * sin(-model.x[4] - .25) + 2 * b * model.x[5]**2 - a * model.x[1] + 400 * a == 0
model.C5 = Constraint(rule=cons5_rule)
def cons6_rule(model):
    return model.x[5] * model.x[6] * sin(model.x[3] - .25) + model.x[6] * model.x[7] * sin(model.x[3] - model.x[4] - .25) + 2 * b * model.x[6]**2 - a * model.x[2] + 400 * a == 0
model.C6 = Constraint(rule=cons6_rule)
def cons7_rule(model):
    return model.x[5] * model.x[7] * sin(model.x[4] - .25) + model.x[6] * model.x[7] * sin(model.x[4] - model.x[3] - .25) + 2 * b * model.x[7]**2 + 881.779 * a == 0
model.C7 = Constraint(rule=cons7_rule)
def cons8_rule(model):
    return a * model.x[8] + model.x[5] * model.x[6] * cos(-model.x[3] - .25) + model.x[5] * model.x[7] * cos(-model.x[4] - .25) - 200 * a - 2 * c * model.x[5]**2 + .7533e-3 * a * model.x[5]**2 == 0
model.C8 = Constraint(rule=cons8_rule)
def cons9_rule(model):
    return a * model.x[9] + model.x[5] * model.x[6] * cos(model.x[3] - .25) + model.x[6] * model.x[7] * cos(model.x[3] - model.x[4] - .25) - 2 * c * model.x[6]**2 + .7533e-3 * a * model.x[6]**2 - 200 * a == 0
model.C9 = Constraint(rule=cons9_rule)
def cons10_rule(model):
    return model.x[5] * model.x[7] * cos(model.x[4] - .25) + model.x[6] * model.x[7] * cos(model.x[4] - model.x[3] - .25) - 2 * c * model.x[7]**2 + 22.938 * a + .7533e-3 * a * model.x[7] **2 == 0
model.C10= Constraint(rule=cons10_rule)

def cons11_rule(model,i):
    return model. x[i] >= 0
#model.C11 = Constraint([1,2], rule=cons11_rule)

def cons12_rule(model,i):
    return  -.55 <= model.x[i] <= .55
#model.C12 = Constraint([3,4], rule=cons12_rule)

def cons13_rule(model,i):
    return 196 <= model.x[i] <= 252
#model.C13 = Constraint([5,6,7], rule=cons13_rule)

def cons14_rule(model,i):
    return -400 <= model.x[i] <= 800
#model.C14 = Constraint([8,9], rule=cons14_rule)
