#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2025
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

# pack-rig2p.py LQR2-MN-v-v
# Original Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer, University of Dundee
#
# An MPEC from Outrata, Kocvara & Zowe, Nonsmooth Approach to
# Optimization Problems with Equilibrium Constraints, Kluwer, 1998.
#
# A packaging problem (see Section 9.2, Example 9.1):
# Minimize membrane surface under the condition that 
# the membrane comes into contact with a rigid obstacle. 
#
# Formulation with penalty on state constraints
#
# A 2D obstacle problem on [0,1] x [0,1].
#
# Several discretizations are available (see pack-rig-i.dat, 
# i=8,16,32).
#
# Formulation uses FE discretization with similar data
# structure as provided by triangulization routines.

import pyomo.environ
from pyomo.core import *
from pyomo.mpec import *


model = AbstractModel()

# ... discretization parameters (change for finer grid)
model.n = Param(within=Integers)    # n = 8, 16, 32, 64
model.h = Param(initialize=1/model.n)     # discretization size
def r_(model):
    if model.n == 8:
        return 1.6e4
    if model.n == 16:
        return 3e5
    if model.n == 32:
        return 5e5
    if model.n == 64:
        return 1e6
    return 0
model.r = Param(initialize=r_)

# ... parameters
model.Nnd = Param(initialize=(model.n+1)*(model.n+1))   # Number of nodes

# ... sets of nodes / classes of nodes
model.nodes = RangeSet(1, model.Nnd)                                    # set of nodes
model.bnd_nodes = Set(within=model.nodes)                               # set of boundary nodes
model.int_nodes = model.nodes - model.bnd_nodes                         # set of internal nodes
model.fix_nodes = Set(within=model.nodes)                               # set of fixed node positions
model.elements = Set(within=model.nodes * model.nodes * model.nodes)    # set of elements

# ... Omega0 = region, where membrane is fixed to obstacle
model.Omega0 = Set(within=model.int_nodes)

# ... node positions on i-j grid of indices
model.i_ref = Param(model.nodes, within=Integers) #bounds=(0, model.n)
model.j_ref = Param(model.nodes, within=Integers) #bounds=(0, model.n)

# ... node positions (y fixed)
def y_(model, i):
    return model.j_ref[i]*model.h
model.y = Param(model.nodes, initialize=y_)

# ... boundary conditions
model.u0 = Param(model.bnd_nodes)

# ... parameterization of "moving" boundary (alpha)
model.a_index = RangeSet(0, model.n)
model.a = Var(model.a_index, bounds=(0.6, 1.0), initialize=1.0)

# ... node positions (x depends on a and w1, w2)
def x_(model, i):
    return model.i_ref[i]*model.h if i in model.fix_nodes \
                     else 0.5+(model.i_ref[i]-model.n/2)*(2*model.a[model.j_ref[i]]-1)/model.n
model.x = Expression(model.nodes, rule=x_)

# ... determinant of Je transformation for element stiffness matrix
def detJe_(model, i, j, k):
    return (model.x[j]-model.x[i])*(model.y[k]-model.y[i]) - (model.y[j]-model.y[i])*(model.x[k]-model.x[i])
model.detJe = Expression(model.elements, rule=detJe_)

# ... obstacle 
def xi_(model, i):
    return - 0.05 * (model.x[i]**2 + (model.y[i]-0.25)**2)
model.xi = Expression(model.nodes, rule=xi_)

# ... unknown height of membrane
model.u = Var(model.nodes)

# ... slack variables to deal with complementarity
model.s1 = Var(model.int_nodes, within=NonNegativeReals)

# ... global load vector (load is f(x,y) = -1.0 constant)
def l_(model, i):
    return  - sum(detJe[i,j,k] for (i,j,k) in model.elements)/6.0 \
            - sum(detJe[j,i,k] for (j,i,k) in model.elements)/6.0 \
            - sum(detJe[k,j,i] for (k,j,i) in model.elements)/6.0
model.l = Expression(model.int_nodes, rule=l_)

# ... set up PDE equation at all internal nodes here
def Au_(model, i):
    return \
    sum(
      (  ( (model.y[k]-model.y[i])**2 + (model.x[k]-model.x[i])**2 + (model.x[j]-model.x[i])**2 
          - 2*(model.x[k]-model.x[i])*(model.x[j]-model.x[i])                                                        ) * model.u[i]
       + (-(model.y[k]-model.y[i])**2 - (model.x[k]-model.x[i])**2 + (model.x[k]-model.x[i])*(model.x[j]-model.x[i]) ) * model.u[j]
       + (-(model.x[j]-model.x[i])**2 + (model.x[k]-model.x[i])*(model.x[j]-model.x[i])                              ) * model.u[k]
      ) / ( 2*model.detJe[i,j,k] ) for (i,j,k) in model.elements)

    + sum(
      (  ( (model.y[k]-model.y[j])**2 + (model.x[k]-model.x[j])**2                                                   ) * model.u[i]
       + (-(model.y[k]-model.y[j])**2 - (model.x[k]-model.x[j])**2 + (model.x[k]-model.x[j])*(model.x[i]-model.x[j]) ) * model.u[j]
       + (-(model.x[k]-model.x[j])*(model.x[i]-model.x[j])                                                           ) * model.u[k]
      ) / ( 2*model.detJe[j,i,k] ) for (j,i,k) in model.elements)

    + sum(
      (  ( (model.x[j]-model.x[k])**2                                                    ) * model.u[i]
       + (-(model.x[i]-model.x[k])*(model.x[j]-model.x[k])                               ) * model.u[j]
       + (-(model.x[j]-model.x[k])**2 + (model.x[i]-model.x[k])*(model.x[j]-model.x[k])  ) * model.u[k]
      ) / ( 2*model.detJe[k,j,i] ) for (k,j,i) in model.elements)
model.Au = Expression(model.int_nodes, rule=Au_)

def area_(model):
    return model.h/2 * sum(model.a[i] + model.a[i-1] for i in sequence(model.n)) + model.r*model.h**2 * sum(model.u[i] - model.xi[i] for i in model.Omega0)
model.area = Objective(rule=area_)

# ... boundary conditions
def bnd_cond_(model, i):
    return model.u[i] == model.u0[i]
model.bnd_cond = Constraint(model.bnd_nodes, rule=bnd_cond_)

# ... constraint on slope of "moving" boundary
def slope_(model, i):
    return -3*model.h <= model.a[i-1] - model.a[i] <= 3*model.h
model.slope = Constraint(RangeSet(1,model.n), rule=slope_)

# ... FE approx to Laplacian
def PDE_(model, i):
    return model.s1[i] == model.Au[i] - model.l[i]
model.PDE = Constraint(model.int_nodes, rule=PDE_)

# ... obstacle lower bound
def obst_(model, i):
    return complements(0 <= model.s1[i], model.u[i] - model.xi[i] >= 0)
model.obst = Complementarity(model.int_nodes, rule=obst_)

