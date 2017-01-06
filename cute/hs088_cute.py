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
#  Formulated in Pyomo by Logan Barnes and Gabe Hackebeil.
#
#  Taken from CUTE models

from pyomo.environ import *
model = AbstractModel()
n = 2
model.N = RangeSet(1,30)
model.M = RangeSet(1,n)
model.mu= Param(model.N)

def A_rule(model,j):
    return 2.0*sin(model.mu[j])/(model.mu[j] + sin(model.mu[j])*cos(model.mu[j]))
model.A = Param(model.N,initialize=A_rule)

def x_init_rule(model,i):
    return 0.5 * (-1)**(i+1)
model.x = Var(model.M,initialize=x_init_rule)

def rho(model,j):
    return  -(exp(-model.mu[j]**2 * sum(model.x[i]**2 for i in model.M))\
        + sum(2.0*(-1)**(ii-1)*exp(-model.mu[j]**2 * sum(model.x[i]**2 for i in range(ii,n+1))) for ii in range(2,n+1))\
        + (-1.0)**n)/model.mu[j]**2

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return sum(model.x[i]**2 for i in model.M)
model.obj = Objective(rule=obj_rule,sense=minimize)

def cons1_rule(model):
    return sum(model.mu[i]**2 * model.mu[j]**2 * model.A[i] * model.A[j] * rho(model,i) * rho(model,j)\
           *(sin(model.mu[i]+model.mu[j])/(model.mu[i]+model.mu[j])+sin(model.mu[i]-model.mu[j])/(model.mu[i]-model.mu[j]))\
           for i in model.N for j in range(i+1,30+1))\
           + sum(model.mu[j]**4 * model.A[j]**2 * rho(model,j)**2 * ((sin(2.0*model.mu[j])/(2.0*model.mu[j]) + 1.0)/2.0)\
           for j in model.N)\
           -sum(model.mu[j]**2 * model.A[j] * rho(model,j) * (2.0*sin(model.mu[j])/(model.mu[j]**3)\
           - 2.0*cos(model.mu[j])/(model.mu[j]**2))\
           for j in model.N) <= -2.0/15.0 + 0.0001
model.constr1 = Constraint(rule=cons1_rule)

