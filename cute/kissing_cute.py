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

#   Source: This problem is associated to the family of Hard-Spheres 
#   problem. It belongs to the family of sphere packing problems, a 
#   class of challenging problems dating from the beginning of the 
#   17th century which is related to practical problems in Chemistry, 
#   Biology and Physics. It consists on maximizing the minimum pairwise 
#   distance between NP points on a sphere in \R^{MDIM}. 
#   This problem may be reduced to a nonconvex nonlinear optimization 
#   problem with a potentially large number of (nonoptimal) points 
#   satisfying optimality conditions. We have, thus, a class of problems 
#   indexed by the parameters MDIM and NP, that provides a suitable 
#   set of test problems for evaluating nonlinear programming codes.
#   After some algebric manipulations, we can formulate this problem as
#
#                            Minimize z
#
#                            subject to
#       
#      z \geq <x_i, x_j> for all different pair of indices i, j
#      
#                            ||x_i||^2 = 1    for all i = 1,...,NP
#
#     The goal is to find an objective value less than 0.5 (This means
#     that the NP points stored belong to the sphere and every distance
#     between two of them is greater than 1.0).
#
#     Obs: the starting point is aleatorally chosen although each 
#     variable belongs to [-1.,1.].
#
#     References:
#     [1] "Validation of an Augmented Lagrangian algorithm with a 
#          Gauss-Newton Hessian approximation using a set of 
#          Hard-Spheres problems", N. Krejic, J. M. Martinez, M. Mello 
#          and E. A. Pilotta, Tech. Report RP 29/98, IMECC-UNICAMP, 
#          Campinas, 1998.
#     [2] "Inexact-Restoration Algorithm for Constrained Optimization",
#          J. M. Martinez and E. A. Pilotta, Tech. Report, IMECC-UNICAMP, 
#          Campinas, 1998.
#     [3]  "Sphere Packings, Lattices and Groups", J. H. Conway and 
#           N. J. C. Sloane, Springer-Verlag, NY, 1988.
#
#
#     SIF input: September 29, 1998
#        Jose Mario Martinez
#                Elvio Angel Pilotta
#

#   classification LQR2-RN-V-V

from pyomo.environ import *
model = AbstractModel()
np   = 42
mdim = 3
model.N = RangeSet(1,np)
model.M = RangeSet(1,mdim)

def cons1_index_init(model):
    return [(i,j) for i in range(1,np) for j in range(i+1,np+1)]
model.cons1_index = Set(dimen=2,initialize=cons1_index_init)

model.x_init = Param(model.N,model.M, mutable=True)

def x_init_rule(model,i,j):
    if i <= 12:
        return model.x_init[i,j]
    else:
        return 0.0
model.x = Var(model.N,model.M,initialize=x_init_rule)
model.z = Var()

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def f_rule(model):
    return model.z
model.f = Objective(rule=f_rule)

def cons1_rule(model,i,j):
    return sum(model.x[i,k]*model.x[j,k] for k in model.M) - model.z <= 0.0
model.cons1 = Constraint(model.cons1_index,rule=cons1_rule)

def cons2_rule(model,i):
    return sum(model.x[i,k]**2 for k in model.M) == 1.0
model.cons2 = Constraint(model.N,rule=cons2_rule)
