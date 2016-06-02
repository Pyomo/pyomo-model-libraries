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

#   classification QLR2-AN-V-V

from pyomo.core import *
model = ConcreteModel()

model.nx = 10
model.ny = 10

model.x = Var(RangeSet(1,model.nx),RangeSet(0,model.ny+1))
model.y = Var(RangeSet(0,model.nx+1),RangeSet(1,model.ny))

model.snx = RangeSet(2,model.nx-1)
model.sny = RangeSet(2,model.ny-1)

def f_rule(model):
    return (sum((model.x[i,j]-1)**2 for i in range(1,model.nx) for j in range(1,model.ny))+\
            sum((model.y[i,j]-1)**2 for i in range(1,model.nx) for j in range(1,model.ny))+\
            sum((model.x[i,model.ny]-1)**2 for i in range(1,model.nx))+\
            sum((model.y[model.nx,j]-1)**2 for j in range(1,model.ny)))/2.0
model.f = Objective(rule=f_rule)

def v1(model,i,j):
    return ((model.x[i,j]-model.x[i-1,j])+(model.y[i,j]-model.y[i,j-1])-1)==0
model.v1 = Constraint(model.snx,model.sny,rule=v1)

def v2(model,i):
    return (model.x[i,0]+(model.x[i,1]-model.x[i-1,1])+model.y[i,1]-1)==0
model.v2 = Constraint(model.snx,rule=v2)

def v3(model,i):
    return model.x[i,model.ny+1]+(model.x[i,model.ny]-model.x[i-1,model.ny])-model.y[i,model.ny-1]-1==0
model.v3 = Constraint(model.snx,rule=v3)

def v4(model,j):
    return model.y[0,j]+(model.y[1,j]-model.y[1,j-1])+model.x[1,j]-1==0
model.v4 = Constraint(model.sny,rule=v4)

def v5(model,j):
    return model.y[model.nx+1,j]+(model.y[model.nx,j]-model.y[model.nx,j-1])-model.x[model.nx-1,j]-1==0
model.v5 = Constraint(model.sny,rule=v5)
