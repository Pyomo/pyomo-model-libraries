#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil
# Taken from:

#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   An expanded system formulation of a 3-D PDE system.
#   A nine-point discretization of Laplace's equation in a 
#   rectangular domain may be expressed in the form 
#         - M v = b, 
#   where M = sum a_i a_i^T. Letting A = (a_1 .... a_m), 
#   this system may be expanded as
#          ( I   A^T ) (x) = (0),
#          ( A    0  ) (v)   (b)
#   which is then equivalentto solving the EQP 
#   minimize 1/2 || x ||_2^2   s.t.    A x = b
#   SIF input: Nick Gould, February 1994
#   classification QLR2-AN-V-V
#   Number of nodes in x direction
#IE NX                  3
#   Number of nodes in y direction
#IE NY                  3
#   Number of nodes in z direction
#IE NZ                  3
#   Other useful parameters
#  It is easier to describe this problem by columns.
# objective function
# constraints
# objective function terms
# constraints : central constraints
from pyomo.core import *
model = ConcreteModel()

model.nx = Param(initialize=10.0)
model.ny = Param(initialize=10.0)
model.nz = Param(initialize=10.0)
model.xp = Param(initialize=1.0 + (10.0))
model.xm = Param(initialize=-1.0 + (10.0))
model.yp = Param(initialize=1.0 + (10.0))
model.ym = Param(initialize=-1.0 + (10.0))
model.zp = Param(initialize=1.0 + (10.0))
model.zm = Param(initialize=-1.0 + (10.0))
model.m = Param(initialize=10.0)
model.n = Param(initialize=10.0)
model.p = Param(initialize=10.0)
model.kp = Param(initialize=1.0 + (9.0))
model.jp = Param(initialize=1.0 + (9.0))
model.ip = Param(initialize=1.0 + (9.0))

model.x1_1_1 = Var()
model.y1_1_1 = Var()
model.z1_1_1 = Var()
model.x2_1_1 = Var()
model.y2_1_1 = Var()
model.z2_1_1 = Var()
model.x3_1_1 = Var()
model.y3_1_1 = Var()
model.z3_1_1 = Var()
model.x4_1_1 = Var()
model.y4_1_1 = Var()
model.z4_1_1 = Var()
model.x5_1_1 = Var()
model.y5_1_1 = Var()
model.z5_1_1 = Var()
model.x6_1_1 = Var()
model.y6_1_1 = Var()
model.z6_1_1 = Var()
model.x7_1_1 = Var()
model.y7_1_1 = Var()
model.z7_1_1 = Var()
model.x8_1_1 = Var()
model.y8_1_1 = Var()
model.z8_1_1 = Var()
model.x9_1_1 = Var()
model.y9_1_1 = Var()
model.z9_1_1 = Var()
model.x1_2_1 = Var()
model.y1_2_1 = Var()
model.z1_2_1 = Var()
model.x2_2_1 = Var()
model.y2_2_1 = Var()
model.z2_2_1 = Var()
model.x3_2_1 = Var()
model.y3_2_1 = Var()
model.z3_2_1 = Var()
model.x4_2_1 = Var()
model.y4_2_1 = Var()
model.z4_2_1 = Var()
model.x5_2_1 = Var()
model.y5_2_1 = Var()
model.z5_2_1 = Var()
model.x6_2_1 = Var()
model.y6_2_1 = Var()
model.z6_2_1 = Var()
model.x7_2_1 = Var()
model.y7_2_1 = Var()
model.z7_2_1 = Var()
model.x8_2_1 = Var()
model.y8_2_1 = Var()
model.z8_2_1 = Var()
model.x9_2_1 = Var()
model.y9_2_1 = Var()
model.z9_2_1 = Var()
model.x1_3_1 = Var()
model.y1_3_1 = Var()
model.z1_3_1 = Var()
model.x2_3_1 = Var()
model.y2_3_1 = Var()
model.z2_3_1 = Var()
model.x3_3_1 = Var()
model.y3_3_1 = Var()
model.z3_3_1 = Var()
model.x4_3_1 = Var()
model.y4_3_1 = Var()
model.z4_3_1 = Var()
model.x5_3_1 = Var()
model.y5_3_1 = Var()
model.z5_3_1 = Var()
model.x6_3_1 = Var()
model.y6_3_1 = Var()
model.z6_3_1 = Var()
model.x7_3_1 = Var()
model.y7_3_1 = Var()
model.z7_3_1 = Var()
model.x8_3_1 = Var()
model.y8_3_1 = Var()
model.z8_3_1 = Var()
model.x9_3_1 = Var()
model.y9_3_1 = Var()
model.z9_3_1 = Var()
model.x1_4_1 = Var()
model.y1_4_1 = Var()
model.z1_4_1 = Var()
model.x2_4_1 = Var()
model.y2_4_1 = Var()
model.z2_4_1 = Var()
model.x3_4_1 = Var()
model.y3_4_1 = Var()
model.z3_4_1 = Var()
model.x4_4_1 = Var()
model.y4_4_1 = Var()
model.z4_4_1 = Var()
model.x5_4_1 = Var()
model.y5_4_1 = Var()
model.z5_4_1 = Var()
model.x6_4_1 = Var()
model.y6_4_1 = Var()
model.z6_4_1 = Var()
model.x7_4_1 = Var()
model.y7_4_1 = Var()
model.z7_4_1 = Var()
model.x8_4_1 = Var()
model.y8_4_1 = Var()
model.z8_4_1 = Var()
model.x9_4_1 = Var()
model.y9_4_1 = Var()
model.z9_4_1 = Var()
model.x1_5_1 = Var()
model.y1_5_1 = Var()
model.z1_5_1 = Var()
model.x2_5_1 = Var()
model.y2_5_1 = Var()
model.z2_5_1 = Var()
model.x3_5_1 = Var()
model.y3_5_1 = Var()
model.z3_5_1 = Var()
model.x4_5_1 = Var()
model.y4_5_1 = Var()
model.z4_5_1 = Var()
model.x5_5_1 = Var()
model.y5_5_1 = Var()
model.z5_5_1 = Var()
model.x6_5_1 = Var()
model.y6_5_1 = Var()
model.z6_5_1 = Var()
model.x7_5_1 = Var()
model.y7_5_1 = Var()
model.z7_5_1 = Var()
model.x8_5_1 = Var()
model.y8_5_1 = Var()
model.z8_5_1 = Var()
model.x9_5_1 = Var()
model.y9_5_1 = Var()
model.z9_5_1 = Var()
model.x1_6_1 = Var()
model.y1_6_1 = Var()
model.z1_6_1 = Var()
model.x2_6_1 = Var()
model.y2_6_1 = Var()
model.z2_6_1 = Var()
model.x3_6_1 = Var()
model.y3_6_1 = Var()
model.z3_6_1 = Var()
model.x4_6_1 = Var()
model.y4_6_1 = Var()
model.z4_6_1 = Var()
model.x5_6_1 = Var()
model.y5_6_1 = Var()
model.z5_6_1 = Var()
model.x6_6_1 = Var()
model.y6_6_1 = Var()
model.z6_6_1 = Var()
model.x7_6_1 = Var()
model.y7_6_1 = Var()
model.z7_6_1 = Var()
model.x8_6_1 = Var()
model.y8_6_1 = Var()
model.z8_6_1 = Var()
model.x9_6_1 = Var()
model.y9_6_1 = Var()
model.z9_6_1 = Var()
model.x1_7_1 = Var()
model.y1_7_1 = Var()
model.z1_7_1 = Var()
model.x2_7_1 = Var()
model.y2_7_1 = Var()
model.z2_7_1 = Var()
model.x3_7_1 = Var()
model.y3_7_1 = Var()
model.z3_7_1 = Var()
model.x4_7_1 = Var()
model.y4_7_1 = Var()
model.z4_7_1 = Var()
model.x5_7_1 = Var()
model.y5_7_1 = Var()
model.z5_7_1 = Var()
model.x6_7_1 = Var()
model.y6_7_1 = Var()
model.z6_7_1 = Var()
model.x7_7_1 = Var()
model.y7_7_1 = Var()
model.z7_7_1 = Var()
model.x8_7_1 = Var()
model.y8_7_1 = Var()
model.z8_7_1 = Var()
model.x9_7_1 = Var()
model.y9_7_1 = Var()
model.z9_7_1 = Var()
model.x1_8_1 = Var()
model.y1_8_1 = Var()
model.z1_8_1 = Var()
model.x2_8_1 = Var()
model.y2_8_1 = Var()
model.z2_8_1 = Var()
model.x3_8_1 = Var()
model.y3_8_1 = Var()
model.z3_8_1 = Var()
model.x4_8_1 = Var()
model.y4_8_1 = Var()
model.z4_8_1 = Var()
model.x5_8_1 = Var()
model.y5_8_1 = Var()
model.z5_8_1 = Var()
model.x6_8_1 = Var()
model.y6_8_1 = Var()
model.z6_8_1 = Var()
model.x7_8_1 = Var()
model.y7_8_1 = Var()
model.z7_8_1 = Var()
model.x8_8_1 = Var()
model.y8_8_1 = Var()
model.z8_8_1 = Var()
model.x9_8_1 = Var()
model.y9_8_1 = Var()
model.z9_8_1 = Var()
model.x1_9_1 = Var()
model.y1_9_1 = Var()
model.z1_9_1 = Var()
model.x2_9_1 = Var()
model.y2_9_1 = Var()
model.z2_9_1 = Var()
model.x3_9_1 = Var()
model.y3_9_1 = Var()
model.z3_9_1 = Var()
model.x4_9_1 = Var()
model.y4_9_1 = Var()
model.z4_9_1 = Var()
model.x5_9_1 = Var()
model.y5_9_1 = Var()
model.z5_9_1 = Var()
model.x6_9_1 = Var()
model.y6_9_1 = Var()
model.z6_9_1 = Var()
model.x7_9_1 = Var()
model.y7_9_1 = Var()
model.z7_9_1 = Var()
model.x8_9_1 = Var()
model.y8_9_1 = Var()
model.z8_9_1 = Var()
model.x9_9_1 = Var()
model.y9_9_1 = Var()
model.z9_9_1 = Var()
model.x1_1_2 = Var()
model.y1_1_2 = Var()
model.z1_1_2 = Var()
model.x2_1_2 = Var()
model.y2_1_2 = Var()
model.z2_1_2 = Var()
model.x3_1_2 = Var()
model.y3_1_2 = Var()
model.z3_1_2 = Var()
model.x4_1_2 = Var()
model.y4_1_2 = Var()
model.z4_1_2 = Var()
model.x5_1_2 = Var()
model.y5_1_2 = Var()
model.z5_1_2 = Var()
model.x6_1_2 = Var()
model.y6_1_2 = Var()
model.z6_1_2 = Var()
model.x7_1_2 = Var()
model.y7_1_2 = Var()
model.z7_1_2 = Var()
model.x8_1_2 = Var()
model.y8_1_2 = Var()
model.z8_1_2 = Var()
model.x9_1_2 = Var()
model.y9_1_2 = Var()
model.z9_1_2 = Var()
model.x1_2_2 = Var()
model.y1_2_2 = Var()
model.z1_2_2 = Var()
model.x2_2_2 = Var()
model.y2_2_2 = Var()
model.z2_2_2 = Var()
model.x3_2_2 = Var()
model.y3_2_2 = Var()
model.z3_2_2 = Var()
model.x4_2_2 = Var()
model.y4_2_2 = Var()
model.z4_2_2 = Var()
model.x5_2_2 = Var()
model.y5_2_2 = Var()
model.z5_2_2 = Var()
model.x6_2_2 = Var()
model.y6_2_2 = Var()
model.z6_2_2 = Var()
model.x7_2_2 = Var()
model.y7_2_2 = Var()
model.z7_2_2 = Var()
model.x8_2_2 = Var()
model.y8_2_2 = Var()
model.z8_2_2 = Var()
model.x9_2_2 = Var()
model.y9_2_2 = Var()
model.z9_2_2 = Var()
model.x1_3_2 = Var()
model.y1_3_2 = Var()
model.z1_3_2 = Var()
model.x2_3_2 = Var()
model.y2_3_2 = Var()
model.z2_3_2 = Var()
model.x3_3_2 = Var()
model.y3_3_2 = Var()
model.z3_3_2 = Var()
model.x4_3_2 = Var()
model.y4_3_2 = Var()
model.z4_3_2 = Var()
model.x5_3_2 = Var()
model.y5_3_2 = Var()
model.z5_3_2 = Var()
model.x6_3_2 = Var()
model.y6_3_2 = Var()
model.z6_3_2 = Var()
model.x7_3_2 = Var()
model.y7_3_2 = Var()
model.z7_3_2 = Var()
model.x8_3_2 = Var()
model.y8_3_2 = Var()
model.z8_3_2 = Var()
model.x9_3_2 = Var()
model.y9_3_2 = Var()
model.z9_3_2 = Var()
model.x1_4_2 = Var()
model.y1_4_2 = Var()
model.z1_4_2 = Var()
model.x2_4_2 = Var()
model.y2_4_2 = Var()
model.z2_4_2 = Var()
model.x3_4_2 = Var()
model.y3_4_2 = Var()
model.z3_4_2 = Var()
model.x4_4_2 = Var()
model.y4_4_2 = Var()
model.z4_4_2 = Var()
model.x5_4_2 = Var()
model.y5_4_2 = Var()
model.z5_4_2 = Var()
model.x6_4_2 = Var()
model.y6_4_2 = Var()
model.z6_4_2 = Var()
model.x7_4_2 = Var()
model.y7_4_2 = Var()
model.z7_4_2 = Var()
model.x8_4_2 = Var()
model.y8_4_2 = Var()
model.z8_4_2 = Var()
model.x9_4_2 = Var()
model.y9_4_2 = Var()
model.z9_4_2 = Var()
model.x1_5_2 = Var()
model.y1_5_2 = Var()
model.z1_5_2 = Var()
model.x2_5_2 = Var()
model.y2_5_2 = Var()
model.z2_5_2 = Var()
model.x3_5_2 = Var()
model.y3_5_2 = Var()
model.z3_5_2 = Var()
model.x4_5_2 = Var()
model.y4_5_2 = Var()
model.z4_5_2 = Var()
model.x5_5_2 = Var()
model.y5_5_2 = Var()
model.z5_5_2 = Var()
model.x6_5_2 = Var()
model.y6_5_2 = Var()
model.z6_5_2 = Var()
model.x7_5_2 = Var()
model.y7_5_2 = Var()
model.z7_5_2 = Var()
model.x8_5_2 = Var()
model.y8_5_2 = Var()
model.z8_5_2 = Var()
model.x9_5_2 = Var()
model.y9_5_2 = Var()
model.z9_5_2 = Var()
model.x1_6_2 = Var()
model.y1_6_2 = Var()
model.z1_6_2 = Var()
model.x2_6_2 = Var()
model.y2_6_2 = Var()
model.z2_6_2 = Var()
model.x3_6_2 = Var()
model.y3_6_2 = Var()
model.z3_6_2 = Var()
model.x4_6_2 = Var()
model.y4_6_2 = Var()
model.z4_6_2 = Var()
model.x5_6_2 = Var()
model.y5_6_2 = Var()
model.z5_6_2 = Var()
model.x6_6_2 = Var()
model.y6_6_2 = Var()
model.z6_6_2 = Var()
model.x7_6_2 = Var()
model.y7_6_2 = Var()
model.z7_6_2 = Var()
model.x8_6_2 = Var()
model.y8_6_2 = Var()
model.z8_6_2 = Var()
model.x9_6_2 = Var()
model.y9_6_2 = Var()
model.z9_6_2 = Var()
model.x1_7_2 = Var()
model.y1_7_2 = Var()
model.z1_7_2 = Var()
model.x2_7_2 = Var()
model.y2_7_2 = Var()
model.z2_7_2 = Var()
model.x3_7_2 = Var()
model.y3_7_2 = Var()
model.z3_7_2 = Var()
model.x4_7_2 = Var()
model.y4_7_2 = Var()
model.z4_7_2 = Var()
model.x5_7_2 = Var()
model.y5_7_2 = Var()
model.z5_7_2 = Var()
model.x6_7_2 = Var()
model.y6_7_2 = Var()
model.z6_7_2 = Var()
model.x7_7_2 = Var()
model.y7_7_2 = Var()
model.z7_7_2 = Var()
model.x8_7_2 = Var()
model.y8_7_2 = Var()
model.z8_7_2 = Var()
model.x9_7_2 = Var()
model.y9_7_2 = Var()
model.z9_7_2 = Var()
model.x1_8_2 = Var()
model.y1_8_2 = Var()
model.z1_8_2 = Var()
model.x2_8_2 = Var()
model.y2_8_2 = Var()
model.z2_8_2 = Var()
model.x3_8_2 = Var()
model.y3_8_2 = Var()
model.z3_8_2 = Var()
model.x4_8_2 = Var()
model.y4_8_2 = Var()
model.z4_8_2 = Var()
model.x5_8_2 = Var()
model.y5_8_2 = Var()
model.z5_8_2 = Var()
model.x6_8_2 = Var()
model.y6_8_2 = Var()
model.z6_8_2 = Var()
model.x7_8_2 = Var()
model.y7_8_2 = Var()
model.z7_8_2 = Var()
model.x8_8_2 = Var()
model.y8_8_2 = Var()
model.z8_8_2 = Var()
model.x9_8_2 = Var()
model.y9_8_2 = Var()
model.z9_8_2 = Var()
model.x1_9_2 = Var()
model.y1_9_2 = Var()
model.z1_9_2 = Var()
model.x2_9_2 = Var()
model.y2_9_2 = Var()
model.z2_9_2 = Var()
model.x3_9_2 = Var()
model.y3_9_2 = Var()
model.z3_9_2 = Var()
model.x4_9_2 = Var()
model.y4_9_2 = Var()
model.z4_9_2 = Var()
model.x5_9_2 = Var()
model.y5_9_2 = Var()
model.z5_9_2 = Var()
model.x6_9_2 = Var()
model.y6_9_2 = Var()
model.z6_9_2 = Var()
model.x7_9_2 = Var()
model.y7_9_2 = Var()
model.z7_9_2 = Var()
model.x8_9_2 = Var()
model.y8_9_2 = Var()
model.z8_9_2 = Var()
model.x9_9_2 = Var()
model.y9_9_2 = Var()
model.z9_9_2 = Var()
model.x1_1_3 = Var()
model.y1_1_3 = Var()
model.z1_1_3 = Var()
model.x2_1_3 = Var()
model.y2_1_3 = Var()
model.z2_1_3 = Var()
model.x3_1_3 = Var()
model.y3_1_3 = Var()
model.z3_1_3 = Var()
model.x4_1_3 = Var()
model.y4_1_3 = Var()
model.z4_1_3 = Var()
model.x5_1_3 = Var()
model.y5_1_3 = Var()
model.z5_1_3 = Var()
model.x6_1_3 = Var()
model.y6_1_3 = Var()
model.z6_1_3 = Var()
model.x7_1_3 = Var()
model.y7_1_3 = Var()
model.z7_1_3 = Var()
model.x8_1_3 = Var()
model.y8_1_3 = Var()
model.z8_1_3 = Var()
model.x9_1_3 = Var()
model.y9_1_3 = Var()
model.z9_1_3 = Var()
model.x1_2_3 = Var()
model.y1_2_3 = Var()
model.z1_2_3 = Var()
model.x2_2_3 = Var()
model.y2_2_3 = Var()
model.z2_2_3 = Var()
model.x3_2_3 = Var()
model.y3_2_3 = Var()
model.z3_2_3 = Var()
model.x4_2_3 = Var()
model.y4_2_3 = Var()
model.z4_2_3 = Var()
model.x5_2_3 = Var()
model.y5_2_3 = Var()
model.z5_2_3 = Var()
model.x6_2_3 = Var()
model.y6_2_3 = Var()
model.z6_2_3 = Var()
model.x7_2_3 = Var()
model.y7_2_3 = Var()
model.z7_2_3 = Var()
model.x8_2_3 = Var()
model.y8_2_3 = Var()
model.z8_2_3 = Var()
model.x9_2_3 = Var()
model.y9_2_3 = Var()
model.z9_2_3 = Var()
model.x1_3_3 = Var()
model.y1_3_3 = Var()
model.z1_3_3 = Var()
model.x2_3_3 = Var()
model.y2_3_3 = Var()
model.z2_3_3 = Var()
model.x3_3_3 = Var()
model.y3_3_3 = Var()
model.z3_3_3 = Var()
model.x4_3_3 = Var()
model.y4_3_3 = Var()
model.z4_3_3 = Var()
model.x5_3_3 = Var()
model.y5_3_3 = Var()
model.z5_3_3 = Var()
model.x6_3_3 = Var()
model.y6_3_3 = Var()
model.z6_3_3 = Var()
model.x7_3_3 = Var()
model.y7_3_3 = Var()
model.z7_3_3 = Var()
model.x8_3_3 = Var()
model.y8_3_3 = Var()
model.z8_3_3 = Var()
model.x9_3_3 = Var()
model.y9_3_3 = Var()
model.z9_3_3 = Var()
model.x1_4_3 = Var()
model.y1_4_3 = Var()
model.z1_4_3 = Var()
model.x2_4_3 = Var()
model.y2_4_3 = Var()
model.z2_4_3 = Var()
model.x3_4_3 = Var()
model.y3_4_3 = Var()
model.z3_4_3 = Var()
model.x4_4_3 = Var()
model.y4_4_3 = Var()
model.z4_4_3 = Var()
model.x5_4_3 = Var()
model.y5_4_3 = Var()
model.z5_4_3 = Var()
model.x6_4_3 = Var()
model.y6_4_3 = Var()
model.z6_4_3 = Var()
model.x7_4_3 = Var()
model.y7_4_3 = Var()
model.z7_4_3 = Var()
model.x8_4_3 = Var()
model.y8_4_3 = Var()
model.z8_4_3 = Var()
model.x9_4_3 = Var()
model.y9_4_3 = Var()
model.z9_4_3 = Var()
model.x1_5_3 = Var()
model.y1_5_3 = Var()
model.z1_5_3 = Var()
model.x2_5_3 = Var()
model.y2_5_3 = Var()
model.z2_5_3 = Var()
model.x3_5_3 = Var()
model.y3_5_3 = Var()
model.z3_5_3 = Var()
model.x4_5_3 = Var()
model.y4_5_3 = Var()
model.z4_5_3 = Var()
model.x5_5_3 = Var()
model.y5_5_3 = Var()
model.z5_5_3 = Var()
model.x6_5_3 = Var()
model.y6_5_3 = Var()
model.z6_5_3 = Var()
model.x7_5_3 = Var()
model.y7_5_3 = Var()
model.z7_5_3 = Var()
model.x8_5_3 = Var()
model.y8_5_3 = Var()
model.z8_5_3 = Var()
model.x9_5_3 = Var()
model.y9_5_3 = Var()
model.z9_5_3 = Var()
model.x1_6_3 = Var()
model.y1_6_3 = Var()
model.z1_6_3 = Var()
model.x2_6_3 = Var()
model.y2_6_3 = Var()
model.z2_6_3 = Var()
model.x3_6_3 = Var()
model.y3_6_3 = Var()
model.z3_6_3 = Var()
model.x4_6_3 = Var()
model.y4_6_3 = Var()
model.z4_6_3 = Var()
model.x5_6_3 = Var()
model.y5_6_3 = Var()
model.z5_6_3 = Var()
model.x6_6_3 = Var()
model.y6_6_3 = Var()
model.z6_6_3 = Var()
model.x7_6_3 = Var()
model.y7_6_3 = Var()
model.z7_6_3 = Var()
model.x8_6_3 = Var()
model.y8_6_3 = Var()
model.z8_6_3 = Var()
model.x9_6_3 = Var()
model.y9_6_3 = Var()
model.z9_6_3 = Var()
model.x1_7_3 = Var()
model.y1_7_3 = Var()
model.z1_7_3 = Var()
model.x2_7_3 = Var()
model.y2_7_3 = Var()
model.z2_7_3 = Var()
model.x3_7_3 = Var()
model.y3_7_3 = Var()
model.z3_7_3 = Var()
model.x4_7_3 = Var()
model.y4_7_3 = Var()
model.z4_7_3 = Var()
model.x5_7_3 = Var()
model.y5_7_3 = Var()
model.z5_7_3 = Var()
model.x6_7_3 = Var()
model.y6_7_3 = Var()
model.z6_7_3 = Var()
model.x7_7_3 = Var()
model.y7_7_3 = Var()
model.z7_7_3 = Var()
model.x8_7_3 = Var()
model.y8_7_3 = Var()
model.z8_7_3 = Var()
model.x9_7_3 = Var()
model.y9_7_3 = Var()
model.z9_7_3 = Var()
model.x1_8_3 = Var()
model.y1_8_3 = Var()
model.z1_8_3 = Var()
model.x2_8_3 = Var()
model.y2_8_3 = Var()
model.z2_8_3 = Var()
model.x3_8_3 = Var()
model.y3_8_3 = Var()
model.z3_8_3 = Var()
model.x4_8_3 = Var()
model.y4_8_3 = Var()
model.z4_8_3 = Var()
model.x5_8_3 = Var()
model.y5_8_3 = Var()
model.z5_8_3 = Var()
model.x6_8_3 = Var()
model.y6_8_3 = Var()
model.z6_8_3 = Var()
model.x7_8_3 = Var()
model.y7_8_3 = Var()
model.z7_8_3 = Var()
model.x8_8_3 = Var()
model.y8_8_3 = Var()
model.z8_8_3 = Var()
model.x9_8_3 = Var()
model.y9_8_3 = Var()
model.z9_8_3 = Var()
model.x1_9_3 = Var()
model.y1_9_3 = Var()
model.z1_9_3 = Var()
model.x2_9_3 = Var()
model.y2_9_3 = Var()
model.z2_9_3 = Var()
model.x3_9_3 = Var()
model.y3_9_3 = Var()
model.z3_9_3 = Var()
model.x4_9_3 = Var()
model.y4_9_3 = Var()
model.z4_9_3 = Var()
model.x5_9_3 = Var()
model.y5_9_3 = Var()
model.z5_9_3 = Var()
model.x6_9_3 = Var()
model.y6_9_3 = Var()
model.z6_9_3 = Var()
model.x7_9_3 = Var()
model.y7_9_3 = Var()
model.z7_9_3 = Var()
model.x8_9_3 = Var()
model.y8_9_3 = Var()
model.z8_9_3 = Var()
model.x9_9_3 = Var()
model.y9_9_3 = Var()
model.z9_9_3 = Var()
model.x1_1_4 = Var()
model.y1_1_4 = Var()
model.z1_1_4 = Var()
model.x2_1_4 = Var()
model.y2_1_4 = Var()
model.z2_1_4 = Var()
model.x3_1_4 = Var()
model.y3_1_4 = Var()
model.z3_1_4 = Var()
model.x4_1_4 = Var()
model.y4_1_4 = Var()
model.z4_1_4 = Var()
model.x5_1_4 = Var()
model.y5_1_4 = Var()
model.z5_1_4 = Var()
model.x6_1_4 = Var()
model.y6_1_4 = Var()
model.z6_1_4 = Var()
model.x7_1_4 = Var()
model.y7_1_4 = Var()
model.z7_1_4 = Var()
model.x8_1_4 = Var()
model.y8_1_4 = Var()
model.z8_1_4 = Var()
model.x9_1_4 = Var()
model.y9_1_4 = Var()
model.z9_1_4 = Var()
model.x1_2_4 = Var()
model.y1_2_4 = Var()
model.z1_2_4 = Var()
model.x2_2_4 = Var()
model.y2_2_4 = Var()
model.z2_2_4 = Var()
model.x3_2_4 = Var()
model.y3_2_4 = Var()
model.z3_2_4 = Var()
model.x4_2_4 = Var()
model.y4_2_4 = Var()
model.z4_2_4 = Var()
model.x5_2_4 = Var()
model.y5_2_4 = Var()
model.z5_2_4 = Var()
model.x6_2_4 = Var()
model.y6_2_4 = Var()
model.z6_2_4 = Var()
model.x7_2_4 = Var()
model.y7_2_4 = Var()
model.z7_2_4 = Var()
model.x8_2_4 = Var()
model.y8_2_4 = Var()
model.z8_2_4 = Var()
model.x9_2_4 = Var()
model.y9_2_4 = Var()
model.z9_2_4 = Var()
model.x1_3_4 = Var()
model.y1_3_4 = Var()
model.z1_3_4 = Var()
model.x2_3_4 = Var()
model.y2_3_4 = Var()
model.z2_3_4 = Var()
model.x3_3_4 = Var()
model.y3_3_4 = Var()
model.z3_3_4 = Var()
model.x4_3_4 = Var()
model.y4_3_4 = Var()
model.z4_3_4 = Var()
model.x5_3_4 = Var()
model.y5_3_4 = Var()
model.z5_3_4 = Var()
model.x6_3_4 = Var()
model.y6_3_4 = Var()
model.z6_3_4 = Var()
model.x7_3_4 = Var()
model.y7_3_4 = Var()
model.z7_3_4 = Var()
model.x8_3_4 = Var()
model.y8_3_4 = Var()
model.z8_3_4 = Var()
model.x9_3_4 = Var()
model.y9_3_4 = Var()
model.z9_3_4 = Var()
model.x1_4_4 = Var()
model.y1_4_4 = Var()
model.z1_4_4 = Var()
model.x2_4_4 = Var()
model.y2_4_4 = Var()
model.z2_4_4 = Var()
model.x3_4_4 = Var()
model.y3_4_4 = Var()
model.z3_4_4 = Var()
model.x4_4_4 = Var()
model.y4_4_4 = Var()
model.z4_4_4 = Var()
model.x5_4_4 = Var()
model.y5_4_4 = Var()
model.z5_4_4 = Var()
model.x6_4_4 = Var()
model.y6_4_4 = Var()
model.z6_4_4 = Var()
model.x7_4_4 = Var()
model.y7_4_4 = Var()
model.z7_4_4 = Var()
model.x8_4_4 = Var()
model.y8_4_4 = Var()
model.z8_4_4 = Var()
model.x9_4_4 = Var()
model.y9_4_4 = Var()
model.z9_4_4 = Var()
model.x1_5_4 = Var()
model.y1_5_4 = Var()
model.z1_5_4 = Var()
model.x2_5_4 = Var()
model.y2_5_4 = Var()
model.z2_5_4 = Var()
model.x3_5_4 = Var()
model.y3_5_4 = Var()
model.z3_5_4 = Var()
model.x4_5_4 = Var()
model.y4_5_4 = Var()
model.z4_5_4 = Var()
model.x5_5_4 = Var()
model.y5_5_4 = Var()
model.z5_5_4 = Var()
model.x6_5_4 = Var()
model.y6_5_4 = Var()
model.z6_5_4 = Var()
model.x7_5_4 = Var()
model.y7_5_4 = Var()
model.z7_5_4 = Var()
model.x8_5_4 = Var()
model.y8_5_4 = Var()
model.z8_5_4 = Var()
model.x9_5_4 = Var()
model.y9_5_4 = Var()
model.z9_5_4 = Var()
model.x1_6_4 = Var()
model.y1_6_4 = Var()
model.z1_6_4 = Var()
model.x2_6_4 = Var()
model.y2_6_4 = Var()
model.z2_6_4 = Var()
model.x3_6_4 = Var()
model.y3_6_4 = Var()
model.z3_6_4 = Var()
model.x4_6_4 = Var()
model.y4_6_4 = Var()
model.z4_6_4 = Var()
model.x5_6_4 = Var()
model.y5_6_4 = Var()
model.z5_6_4 = Var()
model.x6_6_4 = Var()
model.y6_6_4 = Var()
model.z6_6_4 = Var()
model.x7_6_4 = Var()
model.y7_6_4 = Var()
model.z7_6_4 = Var()
model.x8_6_4 = Var()
model.y8_6_4 = Var()
model.z8_6_4 = Var()
model.x9_6_4 = Var()
model.y9_6_4 = Var()
model.z9_6_4 = Var()
model.x1_7_4 = Var()
model.y1_7_4 = Var()
model.z1_7_4 = Var()
model.x2_7_4 = Var()
model.y2_7_4 = Var()
model.z2_7_4 = Var()
model.x3_7_4 = Var()
model.y3_7_4 = Var()
model.z3_7_4 = Var()
model.x4_7_4 = Var()
model.y4_7_4 = Var()
model.z4_7_4 = Var()
model.x5_7_4 = Var()
model.y5_7_4 = Var()
model.z5_7_4 = Var()
model.x6_7_4 = Var()
model.y6_7_4 = Var()
model.z6_7_4 = Var()
model.x7_7_4 = Var()
model.y7_7_4 = Var()
model.z7_7_4 = Var()
model.x8_7_4 = Var()
model.y8_7_4 = Var()
model.z8_7_4 = Var()
model.x9_7_4 = Var()
model.y9_7_4 = Var()
model.z9_7_4 = Var()
model.x1_8_4 = Var()
model.y1_8_4 = Var()
model.z1_8_4 = Var()
model.x2_8_4 = Var()
model.y2_8_4 = Var()
model.z2_8_4 = Var()
model.x3_8_4 = Var()
model.y3_8_4 = Var()
model.z3_8_4 = Var()
model.x4_8_4 = Var()
model.y4_8_4 = Var()
model.z4_8_4 = Var()
model.x5_8_4 = Var()
model.y5_8_4 = Var()
model.z5_8_4 = Var()
model.x6_8_4 = Var()
model.y6_8_4 = Var()
model.z6_8_4 = Var()
model.x7_8_4 = Var()
model.y7_8_4 = Var()
model.z7_8_4 = Var()
model.x8_8_4 = Var()
model.y8_8_4 = Var()
model.z8_8_4 = Var()
model.x9_8_4 = Var()
model.y9_8_4 = Var()
model.z9_8_4 = Var()
model.x1_9_4 = Var()
model.y1_9_4 = Var()
model.z1_9_4 = Var()
model.x2_9_4 = Var()
model.y2_9_4 = Var()
model.z2_9_4 = Var()
model.x3_9_4 = Var()
model.y3_9_4 = Var()
model.z3_9_4 = Var()
model.x4_9_4 = Var()
model.y4_9_4 = Var()
model.z4_9_4 = Var()
model.x5_9_4 = Var()
model.y5_9_4 = Var()
model.z5_9_4 = Var()
model.x6_9_4 = Var()
model.y6_9_4 = Var()
model.z6_9_4 = Var()
model.x7_9_4 = Var()
model.y7_9_4 = Var()
model.z7_9_4 = Var()
model.x8_9_4 = Var()
model.y8_9_4 = Var()
model.z8_9_4 = Var()
model.x9_9_4 = Var()
model.y9_9_4 = Var()
model.z9_9_4 = Var()
model.x1_1_5 = Var()
model.y1_1_5 = Var()
model.z1_1_5 = Var()
model.x2_1_5 = Var()
model.y2_1_5 = Var()
model.z2_1_5 = Var()
model.x3_1_5 = Var()
model.y3_1_5 = Var()
model.z3_1_5 = Var()
model.x4_1_5 = Var()
model.y4_1_5 = Var()
model.z4_1_5 = Var()
model.x5_1_5 = Var()
model.y5_1_5 = Var()
model.z5_1_5 = Var()
model.x6_1_5 = Var()
model.y6_1_5 = Var()
model.z6_1_5 = Var()
model.x7_1_5 = Var()
model.y7_1_5 = Var()
model.z7_1_5 = Var()
model.x8_1_5 = Var()
model.y8_1_5 = Var()
model.z8_1_5 = Var()
model.x9_1_5 = Var()
model.y9_1_5 = Var()
model.z9_1_5 = Var()
model.x1_2_5 = Var()
model.y1_2_5 = Var()
model.z1_2_5 = Var()
model.x2_2_5 = Var()
model.y2_2_5 = Var()
model.z2_2_5 = Var()
model.x3_2_5 = Var()
model.y3_2_5 = Var()
model.z3_2_5 = Var()
model.x4_2_5 = Var()
model.y4_2_5 = Var()
model.z4_2_5 = Var()
model.x5_2_5 = Var()
model.y5_2_5 = Var()
model.z5_2_5 = Var()
model.x6_2_5 = Var()
model.y6_2_5 = Var()
model.z6_2_5 = Var()
model.x7_2_5 = Var()
model.y7_2_5 = Var()
model.z7_2_5 = Var()
model.x8_2_5 = Var()
model.y8_2_5 = Var()
model.z8_2_5 = Var()
model.x9_2_5 = Var()
model.y9_2_5 = Var()
model.z9_2_5 = Var()
model.x1_3_5 = Var()
model.y1_3_5 = Var()
model.z1_3_5 = Var()
model.x2_3_5 = Var()
model.y2_3_5 = Var()
model.z2_3_5 = Var()
model.x3_3_5 = Var()
model.y3_3_5 = Var()
model.z3_3_5 = Var()
model.x4_3_5 = Var()
model.y4_3_5 = Var()
model.z4_3_5 = Var()
model.x5_3_5 = Var()
model.y5_3_5 = Var()
model.z5_3_5 = Var()
model.x6_3_5 = Var()
model.y6_3_5 = Var()
model.z6_3_5 = Var()
model.x7_3_5 = Var()
model.y7_3_5 = Var()
model.z7_3_5 = Var()
model.x8_3_5 = Var()
model.y8_3_5 = Var()
model.z8_3_5 = Var()
model.x9_3_5 = Var()
model.y9_3_5 = Var()
model.z9_3_5 = Var()
model.x1_4_5 = Var()
model.y1_4_5 = Var()
model.z1_4_5 = Var()
model.x2_4_5 = Var()
model.y2_4_5 = Var()
model.z2_4_5 = Var()
model.x3_4_5 = Var()
model.y3_4_5 = Var()
model.z3_4_5 = Var()
model.x4_4_5 = Var()
model.y4_4_5 = Var()
model.z4_4_5 = Var()
model.x5_4_5 = Var()
model.y5_4_5 = Var()
model.z5_4_5 = Var()
model.x6_4_5 = Var()
model.y6_4_5 = Var()
model.z6_4_5 = Var()
model.x7_4_5 = Var()
model.y7_4_5 = Var()
model.z7_4_5 = Var()
model.x8_4_5 = Var()
model.y8_4_5 = Var()
model.z8_4_5 = Var()
model.x9_4_5 = Var()
model.y9_4_5 = Var()
model.z9_4_5 = Var()
model.x1_5_5 = Var()
model.y1_5_5 = Var()
model.z1_5_5 = Var()
model.x2_5_5 = Var()
model.y2_5_5 = Var()
model.z2_5_5 = Var()
model.x3_5_5 = Var()
model.y3_5_5 = Var()
model.z3_5_5 = Var()
model.x4_5_5 = Var()
model.y4_5_5 = Var()
model.z4_5_5 = Var()
model.x5_5_5 = Var()
model.y5_5_5 = Var()
model.z5_5_5 = Var()
model.x6_5_5 = Var()
model.y6_5_5 = Var()
model.z6_5_5 = Var()
model.x7_5_5 = Var()
model.y7_5_5 = Var()
model.z7_5_5 = Var()
model.x8_5_5 = Var()
model.y8_5_5 = Var()
model.z8_5_5 = Var()
model.x9_5_5 = Var()
model.y9_5_5 = Var()
model.z9_5_5 = Var()
model.x1_6_5 = Var()
model.y1_6_5 = Var()
model.z1_6_5 = Var()
model.x2_6_5 = Var()
model.y2_6_5 = Var()
model.z2_6_5 = Var()
model.x3_6_5 = Var()
model.y3_6_5 = Var()
model.z3_6_5 = Var()
model.x4_6_5 = Var()
model.y4_6_5 = Var()
model.z4_6_5 = Var()
model.x5_6_5 = Var()
model.y5_6_5 = Var()
model.z5_6_5 = Var()
model.x6_6_5 = Var()
model.y6_6_5 = Var()
model.z6_6_5 = Var()
model.x7_6_5 = Var()
model.y7_6_5 = Var()
model.z7_6_5 = Var()
model.x8_6_5 = Var()
model.y8_6_5 = Var()
model.z8_6_5 = Var()
model.x9_6_5 = Var()
model.y9_6_5 = Var()
model.z9_6_5 = Var()
model.x1_7_5 = Var()
model.y1_7_5 = Var()
model.z1_7_5 = Var()
model.x2_7_5 = Var()
model.y2_7_5 = Var()
model.z2_7_5 = Var()
model.x3_7_5 = Var()
model.y3_7_5 = Var()
model.z3_7_5 = Var()
model.x4_7_5 = Var()
model.y4_7_5 = Var()
model.z4_7_5 = Var()
model.x5_7_5 = Var()
model.y5_7_5 = Var()
model.z5_7_5 = Var()
model.x6_7_5 = Var()
model.y6_7_5 = Var()
model.z6_7_5 = Var()
model.x7_7_5 = Var()
model.y7_7_5 = Var()
model.z7_7_5 = Var()
model.x8_7_5 = Var()
model.y8_7_5 = Var()
model.z8_7_5 = Var()
model.x9_7_5 = Var()
model.y9_7_5 = Var()
model.z9_7_5 = Var()
model.x1_8_5 = Var()
model.y1_8_5 = Var()
model.z1_8_5 = Var()
model.x2_8_5 = Var()
model.y2_8_5 = Var()
model.z2_8_5 = Var()
model.x3_8_5 = Var()
model.y3_8_5 = Var()
model.z3_8_5 = Var()
model.x4_8_5 = Var()
model.y4_8_5 = Var()
model.z4_8_5 = Var()
model.x5_8_5 = Var()
model.y5_8_5 = Var()
model.z5_8_5 = Var()
model.x6_8_5 = Var()
model.y6_8_5 = Var()
model.z6_8_5 = Var()
model.x7_8_5 = Var()
model.y7_8_5 = Var()
model.z7_8_5 = Var()
model.x8_8_5 = Var()
model.y8_8_5 = Var()
model.z8_8_5 = Var()
model.x9_8_5 = Var()
model.y9_8_5 = Var()
model.z9_8_5 = Var()
model.x1_9_5 = Var()
model.y1_9_5 = Var()
model.z1_9_5 = Var()
model.x2_9_5 = Var()
model.y2_9_5 = Var()
model.z2_9_5 = Var()
model.x3_9_5 = Var()
model.y3_9_5 = Var()
model.z3_9_5 = Var()
model.x4_9_5 = Var()
model.y4_9_5 = Var()
model.z4_9_5 = Var()
model.x5_9_5 = Var()
model.y5_9_5 = Var()
model.z5_9_5 = Var()
model.x6_9_5 = Var()
model.y6_9_5 = Var()
model.z6_9_5 = Var()
model.x7_9_5 = Var()
model.y7_9_5 = Var()
model.z7_9_5 = Var()
model.x8_9_5 = Var()
model.y8_9_5 = Var()
model.z8_9_5 = Var()
model.x9_9_5 = Var()
model.y9_9_5 = Var()
model.z9_9_5 = Var()
model.x1_1_6 = Var()
model.y1_1_6 = Var()
model.z1_1_6 = Var()
model.x2_1_6 = Var()
model.y2_1_6 = Var()
model.z2_1_6 = Var()
model.x3_1_6 = Var()
model.y3_1_6 = Var()
model.z3_1_6 = Var()
model.x4_1_6 = Var()
model.y4_1_6 = Var()
model.z4_1_6 = Var()
model.x5_1_6 = Var()
model.y5_1_6 = Var()
model.z5_1_6 = Var()
model.x6_1_6 = Var()
model.y6_1_6 = Var()
model.z6_1_6 = Var()
model.x7_1_6 = Var()
model.y7_1_6 = Var()
model.z7_1_6 = Var()
model.x8_1_6 = Var()
model.y8_1_6 = Var()
model.z8_1_6 = Var()
model.x9_1_6 = Var()
model.y9_1_6 = Var()
model.z9_1_6 = Var()
model.x1_2_6 = Var()
model.y1_2_6 = Var()
model.z1_2_6 = Var()
model.x2_2_6 = Var()
model.y2_2_6 = Var()
model.z2_2_6 = Var()
model.x3_2_6 = Var()
model.y3_2_6 = Var()
model.z3_2_6 = Var()
model.x4_2_6 = Var()
model.y4_2_6 = Var()
model.z4_2_6 = Var()
model.x5_2_6 = Var()
model.y5_2_6 = Var()
model.z5_2_6 = Var()
model.x6_2_6 = Var()
model.y6_2_6 = Var()
model.z6_2_6 = Var()
model.x7_2_6 = Var()
model.y7_2_6 = Var()
model.z7_2_6 = Var()
model.x8_2_6 = Var()
model.y8_2_6 = Var()
model.z8_2_6 = Var()
model.x9_2_6 = Var()
model.y9_2_6 = Var()
model.z9_2_6 = Var()
model.x1_3_6 = Var()
model.y1_3_6 = Var()
model.z1_3_6 = Var()
model.x2_3_6 = Var()
model.y2_3_6 = Var()
model.z2_3_6 = Var()
model.x3_3_6 = Var()
model.y3_3_6 = Var()
model.z3_3_6 = Var()
model.x4_3_6 = Var()
model.y4_3_6 = Var()
model.z4_3_6 = Var()
model.x5_3_6 = Var()
model.y5_3_6 = Var()
model.z5_3_6 = Var()
model.x6_3_6 = Var()
model.y6_3_6 = Var()
model.z6_3_6 = Var()
model.x7_3_6 = Var()
model.y7_3_6 = Var()
model.z7_3_6 = Var()
model.x8_3_6 = Var()
model.y8_3_6 = Var()
model.z8_3_6 = Var()
model.x9_3_6 = Var()
model.y9_3_6 = Var()
model.z9_3_6 = Var()
model.x1_4_6 = Var()
model.y1_4_6 = Var()
model.z1_4_6 = Var()
model.x2_4_6 = Var()
model.y2_4_6 = Var()
model.z2_4_6 = Var()
model.x3_4_6 = Var()
model.y3_4_6 = Var()
model.z3_4_6 = Var()
model.x4_4_6 = Var()
model.y4_4_6 = Var()
model.z4_4_6 = Var()
model.x5_4_6 = Var()
model.y5_4_6 = Var()
model.z5_4_6 = Var()
model.x6_4_6 = Var()
model.y6_4_6 = Var()
model.z6_4_6 = Var()
model.x7_4_6 = Var()
model.y7_4_6 = Var()
model.z7_4_6 = Var()
model.x8_4_6 = Var()
model.y8_4_6 = Var()
model.z8_4_6 = Var()
model.x9_4_6 = Var()
model.y9_4_6 = Var()
model.z9_4_6 = Var()
model.x1_5_6 = Var()
model.y1_5_6 = Var()
model.z1_5_6 = Var()
model.x2_5_6 = Var()
model.y2_5_6 = Var()
model.z2_5_6 = Var()
model.x3_5_6 = Var()
model.y3_5_6 = Var()
model.z3_5_6 = Var()
model.x4_5_6 = Var()
model.y4_5_6 = Var()
model.z4_5_6 = Var()
model.x5_5_6 = Var()
model.y5_5_6 = Var()
model.z5_5_6 = Var()
model.x6_5_6 = Var()
model.y6_5_6 = Var()
model.z6_5_6 = Var()
model.x7_5_6 = Var()
model.y7_5_6 = Var()
model.z7_5_6 = Var()
model.x8_5_6 = Var()
model.y8_5_6 = Var()
model.z8_5_6 = Var()
model.x9_5_6 = Var()
model.y9_5_6 = Var()
model.z9_5_6 = Var()
model.x1_6_6 = Var()
model.y1_6_6 = Var()
model.z1_6_6 = Var()
model.x2_6_6 = Var()
model.y2_6_6 = Var()
model.z2_6_6 = Var()
model.x3_6_6 = Var()
model.y3_6_6 = Var()
model.z3_6_6 = Var()
model.x4_6_6 = Var()
model.y4_6_6 = Var()
model.z4_6_6 = Var()
model.x5_6_6 = Var()
model.y5_6_6 = Var()
model.z5_6_6 = Var()
model.x6_6_6 = Var()
model.y6_6_6 = Var()
model.z6_6_6 = Var()
model.x7_6_6 = Var()
model.y7_6_6 = Var()
model.z7_6_6 = Var()
model.x8_6_6 = Var()
model.y8_6_6 = Var()
model.z8_6_6 = Var()
model.x9_6_6 = Var()
model.y9_6_6 = Var()
model.z9_6_6 = Var()
model.x1_7_6 = Var()
model.y1_7_6 = Var()
model.z1_7_6 = Var()
model.x2_7_6 = Var()
model.y2_7_6 = Var()
model.z2_7_6 = Var()
model.x3_7_6 = Var()
model.y3_7_6 = Var()
model.z3_7_6 = Var()
model.x4_7_6 = Var()
model.y4_7_6 = Var()
model.z4_7_6 = Var()
model.x5_7_6 = Var()
model.y5_7_6 = Var()
model.z5_7_6 = Var()
model.x6_7_6 = Var()
model.y6_7_6 = Var()
model.z6_7_6 = Var()
model.x7_7_6 = Var()
model.y7_7_6 = Var()
model.z7_7_6 = Var()
model.x8_7_6 = Var()
model.y8_7_6 = Var()
model.z8_7_6 = Var()
model.x9_7_6 = Var()
model.y9_7_6 = Var()
model.z9_7_6 = Var()
model.x1_8_6 = Var()
model.y1_8_6 = Var()
model.z1_8_6 = Var()
model.x2_8_6 = Var()
model.y2_8_6 = Var()
model.z2_8_6 = Var()
model.x3_8_6 = Var()
model.y3_8_6 = Var()
model.z3_8_6 = Var()
model.x4_8_6 = Var()
model.y4_8_6 = Var()
model.z4_8_6 = Var()
model.x5_8_6 = Var()
model.y5_8_6 = Var()
model.z5_8_6 = Var()
model.x6_8_6 = Var()
model.y6_8_6 = Var()
model.z6_8_6 = Var()
model.x7_8_6 = Var()
model.y7_8_6 = Var()
model.z7_8_6 = Var()
model.x8_8_6 = Var()
model.y8_8_6 = Var()
model.z8_8_6 = Var()
model.x9_8_6 = Var()
model.y9_8_6 = Var()
model.z9_8_6 = Var()
model.x1_9_6 = Var()
model.y1_9_6 = Var()
model.z1_9_6 = Var()
model.x2_9_6 = Var()
model.y2_9_6 = Var()
model.z2_9_6 = Var()
model.x3_9_6 = Var()
model.y3_9_6 = Var()
model.z3_9_6 = Var()
model.x4_9_6 = Var()
model.y4_9_6 = Var()
model.z4_9_6 = Var()
model.x5_9_6 = Var()
model.y5_9_6 = Var()
model.z5_9_6 = Var()
model.x6_9_6 = Var()
model.y6_9_6 = Var()
model.z6_9_6 = Var()
model.x7_9_6 = Var()
model.y7_9_6 = Var()
model.z7_9_6 = Var()
model.x8_9_6 = Var()
model.y8_9_6 = Var()
model.z8_9_6 = Var()
model.x9_9_6 = Var()
model.y9_9_6 = Var()
model.z9_9_6 = Var()
model.x1_1_7 = Var()
model.y1_1_7 = Var()
model.z1_1_7 = Var()
model.x2_1_7 = Var()
model.y2_1_7 = Var()
model.z2_1_7 = Var()
model.x3_1_7 = Var()
model.y3_1_7 = Var()
model.z3_1_7 = Var()
model.x4_1_7 = Var()
model.y4_1_7 = Var()
model.z4_1_7 = Var()
model.x5_1_7 = Var()
model.y5_1_7 = Var()
model.z5_1_7 = Var()
model.x6_1_7 = Var()
model.y6_1_7 = Var()
model.z6_1_7 = Var()
model.x7_1_7 = Var()
model.y7_1_7 = Var()
model.z7_1_7 = Var()
model.x8_1_7 = Var()
model.y8_1_7 = Var()
model.z8_1_7 = Var()
model.x9_1_7 = Var()
model.y9_1_7 = Var()
model.z9_1_7 = Var()
model.x1_2_7 = Var()
model.y1_2_7 = Var()
model.z1_2_7 = Var()
model.x2_2_7 = Var()
model.y2_2_7 = Var()
model.z2_2_7 = Var()
model.x3_2_7 = Var()
model.y3_2_7 = Var()
model.z3_2_7 = Var()
model.x4_2_7 = Var()
model.y4_2_7 = Var()
model.z4_2_7 = Var()
model.x5_2_7 = Var()
model.y5_2_7 = Var()
model.z5_2_7 = Var()
model.x6_2_7 = Var()
model.y6_2_7 = Var()
model.z6_2_7 = Var()
model.x7_2_7 = Var()
model.y7_2_7 = Var()
model.z7_2_7 = Var()
model.x8_2_7 = Var()
model.y8_2_7 = Var()
model.z8_2_7 = Var()
model.x9_2_7 = Var()
model.y9_2_7 = Var()
model.z9_2_7 = Var()
model.x1_3_7 = Var()
model.y1_3_7 = Var()
model.z1_3_7 = Var()
model.x2_3_7 = Var()
model.y2_3_7 = Var()
model.z2_3_7 = Var()
model.x3_3_7 = Var()
model.y3_3_7 = Var()
model.z3_3_7 = Var()
model.x4_3_7 = Var()
model.y4_3_7 = Var()
model.z4_3_7 = Var()
model.x5_3_7 = Var()
model.y5_3_7 = Var()
model.z5_3_7 = Var()
model.x6_3_7 = Var()
model.y6_3_7 = Var()
model.z6_3_7 = Var()
model.x7_3_7 = Var()
model.y7_3_7 = Var()
model.z7_3_7 = Var()
model.x8_3_7 = Var()
model.y8_3_7 = Var()
model.z8_3_7 = Var()
model.x9_3_7 = Var()
model.y9_3_7 = Var()
model.z9_3_7 = Var()
model.x1_4_7 = Var()
model.y1_4_7 = Var()
model.z1_4_7 = Var()
model.x2_4_7 = Var()
model.y2_4_7 = Var()
model.z2_4_7 = Var()
model.x3_4_7 = Var()
model.y3_4_7 = Var()
model.z3_4_7 = Var()
model.x4_4_7 = Var()
model.y4_4_7 = Var()
model.z4_4_7 = Var()
model.x5_4_7 = Var()
model.y5_4_7 = Var()
model.z5_4_7 = Var()
model.x6_4_7 = Var()
model.y6_4_7 = Var()
model.z6_4_7 = Var()
model.x7_4_7 = Var()
model.y7_4_7 = Var()
model.z7_4_7 = Var()
model.x8_4_7 = Var()
model.y8_4_7 = Var()
model.z8_4_7 = Var()
model.x9_4_7 = Var()
model.y9_4_7 = Var()
model.z9_4_7 = Var()
model.x1_5_7 = Var()
model.y1_5_7 = Var()
model.z1_5_7 = Var()
model.x2_5_7 = Var()
model.y2_5_7 = Var()
model.z2_5_7 = Var()
model.x3_5_7 = Var()
model.y3_5_7 = Var()
model.z3_5_7 = Var()
model.x4_5_7 = Var()
model.y4_5_7 = Var()
model.z4_5_7 = Var()
model.x5_5_7 = Var()
model.y5_5_7 = Var()
model.z5_5_7 = Var()
model.x6_5_7 = Var()
model.y6_5_7 = Var()
model.z6_5_7 = Var()
model.x7_5_7 = Var()
model.y7_5_7 = Var()
model.z7_5_7 = Var()
model.x8_5_7 = Var()
model.y8_5_7 = Var()
model.z8_5_7 = Var()
model.x9_5_7 = Var()
model.y9_5_7 = Var()
model.z9_5_7 = Var()
model.x1_6_7 = Var()
model.y1_6_7 = Var()
model.z1_6_7 = Var()
model.x2_6_7 = Var()
model.y2_6_7 = Var()
model.z2_6_7 = Var()
model.x3_6_7 = Var()
model.y3_6_7 = Var()
model.z3_6_7 = Var()
model.x4_6_7 = Var()
model.y4_6_7 = Var()
model.z4_6_7 = Var()
model.x5_6_7 = Var()
model.y5_6_7 = Var()
model.z5_6_7 = Var()
model.x6_6_7 = Var()
model.y6_6_7 = Var()
model.z6_6_7 = Var()
model.x7_6_7 = Var()
model.y7_6_7 = Var()
model.z7_6_7 = Var()
model.x8_6_7 = Var()
model.y8_6_7 = Var()
model.z8_6_7 = Var()
model.x9_6_7 = Var()
model.y9_6_7 = Var()
model.z9_6_7 = Var()
model.x1_7_7 = Var()
model.y1_7_7 = Var()
model.z1_7_7 = Var()
model.x2_7_7 = Var()
model.y2_7_7 = Var()
model.z2_7_7 = Var()
model.x3_7_7 = Var()
model.y3_7_7 = Var()
model.z3_7_7 = Var()
model.x4_7_7 = Var()
model.y4_7_7 = Var()
model.z4_7_7 = Var()
model.x5_7_7 = Var()
model.y5_7_7 = Var()
model.z5_7_7 = Var()
model.x6_7_7 = Var()
model.y6_7_7 = Var()
model.z6_7_7 = Var()
model.x7_7_7 = Var()
model.y7_7_7 = Var()
model.z7_7_7 = Var()
model.x8_7_7 = Var()
model.y8_7_7 = Var()
model.z8_7_7 = Var()
model.x9_7_7 = Var()
model.y9_7_7 = Var()
model.z9_7_7 = Var()
model.x1_8_7 = Var()
model.y1_8_7 = Var()
model.z1_8_7 = Var()
model.x2_8_7 = Var()
model.y2_8_7 = Var()
model.z2_8_7 = Var()
model.x3_8_7 = Var()
model.y3_8_7 = Var()
model.z3_8_7 = Var()
model.x4_8_7 = Var()
model.y4_8_7 = Var()
model.z4_8_7 = Var()
model.x5_8_7 = Var()
model.y5_8_7 = Var()
model.z5_8_7 = Var()
model.x6_8_7 = Var()
model.y6_8_7 = Var()
model.z6_8_7 = Var()
model.x7_8_7 = Var()
model.y7_8_7 = Var()
model.z7_8_7 = Var()
model.x8_8_7 = Var()
model.y8_8_7 = Var()
model.z8_8_7 = Var()
model.x9_8_7 = Var()
model.y9_8_7 = Var()
model.z9_8_7 = Var()
model.x1_9_7 = Var()
model.y1_9_7 = Var()
model.z1_9_7 = Var()
model.x2_9_7 = Var()
model.y2_9_7 = Var()
model.z2_9_7 = Var()
model.x3_9_7 = Var()
model.y3_9_7 = Var()
model.z3_9_7 = Var()
model.x4_9_7 = Var()
model.y4_9_7 = Var()
model.z4_9_7 = Var()
model.x5_9_7 = Var()
model.y5_9_7 = Var()
model.z5_9_7 = Var()
model.x6_9_7 = Var()
model.y6_9_7 = Var()
model.z6_9_7 = Var()
model.x7_9_7 = Var()
model.y7_9_7 = Var()
model.z7_9_7 = Var()
model.x8_9_7 = Var()
model.y8_9_7 = Var()
model.z8_9_7 = Var()
model.x9_9_7 = Var()
model.y9_9_7 = Var()
model.z9_9_7 = Var()
model.x1_1_8 = Var()
model.y1_1_8 = Var()
model.z1_1_8 = Var()
model.x2_1_8 = Var()
model.y2_1_8 = Var()
model.z2_1_8 = Var()
model.x3_1_8 = Var()
model.y3_1_8 = Var()
model.z3_1_8 = Var()
model.x4_1_8 = Var()
model.y4_1_8 = Var()
model.z4_1_8 = Var()
model.x5_1_8 = Var()
model.y5_1_8 = Var()
model.z5_1_8 = Var()
model.x6_1_8 = Var()
model.y6_1_8 = Var()
model.z6_1_8 = Var()
model.x7_1_8 = Var()
model.y7_1_8 = Var()
model.z7_1_8 = Var()
model.x8_1_8 = Var()
model.y8_1_8 = Var()
model.z8_1_8 = Var()
model.x9_1_8 = Var()
model.y9_1_8 = Var()
model.z9_1_8 = Var()
model.x1_2_8 = Var()
model.y1_2_8 = Var()
model.z1_2_8 = Var()
model.x2_2_8 = Var()
model.y2_2_8 = Var()
model.z2_2_8 = Var()
model.x3_2_8 = Var()
model.y3_2_8 = Var()
model.z3_2_8 = Var()
model.x4_2_8 = Var()
model.y4_2_8 = Var()
model.z4_2_8 = Var()
model.x5_2_8 = Var()
model.y5_2_8 = Var()
model.z5_2_8 = Var()
model.x6_2_8 = Var()
model.y6_2_8 = Var()
model.z6_2_8 = Var()
model.x7_2_8 = Var()
model.y7_2_8 = Var()
model.z7_2_8 = Var()
model.x8_2_8 = Var()
model.y8_2_8 = Var()
model.z8_2_8 = Var()
model.x9_2_8 = Var()
model.y9_2_8 = Var()
model.z9_2_8 = Var()
model.x1_3_8 = Var()
model.y1_3_8 = Var()
model.z1_3_8 = Var()
model.x2_3_8 = Var()
model.y2_3_8 = Var()
model.z2_3_8 = Var()
model.x3_3_8 = Var()
model.y3_3_8 = Var()
model.z3_3_8 = Var()
model.x4_3_8 = Var()
model.y4_3_8 = Var()
model.z4_3_8 = Var()
model.x5_3_8 = Var()
model.y5_3_8 = Var()
model.z5_3_8 = Var()
model.x6_3_8 = Var()
model.y6_3_8 = Var()
model.z6_3_8 = Var()
model.x7_3_8 = Var()
model.y7_3_8 = Var()
model.z7_3_8 = Var()
model.x8_3_8 = Var()
model.y8_3_8 = Var()
model.z8_3_8 = Var()
model.x9_3_8 = Var()
model.y9_3_8 = Var()
model.z9_3_8 = Var()
model.x1_4_8 = Var()
model.y1_4_8 = Var()
model.z1_4_8 = Var()
model.x2_4_8 = Var()
model.y2_4_8 = Var()
model.z2_4_8 = Var()
model.x3_4_8 = Var()
model.y3_4_8 = Var()
model.z3_4_8 = Var()
model.x4_4_8 = Var()
model.y4_4_8 = Var()
model.z4_4_8 = Var()
model.x5_4_8 = Var()
model.y5_4_8 = Var()
model.z5_4_8 = Var()
model.x6_4_8 = Var()
model.y6_4_8 = Var()
model.z6_4_8 = Var()
model.x7_4_8 = Var()
model.y7_4_8 = Var()
model.z7_4_8 = Var()
model.x8_4_8 = Var()
model.y8_4_8 = Var()
model.z8_4_8 = Var()
model.x9_4_8 = Var()
model.y9_4_8 = Var()
model.z9_4_8 = Var()
model.x1_5_8 = Var()
model.y1_5_8 = Var()
model.z1_5_8 = Var()
model.x2_5_8 = Var()
model.y2_5_8 = Var()
model.z2_5_8 = Var()
model.x3_5_8 = Var()
model.y3_5_8 = Var()
model.z3_5_8 = Var()
model.x4_5_8 = Var()
model.y4_5_8 = Var()
model.z4_5_8 = Var()
model.x5_5_8 = Var()
model.y5_5_8 = Var()
model.z5_5_8 = Var()
model.x6_5_8 = Var()
model.y6_5_8 = Var()
model.z6_5_8 = Var()
model.x7_5_8 = Var()
model.y7_5_8 = Var()
model.z7_5_8 = Var()
model.x8_5_8 = Var()
model.y8_5_8 = Var()
model.z8_5_8 = Var()
model.x9_5_8 = Var()
model.y9_5_8 = Var()
model.z9_5_8 = Var()
model.x1_6_8 = Var()
model.y1_6_8 = Var()
model.z1_6_8 = Var()
model.x2_6_8 = Var()
model.y2_6_8 = Var()
model.z2_6_8 = Var()
model.x3_6_8 = Var()
model.y3_6_8 = Var()
model.z3_6_8 = Var()
model.x4_6_8 = Var()
model.y4_6_8 = Var()
model.z4_6_8 = Var()
model.x5_6_8 = Var()
model.y5_6_8 = Var()
model.z5_6_8 = Var()
model.x6_6_8 = Var()
model.y6_6_8 = Var()
model.z6_6_8 = Var()
model.x7_6_8 = Var()
model.y7_6_8 = Var()
model.z7_6_8 = Var()
model.x8_6_8 = Var()
model.y8_6_8 = Var()
model.z8_6_8 = Var()
model.x9_6_8 = Var()
model.y9_6_8 = Var()
model.z9_6_8 = Var()
model.x1_7_8 = Var()
model.y1_7_8 = Var()
model.z1_7_8 = Var()
model.x2_7_8 = Var()
model.y2_7_8 = Var()
model.z2_7_8 = Var()
model.x3_7_8 = Var()
model.y3_7_8 = Var()
model.z3_7_8 = Var()
model.x4_7_8 = Var()
model.y4_7_8 = Var()
model.z4_7_8 = Var()
model.x5_7_8 = Var()
model.y5_7_8 = Var()
model.z5_7_8 = Var()
model.x6_7_8 = Var()
model.y6_7_8 = Var()
model.z6_7_8 = Var()
model.x7_7_8 = Var()
model.y7_7_8 = Var()
model.z7_7_8 = Var()
model.x8_7_8 = Var()
model.y8_7_8 = Var()
model.z8_7_8 = Var()
model.x9_7_8 = Var()
model.y9_7_8 = Var()
model.z9_7_8 = Var()
model.x1_8_8 = Var()
model.y1_8_8 = Var()
model.z1_8_8 = Var()
model.x2_8_8 = Var()
model.y2_8_8 = Var()
model.z2_8_8 = Var()
model.x3_8_8 = Var()
model.y3_8_8 = Var()
model.z3_8_8 = Var()
model.x4_8_8 = Var()
model.y4_8_8 = Var()
model.z4_8_8 = Var()
model.x5_8_8 = Var()
model.y5_8_8 = Var()
model.z5_8_8 = Var()
model.x6_8_8 = Var()
model.y6_8_8 = Var()
model.z6_8_8 = Var()
model.x7_8_8 = Var()
model.y7_8_8 = Var()
model.z7_8_8 = Var()
model.x8_8_8 = Var()
model.y8_8_8 = Var()
model.z8_8_8 = Var()
model.x9_8_8 = Var()
model.y9_8_8 = Var()
model.z9_8_8 = Var()
model.x1_9_8 = Var()
model.y1_9_8 = Var()
model.z1_9_8 = Var()
model.x2_9_8 = Var()
model.y2_9_8 = Var()
model.z2_9_8 = Var()
model.x3_9_8 = Var()
model.y3_9_8 = Var()
model.z3_9_8 = Var()
model.x4_9_8 = Var()
model.y4_9_8 = Var()
model.z4_9_8 = Var()
model.x5_9_8 = Var()
model.y5_9_8 = Var()
model.z5_9_8 = Var()
model.x6_9_8 = Var()
model.y6_9_8 = Var()
model.z6_9_8 = Var()
model.x7_9_8 = Var()
model.y7_9_8 = Var()
model.z7_9_8 = Var()
model.x8_9_8 = Var()
model.y8_9_8 = Var()
model.z8_9_8 = Var()
model.x9_9_8 = Var()
model.y9_9_8 = Var()
model.z9_9_8 = Var()
model.x1_1_9 = Var()
model.y1_1_9 = Var()
model.z1_1_9 = Var()
model.x2_1_9 = Var()
model.y2_1_9 = Var()
model.z2_1_9 = Var()
model.x3_1_9 = Var()
model.y3_1_9 = Var()
model.z3_1_9 = Var()
model.x4_1_9 = Var()
model.y4_1_9 = Var()
model.z4_1_9 = Var()
model.x5_1_9 = Var()
model.y5_1_9 = Var()
model.z5_1_9 = Var()
model.x6_1_9 = Var()
model.y6_1_9 = Var()
model.z6_1_9 = Var()
model.x7_1_9 = Var()
model.y7_1_9 = Var()
model.z7_1_9 = Var()
model.x8_1_9 = Var()
model.y8_1_9 = Var()
model.z8_1_9 = Var()
model.x9_1_9 = Var()
model.y9_1_9 = Var()
model.z9_1_9 = Var()
model.x1_2_9 = Var()
model.y1_2_9 = Var()
model.z1_2_9 = Var()
model.x2_2_9 = Var()
model.y2_2_9 = Var()
model.z2_2_9 = Var()
model.x3_2_9 = Var()
model.y3_2_9 = Var()
model.z3_2_9 = Var()
model.x4_2_9 = Var()
model.y4_2_9 = Var()
model.z4_2_9 = Var()
model.x5_2_9 = Var()
model.y5_2_9 = Var()
model.z5_2_9 = Var()
model.x6_2_9 = Var()
model.y6_2_9 = Var()
model.z6_2_9 = Var()
model.x7_2_9 = Var()
model.y7_2_9 = Var()
model.z7_2_9 = Var()
model.x8_2_9 = Var()
model.y8_2_9 = Var()
model.z8_2_9 = Var()
model.x9_2_9 = Var()
model.y9_2_9 = Var()
model.z9_2_9 = Var()
model.x1_3_9 = Var()
model.y1_3_9 = Var()
model.z1_3_9 = Var()
model.x2_3_9 = Var()
model.y2_3_9 = Var()
model.z2_3_9 = Var()
model.x3_3_9 = Var()
model.y3_3_9 = Var()
model.z3_3_9 = Var()
model.x4_3_9 = Var()
model.y4_3_9 = Var()
model.z4_3_9 = Var()
model.x5_3_9 = Var()
model.y5_3_9 = Var()
model.z5_3_9 = Var()
model.x6_3_9 = Var()
model.y6_3_9 = Var()
model.z6_3_9 = Var()
model.x7_3_9 = Var()
model.y7_3_9 = Var()
model.z7_3_9 = Var()
model.x8_3_9 = Var()
model.y8_3_9 = Var()
model.z8_3_9 = Var()
model.x9_3_9 = Var()
model.y9_3_9 = Var()
model.z9_3_9 = Var()
model.x1_4_9 = Var()
model.y1_4_9 = Var()
model.z1_4_9 = Var()
model.x2_4_9 = Var()
model.y2_4_9 = Var()
model.z2_4_9 = Var()
model.x3_4_9 = Var()
model.y3_4_9 = Var()
model.z3_4_9 = Var()
model.x4_4_9 = Var()
model.y4_4_9 = Var()
model.z4_4_9 = Var()
model.x5_4_9 = Var()
model.y5_4_9 = Var()
model.z5_4_9 = Var()
model.x6_4_9 = Var()
model.y6_4_9 = Var()
model.z6_4_9 = Var()
model.x7_4_9 = Var()
model.y7_4_9 = Var()
model.z7_4_9 = Var()
model.x8_4_9 = Var()
model.y8_4_9 = Var()
model.z8_4_9 = Var()
model.x9_4_9 = Var()
model.y9_4_9 = Var()
model.z9_4_9 = Var()
model.x1_5_9 = Var()
model.y1_5_9 = Var()
model.z1_5_9 = Var()
model.x2_5_9 = Var()
model.y2_5_9 = Var()
model.z2_5_9 = Var()
model.x3_5_9 = Var()
model.y3_5_9 = Var()
model.z3_5_9 = Var()
model.x4_5_9 = Var()
model.y4_5_9 = Var()
model.z4_5_9 = Var()
model.x5_5_9 = Var()
model.y5_5_9 = Var()
model.z5_5_9 = Var()
model.x6_5_9 = Var()
model.y6_5_9 = Var()
model.z6_5_9 = Var()
model.x7_5_9 = Var()
model.y7_5_9 = Var()
model.z7_5_9 = Var()
model.x8_5_9 = Var()
model.y8_5_9 = Var()
model.z8_5_9 = Var()
model.x9_5_9 = Var()
model.y9_5_9 = Var()
model.z9_5_9 = Var()
model.x1_6_9 = Var()
model.y1_6_9 = Var()
model.z1_6_9 = Var()
model.x2_6_9 = Var()
model.y2_6_9 = Var()
model.z2_6_9 = Var()
model.x3_6_9 = Var()
model.y3_6_9 = Var()
model.z3_6_9 = Var()
model.x4_6_9 = Var()
model.y4_6_9 = Var()
model.z4_6_9 = Var()
model.x5_6_9 = Var()
model.y5_6_9 = Var()
model.z5_6_9 = Var()
model.x6_6_9 = Var()
model.y6_6_9 = Var()
model.z6_6_9 = Var()
model.x7_6_9 = Var()
model.y7_6_9 = Var()
model.z7_6_9 = Var()
model.x8_6_9 = Var()
model.y8_6_9 = Var()
model.z8_6_9 = Var()
model.x9_6_9 = Var()
model.y9_6_9 = Var()
model.z9_6_9 = Var()
model.x1_7_9 = Var()
model.y1_7_9 = Var()
model.z1_7_9 = Var()
model.x2_7_9 = Var()
model.y2_7_9 = Var()
model.z2_7_9 = Var()
model.x3_7_9 = Var()
model.y3_7_9 = Var()
model.z3_7_9 = Var()
model.x4_7_9 = Var()
model.y4_7_9 = Var()
model.z4_7_9 = Var()
model.x5_7_9 = Var()
model.y5_7_9 = Var()
model.z5_7_9 = Var()
model.x6_7_9 = Var()
model.y6_7_9 = Var()
model.z6_7_9 = Var()
model.x7_7_9 = Var()
model.y7_7_9 = Var()
model.z7_7_9 = Var()
model.x8_7_9 = Var()
model.y8_7_9 = Var()
model.z8_7_9 = Var()
model.x9_7_9 = Var()
model.y9_7_9 = Var()
model.z9_7_9 = Var()
model.x1_8_9 = Var()
model.y1_8_9 = Var()
model.z1_8_9 = Var()
model.x2_8_9 = Var()
model.y2_8_9 = Var()
model.z2_8_9 = Var()
model.x3_8_9 = Var()
model.y3_8_9 = Var()
model.z3_8_9 = Var()
model.x4_8_9 = Var()
model.y4_8_9 = Var()
model.z4_8_9 = Var()
model.x5_8_9 = Var()
model.y5_8_9 = Var()
model.z5_8_9 = Var()
model.x6_8_9 = Var()
model.y6_8_9 = Var()
model.z6_8_9 = Var()
model.x7_8_9 = Var()
model.y7_8_9 = Var()
model.z7_8_9 = Var()
model.x8_8_9 = Var()
model.y8_8_9 = Var()
model.z8_8_9 = Var()
model.x9_8_9 = Var()
model.y9_8_9 = Var()
model.z9_8_9 = Var()
model.x1_9_9 = Var()
model.y1_9_9 = Var()
model.z1_9_9 = Var()
model.x2_9_9 = Var()
model.y2_9_9 = Var()
model.z2_9_9 = Var()
model.x3_9_9 = Var()
model.y3_9_9 = Var()
model.z3_9_9 = Var()
model.x4_9_9 = Var()
model.y4_9_9 = Var()
model.z4_9_9 = Var()
model.x5_9_9 = Var()
model.y5_9_9 = Var()
model.z5_9_9 = Var()
model.x6_9_9 = Var()
model.y6_9_9 = Var()
model.z6_9_9 = Var()
model.x7_9_9 = Var()
model.y7_9_9 = Var()
model.z7_9_9 = Var()
model.x8_9_9 = Var()
model.y8_9_9 = Var()
model.z8_9_9 = Var()
model.x9_9_9 = Var()
model.y9_9_9 = Var()
model.z9_9_9 = Var()
model.y10_1_1 = Var()
model.z10_1_1 = Var()
model.y10_2_1 = Var()
model.z10_2_1 = Var()
model.y10_3_1 = Var()
model.z10_3_1 = Var()
model.y10_4_1 = Var()
model.z10_4_1 = Var()
model.y10_5_1 = Var()
model.z10_5_1 = Var()
model.y10_6_1 = Var()
model.z10_6_1 = Var()
model.y10_7_1 = Var()
model.z10_7_1 = Var()
model.y10_8_1 = Var()
model.z10_8_1 = Var()
model.y10_9_1 = Var()
model.z10_9_1 = Var()
model.y10_1_2 = Var()
model.z10_1_2 = Var()
model.y10_2_2 = Var()
model.z10_2_2 = Var()
model.y10_3_2 = Var()
model.z10_3_2 = Var()
model.y10_4_2 = Var()
model.z10_4_2 = Var()
model.y10_5_2 = Var()
model.z10_5_2 = Var()
model.y10_6_2 = Var()
model.z10_6_2 = Var()
model.y10_7_2 = Var()
model.z10_7_2 = Var()
model.y10_8_2 = Var()
model.z10_8_2 = Var()
model.y10_9_2 = Var()
model.z10_9_2 = Var()
model.y10_1_3 = Var()
model.z10_1_3 = Var()
model.y10_2_3 = Var()
model.z10_2_3 = Var()
model.y10_3_3 = Var()
model.z10_3_3 = Var()
model.y10_4_3 = Var()
model.z10_4_3 = Var()
model.y10_5_3 = Var()
model.z10_5_3 = Var()
model.y10_6_3 = Var()
model.z10_6_3 = Var()
model.y10_7_3 = Var()
model.z10_7_3 = Var()
model.y10_8_3 = Var()
model.z10_8_3 = Var()
model.y10_9_3 = Var()
model.z10_9_3 = Var()
model.y10_1_4 = Var()
model.z10_1_4 = Var()
model.y10_2_4 = Var()
model.z10_2_4 = Var()
model.y10_3_4 = Var()
model.z10_3_4 = Var()
model.y10_4_4 = Var()
model.z10_4_4 = Var()
model.y10_5_4 = Var()
model.z10_5_4 = Var()
model.y10_6_4 = Var()
model.z10_6_4 = Var()
model.y10_7_4 = Var()
model.z10_7_4 = Var()
model.y10_8_4 = Var()
model.z10_8_4 = Var()
model.y10_9_4 = Var()
model.z10_9_4 = Var()
model.y10_1_5 = Var()
model.z10_1_5 = Var()
model.y10_2_5 = Var()
model.z10_2_5 = Var()
model.y10_3_5 = Var()
model.z10_3_5 = Var()
model.y10_4_5 = Var()
model.z10_4_5 = Var()
model.y10_5_5 = Var()
model.z10_5_5 = Var()
model.y10_6_5 = Var()
model.z10_6_5 = Var()
model.y10_7_5 = Var()
model.z10_7_5 = Var()
model.y10_8_5 = Var()
model.z10_8_5 = Var()
model.y10_9_5 = Var()
model.z10_9_5 = Var()
model.y10_1_6 = Var()
model.z10_1_6 = Var()
model.y10_2_6 = Var()
model.z10_2_6 = Var()
model.y10_3_6 = Var()
model.z10_3_6 = Var()
model.y10_4_6 = Var()
model.z10_4_6 = Var()
model.y10_5_6 = Var()
model.z10_5_6 = Var()
model.y10_6_6 = Var()
model.z10_6_6 = Var()
model.y10_7_6 = Var()
model.z10_7_6 = Var()
model.y10_8_6 = Var()
model.z10_8_6 = Var()
model.y10_9_6 = Var()
model.z10_9_6 = Var()
model.y10_1_7 = Var()
model.z10_1_7 = Var()
model.y10_2_7 = Var()
model.z10_2_7 = Var()
model.y10_3_7 = Var()
model.z10_3_7 = Var()
model.y10_4_7 = Var()
model.z10_4_7 = Var()
model.y10_5_7 = Var()
model.z10_5_7 = Var()
model.y10_6_7 = Var()
model.z10_6_7 = Var()
model.y10_7_7 = Var()
model.z10_7_7 = Var()
model.y10_8_7 = Var()
model.z10_8_7 = Var()
model.y10_9_7 = Var()
model.z10_9_7 = Var()
model.y10_1_8 = Var()
model.z10_1_8 = Var()
model.y10_2_8 = Var()
model.z10_2_8 = Var()
model.y10_3_8 = Var()
model.z10_3_8 = Var()
model.y10_4_8 = Var()
model.z10_4_8 = Var()
model.y10_5_8 = Var()
model.z10_5_8 = Var()
model.y10_6_8 = Var()
model.z10_6_8 = Var()
model.y10_7_8 = Var()
model.z10_7_8 = Var()
model.y10_8_8 = Var()
model.z10_8_8 = Var()
model.y10_9_8 = Var()
model.z10_9_8 = Var()
model.y10_1_9 = Var()
model.z10_1_9 = Var()
model.y10_2_9 = Var()
model.z10_2_9 = Var()
model.y10_3_9 = Var()
model.z10_3_9 = Var()
model.y10_4_9 = Var()
model.z10_4_9 = Var()
model.y10_5_9 = Var()
model.z10_5_9 = Var()
model.y10_6_9 = Var()
model.z10_6_9 = Var()
model.y10_7_9 = Var()
model.z10_7_9 = Var()
model.y10_8_9 = Var()
model.z10_8_9 = Var()
model.y10_9_9 = Var()
model.z10_9_9 = Var()
model.x1_10_1 = Var()
model.z1_10_1 = Var()
model.x2_10_1 = Var()
model.z2_10_1 = Var()
model.x3_10_1 = Var()
model.z3_10_1 = Var()
model.x4_10_1 = Var()
model.z4_10_1 = Var()
model.x5_10_1 = Var()
model.z5_10_1 = Var()
model.x6_10_1 = Var()
model.z6_10_1 = Var()
model.x7_10_1 = Var()
model.z7_10_1 = Var()
model.x8_10_1 = Var()
model.z8_10_1 = Var()
model.x9_10_1 = Var()
model.z9_10_1 = Var()
model.x1_10_2 = Var()
model.z1_10_2 = Var()
model.x2_10_2 = Var()
model.z2_10_2 = Var()
model.x3_10_2 = Var()
model.z3_10_2 = Var()
model.x4_10_2 = Var()
model.z4_10_2 = Var()
model.x5_10_2 = Var()
model.z5_10_2 = Var()
model.x6_10_2 = Var()
model.z6_10_2 = Var()
model.x7_10_2 = Var()
model.z7_10_2 = Var()
model.x8_10_2 = Var()
model.z8_10_2 = Var()
model.x9_10_2 = Var()
model.z9_10_2 = Var()
model.x1_10_3 = Var()
model.z1_10_3 = Var()
model.x2_10_3 = Var()
model.z2_10_3 = Var()
model.x3_10_3 = Var()
model.z3_10_3 = Var()
model.x4_10_3 = Var()
model.z4_10_3 = Var()
model.x5_10_3 = Var()
model.z5_10_3 = Var()
model.x6_10_3 = Var()
model.z6_10_3 = Var()
model.x7_10_3 = Var()
model.z7_10_3 = Var()
model.x8_10_3 = Var()
model.z8_10_3 = Var()
model.x9_10_3 = Var()
model.z9_10_3 = Var()
model.x1_10_4 = Var()
model.z1_10_4 = Var()
model.x2_10_4 = Var()
model.z2_10_4 = Var()
model.x3_10_4 = Var()
model.z3_10_4 = Var()
model.x4_10_4 = Var()
model.z4_10_4 = Var()
model.x5_10_4 = Var()
model.z5_10_4 = Var()
model.x6_10_4 = Var()
model.z6_10_4 = Var()
model.x7_10_4 = Var()
model.z7_10_4 = Var()
model.x8_10_4 = Var()
model.z8_10_4 = Var()
model.x9_10_4 = Var()
model.z9_10_4 = Var()
model.x1_10_5 = Var()
model.z1_10_5 = Var()
model.x2_10_5 = Var()
model.z2_10_5 = Var()
model.x3_10_5 = Var()
model.z3_10_5 = Var()
model.x4_10_5 = Var()
model.z4_10_5 = Var()
model.x5_10_5 = Var()
model.z5_10_5 = Var()
model.x6_10_5 = Var()
model.z6_10_5 = Var()
model.x7_10_5 = Var()
model.z7_10_5 = Var()
model.x8_10_5 = Var()
model.z8_10_5 = Var()
model.x9_10_5 = Var()
model.z9_10_5 = Var()
model.x1_10_6 = Var()
model.z1_10_6 = Var()
model.x2_10_6 = Var()
model.z2_10_6 = Var()
model.x3_10_6 = Var()
model.z3_10_6 = Var()
model.x4_10_6 = Var()
model.z4_10_6 = Var()
model.x5_10_6 = Var()
model.z5_10_6 = Var()
model.x6_10_6 = Var()
model.z6_10_6 = Var()
model.x7_10_6 = Var()
model.z7_10_6 = Var()
model.x8_10_6 = Var()
model.z8_10_6 = Var()
model.x9_10_6 = Var()
model.z9_10_6 = Var()
model.x1_10_7 = Var()
model.z1_10_7 = Var()
model.x2_10_7 = Var()
model.z2_10_7 = Var()
model.x3_10_7 = Var()
model.z3_10_7 = Var()
model.x4_10_7 = Var()
model.z4_10_7 = Var()
model.x5_10_7 = Var()
model.z5_10_7 = Var()
model.x6_10_7 = Var()
model.z6_10_7 = Var()
model.x7_10_7 = Var()
model.z7_10_7 = Var()
model.x8_10_7 = Var()
model.z8_10_7 = Var()
model.x9_10_7 = Var()
model.z9_10_7 = Var()
model.x1_10_8 = Var()
model.z1_10_8 = Var()
model.x2_10_8 = Var()
model.z2_10_8 = Var()
model.x3_10_8 = Var()
model.z3_10_8 = Var()
model.x4_10_8 = Var()
model.z4_10_8 = Var()
model.x5_10_8 = Var()
model.z5_10_8 = Var()
model.x6_10_8 = Var()
model.z6_10_8 = Var()
model.x7_10_8 = Var()
model.z7_10_8 = Var()
model.x8_10_8 = Var()
model.z8_10_8 = Var()
model.x9_10_8 = Var()
model.z9_10_8 = Var()
model.x1_10_9 = Var()
model.z1_10_9 = Var()
model.x2_10_9 = Var()
model.z2_10_9 = Var()
model.x3_10_9 = Var()
model.z3_10_9 = Var()
model.x4_10_9 = Var()
model.z4_10_9 = Var()
model.x5_10_9 = Var()
model.z5_10_9 = Var()
model.x6_10_9 = Var()
model.z6_10_9 = Var()
model.x7_10_9 = Var()
model.z7_10_9 = Var()
model.x8_10_9 = Var()
model.z8_10_9 = Var()
model.x9_10_9 = Var()
model.z9_10_9 = Var()
model.x1_1_10 = Var()
model.y1_1_10 = Var()
model.x2_1_10 = Var()
model.y2_1_10 = Var()
model.x3_1_10 = Var()
model.y3_1_10 = Var()
model.x4_1_10 = Var()
model.y4_1_10 = Var()
model.x5_1_10 = Var()
model.y5_1_10 = Var()
model.x6_1_10 = Var()
model.y6_1_10 = Var()
model.x7_1_10 = Var()
model.y7_1_10 = Var()
model.x8_1_10 = Var()
model.y8_1_10 = Var()
model.x9_1_10 = Var()
model.y9_1_10 = Var()
model.x1_2_10 = Var()
model.y1_2_10 = Var()
model.x2_2_10 = Var()
model.y2_2_10 = Var()
model.x3_2_10 = Var()
model.y3_2_10 = Var()
model.x4_2_10 = Var()
model.y4_2_10 = Var()
model.x5_2_10 = Var()
model.y5_2_10 = Var()
model.x6_2_10 = Var()
model.y6_2_10 = Var()
model.x7_2_10 = Var()
model.y7_2_10 = Var()
model.x8_2_10 = Var()
model.y8_2_10 = Var()
model.x9_2_10 = Var()
model.y9_2_10 = Var()
model.x1_3_10 = Var()
model.y1_3_10 = Var()
model.x2_3_10 = Var()
model.y2_3_10 = Var()
model.x3_3_10 = Var()
model.y3_3_10 = Var()
model.x4_3_10 = Var()
model.y4_3_10 = Var()
model.x5_3_10 = Var()
model.y5_3_10 = Var()
model.x6_3_10 = Var()
model.y6_3_10 = Var()
model.x7_3_10 = Var()
model.y7_3_10 = Var()
model.x8_3_10 = Var()
model.y8_3_10 = Var()
model.x9_3_10 = Var()
model.y9_3_10 = Var()
model.x1_4_10 = Var()
model.y1_4_10 = Var()
model.x2_4_10 = Var()
model.y2_4_10 = Var()
model.x3_4_10 = Var()
model.y3_4_10 = Var()
model.x4_4_10 = Var()
model.y4_4_10 = Var()
model.x5_4_10 = Var()
model.y5_4_10 = Var()
model.x6_4_10 = Var()
model.y6_4_10 = Var()
model.x7_4_10 = Var()
model.y7_4_10 = Var()
model.x8_4_10 = Var()
model.y8_4_10 = Var()
model.x9_4_10 = Var()
model.y9_4_10 = Var()
model.x1_5_10 = Var()
model.y1_5_10 = Var()
model.x2_5_10 = Var()
model.y2_5_10 = Var()
model.x3_5_10 = Var()
model.y3_5_10 = Var()
model.x4_5_10 = Var()
model.y4_5_10 = Var()
model.x5_5_10 = Var()
model.y5_5_10 = Var()
model.x6_5_10 = Var()
model.y6_5_10 = Var()
model.x7_5_10 = Var()
model.y7_5_10 = Var()
model.x8_5_10 = Var()
model.y8_5_10 = Var()
model.x9_5_10 = Var()
model.y9_5_10 = Var()
model.x1_6_10 = Var()
model.y1_6_10 = Var()
model.x2_6_10 = Var()
model.y2_6_10 = Var()
model.x3_6_10 = Var()
model.y3_6_10 = Var()
model.x4_6_10 = Var()
model.y4_6_10 = Var()
model.x5_6_10 = Var()
model.y5_6_10 = Var()
model.x6_6_10 = Var()
model.y6_6_10 = Var()
model.x7_6_10 = Var()
model.y7_6_10 = Var()
model.x8_6_10 = Var()
model.y8_6_10 = Var()
model.x9_6_10 = Var()
model.y9_6_10 = Var()
model.x1_7_10 = Var()
model.y1_7_10 = Var()
model.x2_7_10 = Var()
model.y2_7_10 = Var()
model.x3_7_10 = Var()
model.y3_7_10 = Var()
model.x4_7_10 = Var()
model.y4_7_10 = Var()
model.x5_7_10 = Var()
model.y5_7_10 = Var()
model.x6_7_10 = Var()
model.y6_7_10 = Var()
model.x7_7_10 = Var()
model.y7_7_10 = Var()
model.x8_7_10 = Var()
model.y8_7_10 = Var()
model.x9_7_10 = Var()
model.y9_7_10 = Var()
model.x1_8_10 = Var()
model.y1_8_10 = Var()
model.x2_8_10 = Var()
model.y2_8_10 = Var()
model.x3_8_10 = Var()
model.y3_8_10 = Var()
model.x4_8_10 = Var()
model.y4_8_10 = Var()
model.x5_8_10 = Var()
model.y5_8_10 = Var()
model.x6_8_10 = Var()
model.y6_8_10 = Var()
model.x7_8_10 = Var()
model.y7_8_10 = Var()
model.x8_8_10 = Var()
model.y8_8_10 = Var()
model.x9_8_10 = Var()
model.y9_8_10 = Var()
model.x1_9_10 = Var()
model.y1_9_10 = Var()
model.x2_9_10 = Var()
model.y2_9_10 = Var()
model.x3_9_10 = Var()
model.y3_9_10 = Var()
model.x4_9_10 = Var()
model.y4_9_10 = Var()
model.x5_9_10 = Var()
model.y5_9_10 = Var()
model.x6_9_10 = Var()
model.y6_9_10 = Var()
model.x7_9_10 = Var()
model.y7_9_10 = Var()
model.x8_9_10 = Var()
model.y8_9_10 = Var()
model.x9_9_10 = Var()
model.y9_9_10 = Var()
model.y0_1_1 = Var()
model.z0_1_1 = Var()
model.y11_1_1 = Var()
model.z11_1_1 = Var()
model.y0_2_1 = Var()
model.z0_2_1 = Var()
model.y11_2_1 = Var()
model.z11_2_1 = Var()
model.y0_3_1 = Var()
model.z0_3_1 = Var()
model.y11_3_1 = Var()
model.z11_3_1 = Var()
model.y0_4_1 = Var()
model.z0_4_1 = Var()
model.y11_4_1 = Var()
model.z11_4_1 = Var()
model.y0_5_1 = Var()
model.z0_5_1 = Var()
model.y11_5_1 = Var()
model.z11_5_1 = Var()
model.y0_6_1 = Var()
model.z0_6_1 = Var()
model.y11_6_1 = Var()
model.z11_6_1 = Var()
model.y0_7_1 = Var()
model.z0_7_1 = Var()
model.y11_7_1 = Var()
model.z11_7_1 = Var()
model.y0_8_1 = Var()
model.z0_8_1 = Var()
model.y11_8_1 = Var()
model.z11_8_1 = Var()
model.y0_9_1 = Var()
model.z0_9_1 = Var()
model.y11_9_1 = Var()
model.z11_9_1 = Var()
model.y0_10_1 = Var()
model.z0_10_1 = Var()
model.y11_10_1 = Var()
model.z11_10_1 = Var()
model.y0_1_2 = Var()
model.z0_1_2 = Var()
model.y11_1_2 = Var()
model.z11_1_2 = Var()
model.y0_2_2 = Var()
model.z0_2_2 = Var()
model.y11_2_2 = Var()
model.z11_2_2 = Var()
model.y0_3_2 = Var()
model.z0_3_2 = Var()
model.y11_3_2 = Var()
model.z11_3_2 = Var()
model.y0_4_2 = Var()
model.z0_4_2 = Var()
model.y11_4_2 = Var()
model.z11_4_2 = Var()
model.y0_5_2 = Var()
model.z0_5_2 = Var()
model.y11_5_2 = Var()
model.z11_5_2 = Var()
model.y0_6_2 = Var()
model.z0_6_2 = Var()
model.y11_6_2 = Var()
model.z11_6_2 = Var()
model.y0_7_2 = Var()
model.z0_7_2 = Var()
model.y11_7_2 = Var()
model.z11_7_2 = Var()
model.y0_8_2 = Var()
model.z0_8_2 = Var()
model.y11_8_2 = Var()
model.z11_8_2 = Var()
model.y0_9_2 = Var()
model.z0_9_2 = Var()
model.y11_9_2 = Var()
model.z11_9_2 = Var()
model.y0_10_2 = Var()
model.z0_10_2 = Var()
model.y11_10_2 = Var()
model.z11_10_2 = Var()
model.y0_1_3 = Var()
model.z0_1_3 = Var()
model.y11_1_3 = Var()
model.z11_1_3 = Var()
model.y0_2_3 = Var()
model.z0_2_3 = Var()
model.y11_2_3 = Var()
model.z11_2_3 = Var()
model.y0_3_3 = Var()
model.z0_3_3 = Var()
model.y11_3_3 = Var()
model.z11_3_3 = Var()
model.y0_4_3 = Var()
model.z0_4_3 = Var()
model.y11_4_3 = Var()
model.z11_4_3 = Var()
model.y0_5_3 = Var()
model.z0_5_3 = Var()
model.y11_5_3 = Var()
model.z11_5_3 = Var()
model.y0_6_3 = Var()
model.z0_6_3 = Var()
model.y11_6_3 = Var()
model.z11_6_3 = Var()
model.y0_7_3 = Var()
model.z0_7_3 = Var()
model.y11_7_3 = Var()
model.z11_7_3 = Var()
model.y0_8_3 = Var()
model.z0_8_3 = Var()
model.y11_8_3 = Var()
model.z11_8_3 = Var()
model.y0_9_3 = Var()
model.z0_9_3 = Var()
model.y11_9_3 = Var()
model.z11_9_3 = Var()
model.y0_10_3 = Var()
model.z0_10_3 = Var()
model.y11_10_3 = Var()
model.z11_10_3 = Var()
model.y0_1_4 = Var()
model.z0_1_4 = Var()
model.y11_1_4 = Var()
model.z11_1_4 = Var()
model.y0_2_4 = Var()
model.z0_2_4 = Var()
model.y11_2_4 = Var()
model.z11_2_4 = Var()
model.y0_3_4 = Var()
model.z0_3_4 = Var()
model.y11_3_4 = Var()
model.z11_3_4 = Var()
model.y0_4_4 = Var()
model.z0_4_4 = Var()
model.y11_4_4 = Var()
model.z11_4_4 = Var()
model.y0_5_4 = Var()
model.z0_5_4 = Var()
model.y11_5_4 = Var()
model.z11_5_4 = Var()
model.y0_6_4 = Var()
model.z0_6_4 = Var()
model.y11_6_4 = Var()
model.z11_6_4 = Var()
model.y0_7_4 = Var()
model.z0_7_4 = Var()
model.y11_7_4 = Var()
model.z11_7_4 = Var()
model.y0_8_4 = Var()
model.z0_8_4 = Var()
model.y11_8_4 = Var()
model.z11_8_4 = Var()
model.y0_9_4 = Var()
model.z0_9_4 = Var()
model.y11_9_4 = Var()
model.z11_9_4 = Var()
model.y0_10_4 = Var()
model.z0_10_4 = Var()
model.y11_10_4 = Var()
model.z11_10_4 = Var()
model.y0_1_5 = Var()
model.z0_1_5 = Var()
model.y11_1_5 = Var()
model.z11_1_5 = Var()
model.y0_2_5 = Var()
model.z0_2_5 = Var()
model.y11_2_5 = Var()
model.z11_2_5 = Var()
model.y0_3_5 = Var()
model.z0_3_5 = Var()
model.y11_3_5 = Var()
model.z11_3_5 = Var()
model.y0_4_5 = Var()
model.z0_4_5 = Var()
model.y11_4_5 = Var()
model.z11_4_5 = Var()
model.y0_5_5 = Var()
model.z0_5_5 = Var()
model.y11_5_5 = Var()
model.z11_5_5 = Var()
model.y0_6_5 = Var()
model.z0_6_5 = Var()
model.y11_6_5 = Var()
model.z11_6_5 = Var()
model.y0_7_5 = Var()
model.z0_7_5 = Var()
model.y11_7_5 = Var()
model.z11_7_5 = Var()
model.y0_8_5 = Var()
model.z0_8_5 = Var()
model.y11_8_5 = Var()
model.z11_8_5 = Var()
model.y0_9_5 = Var()
model.z0_9_5 = Var()
model.y11_9_5 = Var()
model.z11_9_5 = Var()
model.y0_10_5 = Var()
model.z0_10_5 = Var()
model.y11_10_5 = Var()
model.z11_10_5 = Var()
model.y0_1_6 = Var()
model.z0_1_6 = Var()
model.y11_1_6 = Var()
model.z11_1_6 = Var()
model.y0_2_6 = Var()
model.z0_2_6 = Var()
model.y11_2_6 = Var()
model.z11_2_6 = Var()
model.y0_3_6 = Var()
model.z0_3_6 = Var()
model.y11_3_6 = Var()
model.z11_3_6 = Var()
model.y0_4_6 = Var()
model.z0_4_6 = Var()
model.y11_4_6 = Var()
model.z11_4_6 = Var()
model.y0_5_6 = Var()
model.z0_5_6 = Var()
model.y11_5_6 = Var()
model.z11_5_6 = Var()
model.y0_6_6 = Var()
model.z0_6_6 = Var()
model.y11_6_6 = Var()
model.z11_6_6 = Var()
model.y0_7_6 = Var()
model.z0_7_6 = Var()
model.y11_7_6 = Var()
model.z11_7_6 = Var()
model.y0_8_6 = Var()
model.z0_8_6 = Var()
model.y11_8_6 = Var()
model.z11_8_6 = Var()
model.y0_9_6 = Var()
model.z0_9_6 = Var()
model.y11_9_6 = Var()
model.z11_9_6 = Var()
model.y0_10_6 = Var()
model.z0_10_6 = Var()
model.y11_10_6 = Var()
model.z11_10_6 = Var()
model.y0_1_7 = Var()
model.z0_1_7 = Var()
model.y11_1_7 = Var()
model.z11_1_7 = Var()
model.y0_2_7 = Var()
model.z0_2_7 = Var()
model.y11_2_7 = Var()
model.z11_2_7 = Var()
model.y0_3_7 = Var()
model.z0_3_7 = Var()
model.y11_3_7 = Var()
model.z11_3_7 = Var()
model.y0_4_7 = Var()
model.z0_4_7 = Var()
model.y11_4_7 = Var()
model.z11_4_7 = Var()
model.y0_5_7 = Var()
model.z0_5_7 = Var()
model.y11_5_7 = Var()
model.z11_5_7 = Var()
model.y0_6_7 = Var()
model.z0_6_7 = Var()
model.y11_6_7 = Var()
model.z11_6_7 = Var()
model.y0_7_7 = Var()
model.z0_7_7 = Var()
model.y11_7_7 = Var()
model.z11_7_7 = Var()
model.y0_8_7 = Var()
model.z0_8_7 = Var()
model.y11_8_7 = Var()
model.z11_8_7 = Var()
model.y0_9_7 = Var()
model.z0_9_7 = Var()
model.y11_9_7 = Var()
model.z11_9_7 = Var()
model.y0_10_7 = Var()
model.z0_10_7 = Var()
model.y11_10_7 = Var()
model.z11_10_7 = Var()
model.y0_1_8 = Var()
model.z0_1_8 = Var()
model.y11_1_8 = Var()
model.z11_1_8 = Var()
model.y0_2_8 = Var()
model.z0_2_8 = Var()
model.y11_2_8 = Var()
model.z11_2_8 = Var()
model.y0_3_8 = Var()
model.z0_3_8 = Var()
model.y11_3_8 = Var()
model.z11_3_8 = Var()
model.y0_4_8 = Var()
model.z0_4_8 = Var()
model.y11_4_8 = Var()
model.z11_4_8 = Var()
model.y0_5_8 = Var()
model.z0_5_8 = Var()
model.y11_5_8 = Var()
model.z11_5_8 = Var()
model.y0_6_8 = Var()
model.z0_6_8 = Var()
model.y11_6_8 = Var()
model.z11_6_8 = Var()
model.y0_7_8 = Var()
model.z0_7_8 = Var()
model.y11_7_8 = Var()
model.z11_7_8 = Var()
model.y0_8_8 = Var()
model.z0_8_8 = Var()
model.y11_8_8 = Var()
model.z11_8_8 = Var()
model.y0_9_8 = Var()
model.z0_9_8 = Var()
model.y11_9_8 = Var()
model.z11_9_8 = Var()
model.y0_10_8 = Var()
model.z0_10_8 = Var()
model.y11_10_8 = Var()
model.z11_10_8 = Var()
model.y0_1_9 = Var()
model.z0_1_9 = Var()
model.y11_1_9 = Var()
model.z11_1_9 = Var()
model.y0_2_9 = Var()
model.z0_2_9 = Var()
model.y11_2_9 = Var()
model.z11_2_9 = Var()
model.y0_3_9 = Var()
model.z0_3_9 = Var()
model.y11_3_9 = Var()
model.z11_3_9 = Var()
model.y0_4_9 = Var()
model.z0_4_9 = Var()
model.y11_4_9 = Var()
model.z11_4_9 = Var()
model.y0_5_9 = Var()
model.z0_5_9 = Var()
model.y11_5_9 = Var()
model.z11_5_9 = Var()
model.y0_6_9 = Var()
model.z0_6_9 = Var()
model.y11_6_9 = Var()
model.z11_6_9 = Var()
model.y0_7_9 = Var()
model.z0_7_9 = Var()
model.y11_7_9 = Var()
model.z11_7_9 = Var()
model.y0_8_9 = Var()
model.z0_8_9 = Var()
model.y11_8_9 = Var()
model.z11_8_9 = Var()
model.y0_9_9 = Var()
model.z0_9_9 = Var()
model.y11_9_9 = Var()
model.z11_9_9 = Var()
model.y0_10_9 = Var()
model.z0_10_9 = Var()
model.y11_10_9 = Var()
model.z11_10_9 = Var()
model.y0_1_10 = Var()
model.z0_1_10 = Var()
model.y11_1_10 = Var()
model.z11_1_10 = Var()
model.y0_2_10 = Var()
model.z0_2_10 = Var()
model.y11_2_10 = Var()
model.z11_2_10 = Var()
model.y0_3_10 = Var()
model.z0_3_10 = Var()
model.y11_3_10 = Var()
model.z11_3_10 = Var()
model.y0_4_10 = Var()
model.z0_4_10 = Var()
model.y11_4_10 = Var()
model.z11_4_10 = Var()
model.y0_5_10 = Var()
model.z0_5_10 = Var()
model.y11_5_10 = Var()
model.z11_5_10 = Var()
model.y0_6_10 = Var()
model.z0_6_10 = Var()
model.y11_6_10 = Var()
model.z11_6_10 = Var()
model.y0_7_10 = Var()
model.z0_7_10 = Var()
model.y11_7_10 = Var()
model.z11_7_10 = Var()
model.y0_8_10 = Var()
model.z0_8_10 = Var()
model.y11_8_10 = Var()
model.z11_8_10 = Var()
model.y0_9_10 = Var()
model.z0_9_10 = Var()
model.y11_9_10 = Var()
model.z11_9_10 = Var()
model.y0_10_10 = Var()
model.z0_10_10 = Var()
model.y11_10_10 = Var()
model.z11_10_10 = Var()
model.x1_0_1 = Var()
model.z1_0_1 = Var()
model.x1_11_1 = Var()
model.z1_11_1 = Var()
model.x2_0_1 = Var()
model.z2_0_1 = Var()
model.x2_11_1 = Var()
model.z2_11_1 = Var()
model.x3_0_1 = Var()
model.z3_0_1 = Var()
model.x3_11_1 = Var()
model.z3_11_1 = Var()
model.x4_0_1 = Var()
model.z4_0_1 = Var()
model.x4_11_1 = Var()
model.z4_11_1 = Var()
model.x5_0_1 = Var()
model.z5_0_1 = Var()
model.x5_11_1 = Var()
model.z5_11_1 = Var()
model.x6_0_1 = Var()
model.z6_0_1 = Var()
model.x6_11_1 = Var()
model.z6_11_1 = Var()
model.x7_0_1 = Var()
model.z7_0_1 = Var()
model.x7_11_1 = Var()
model.z7_11_1 = Var()
model.x8_0_1 = Var()
model.z8_0_1 = Var()
model.x8_11_1 = Var()
model.z8_11_1 = Var()
model.x9_0_1 = Var()
model.z9_0_1 = Var()
model.x9_11_1 = Var()
model.z9_11_1 = Var()
model.x10_0_1 = Var()
model.z10_0_1 = Var()
model.x10_11_1 = Var()
model.z10_11_1 = Var()
model.x1_0_2 = Var()
model.z1_0_2 = Var()
model.x1_11_2 = Var()
model.z1_11_2 = Var()
model.x2_0_2 = Var()
model.z2_0_2 = Var()
model.x2_11_2 = Var()
model.z2_11_2 = Var()
model.x3_0_2 = Var()
model.z3_0_2 = Var()
model.x3_11_2 = Var()
model.z3_11_2 = Var()
model.x4_0_2 = Var()
model.z4_0_2 = Var()
model.x4_11_2 = Var()
model.z4_11_2 = Var()
model.x5_0_2 = Var()
model.z5_0_2 = Var()
model.x5_11_2 = Var()
model.z5_11_2 = Var()
model.x6_0_2 = Var()
model.z6_0_2 = Var()
model.x6_11_2 = Var()
model.z6_11_2 = Var()
model.x7_0_2 = Var()
model.z7_0_2 = Var()
model.x7_11_2 = Var()
model.z7_11_2 = Var()
model.x8_0_2 = Var()
model.z8_0_2 = Var()
model.x8_11_2 = Var()
model.z8_11_2 = Var()
model.x9_0_2 = Var()
model.z9_0_2 = Var()
model.x9_11_2 = Var()
model.z9_11_2 = Var()
model.x10_0_2 = Var()
model.z10_0_2 = Var()
model.x10_11_2 = Var()
model.z10_11_2 = Var()
model.x1_0_3 = Var()
model.z1_0_3 = Var()
model.x1_11_3 = Var()
model.z1_11_3 = Var()
model.x2_0_3 = Var()
model.z2_0_3 = Var()
model.x2_11_3 = Var()
model.z2_11_3 = Var()
model.x3_0_3 = Var()
model.z3_0_3 = Var()
model.x3_11_3 = Var()
model.z3_11_3 = Var()
model.x4_0_3 = Var()
model.z4_0_3 = Var()
model.x4_11_3 = Var()
model.z4_11_3 = Var()
model.x5_0_3 = Var()
model.z5_0_3 = Var()
model.x5_11_3 = Var()
model.z5_11_3 = Var()
model.x6_0_3 = Var()
model.z6_0_3 = Var()
model.x6_11_3 = Var()
model.z6_11_3 = Var()
model.x7_0_3 = Var()
model.z7_0_3 = Var()
model.x7_11_3 = Var()
model.z7_11_3 = Var()
model.x8_0_3 = Var()
model.z8_0_3 = Var()
model.x8_11_3 = Var()
model.z8_11_3 = Var()
model.x9_0_3 = Var()
model.z9_0_3 = Var()
model.x9_11_3 = Var()
model.z9_11_3 = Var()
model.x10_0_3 = Var()
model.z10_0_3 = Var()
model.x10_11_3 = Var()
model.z10_11_3 = Var()
model.x1_0_4 = Var()
model.z1_0_4 = Var()
model.x1_11_4 = Var()
model.z1_11_4 = Var()
model.x2_0_4 = Var()
model.z2_0_4 = Var()
model.x2_11_4 = Var()
model.z2_11_4 = Var()
model.x3_0_4 = Var()
model.z3_0_4 = Var()
model.x3_11_4 = Var()
model.z3_11_4 = Var()
model.x4_0_4 = Var()
model.z4_0_4 = Var()
model.x4_11_4 = Var()
model.z4_11_4 = Var()
model.x5_0_4 = Var()
model.z5_0_4 = Var()
model.x5_11_4 = Var()
model.z5_11_4 = Var()
model.x6_0_4 = Var()
model.z6_0_4 = Var()
model.x6_11_4 = Var()
model.z6_11_4 = Var()
model.x7_0_4 = Var()
model.z7_0_4 = Var()
model.x7_11_4 = Var()
model.z7_11_4 = Var()
model.x8_0_4 = Var()
model.z8_0_4 = Var()
model.x8_11_4 = Var()
model.z8_11_4 = Var()
model.x9_0_4 = Var()
model.z9_0_4 = Var()
model.x9_11_4 = Var()
model.z9_11_4 = Var()
model.x10_0_4 = Var()
model.z10_0_4 = Var()
model.x10_11_4 = Var()
model.z10_11_4 = Var()
model.x1_0_5 = Var()
model.z1_0_5 = Var()
model.x1_11_5 = Var()
model.z1_11_5 = Var()
model.x2_0_5 = Var()
model.z2_0_5 = Var()
model.x2_11_5 = Var()
model.z2_11_5 = Var()
model.x3_0_5 = Var()
model.z3_0_5 = Var()
model.x3_11_5 = Var()
model.z3_11_5 = Var()
model.x4_0_5 = Var()
model.z4_0_5 = Var()
model.x4_11_5 = Var()
model.z4_11_5 = Var()
model.x5_0_5 = Var()
model.z5_0_5 = Var()
model.x5_11_5 = Var()
model.z5_11_5 = Var()
model.x6_0_5 = Var()
model.z6_0_5 = Var()
model.x6_11_5 = Var()
model.z6_11_5 = Var()
model.x7_0_5 = Var()
model.z7_0_5 = Var()
model.x7_11_5 = Var()
model.z7_11_5 = Var()
model.x8_0_5 = Var()
model.z8_0_5 = Var()
model.x8_11_5 = Var()
model.z8_11_5 = Var()
model.x9_0_5 = Var()
model.z9_0_5 = Var()
model.x9_11_5 = Var()
model.z9_11_5 = Var()
model.x10_0_5 = Var()
model.z10_0_5 = Var()
model.x10_11_5 = Var()
model.z10_11_5 = Var()
model.x1_0_6 = Var()
model.z1_0_6 = Var()
model.x1_11_6 = Var()
model.z1_11_6 = Var()
model.x2_0_6 = Var()
model.z2_0_6 = Var()
model.x2_11_6 = Var()
model.z2_11_6 = Var()
model.x3_0_6 = Var()
model.z3_0_6 = Var()
model.x3_11_6 = Var()
model.z3_11_6 = Var()
model.x4_0_6 = Var()
model.z4_0_6 = Var()
model.x4_11_6 = Var()
model.z4_11_6 = Var()
model.x5_0_6 = Var()
model.z5_0_6 = Var()
model.x5_11_6 = Var()
model.z5_11_6 = Var()
model.x6_0_6 = Var()
model.z6_0_6 = Var()
model.x6_11_6 = Var()
model.z6_11_6 = Var()
model.x7_0_6 = Var()
model.z7_0_6 = Var()
model.x7_11_6 = Var()
model.z7_11_6 = Var()
model.x8_0_6 = Var()
model.z8_0_6 = Var()
model.x8_11_6 = Var()
model.z8_11_6 = Var()
model.x9_0_6 = Var()
model.z9_0_6 = Var()
model.x9_11_6 = Var()
model.z9_11_6 = Var()
model.x10_0_6 = Var()
model.z10_0_6 = Var()
model.x10_11_6 = Var()
model.z10_11_6 = Var()
model.x1_0_7 = Var()
model.z1_0_7 = Var()
model.x1_11_7 = Var()
model.z1_11_7 = Var()
model.x2_0_7 = Var()
model.z2_0_7 = Var()
model.x2_11_7 = Var()
model.z2_11_7 = Var()
model.x3_0_7 = Var()
model.z3_0_7 = Var()
model.x3_11_7 = Var()
model.z3_11_7 = Var()
model.x4_0_7 = Var()
model.z4_0_7 = Var()
model.x4_11_7 = Var()
model.z4_11_7 = Var()
model.x5_0_7 = Var()
model.z5_0_7 = Var()
model.x5_11_7 = Var()
model.z5_11_7 = Var()
model.x6_0_7 = Var()
model.z6_0_7 = Var()
model.x6_11_7 = Var()
model.z6_11_7 = Var()
model.x7_0_7 = Var()
model.z7_0_7 = Var()
model.x7_11_7 = Var()
model.z7_11_7 = Var()
model.x8_0_7 = Var()
model.z8_0_7 = Var()
model.x8_11_7 = Var()
model.z8_11_7 = Var()
model.x9_0_7 = Var()
model.z9_0_7 = Var()
model.x9_11_7 = Var()
model.z9_11_7 = Var()
model.x10_0_7 = Var()
model.z10_0_7 = Var()
model.x10_11_7 = Var()
model.z10_11_7 = Var()
model.x1_0_8 = Var()
model.z1_0_8 = Var()
model.x1_11_8 = Var()
model.z1_11_8 = Var()
model.x2_0_8 = Var()
model.z2_0_8 = Var()
model.x2_11_8 = Var()
model.z2_11_8 = Var()
model.x3_0_8 = Var()
model.z3_0_8 = Var()
model.x3_11_8 = Var()
model.z3_11_8 = Var()
model.x4_0_8 = Var()
model.z4_0_8 = Var()
model.x4_11_8 = Var()
model.z4_11_8 = Var()
model.x5_0_8 = Var()
model.z5_0_8 = Var()
model.x5_11_8 = Var()
model.z5_11_8 = Var()
model.x6_0_8 = Var()
model.z6_0_8 = Var()
model.x6_11_8 = Var()
model.z6_11_8 = Var()
model.x7_0_8 = Var()
model.z7_0_8 = Var()
model.x7_11_8 = Var()
model.z7_11_8 = Var()
model.x8_0_8 = Var()
model.z8_0_8 = Var()
model.x8_11_8 = Var()
model.z8_11_8 = Var()
model.x9_0_8 = Var()
model.z9_0_8 = Var()
model.x9_11_8 = Var()
model.z9_11_8 = Var()
model.x10_0_8 = Var()
model.z10_0_8 = Var()
model.x10_11_8 = Var()
model.z10_11_8 = Var()
model.x1_0_9 = Var()
model.z1_0_9 = Var()
model.x1_11_9 = Var()
model.z1_11_9 = Var()
model.x2_0_9 = Var()
model.z2_0_9 = Var()
model.x2_11_9 = Var()
model.z2_11_9 = Var()
model.x3_0_9 = Var()
model.z3_0_9 = Var()
model.x3_11_9 = Var()
model.z3_11_9 = Var()
model.x4_0_9 = Var()
model.z4_0_9 = Var()
model.x4_11_9 = Var()
model.z4_11_9 = Var()
model.x5_0_9 = Var()
model.z5_0_9 = Var()
model.x5_11_9 = Var()
model.z5_11_9 = Var()
model.x6_0_9 = Var()
model.z6_0_9 = Var()
model.x6_11_9 = Var()
model.z6_11_9 = Var()
model.x7_0_9 = Var()
model.z7_0_9 = Var()
model.x7_11_9 = Var()
model.z7_11_9 = Var()
model.x8_0_9 = Var()
model.z8_0_9 = Var()
model.x8_11_9 = Var()
model.z8_11_9 = Var()
model.x9_0_9 = Var()
model.z9_0_9 = Var()
model.x9_11_9 = Var()
model.z9_11_9 = Var()
model.x10_0_9 = Var()
model.z10_0_9 = Var()
model.x10_11_9 = Var()
model.z10_11_9 = Var()
model.x1_0_10 = Var()
model.z1_0_10 = Var()
model.x1_11_10 = Var()
model.z1_11_10 = Var()
model.x2_0_10 = Var()
model.z2_0_10 = Var()
model.x2_11_10 = Var()
model.z2_11_10 = Var()
model.x3_0_10 = Var()
model.z3_0_10 = Var()
model.x3_11_10 = Var()
model.z3_11_10 = Var()
model.x4_0_10 = Var()
model.z4_0_10 = Var()
model.x4_11_10 = Var()
model.z4_11_10 = Var()
model.x5_0_10 = Var()
model.z5_0_10 = Var()
model.x5_11_10 = Var()
model.z5_11_10 = Var()
model.x6_0_10 = Var()
model.z6_0_10 = Var()
model.x6_11_10 = Var()
model.z6_11_10 = Var()
model.x7_0_10 = Var()
model.z7_0_10 = Var()
model.x7_11_10 = Var()
model.z7_11_10 = Var()
model.x8_0_10 = Var()
model.z8_0_10 = Var()
model.x8_11_10 = Var()
model.z8_11_10 = Var()
model.x9_0_10 = Var()
model.z9_0_10 = Var()
model.x9_11_10 = Var()
model.z9_11_10 = Var()
model.x10_0_10 = Var()
model.z10_0_10 = Var()
model.x10_11_10 = Var()
model.z10_11_10 = Var()
model.x1_1_0 = Var()
model.y1_1_0 = Var()
model.x1_1_11 = Var()
model.y1_1_11 = Var()
model.x2_1_0 = Var()
model.y2_1_0 = Var()
model.x2_1_11 = Var()
model.y2_1_11 = Var()
model.x3_1_0 = Var()
model.y3_1_0 = Var()
model.x3_1_11 = Var()
model.y3_1_11 = Var()
model.x4_1_0 = Var()
model.y4_1_0 = Var()
model.x4_1_11 = Var()
model.y4_1_11 = Var()
model.x5_1_0 = Var()
model.y5_1_0 = Var()
model.x5_1_11 = Var()
model.y5_1_11 = Var()
model.x6_1_0 = Var()
model.y6_1_0 = Var()
model.x6_1_11 = Var()
model.y6_1_11 = Var()
model.x7_1_0 = Var()
model.y7_1_0 = Var()
model.x7_1_11 = Var()
model.y7_1_11 = Var()
model.x8_1_0 = Var()
model.y8_1_0 = Var()
model.x8_1_11 = Var()
model.y8_1_11 = Var()
model.x9_1_0 = Var()
model.y9_1_0 = Var()
model.x9_1_11 = Var()
model.y9_1_11 = Var()
model.x10_1_0 = Var()
model.y10_1_0 = Var()
model.x10_1_11 = Var()
model.y10_1_11 = Var()
model.x1_2_0 = Var()
model.y1_2_0 = Var()
model.x1_2_11 = Var()
model.y1_2_11 = Var()
model.x2_2_0 = Var()
model.y2_2_0 = Var()
model.x2_2_11 = Var()
model.y2_2_11 = Var()
model.x3_2_0 = Var()
model.y3_2_0 = Var()
model.x3_2_11 = Var()
model.y3_2_11 = Var()
model.x4_2_0 = Var()
model.y4_2_0 = Var()
model.x4_2_11 = Var()
model.y4_2_11 = Var()
model.x5_2_0 = Var()
model.y5_2_0 = Var()
model.x5_2_11 = Var()
model.y5_2_11 = Var()
model.x6_2_0 = Var()
model.y6_2_0 = Var()
model.x6_2_11 = Var()
model.y6_2_11 = Var()
model.x7_2_0 = Var()
model.y7_2_0 = Var()
model.x7_2_11 = Var()
model.y7_2_11 = Var()
model.x8_2_0 = Var()
model.y8_2_0 = Var()
model.x8_2_11 = Var()
model.y8_2_11 = Var()
model.x9_2_0 = Var()
model.y9_2_0 = Var()
model.x9_2_11 = Var()
model.y9_2_11 = Var()
model.x10_2_0 = Var()
model.y10_2_0 = Var()
model.x10_2_11 = Var()
model.y10_2_11 = Var()
model.x1_3_0 = Var()
model.y1_3_0 = Var()
model.x1_3_11 = Var()
model.y1_3_11 = Var()
model.x2_3_0 = Var()
model.y2_3_0 = Var()
model.x2_3_11 = Var()
model.y2_3_11 = Var()
model.x3_3_0 = Var()
model.y3_3_0 = Var()
model.x3_3_11 = Var()
model.y3_3_11 = Var()
model.x4_3_0 = Var()
model.y4_3_0 = Var()
model.x4_3_11 = Var()
model.y4_3_11 = Var()
model.x5_3_0 = Var()
model.y5_3_0 = Var()
model.x5_3_11 = Var()
model.y5_3_11 = Var()
model.x6_3_0 = Var()
model.y6_3_0 = Var()
model.x6_3_11 = Var()
model.y6_3_11 = Var()
model.x7_3_0 = Var()
model.y7_3_0 = Var()
model.x7_3_11 = Var()
model.y7_3_11 = Var()
model.x8_3_0 = Var()
model.y8_3_0 = Var()
model.x8_3_11 = Var()
model.y8_3_11 = Var()
model.x9_3_0 = Var()
model.y9_3_0 = Var()
model.x9_3_11 = Var()
model.y9_3_11 = Var()
model.x10_3_0 = Var()
model.y10_3_0 = Var()
model.x10_3_11 = Var()
model.y10_3_11 = Var()
model.x1_4_0 = Var()
model.y1_4_0 = Var()
model.x1_4_11 = Var()
model.y1_4_11 = Var()
model.x2_4_0 = Var()
model.y2_4_0 = Var()
model.x2_4_11 = Var()
model.y2_4_11 = Var()
model.x3_4_0 = Var()
model.y3_4_0 = Var()
model.x3_4_11 = Var()
model.y3_4_11 = Var()
model.x4_4_0 = Var()
model.y4_4_0 = Var()
model.x4_4_11 = Var()
model.y4_4_11 = Var()
model.x5_4_0 = Var()
model.y5_4_0 = Var()
model.x5_4_11 = Var()
model.y5_4_11 = Var()
model.x6_4_0 = Var()
model.y6_4_0 = Var()
model.x6_4_11 = Var()
model.y6_4_11 = Var()
model.x7_4_0 = Var()
model.y7_4_0 = Var()
model.x7_4_11 = Var()
model.y7_4_11 = Var()
model.x8_4_0 = Var()
model.y8_4_0 = Var()
model.x8_4_11 = Var()
model.y8_4_11 = Var()
model.x9_4_0 = Var()
model.y9_4_0 = Var()
model.x9_4_11 = Var()
model.y9_4_11 = Var()
model.x10_4_0 = Var()
model.y10_4_0 = Var()
model.x10_4_11 = Var()
model.y10_4_11 = Var()
model.x1_5_0 = Var()
model.y1_5_0 = Var()
model.x1_5_11 = Var()
model.y1_5_11 = Var()
model.x2_5_0 = Var()
model.y2_5_0 = Var()
model.x2_5_11 = Var()
model.y2_5_11 = Var()
model.x3_5_0 = Var()
model.y3_5_0 = Var()
model.x3_5_11 = Var()
model.y3_5_11 = Var()
model.x4_5_0 = Var()
model.y4_5_0 = Var()
model.x4_5_11 = Var()
model.y4_5_11 = Var()
model.x5_5_0 = Var()
model.y5_5_0 = Var()
model.x5_5_11 = Var()
model.y5_5_11 = Var()
model.x6_5_0 = Var()
model.y6_5_0 = Var()
model.x6_5_11 = Var()
model.y6_5_11 = Var()
model.x7_5_0 = Var()
model.y7_5_0 = Var()
model.x7_5_11 = Var()
model.y7_5_11 = Var()
model.x8_5_0 = Var()
model.y8_5_0 = Var()
model.x8_5_11 = Var()
model.y8_5_11 = Var()
model.x9_5_0 = Var()
model.y9_5_0 = Var()
model.x9_5_11 = Var()
model.y9_5_11 = Var()
model.x10_5_0 = Var()
model.y10_5_0 = Var()
model.x10_5_11 = Var()
model.y10_5_11 = Var()
model.x1_6_0 = Var()
model.y1_6_0 = Var()
model.x1_6_11 = Var()
model.y1_6_11 = Var()
model.x2_6_0 = Var()
model.y2_6_0 = Var()
model.x2_6_11 = Var()
model.y2_6_11 = Var()
model.x3_6_0 = Var()
model.y3_6_0 = Var()
model.x3_6_11 = Var()
model.y3_6_11 = Var()
model.x4_6_0 = Var()
model.y4_6_0 = Var()
model.x4_6_11 = Var()
model.y4_6_11 = Var()
model.x5_6_0 = Var()
model.y5_6_0 = Var()
model.x5_6_11 = Var()
model.y5_6_11 = Var()
model.x6_6_0 = Var()
model.y6_6_0 = Var()
model.x6_6_11 = Var()
model.y6_6_11 = Var()
model.x7_6_0 = Var()
model.y7_6_0 = Var()
model.x7_6_11 = Var()
model.y7_6_11 = Var()
model.x8_6_0 = Var()
model.y8_6_0 = Var()
model.x8_6_11 = Var()
model.y8_6_11 = Var()
model.x9_6_0 = Var()
model.y9_6_0 = Var()
model.x9_6_11 = Var()
model.y9_6_11 = Var()
model.x10_6_0 = Var()
model.y10_6_0 = Var()
model.x10_6_11 = Var()
model.y10_6_11 = Var()
model.x1_7_0 = Var()
model.y1_7_0 = Var()
model.x1_7_11 = Var()
model.y1_7_11 = Var()
model.x2_7_0 = Var()
model.y2_7_0 = Var()
model.x2_7_11 = Var()
model.y2_7_11 = Var()
model.x3_7_0 = Var()
model.y3_7_0 = Var()
model.x3_7_11 = Var()
model.y3_7_11 = Var()
model.x4_7_0 = Var()
model.y4_7_0 = Var()
model.x4_7_11 = Var()
model.y4_7_11 = Var()
model.x5_7_0 = Var()
model.y5_7_0 = Var()
model.x5_7_11 = Var()
model.y5_7_11 = Var()
model.x6_7_0 = Var()
model.y6_7_0 = Var()
model.x6_7_11 = Var()
model.y6_7_11 = Var()
model.x7_7_0 = Var()
model.y7_7_0 = Var()
model.x7_7_11 = Var()
model.y7_7_11 = Var()
model.x8_7_0 = Var()
model.y8_7_0 = Var()
model.x8_7_11 = Var()
model.y8_7_11 = Var()
model.x9_7_0 = Var()
model.y9_7_0 = Var()
model.x9_7_11 = Var()
model.y9_7_11 = Var()
model.x10_7_0 = Var()
model.y10_7_0 = Var()
model.x10_7_11 = Var()
model.y10_7_11 = Var()
model.x1_8_0 = Var()
model.y1_8_0 = Var()
model.x1_8_11 = Var()
model.y1_8_11 = Var()
model.x2_8_0 = Var()
model.y2_8_0 = Var()
model.x2_8_11 = Var()
model.y2_8_11 = Var()
model.x3_8_0 = Var()
model.y3_8_0 = Var()
model.x3_8_11 = Var()
model.y3_8_11 = Var()
model.x4_8_0 = Var()
model.y4_8_0 = Var()
model.x4_8_11 = Var()
model.y4_8_11 = Var()
model.x5_8_0 = Var()
model.y5_8_0 = Var()
model.x5_8_11 = Var()
model.y5_8_11 = Var()
model.x6_8_0 = Var()
model.y6_8_0 = Var()
model.x6_8_11 = Var()
model.y6_8_11 = Var()
model.x7_8_0 = Var()
model.y7_8_0 = Var()
model.x7_8_11 = Var()
model.y7_8_11 = Var()
model.x8_8_0 = Var()
model.y8_8_0 = Var()
model.x8_8_11 = Var()
model.y8_8_11 = Var()
model.x9_8_0 = Var()
model.y9_8_0 = Var()
model.x9_8_11 = Var()
model.y9_8_11 = Var()
model.x10_8_0 = Var()
model.y10_8_0 = Var()
model.x10_8_11 = Var()
model.y10_8_11 = Var()
model.x1_9_0 = Var()
model.y1_9_0 = Var()
model.x1_9_11 = Var()
model.y1_9_11 = Var()
model.x2_9_0 = Var()
model.y2_9_0 = Var()
model.x2_9_11 = Var()
model.y2_9_11 = Var()
model.x3_9_0 = Var()
model.y3_9_0 = Var()
model.x3_9_11 = Var()
model.y3_9_11 = Var()
model.x4_9_0 = Var()
model.y4_9_0 = Var()
model.x4_9_11 = Var()
model.y4_9_11 = Var()
model.x5_9_0 = Var()
model.y5_9_0 = Var()
model.x5_9_11 = Var()
model.y5_9_11 = Var()
model.x6_9_0 = Var()
model.y6_9_0 = Var()
model.x6_9_11 = Var()
model.y6_9_11 = Var()
model.x7_9_0 = Var()
model.y7_9_0 = Var()
model.x7_9_11 = Var()
model.y7_9_11 = Var()
model.x8_9_0 = Var()
model.y8_9_0 = Var()
model.x8_9_11 = Var()
model.y8_9_11 = Var()
model.x9_9_0 = Var()
model.y9_9_0 = Var()
model.x9_9_11 = Var()
model.y9_9_11 = Var()
model.x10_9_0 = Var()
model.y10_9_0 = Var()
model.x10_9_11 = Var()
model.y10_9_11 = Var()
model.x1_10_0 = Var()
model.y1_10_0 = Var()
model.x1_10_11 = Var()
model.y1_10_11 = Var()
model.x2_10_0 = Var()
model.y2_10_0 = Var()
model.x2_10_11 = Var()
model.y2_10_11 = Var()
model.x3_10_0 = Var()
model.y3_10_0 = Var()
model.x3_10_11 = Var()
model.y3_10_11 = Var()
model.x4_10_0 = Var()
model.y4_10_0 = Var()
model.x4_10_11 = Var()
model.y4_10_11 = Var()
model.x5_10_0 = Var()
model.y5_10_0 = Var()
model.x5_10_11 = Var()
model.y5_10_11 = Var()
model.x6_10_0 = Var()
model.y6_10_0 = Var()
model.x6_10_11 = Var()
model.y6_10_11 = Var()
model.x7_10_0 = Var()
model.y7_10_0 = Var()
model.x7_10_11 = Var()
model.y7_10_11 = Var()
model.x8_10_0 = Var()
model.y8_10_0 = Var()
model.x8_10_11 = Var()
model.y8_10_11 = Var()
model.x9_10_0 = Var()
model.y9_10_0 = Var()
model.x9_10_11 = Var()
model.y9_10_11 = Var()
model.x10_10_0 = Var()
model.y10_10_0 = Var()
model.x10_10_11 = Var()
model.y10_10_11 = Var()

model.obj = Objective(expr=\
    0.5*(model.x1_1_1 - 1.0)*(model.x1_1_1 - 1.0) + 0.5*(model.y1_1_1 - 1.0)*(model.y1_1_1 - 1.0) + \
    0.5*(model.z1_1_1 - 1.0)*(model.z1_1_1 - 1.0) + 0.5*(model.x2_1_1 - 1.0)*(model.x2_1_1 - 1.0) + \
    0.5*(model.y2_1_1 - 1.0)*(model.y2_1_1 - 1.0) + 0.5*(model.z2_1_1 - 1.0)*(model.z2_1_1 - 1.0) + \
    0.5*(model.x3_1_1 - 1.0)*(model.x3_1_1 - 1.0) + 0.5*(model.y3_1_1 - 1.0)*(model.y3_1_1 - 1.0) + \
    0.5*(model.z3_1_1 - 1.0)*(model.z3_1_1 - 1.0) + 0.5*(model.x4_1_1 - 1.0)*(model.x4_1_1 - 1.0) + \
    0.5*(model.y4_1_1 - 1.0)*(model.y4_1_1 - 1.0) + 0.5*(model.z4_1_1 - 1.0)*(model.z4_1_1 - 1.0) + \
    0.5*(model.x5_1_1 - 1.0)*(model.x5_1_1 - 1.0) + 0.5*(model.y5_1_1 - 1.0)*(model.y5_1_1 - 1.0) + \
    0.5*(model.z5_1_1 - 1.0)*(model.z5_1_1 - 1.0) + 0.5*(model.x6_1_1 - 1.0)*(model.x6_1_1 - 1.0) + \
    0.5*(model.y6_1_1 - 1.0)*(model.y6_1_1 - 1.0) + 0.5*(model.z6_1_1 - 1.0)*(model.z6_1_1 - 1.0) + \
    0.5*(model.x7_1_1 - 1.0)*(model.x7_1_1 - 1.0) + 0.5*(model.y7_1_1 - 1.0)*(model.y7_1_1 - 1.0) + \
    0.5*(model.z7_1_1 - 1.0)*(model.z7_1_1 - 1.0) + 0.5*(model.x8_1_1 - 1.0)*(model.x8_1_1 - 1.0) + \
    0.5*(model.y8_1_1 - 1.0)*(model.y8_1_1 - 1.0) + 0.5*(model.z8_1_1 - 1.0)*(model.z8_1_1 - 1.0) + \
    0.5*(model.x9_1_1 - 1.0)*(model.x9_1_1 - 1.0) + 0.5*(model.y9_1_1 - 1.0)*(model.y9_1_1 - 1.0) + \
    0.5*(model.z9_1_1 - 1.0)*(model.z9_1_1 - 1.0) + 0.5*(model.x1_2_1 - 1.0)*(model.x1_2_1 - 1.0) + \
    0.5*(model.y1_2_1 - 1.0)*(model.y1_2_1 - 1.0) + 0.5*(model.z1_2_1 - 1.0)*(model.z1_2_1 - 1.0) + \
    0.5*(model.x2_2_1 - 1.0)*(model.x2_2_1 - 1.0) + 0.5*(model.y2_2_1 - 1.0)*(model.y2_2_1 - 1.0) + \
    0.5*(model.z2_2_1 - 1.0)*(model.z2_2_1 - 1.0) + 0.5*(model.x3_2_1 - 1.0)*(model.x3_2_1 - 1.0) + \
    0.5*(model.y3_2_1 - 1.0)*(model.y3_2_1 - 1.0) + 0.5*(model.z3_2_1 - 1.0)*(model.z3_2_1 - 1.0) + \
    0.5*(model.x4_2_1 - 1.0)*(model.x4_2_1 - 1.0) + 0.5*(model.y4_2_1 - 1.0)*(model.y4_2_1 - 1.0) + \
    0.5*(model.z4_2_1 - 1.0)*(model.z4_2_1 - 1.0) + 0.5*(model.x5_2_1 - 1.0)*(model.x5_2_1 - 1.0) + \
    0.5*(model.y5_2_1 - 1.0)*(model.y5_2_1 - 1.0) + 0.5*(model.z5_2_1 - 1.0)*(model.z5_2_1 - 1.0) + \
    0.5*(model.x6_2_1 - 1.0)*(model.x6_2_1 - 1.0) + 0.5*(model.y6_2_1 - 1.0)*(model.y6_2_1 - 1.0) + \
    0.5*(model.z6_2_1 - 1.0)*(model.z6_2_1 - 1.0) + 0.5*(model.x7_2_1 - 1.0)*(model.x7_2_1 - 1.0) + \
    0.5*(model.y7_2_1 - 1.0)*(model.y7_2_1 - 1.0) + 0.5*(model.z7_2_1 - 1.0)*(model.z7_2_1 - 1.0) + \
    0.5*(model.x8_2_1 - 1.0)*(model.x8_2_1 - 1.0) + 0.5*(model.y8_2_1 - 1.0)*(model.y8_2_1 - 1.0) + \
    0.5*(model.z8_2_1 - 1.0)*(model.z8_2_1 - 1.0) + 0.5*(model.x9_2_1 - 1.0)*(model.x9_2_1 - 1.0) + \
    0.5*(model.y9_2_1 - 1.0)*(model.y9_2_1 - 1.0) + 0.5*(model.z9_2_1 - 1.0)*(model.z9_2_1 - 1.0) + \
    0.5*(model.x1_3_1 - 1.0)*(model.x1_3_1 - 1.0) + 0.5*(model.y1_3_1 - 1.0)*(model.y1_3_1 - 1.0) + \
    0.5*(model.z1_3_1 - 1.0)*(model.z1_3_1 - 1.0) + 0.5*(model.x2_3_1 - 1.0)*(model.x2_3_1 - 1.0) + \
    0.5*(model.y2_3_1 - 1.0)*(model.y2_3_1 - 1.0) + 0.5*(model.z2_3_1 - 1.0)*(model.z2_3_1 - 1.0) + \
    0.5*(model.x3_3_1 - 1.0)*(model.x3_3_1 - 1.0) + 0.5*(model.y3_3_1 - 1.0)*(model.y3_3_1 - 1.0) + \
    0.5*(model.z3_3_1 - 1.0)*(model.z3_3_1 - 1.0) + 0.5*(model.x4_3_1 - 1.0)*(model.x4_3_1 - 1.0) + \
    0.5*(model.y4_3_1 - 1.0)*(model.y4_3_1 - 1.0) + 0.5*(model.z4_3_1 - 1.0)*(model.z4_3_1 - 1.0) + \
    0.5*(model.x5_3_1 - 1.0)*(model.x5_3_1 - 1.0) + 0.5*(model.y5_3_1 - 1.0)*(model.y5_3_1 - 1.0) + \
    0.5*(model.z5_3_1 - 1.0)*(model.z5_3_1 - 1.0) + 0.5*(model.x6_3_1 - 1.0)*(model.x6_3_1 - 1.0) + \
    0.5*(model.y6_3_1 - 1.0)*(model.y6_3_1 - 1.0) + 0.5*(model.z6_3_1 - 1.0)*(model.z6_3_1 - 1.0) + \
    0.5*(model.x7_3_1 - 1.0)*(model.x7_3_1 - 1.0) + 0.5*(model.y7_3_1 - 1.0)*(model.y7_3_1 - 1.0) + \
    0.5*(model.z7_3_1 - 1.0)*(model.z7_3_1 - 1.0) + 0.5*(model.x8_3_1 - 1.0)*(model.x8_3_1 - 1.0) + \
    0.5*(model.y8_3_1 - 1.0)*(model.y8_3_1 - 1.0) + 0.5*(model.z8_3_1 - 1.0)*(model.z8_3_1 - 1.0) + \
    0.5*(model.x9_3_1 - 1.0)*(model.x9_3_1 - 1.0) + 0.5*(model.y9_3_1 - 1.0)*(model.y9_3_1 - 1.0) + \
    0.5*(model.z9_3_1 - 1.0)*(model.z9_3_1 - 1.0) + 0.5*(model.x1_4_1 - 1.0)*(model.x1_4_1 - 1.0) + \
    0.5*(model.y1_4_1 - 1.0)*(model.y1_4_1 - 1.0) + 0.5*(model.z1_4_1 - 1.0)*(model.z1_4_1 - 1.0) + \
    0.5*(model.x2_4_1 - 1.0)*(model.x2_4_1 - 1.0) + 0.5*(model.y2_4_1 - 1.0)*(model.y2_4_1 - 1.0) + \
    0.5*(model.z2_4_1 - 1.0)*(model.z2_4_1 - 1.0) + 0.5*(model.x3_4_1 - 1.0)*(model.x3_4_1 - 1.0) + \
    0.5*(model.y3_4_1 - 1.0)*(model.y3_4_1 - 1.0) + 0.5*(model.z3_4_1 - 1.0)*(model.z3_4_1 - 1.0) + \
    0.5*(model.x4_4_1 - 1.0)*(model.x4_4_1 - 1.0) + 0.5*(model.y4_4_1 - 1.0)*(model.y4_4_1 - 1.0) + \
    0.5*(model.z4_4_1 - 1.0)*(model.z4_4_1 - 1.0) + 0.5*(model.x5_4_1 - 1.0)*(model.x5_4_1 - 1.0) + \
    0.5*(model.y5_4_1 - 1.0)*(model.y5_4_1 - 1.0) + 0.5*(model.z5_4_1 - 1.0)*(model.z5_4_1 - 1.0) + \
    0.5*(model.x6_4_1 - 1.0)*(model.x6_4_1 - 1.0) + 0.5*(model.y6_4_1 - 1.0)*(model.y6_4_1 - 1.0) + \
    0.5*(model.z6_4_1 - 1.0)*(model.z6_4_1 - 1.0) + 0.5*(model.x7_4_1 - 1.0)*(model.x7_4_1 - 1.0) + \
    0.5*(model.y7_4_1 - 1.0)*(model.y7_4_1 - 1.0) + 0.5*(model.z7_4_1 - 1.0)*(model.z7_4_1 - 1.0) + \
    0.5*(model.x8_4_1 - 1.0)*(model.x8_4_1 - 1.0) + 0.5*(model.y8_4_1 - 1.0)*(model.y8_4_1 - 1.0) + \
    0.5*(model.z8_4_1 - 1.0)*(model.z8_4_1 - 1.0) + 0.5*(model.x9_4_1 - 1.0)*(model.x9_4_1 - 1.0) + \
    0.5*(model.y9_4_1 - 1.0)*(model.y9_4_1 - 1.0) + 0.5*(model.z9_4_1 - 1.0)*(model.z9_4_1 - 1.0) + \
    0.5*(model.x1_5_1 - 1.0)*(model.x1_5_1 - 1.0) + 0.5*(model.y1_5_1 - 1.0)*(model.y1_5_1 - 1.0) + \
    0.5*(model.z1_5_1 - 1.0)*(model.z1_5_1 - 1.0) + 0.5*(model.x2_5_1 - 1.0)*(model.x2_5_1 - 1.0) + \
    0.5*(model.y2_5_1 - 1.0)*(model.y2_5_1 - 1.0) + 0.5*(model.z2_5_1 - 1.0)*(model.z2_5_1 - 1.0) + \
    0.5*(model.x3_5_1 - 1.0)*(model.x3_5_1 - 1.0) + 0.5*(model.y3_5_1 - 1.0)*(model.y3_5_1 - 1.0) + \
    0.5*(model.z3_5_1 - 1.0)*(model.z3_5_1 - 1.0) + 0.5*(model.x4_5_1 - 1.0)*(model.x4_5_1 - 1.0) + \
    0.5*(model.y4_5_1 - 1.0)*(model.y4_5_1 - 1.0) + 0.5*(model.z4_5_1 - 1.0)*(model.z4_5_1 - 1.0) + \
    0.5*(model.x5_5_1 - 1.0)*(model.x5_5_1 - 1.0) + 0.5*(model.y5_5_1 - 1.0)*(model.y5_5_1 - 1.0) + \
    0.5*(model.z5_5_1 - 1.0)*(model.z5_5_1 - 1.0) + 0.5*(model.x6_5_1 - 1.0)*(model.x6_5_1 - 1.0) + \
    0.5*(model.y6_5_1 - 1.0)*(model.y6_5_1 - 1.0) + 0.5*(model.z6_5_1 - 1.0)*(model.z6_5_1 - 1.0) + \
    0.5*(model.x7_5_1 - 1.0)*(model.x7_5_1 - 1.0) + 0.5*(model.y7_5_1 - 1.0)*(model.y7_5_1 - 1.0) + \
    0.5*(model.z7_5_1 - 1.0)*(model.z7_5_1 - 1.0) + 0.5*(model.x8_5_1 - 1.0)*(model.x8_5_1 - 1.0) + \
    0.5*(model.y8_5_1 - 1.0)*(model.y8_5_1 - 1.0) + 0.5*(model.z8_5_1 - 1.0)*(model.z8_5_1 - 1.0) + \
    0.5*(model.x9_5_1 - 1.0)*(model.x9_5_1 - 1.0) + 0.5*(model.y9_5_1 - 1.0)*(model.y9_5_1 - 1.0) + \
    0.5*(model.z9_5_1 - 1.0)*(model.z9_5_1 - 1.0) + 0.5*(model.x1_6_1 - 1.0)*(model.x1_6_1 - 1.0) + \
    0.5*(model.y1_6_1 - 1.0)*(model.y1_6_1 - 1.0) + 0.5*(model.z1_6_1 - 1.0)*(model.z1_6_1 - 1.0) + \
    0.5*(model.x2_6_1 - 1.0)*(model.x2_6_1 - 1.0) + 0.5*(model.y2_6_1 - 1.0)*(model.y2_6_1 - 1.0) + \
    0.5*(model.z2_6_1 - 1.0)*(model.z2_6_1 - 1.0) + 0.5*(model.x3_6_1 - 1.0)*(model.x3_6_1 - 1.0) + \
    0.5*(model.y3_6_1 - 1.0)*(model.y3_6_1 - 1.0) + 0.5*(model.z3_6_1 - 1.0)*(model.z3_6_1 - 1.0) + \
    0.5*(model.x4_6_1 - 1.0)*(model.x4_6_1 - 1.0) + 0.5*(model.y4_6_1 - 1.0)*(model.y4_6_1 - 1.0) + \
    0.5*(model.z4_6_1 - 1.0)*(model.z4_6_1 - 1.0) + 0.5*(model.x5_6_1 - 1.0)*(model.x5_6_1 - 1.0) + \
    0.5*(model.y5_6_1 - 1.0)*(model.y5_6_1 - 1.0) + 0.5*(model.z5_6_1 - 1.0)*(model.z5_6_1 - 1.0) + \
    0.5*(model.x6_6_1 - 1.0)*(model.x6_6_1 - 1.0) + 0.5*(model.y6_6_1 - 1.0)*(model.y6_6_1 - 1.0) + \
    0.5*(model.z6_6_1 - 1.0)*(model.z6_6_1 - 1.0) + 0.5*(model.x7_6_1 - 1.0)*(model.x7_6_1 - 1.0) + \
    0.5*(model.y7_6_1 - 1.0)*(model.y7_6_1 - 1.0) + 0.5*(model.z7_6_1 - 1.0)*(model.z7_6_1 - 1.0) + \
    0.5*(model.x8_6_1 - 1.0)*(model.x8_6_1 - 1.0) + 0.5*(model.y8_6_1 - 1.0)*(model.y8_6_1 - 1.0) + \
    0.5*(model.z8_6_1 - 1.0)*(model.z8_6_1 - 1.0) + 0.5*(model.x9_6_1 - 1.0)*(model.x9_6_1 - 1.0) + \
    0.5*(model.y9_6_1 - 1.0)*(model.y9_6_1 - 1.0) + 0.5*(model.z9_6_1 - 1.0)*(model.z9_6_1 - 1.0) + \
    0.5*(model.x1_7_1 - 1.0)*(model.x1_7_1 - 1.0) + 0.5*(model.y1_7_1 - 1.0)*(model.y1_7_1 - 1.0) + \
    0.5*(model.z1_7_1 - 1.0)*(model.z1_7_1 - 1.0) + 0.5*(model.x2_7_1 - 1.0)*(model.x2_7_1 - 1.0) + \
    0.5*(model.y2_7_1 - 1.0)*(model.y2_7_1 - 1.0) + 0.5*(model.z2_7_1 - 1.0)*(model.z2_7_1 - 1.0) + \
    0.5*(model.x3_7_1 - 1.0)*(model.x3_7_1 - 1.0) + 0.5*(model.y3_7_1 - 1.0)*(model.y3_7_1 - 1.0) + \
    0.5*(model.z3_7_1 - 1.0)*(model.z3_7_1 - 1.0) + 0.5*(model.x4_7_1 - 1.0)*(model.x4_7_1 - 1.0) + \
    0.5*(model.y4_7_1 - 1.0)*(model.y4_7_1 - 1.0) + 0.5*(model.z4_7_1 - 1.0)*(model.z4_7_1 - 1.0) + \
    0.5*(model.x5_7_1 - 1.0)*(model.x5_7_1 - 1.0) + 0.5*(model.y5_7_1 - 1.0)*(model.y5_7_1 - 1.0) + \
    0.5*(model.z5_7_1 - 1.0)*(model.z5_7_1 - 1.0) + 0.5*(model.x6_7_1 - 1.0)*(model.x6_7_1 - 1.0) + \
    0.5*(model.y6_7_1 - 1.0)*(model.y6_7_1 - 1.0) + 0.5*(model.z6_7_1 - 1.0)*(model.z6_7_1 - 1.0) + \
    0.5*(model.x7_7_1 - 1.0)*(model.x7_7_1 - 1.0) + 0.5*(model.y7_7_1 - 1.0)*(model.y7_7_1 - 1.0) + \
    0.5*(model.z7_7_1 - 1.0)*(model.z7_7_1 - 1.0) + 0.5*(model.x8_7_1 - 1.0)*(model.x8_7_1 - 1.0) + \
    0.5*(model.y8_7_1 - 1.0)*(model.y8_7_1 - 1.0) + 0.5*(model.z8_7_1 - 1.0)*(model.z8_7_1 - 1.0) + \
    0.5*(model.x9_7_1 - 1.0)*(model.x9_7_1 - 1.0) + 0.5*(model.y9_7_1 - 1.0)*(model.y9_7_1 - 1.0) + \
    0.5*(model.z9_7_1 - 1.0)*(model.z9_7_1 - 1.0) + 0.5*(model.x1_8_1 - 1.0)*(model.x1_8_1 - 1.0) + \
    0.5*(model.y1_8_1 - 1.0)*(model.y1_8_1 - 1.0) + 0.5*(model.z1_8_1 - 1.0)*(model.z1_8_1 - 1.0) + \
    0.5*(model.x2_8_1 - 1.0)*(model.x2_8_1 - 1.0) + 0.5*(model.y2_8_1 - 1.0)*(model.y2_8_1 - 1.0) + \
    0.5*(model.z2_8_1 - 1.0)*(model.z2_8_1 - 1.0) + 0.5*(model.x3_8_1 - 1.0)*(model.x3_8_1 - 1.0) + \
    0.5*(model.y3_8_1 - 1.0)*(model.y3_8_1 - 1.0) + 0.5*(model.z3_8_1 - 1.0)*(model.z3_8_1 - 1.0) + \
    0.5*(model.x4_8_1 - 1.0)*(model.x4_8_1 - 1.0) + 0.5*(model.y4_8_1 - 1.0)*(model.y4_8_1 - 1.0) + \
    0.5*(model.z4_8_1 - 1.0)*(model.z4_8_1 - 1.0) + 0.5*(model.x5_8_1 - 1.0)*(model.x5_8_1 - 1.0) + \
    0.5*(model.y5_8_1 - 1.0)*(model.y5_8_1 - 1.0) + 0.5*(model.z5_8_1 - 1.0)*(model.z5_8_1 - 1.0) + \
    0.5*(model.x6_8_1 - 1.0)*(model.x6_8_1 - 1.0) + 0.5*(model.y6_8_1 - 1.0)*(model.y6_8_1 - 1.0) + \
    0.5*(model.z6_8_1 - 1.0)*(model.z6_8_1 - 1.0) + 0.5*(model.x7_8_1 - 1.0)*(model.x7_8_1 - 1.0) + \
    0.5*(model.y7_8_1 - 1.0)*(model.y7_8_1 - 1.0) + 0.5*(model.z7_8_1 - 1.0)*(model.z7_8_1 - 1.0) + \
    0.5*(model.x8_8_1 - 1.0)*(model.x8_8_1 - 1.0) + 0.5*(model.y8_8_1 - 1.0)*(model.y8_8_1 - 1.0) + \
    0.5*(model.z8_8_1 - 1.0)*(model.z8_8_1 - 1.0) + 0.5*(model.x9_8_1 - 1.0)*(model.x9_8_1 - 1.0) + \
    0.5*(model.y9_8_1 - 1.0)*(model.y9_8_1 - 1.0) + 0.5*(model.z9_8_1 - 1.0)*(model.z9_8_1 - 1.0) + \
    0.5*(model.x1_9_1 - 1.0)*(model.x1_9_1 - 1.0) + 0.5*(model.y1_9_1 - 1.0)*(model.y1_9_1 - 1.0) + \
    0.5*(model.z1_9_1 - 1.0)*(model.z1_9_1 - 1.0) + 0.5*(model.x2_9_1 - 1.0)*(model.x2_9_1 - 1.0) + \
    0.5*(model.y2_9_1 - 1.0)*(model.y2_9_1 - 1.0) + 0.5*(model.z2_9_1 - 1.0)*(model.z2_9_1 - 1.0) + \
    0.5*(model.x3_9_1 - 1.0)*(model.x3_9_1 - 1.0) + 0.5*(model.y3_9_1 - 1.0)*(model.y3_9_1 - 1.0) + \
    0.5*(model.z3_9_1 - 1.0)*(model.z3_9_1 - 1.0) + 0.5*(model.x4_9_1 - 1.0)*(model.x4_9_1 - 1.0) + \
    0.5*(model.y4_9_1 - 1.0)*(model.y4_9_1 - 1.0) + 0.5*(model.z4_9_1 - 1.0)*(model.z4_9_1 - 1.0) + \
    0.5*(model.x5_9_1 - 1.0)*(model.x5_9_1 - 1.0) + 0.5*(model.y5_9_1 - 1.0)*(model.y5_9_1 - 1.0) + \
    0.5*(model.z5_9_1 - 1.0)*(model.z5_9_1 - 1.0) + 0.5*(model.x6_9_1 - 1.0)*(model.x6_9_1 - 1.0) + \
    0.5*(model.y6_9_1 - 1.0)*(model.y6_9_1 - 1.0) + 0.5*(model.z6_9_1 - 1.0)*(model.z6_9_1 - 1.0) + \
    0.5*(model.x7_9_1 - 1.0)*(model.x7_9_1 - 1.0) + 0.5*(model.y7_9_1 - 1.0)*(model.y7_9_1 - 1.0) + \
    0.5*(model.z7_9_1 - 1.0)*(model.z7_9_1 - 1.0) + 0.5*(model.x8_9_1 - 1.0)*(model.x8_9_1 - 1.0) + \
    0.5*(model.y8_9_1 - 1.0)*(model.y8_9_1 - 1.0) + 0.5*(model.z8_9_1 - 1.0)*(model.z8_9_1 - 1.0) + \
    0.5*(model.x9_9_1 - 1.0)*(model.x9_9_1 - 1.0) + 0.5*(model.y9_9_1 - 1.0)*(model.y9_9_1 - 1.0) + \
    0.5*(model.z9_9_1 - 1.0)*(model.z9_9_1 - 1.0) + 0.5*(model.x1_1_2 - 1.0)*(model.x1_1_2 - 1.0) + \
    0.5*(model.y1_1_2 - 1.0)*(model.y1_1_2 - 1.0) + 0.5*(model.z1_1_2 - 1.0)*(model.z1_1_2 - 1.0) + \
    0.5*(model.x2_1_2 - 1.0)*(model.x2_1_2 - 1.0) + 0.5*(model.y2_1_2 - 1.0)*(model.y2_1_2 - 1.0) + \
    0.5*(model.z2_1_2 - 1.0)*(model.z2_1_2 - 1.0) + 0.5*(model.x3_1_2 - 1.0)*(model.x3_1_2 - 1.0) + \
    0.5*(model.y3_1_2 - 1.0)*(model.y3_1_2 - 1.0) + 0.5*(model.z3_1_2 - 1.0)*(model.z3_1_2 - 1.0) + \
    0.5*(model.x4_1_2 - 1.0)*(model.x4_1_2 - 1.0) + 0.5*(model.y4_1_2 - 1.0)*(model.y4_1_2 - 1.0) + \
    0.5*(model.z4_1_2 - 1.0)*(model.z4_1_2 - 1.0) + 0.5*(model.x5_1_2 - 1.0)*(model.x5_1_2 - 1.0) + \
    0.5*(model.y5_1_2 - 1.0)*(model.y5_1_2 - 1.0) + 0.5*(model.z5_1_2 - 1.0)*(model.z5_1_2 - 1.0) + \
    0.5*(model.x6_1_2 - 1.0)*(model.x6_1_2 - 1.0) + 0.5*(model.y6_1_2 - 1.0)*(model.y6_1_2 - 1.0) + \
    0.5*(model.z6_1_2 - 1.0)*(model.z6_1_2 - 1.0) + 0.5*(model.x7_1_2 - 1.0)*(model.x7_1_2 - 1.0) + \
    0.5*(model.y7_1_2 - 1.0)*(model.y7_1_2 - 1.0) + 0.5*(model.z7_1_2 - 1.0)*(model.z7_1_2 - 1.0) + \
    0.5*(model.x8_1_2 - 1.0)*(model.x8_1_2 - 1.0) + 0.5*(model.y8_1_2 - 1.0)*(model.y8_1_2 - 1.0) + \
    0.5*(model.z8_1_2 - 1.0)*(model.z8_1_2 - 1.0) + 0.5*(model.x9_1_2 - 1.0)*(model.x9_1_2 - 1.0) + \
    0.5*(model.y9_1_2 - 1.0)*(model.y9_1_2 - 1.0) + 0.5*(model.z9_1_2 - 1.0)*(model.z9_1_2 - 1.0) + \
    0.5*(model.x1_2_2 - 1.0)*(model.x1_2_2 - 1.0) + 0.5*(model.y1_2_2 - 1.0)*(model.y1_2_2 - 1.0) + \
    0.5*(model.z1_2_2 - 1.0)*(model.z1_2_2 - 1.0) + 0.5*(model.x2_2_2 - 1.0)*(model.x2_2_2 - 1.0) + \
    0.5*(model.y2_2_2 - 1.0)*(model.y2_2_2 - 1.0) + 0.5*(model.z2_2_2 - 1.0)*(model.z2_2_2 - 1.0) + \
    0.5*(model.x3_2_2 - 1.0)*(model.x3_2_2 - 1.0) + 0.5*(model.y3_2_2 - 1.0)*(model.y3_2_2 - 1.0) + \
    0.5*(model.z3_2_2 - 1.0)*(model.z3_2_2 - 1.0) + 0.5*(model.x4_2_2 - 1.0)*(model.x4_2_2 - 1.0) + \
    0.5*(model.y4_2_2 - 1.0)*(model.y4_2_2 - 1.0) + 0.5*(model.z4_2_2 - 1.0)*(model.z4_2_2 - 1.0) + \
    0.5*(model.x5_2_2 - 1.0)*(model.x5_2_2 - 1.0) + 0.5*(model.y5_2_2 - 1.0)*(model.y5_2_2 - 1.0) + \
    0.5*(model.z5_2_2 - 1.0)*(model.z5_2_2 - 1.0) + 0.5*(model.x6_2_2 - 1.0)*(model.x6_2_2 - 1.0) + \
    0.5*(model.y6_2_2 - 1.0)*(model.y6_2_2 - 1.0) + 0.5*(model.z6_2_2 - 1.0)*(model.z6_2_2 - 1.0) + \
    0.5*(model.x7_2_2 - 1.0)*(model.x7_2_2 - 1.0) + 0.5*(model.y7_2_2 - 1.0)*(model.y7_2_2 - 1.0) + \
    0.5*(model.z7_2_2 - 1.0)*(model.z7_2_2 - 1.0) + 0.5*(model.x8_2_2 - 1.0)*(model.x8_2_2 - 1.0) + \
    0.5*(model.y8_2_2 - 1.0)*(model.y8_2_2 - 1.0) + 0.5*(model.z8_2_2 - 1.0)*(model.z8_2_2 - 1.0) + \
    0.5*(model.x9_2_2 - 1.0)*(model.x9_2_2 - 1.0) + 0.5*(model.y9_2_2 - 1.0)*(model.y9_2_2 - 1.0) + \
    0.5*(model.z9_2_2 - 1.0)*(model.z9_2_2 - 1.0) + 0.5*(model.x1_3_2 - 1.0)*(model.x1_3_2 - 1.0) + \
    0.5*(model.y1_3_2 - 1.0)*(model.y1_3_2 - 1.0) + 0.5*(model.z1_3_2 - 1.0)*(model.z1_3_2 - 1.0) + \
    0.5*(model.x2_3_2 - 1.0)*(model.x2_3_2 - 1.0) + 0.5*(model.y2_3_2 - 1.0)*(model.y2_3_2 - 1.0) + \
    0.5*(model.z2_3_2 - 1.0)*(model.z2_3_2 - 1.0) + 0.5*(model.x3_3_2 - 1.0)*(model.x3_3_2 - 1.0) + \
    0.5*(model.y3_3_2 - 1.0)*(model.y3_3_2 - 1.0) + 0.5*(model.z3_3_2 - 1.0)*(model.z3_3_2 - 1.0) + \
    0.5*(model.x4_3_2 - 1.0)*(model.x4_3_2 - 1.0) + 0.5*(model.y4_3_2 - 1.0)*(model.y4_3_2 - 1.0) + \
    0.5*(model.z4_3_2 - 1.0)*(model.z4_3_2 - 1.0) + 0.5*(model.x5_3_2 - 1.0)*(model.x5_3_2 - 1.0) + \
    0.5*(model.y5_3_2 - 1.0)*(model.y5_3_2 - 1.0) + 0.5*(model.z5_3_2 - 1.0)*(model.z5_3_2 - 1.0) + \
    0.5*(model.x6_3_2 - 1.0)*(model.x6_3_2 - 1.0) + 0.5*(model.y6_3_2 - 1.0)*(model.y6_3_2 - 1.0) + \
    0.5*(model.z6_3_2 - 1.0)*(model.z6_3_2 - 1.0) + 0.5*(model.x7_3_2 - 1.0)*(model.x7_3_2 - 1.0) + \
    0.5*(model.y7_3_2 - 1.0)*(model.y7_3_2 - 1.0) + 0.5*(model.z7_3_2 - 1.0)*(model.z7_3_2 - 1.0) + \
    0.5*(model.x8_3_2 - 1.0)*(model.x8_3_2 - 1.0) + 0.5*(model.y8_3_2 - 1.0)*(model.y8_3_2 - 1.0) + \
    0.5*(model.z8_3_2 - 1.0)*(model.z8_3_2 - 1.0) + 0.5*(model.x9_3_2 - 1.0)*(model.x9_3_2 - 1.0) + \
    0.5*(model.y9_3_2 - 1.0)*(model.y9_3_2 - 1.0) + 0.5*(model.z9_3_2 - 1.0)*(model.z9_3_2 - 1.0) + \
    0.5*(model.x1_4_2 - 1.0)*(model.x1_4_2 - 1.0) + 0.5*(model.y1_4_2 - 1.0)*(model.y1_4_2 - 1.0) + \
    0.5*(model.z1_4_2 - 1.0)*(model.z1_4_2 - 1.0) + 0.5*(model.x2_4_2 - 1.0)*(model.x2_4_2 - 1.0) + \
    0.5*(model.y2_4_2 - 1.0)*(model.y2_4_2 - 1.0) + 0.5*(model.z2_4_2 - 1.0)*(model.z2_4_2 - 1.0) + \
    0.5*(model.x3_4_2 - 1.0)*(model.x3_4_2 - 1.0) + 0.5*(model.y3_4_2 - 1.0)*(model.y3_4_2 - 1.0) + \
    0.5*(model.z3_4_2 - 1.0)*(model.z3_4_2 - 1.0) + 0.5*(model.x4_4_2 - 1.0)*(model.x4_4_2 - 1.0) + \
    0.5*(model.y4_4_2 - 1.0)*(model.y4_4_2 - 1.0) + 0.5*(model.z4_4_2 - 1.0)*(model.z4_4_2 - 1.0) + \
    0.5*(model.x5_4_2 - 1.0)*(model.x5_4_2 - 1.0) + 0.5*(model.y5_4_2 - 1.0)*(model.y5_4_2 - 1.0) + \
    0.5*(model.z5_4_2 - 1.0)*(model.z5_4_2 - 1.0) + 0.5*(model.x6_4_2 - 1.0)*(model.x6_4_2 - 1.0) + \
    0.5*(model.y6_4_2 - 1.0)*(model.y6_4_2 - 1.0) + 0.5*(model.z6_4_2 - 1.0)*(model.z6_4_2 - 1.0) + \
    0.5*(model.x7_4_2 - 1.0)*(model.x7_4_2 - 1.0) + 0.5*(model.y7_4_2 - 1.0)*(model.y7_4_2 - 1.0) + \
    0.5*(model.z7_4_2 - 1.0)*(model.z7_4_2 - 1.0) + 0.5*(model.x8_4_2 - 1.0)*(model.x8_4_2 - 1.0) + \
    0.5*(model.y8_4_2 - 1.0)*(model.y8_4_2 - 1.0) + 0.5*(model.z8_4_2 - 1.0)*(model.z8_4_2 - 1.0) + \
    0.5*(model.x9_4_2 - 1.0)*(model.x9_4_2 - 1.0) + 0.5*(model.y9_4_2 - 1.0)*(model.y9_4_2 - 1.0) + \
    0.5*(model.z9_4_2 - 1.0)*(model.z9_4_2 - 1.0) + 0.5*(model.x1_5_2 - 1.0)*(model.x1_5_2 - 1.0) + \
    0.5*(model.y1_5_2 - 1.0)*(model.y1_5_2 - 1.0) + 0.5*(model.z1_5_2 - 1.0)*(model.z1_5_2 - 1.0) + \
    0.5*(model.x2_5_2 - 1.0)*(model.x2_5_2 - 1.0) + 0.5*(model.y2_5_2 - 1.0)*(model.y2_5_2 - 1.0) + \
    0.5*(model.z2_5_2 - 1.0)*(model.z2_5_2 - 1.0) + 0.5*(model.x3_5_2 - 1.0)*(model.x3_5_2 - 1.0) + \
    0.5*(model.y3_5_2 - 1.0)*(model.y3_5_2 - 1.0) + 0.5*(model.z3_5_2 - 1.0)*(model.z3_5_2 - 1.0) + \
    0.5*(model.x4_5_2 - 1.0)*(model.x4_5_2 - 1.0) + 0.5*(model.y4_5_2 - 1.0)*(model.y4_5_2 - 1.0) + \
    0.5*(model.z4_5_2 - 1.0)*(model.z4_5_2 - 1.0) + 0.5*(model.x5_5_2 - 1.0)*(model.x5_5_2 - 1.0) + \
    0.5*(model.y5_5_2 - 1.0)*(model.y5_5_2 - 1.0) + 0.5*(model.z5_5_2 - 1.0)*(model.z5_5_2 - 1.0) + \
    0.5*(model.x6_5_2 - 1.0)*(model.x6_5_2 - 1.0) + 0.5*(model.y6_5_2 - 1.0)*(model.y6_5_2 - 1.0) + \
    0.5*(model.z6_5_2 - 1.0)*(model.z6_5_2 - 1.0) + 0.5*(model.x7_5_2 - 1.0)*(model.x7_5_2 - 1.0) + \
    0.5*(model.y7_5_2 - 1.0)*(model.y7_5_2 - 1.0) + 0.5*(model.z7_5_2 - 1.0)*(model.z7_5_2 - 1.0) + \
    0.5*(model.x8_5_2 - 1.0)*(model.x8_5_2 - 1.0) + 0.5*(model.y8_5_2 - 1.0)*(model.y8_5_2 - 1.0) + \
    0.5*(model.z8_5_2 - 1.0)*(model.z8_5_2 - 1.0) + 0.5*(model.x9_5_2 - 1.0)*(model.x9_5_2 - 1.0) + \
    0.5*(model.y9_5_2 - 1.0)*(model.y9_5_2 - 1.0) + 0.5*(model.z9_5_2 - 1.0)*(model.z9_5_2 - 1.0) + \
    0.5*(model.x1_6_2 - 1.0)*(model.x1_6_2 - 1.0) + 0.5*(model.y1_6_2 - 1.0)*(model.y1_6_2 - 1.0) + \
    0.5*(model.z1_6_2 - 1.0)*(model.z1_6_2 - 1.0) + 0.5*(model.x2_6_2 - 1.0)*(model.x2_6_2 - 1.0) + \
    0.5*(model.y2_6_2 - 1.0)*(model.y2_6_2 - 1.0) + 0.5*(model.z2_6_2 - 1.0)*(model.z2_6_2 - 1.0) + \
    0.5*(model.x3_6_2 - 1.0)*(model.x3_6_2 - 1.0) + 0.5*(model.y3_6_2 - 1.0)*(model.y3_6_2 - 1.0) + \
    0.5*(model.z3_6_2 - 1.0)*(model.z3_6_2 - 1.0) + 0.5*(model.x4_6_2 - 1.0)*(model.x4_6_2 - 1.0) + \
    0.5*(model.y4_6_2 - 1.0)*(model.y4_6_2 - 1.0) + 0.5*(model.z4_6_2 - 1.0)*(model.z4_6_2 - 1.0) + \
    0.5*(model.x5_6_2 - 1.0)*(model.x5_6_2 - 1.0) + 0.5*(model.y5_6_2 - 1.0)*(model.y5_6_2 - 1.0) + \
    0.5*(model.z5_6_2 - 1.0)*(model.z5_6_2 - 1.0) + 0.5*(model.x6_6_2 - 1.0)*(model.x6_6_2 - 1.0) + \
    0.5*(model.y6_6_2 - 1.0)*(model.y6_6_2 - 1.0) + 0.5*(model.z6_6_2 - 1.0)*(model.z6_6_2 - 1.0) + \
    0.5*(model.x7_6_2 - 1.0)*(model.x7_6_2 - 1.0) + 0.5*(model.y7_6_2 - 1.0)*(model.y7_6_2 - 1.0) + \
    0.5*(model.z7_6_2 - 1.0)*(model.z7_6_2 - 1.0) + 0.5*(model.x8_6_2 - 1.0)*(model.x8_6_2 - 1.0) + \
    0.5*(model.y8_6_2 - 1.0)*(model.y8_6_2 - 1.0) + 0.5*(model.z8_6_2 - 1.0)*(model.z8_6_2 - 1.0) + \
    0.5*(model.x9_6_2 - 1.0)*(model.x9_6_2 - 1.0) + 0.5*(model.y9_6_2 - 1.0)*(model.y9_6_2 - 1.0) + \
    0.5*(model.z9_6_2 - 1.0)*(model.z9_6_2 - 1.0) + 0.5*(model.x1_7_2 - 1.0)*(model.x1_7_2 - 1.0) + \
    0.5*(model.y1_7_2 - 1.0)*(model.y1_7_2 - 1.0) + 0.5*(model.z1_7_2 - 1.0)*(model.z1_7_2 - 1.0) + \
    0.5*(model.x2_7_2 - 1.0)*(model.x2_7_2 - 1.0) + 0.5*(model.y2_7_2 - 1.0)*(model.y2_7_2 - 1.0) + \
    0.5*(model.z2_7_2 - 1.0)*(model.z2_7_2 - 1.0) + 0.5*(model.x3_7_2 - 1.0)*(model.x3_7_2 - 1.0) + \
    0.5*(model.y3_7_2 - 1.0)*(model.y3_7_2 - 1.0) + 0.5*(model.z3_7_2 - 1.0)*(model.z3_7_2 - 1.0) + \
    0.5*(model.x4_7_2 - 1.0)*(model.x4_7_2 - 1.0) + 0.5*(model.y4_7_2 - 1.0)*(model.y4_7_2 - 1.0) + \
    0.5*(model.z4_7_2 - 1.0)*(model.z4_7_2 - 1.0) + 0.5*(model.x5_7_2 - 1.0)*(model.x5_7_2 - 1.0) + \
    0.5*(model.y5_7_2 - 1.0)*(model.y5_7_2 - 1.0) + 0.5*(model.z5_7_2 - 1.0)*(model.z5_7_2 - 1.0) + \
    0.5*(model.x6_7_2 - 1.0)*(model.x6_7_2 - 1.0) + 0.5*(model.y6_7_2 - 1.0)*(model.y6_7_2 - 1.0) + \
    0.5*(model.z6_7_2 - 1.0)*(model.z6_7_2 - 1.0) + 0.5*(model.x7_7_2 - 1.0)*(model.x7_7_2 - 1.0) + \
    0.5*(model.y7_7_2 - 1.0)*(model.y7_7_2 - 1.0) + 0.5*(model.z7_7_2 - 1.0)*(model.z7_7_2 - 1.0) + \
    0.5*(model.x8_7_2 - 1.0)*(model.x8_7_2 - 1.0) + 0.5*(model.y8_7_2 - 1.0)*(model.y8_7_2 - 1.0) + \
    0.5*(model.z8_7_2 - 1.0)*(model.z8_7_2 - 1.0) + 0.5*(model.x9_7_2 - 1.0)*(model.x9_7_2 - 1.0) + \
    0.5*(model.y9_7_2 - 1.0)*(model.y9_7_2 - 1.0) + 0.5*(model.z9_7_2 - 1.0)*(model.z9_7_2 - 1.0) + \
    0.5*(model.x1_8_2 - 1.0)*(model.x1_8_2 - 1.0) + 0.5*(model.y1_8_2 - 1.0)*(model.y1_8_2 - 1.0) + \
    0.5*(model.z1_8_2 - 1.0)*(model.z1_8_2 - 1.0) + 0.5*(model.x2_8_2 - 1.0)*(model.x2_8_2 - 1.0) + \
    0.5*(model.y2_8_2 - 1.0)*(model.y2_8_2 - 1.0) + 0.5*(model.z2_8_2 - 1.0)*(model.z2_8_2 - 1.0) + \
    0.5*(model.x3_8_2 - 1.0)*(model.x3_8_2 - 1.0) + 0.5*(model.y3_8_2 - 1.0)*(model.y3_8_2 - 1.0) + \
    0.5*(model.z3_8_2 - 1.0)*(model.z3_8_2 - 1.0) + 0.5*(model.x4_8_2 - 1.0)*(model.x4_8_2 - 1.0) + \
    0.5*(model.y4_8_2 - 1.0)*(model.y4_8_2 - 1.0) + 0.5*(model.z4_8_2 - 1.0)*(model.z4_8_2 - 1.0) + \
    0.5*(model.x5_8_2 - 1.0)*(model.x5_8_2 - 1.0) + 0.5*(model.y5_8_2 - 1.0)*(model.y5_8_2 - 1.0) + \
    0.5*(model.z5_8_2 - 1.0)*(model.z5_8_2 - 1.0) + 0.5*(model.x6_8_2 - 1.0)*(model.x6_8_2 - 1.0) + \
    0.5*(model.y6_8_2 - 1.0)*(model.y6_8_2 - 1.0) + 0.5*(model.z6_8_2 - 1.0)*(model.z6_8_2 - 1.0) + \
    0.5*(model.x7_8_2 - 1.0)*(model.x7_8_2 - 1.0) + 0.5*(model.y7_8_2 - 1.0)*(model.y7_8_2 - 1.0) + \
    0.5*(model.z7_8_2 - 1.0)*(model.z7_8_2 - 1.0) + 0.5*(model.x8_8_2 - 1.0)*(model.x8_8_2 - 1.0) + \
    0.5*(model.y8_8_2 - 1.0)*(model.y8_8_2 - 1.0) + 0.5*(model.z8_8_2 - 1.0)*(model.z8_8_2 - 1.0) + \
    0.5*(model.x9_8_2 - 1.0)*(model.x9_8_2 - 1.0) + 0.5*(model.y9_8_2 - 1.0)*(model.y9_8_2 - 1.0) + \
    0.5*(model.z9_8_2 - 1.0)*(model.z9_8_2 - 1.0) + 0.5*(model.x1_9_2 - 1.0)*(model.x1_9_2 - 1.0) + \
    0.5*(model.y1_9_2 - 1.0)*(model.y1_9_2 - 1.0) + 0.5*(model.z1_9_2 - 1.0)*(model.z1_9_2 - 1.0) + \
    0.5*(model.x2_9_2 - 1.0)*(model.x2_9_2 - 1.0) + 0.5*(model.y2_9_2 - 1.0)*(model.y2_9_2 - 1.0) + \
    0.5*(model.z2_9_2 - 1.0)*(model.z2_9_2 - 1.0) + 0.5*(model.x3_9_2 - 1.0)*(model.x3_9_2 - 1.0) + \
    0.5*(model.y3_9_2 - 1.0)*(model.y3_9_2 - 1.0) + 0.5*(model.z3_9_2 - 1.0)*(model.z3_9_2 - 1.0) + \
    0.5*(model.x4_9_2 - 1.0)*(model.x4_9_2 - 1.0) + 0.5*(model.y4_9_2 - 1.0)*(model.y4_9_2 - 1.0) + \
    0.5*(model.z4_9_2 - 1.0)*(model.z4_9_2 - 1.0) + 0.5*(model.x5_9_2 - 1.0)*(model.x5_9_2 - 1.0) + \
    0.5*(model.y5_9_2 - 1.0)*(model.y5_9_2 - 1.0) + 0.5*(model.z5_9_2 - 1.0)*(model.z5_9_2 - 1.0) + \
    0.5*(model.x6_9_2 - 1.0)*(model.x6_9_2 - 1.0) + 0.5*(model.y6_9_2 - 1.0)*(model.y6_9_2 - 1.0) + \
    0.5*(model.z6_9_2 - 1.0)*(model.z6_9_2 - 1.0) + 0.5*(model.x7_9_2 - 1.0)*(model.x7_9_2 - 1.0) + \
    0.5*(model.y7_9_2 - 1.0)*(model.y7_9_2 - 1.0) + 0.5*(model.z7_9_2 - 1.0)*(model.z7_9_2 - 1.0) + \
    0.5*(model.x8_9_2 - 1.0)*(model.x8_9_2 - 1.0) + 0.5*(model.y8_9_2 - 1.0)*(model.y8_9_2 - 1.0) + \
    0.5*(model.z8_9_2 - 1.0)*(model.z8_9_2 - 1.0) + 0.5*(model.x9_9_2 - 1.0)*(model.x9_9_2 - 1.0) + \
    0.5*(model.y9_9_2 - 1.0)*(model.y9_9_2 - 1.0) + 0.5*(model.z9_9_2 - 1.0)*(model.z9_9_2 - 1.0) + \
    0.5*(model.x1_1_3 - 1.0)*(model.x1_1_3 - 1.0) + 0.5*(model.y1_1_3 - 1.0)*(model.y1_1_3 - 1.0) + \
    0.5*(model.z1_1_3 - 1.0)*(model.z1_1_3 - 1.0) + 0.5*(model.x2_1_3 - 1.0)*(model.x2_1_3 - 1.0) + \
    0.5*(model.y2_1_3 - 1.0)*(model.y2_1_3 - 1.0) + 0.5*(model.z2_1_3 - 1.0)*(model.z2_1_3 - 1.0) + \
    0.5*(model.x3_1_3 - 1.0)*(model.x3_1_3 - 1.0) + 0.5*(model.y3_1_3 - 1.0)*(model.y3_1_3 - 1.0) + \
    0.5*(model.z3_1_3 - 1.0)*(model.z3_1_3 - 1.0) + 0.5*(model.x4_1_3 - 1.0)*(model.x4_1_3 - 1.0) + \
    0.5*(model.y4_1_3 - 1.0)*(model.y4_1_3 - 1.0) + 0.5*(model.z4_1_3 - 1.0)*(model.z4_1_3 - 1.0) + \
    0.5*(model.x5_1_3 - 1.0)*(model.x5_1_3 - 1.0) + 0.5*(model.y5_1_3 - 1.0)*(model.y5_1_3 - 1.0) + \
    0.5*(model.z5_1_3 - 1.0)*(model.z5_1_3 - 1.0) + 0.5*(model.x6_1_3 - 1.0)*(model.x6_1_3 - 1.0) + \
    0.5*(model.y6_1_3 - 1.0)*(model.y6_1_3 - 1.0) + 0.5*(model.z6_1_3 - 1.0)*(model.z6_1_3 - 1.0) + \
    0.5*(model.x7_1_3 - 1.0)*(model.x7_1_3 - 1.0) + 0.5*(model.y7_1_3 - 1.0)*(model.y7_1_3 - 1.0) + \
    0.5*(model.z7_1_3 - 1.0)*(model.z7_1_3 - 1.0) + 0.5*(model.x8_1_3 - 1.0)*(model.x8_1_3 - 1.0) + \
    0.5*(model.y8_1_3 - 1.0)*(model.y8_1_3 - 1.0) + 0.5*(model.z8_1_3 - 1.0)*(model.z8_1_3 - 1.0) + \
    0.5*(model.x9_1_3 - 1.0)*(model.x9_1_3 - 1.0) + 0.5*(model.y9_1_3 - 1.0)*(model.y9_1_3 - 1.0) + \
    0.5*(model.z9_1_3 - 1.0)*(model.z9_1_3 - 1.0) + 0.5*(model.x1_2_3 - 1.0)*(model.x1_2_3 - 1.0) + \
    0.5*(model.y1_2_3 - 1.0)*(model.y1_2_3 - 1.0) + 0.5*(model.z1_2_3 - 1.0)*(model.z1_2_3 - 1.0) + \
    0.5*(model.x2_2_3 - 1.0)*(model.x2_2_3 - 1.0) + 0.5*(model.y2_2_3 - 1.0)*(model.y2_2_3 - 1.0) + \
    0.5*(model.z2_2_3 - 1.0)*(model.z2_2_3 - 1.0) + 0.5*(model.x3_2_3 - 1.0)*(model.x3_2_3 - 1.0) + \
    0.5*(model.y3_2_3 - 1.0)*(model.y3_2_3 - 1.0) + 0.5*(model.z3_2_3 - 1.0)*(model.z3_2_3 - 1.0) + \
    0.5*(model.x4_2_3 - 1.0)*(model.x4_2_3 - 1.0) + 0.5*(model.y4_2_3 - 1.0)*(model.y4_2_3 - 1.0) + \
    0.5*(model.z4_2_3 - 1.0)*(model.z4_2_3 - 1.0) + 0.5*(model.x5_2_3 - 1.0)*(model.x5_2_3 - 1.0) + \
    0.5*(model.y5_2_3 - 1.0)*(model.y5_2_3 - 1.0) + 0.5*(model.z5_2_3 - 1.0)*(model.z5_2_3 - 1.0) + \
    0.5*(model.x6_2_3 - 1.0)*(model.x6_2_3 - 1.0) + 0.5*(model.y6_2_3 - 1.0)*(model.y6_2_3 - 1.0) + \
    0.5*(model.z6_2_3 - 1.0)*(model.z6_2_3 - 1.0) + 0.5*(model.x7_2_3 - 1.0)*(model.x7_2_3 - 1.0) + \
    0.5*(model.y7_2_3 - 1.0)*(model.y7_2_3 - 1.0) + 0.5*(model.z7_2_3 - 1.0)*(model.z7_2_3 - 1.0) + \
    0.5*(model.x8_2_3 - 1.0)*(model.x8_2_3 - 1.0) + 0.5*(model.y8_2_3 - 1.0)*(model.y8_2_3 - 1.0) + \
    0.5*(model.z8_2_3 - 1.0)*(model.z8_2_3 - 1.0) + 0.5*(model.x9_2_3 - 1.0)*(model.x9_2_3 - 1.0) + \
    0.5*(model.y9_2_3 - 1.0)*(model.y9_2_3 - 1.0) + 0.5*(model.z9_2_3 - 1.0)*(model.z9_2_3 - 1.0) + \
    0.5*(model.x1_3_3 - 1.0)*(model.x1_3_3 - 1.0) + 0.5*(model.y1_3_3 - 1.0)*(model.y1_3_3 - 1.0) + \
    0.5*(model.z1_3_3 - 1.0)*(model.z1_3_3 - 1.0) + 0.5*(model.x2_3_3 - 1.0)*(model.x2_3_3 - 1.0) + \
    0.5*(model.y2_3_3 - 1.0)*(model.y2_3_3 - 1.0) + 0.5*(model.z2_3_3 - 1.0)*(model.z2_3_3 - 1.0) + \
    0.5*(model.x3_3_3 - 1.0)*(model.x3_3_3 - 1.0) + 0.5*(model.y3_3_3 - 1.0)*(model.y3_3_3 - 1.0) + \
    0.5*(model.z3_3_3 - 1.0)*(model.z3_3_3 - 1.0) + 0.5*(model.x4_3_3 - 1.0)*(model.x4_3_3 - 1.0) + \
    0.5*(model.y4_3_3 - 1.0)*(model.y4_3_3 - 1.0) + 0.5*(model.z4_3_3 - 1.0)*(model.z4_3_3 - 1.0) + \
    0.5*(model.x5_3_3 - 1.0)*(model.x5_3_3 - 1.0) + 0.5*(model.y5_3_3 - 1.0)*(model.y5_3_3 - 1.0) + \
    0.5*(model.z5_3_3 - 1.0)*(model.z5_3_3 - 1.0) + 0.5*(model.x6_3_3 - 1.0)*(model.x6_3_3 - 1.0) + \
    0.5*(model.y6_3_3 - 1.0)*(model.y6_3_3 - 1.0) + 0.5*(model.z6_3_3 - 1.0)*(model.z6_3_3 - 1.0) + \
    0.5*(model.x7_3_3 - 1.0)*(model.x7_3_3 - 1.0) + 0.5*(model.y7_3_3 - 1.0)*(model.y7_3_3 - 1.0) + \
    0.5*(model.z7_3_3 - 1.0)*(model.z7_3_3 - 1.0) + 0.5*(model.x8_3_3 - 1.0)*(model.x8_3_3 - 1.0) + \
    0.5*(model.y8_3_3 - 1.0)*(model.y8_3_3 - 1.0) + 0.5*(model.z8_3_3 - 1.0)*(model.z8_3_3 - 1.0) + \
    0.5*(model.x9_3_3 - 1.0)*(model.x9_3_3 - 1.0) + 0.5*(model.y9_3_3 - 1.0)*(model.y9_3_3 - 1.0) + \
    0.5*(model.z9_3_3 - 1.0)*(model.z9_3_3 - 1.0) + 0.5*(model.x1_4_3 - 1.0)*(model.x1_4_3 - 1.0) + \
    0.5*(model.y1_4_3 - 1.0)*(model.y1_4_3 - 1.0) + 0.5*(model.z1_4_3 - 1.0)*(model.z1_4_3 - 1.0) + \
    0.5*(model.x2_4_3 - 1.0)*(model.x2_4_3 - 1.0) + 0.5*(model.y2_4_3 - 1.0)*(model.y2_4_3 - 1.0) + \
    0.5*(model.z2_4_3 - 1.0)*(model.z2_4_3 - 1.0) + 0.5*(model.x3_4_3 - 1.0)*(model.x3_4_3 - 1.0) + \
    0.5*(model.y3_4_3 - 1.0)*(model.y3_4_3 - 1.0) + 0.5*(model.z3_4_3 - 1.0)*(model.z3_4_3 - 1.0) + \
    0.5*(model.x4_4_3 - 1.0)*(model.x4_4_3 - 1.0) + 0.5*(model.y4_4_3 - 1.0)*(model.y4_4_3 - 1.0) + \
    0.5*(model.z4_4_3 - 1.0)*(model.z4_4_3 - 1.0) + 0.5*(model.x5_4_3 - 1.0)*(model.x5_4_3 - 1.0) + \
    0.5*(model.y5_4_3 - 1.0)*(model.y5_4_3 - 1.0) + 0.5*(model.z5_4_3 - 1.0)*(model.z5_4_3 - 1.0) + \
    0.5*(model.x6_4_3 - 1.0)*(model.x6_4_3 - 1.0) + 0.5*(model.y6_4_3 - 1.0)*(model.y6_4_3 - 1.0) + \
    0.5*(model.z6_4_3 - 1.0)*(model.z6_4_3 - 1.0) + 0.5*(model.x7_4_3 - 1.0)*(model.x7_4_3 - 1.0) + \
    0.5*(model.y7_4_3 - 1.0)*(model.y7_4_3 - 1.0) + 0.5*(model.z7_4_3 - 1.0)*(model.z7_4_3 - 1.0) + \
    0.5*(model.x8_4_3 - 1.0)*(model.x8_4_3 - 1.0) + 0.5*(model.y8_4_3 - 1.0)*(model.y8_4_3 - 1.0) + \
    0.5*(model.z8_4_3 - 1.0)*(model.z8_4_3 - 1.0) + 0.5*(model.x9_4_3 - 1.0)*(model.x9_4_3 - 1.0) + \
    0.5*(model.y9_4_3 - 1.0)*(model.y9_4_3 - 1.0) + 0.5*(model.z9_4_3 - 1.0)*(model.z9_4_3 - 1.0) + \
    0.5*(model.x1_5_3 - 1.0)*(model.x1_5_3 - 1.0) + 0.5*(model.y1_5_3 - 1.0)*(model.y1_5_3 - 1.0) + \
    0.5*(model.z1_5_3 - 1.0)*(model.z1_5_3 - 1.0) + 0.5*(model.x2_5_3 - 1.0)*(model.x2_5_3 - 1.0) + \
    0.5*(model.y2_5_3 - 1.0)*(model.y2_5_3 - 1.0) + 0.5*(model.z2_5_3 - 1.0)*(model.z2_5_3 - 1.0) + \
    0.5*(model.x3_5_3 - 1.0)*(model.x3_5_3 - 1.0) + 0.5*(model.y3_5_3 - 1.0)*(model.y3_5_3 - 1.0) + \
    0.5*(model.z3_5_3 - 1.0)*(model.z3_5_3 - 1.0) + 0.5*(model.x4_5_3 - 1.0)*(model.x4_5_3 - 1.0) + \
    0.5*(model.y4_5_3 - 1.0)*(model.y4_5_3 - 1.0) + 0.5*(model.z4_5_3 - 1.0)*(model.z4_5_3 - 1.0) + \
    0.5*(model.x5_5_3 - 1.0)*(model.x5_5_3 - 1.0) + 0.5*(model.y5_5_3 - 1.0)*(model.y5_5_3 - 1.0) + \
    0.5*(model.z5_5_3 - 1.0)*(model.z5_5_3 - 1.0) + 0.5*(model.x6_5_3 - 1.0)*(model.x6_5_3 - 1.0) + \
    0.5*(model.y6_5_3 - 1.0)*(model.y6_5_3 - 1.0) + 0.5*(model.z6_5_3 - 1.0)*(model.z6_5_3 - 1.0) + \
    0.5*(model.x7_5_3 - 1.0)*(model.x7_5_3 - 1.0) + 0.5*(model.y7_5_3 - 1.0)*(model.y7_5_3 - 1.0) + \
    0.5*(model.z7_5_3 - 1.0)*(model.z7_5_3 - 1.0) + 0.5*(model.x8_5_3 - 1.0)*(model.x8_5_3 - 1.0) + \
    0.5*(model.y8_5_3 - 1.0)*(model.y8_5_3 - 1.0) + 0.5*(model.z8_5_3 - 1.0)*(model.z8_5_3 - 1.0) + \
    0.5*(model.x9_5_3 - 1.0)*(model.x9_5_3 - 1.0) + 0.5*(model.y9_5_3 - 1.0)*(model.y9_5_3 - 1.0) + \
    0.5*(model.z9_5_3 - 1.0)*(model.z9_5_3 - 1.0) + 0.5*(model.x1_6_3 - 1.0)*(model.x1_6_3 - 1.0) + \
    0.5*(model.y1_6_3 - 1.0)*(model.y1_6_3 - 1.0) + 0.5*(model.z1_6_3 - 1.0)*(model.z1_6_3 - 1.0) + \
    0.5*(model.x2_6_3 - 1.0)*(model.x2_6_3 - 1.0) + 0.5*(model.y2_6_3 - 1.0)*(model.y2_6_3 - 1.0) + \
    0.5*(model.z2_6_3 - 1.0)*(model.z2_6_3 - 1.0) + 0.5*(model.x3_6_3 - 1.0)*(model.x3_6_3 - 1.0) + \
    0.5*(model.y3_6_3 - 1.0)*(model.y3_6_3 - 1.0) + 0.5*(model.z3_6_3 - 1.0)*(model.z3_6_3 - 1.0) + \
    0.5*(model.x4_6_3 - 1.0)*(model.x4_6_3 - 1.0) + 0.5*(model.y4_6_3 - 1.0)*(model.y4_6_3 - 1.0) + \
    0.5*(model.z4_6_3 - 1.0)*(model.z4_6_3 - 1.0) + 0.5*(model.x5_6_3 - 1.0)*(model.x5_6_3 - 1.0) + \
    0.5*(model.y5_6_3 - 1.0)*(model.y5_6_3 - 1.0) + 0.5*(model.z5_6_3 - 1.0)*(model.z5_6_3 - 1.0) + \
    0.5*(model.x6_6_3 - 1.0)*(model.x6_6_3 - 1.0) + 0.5*(model.y6_6_3 - 1.0)*(model.y6_6_3 - 1.0) + \
    0.5*(model.z6_6_3 - 1.0)*(model.z6_6_3 - 1.0) + 0.5*(model.x7_6_3 - 1.0)*(model.x7_6_3 - 1.0) + \
    0.5*(model.y7_6_3 - 1.0)*(model.y7_6_3 - 1.0) + 0.5*(model.z7_6_3 - 1.0)*(model.z7_6_3 - 1.0) + \
    0.5*(model.x8_6_3 - 1.0)*(model.x8_6_3 - 1.0) + 0.5*(model.y8_6_3 - 1.0)*(model.y8_6_3 - 1.0) + \
    0.5*(model.z8_6_3 - 1.0)*(model.z8_6_3 - 1.0) + 0.5*(model.x9_6_3 - 1.0)*(model.x9_6_3 - 1.0) + \
    0.5*(model.y9_6_3 - 1.0)*(model.y9_6_3 - 1.0) + 0.5*(model.z9_6_3 - 1.0)*(model.z9_6_3 - 1.0) + \
    0.5*(model.x1_7_3 - 1.0)*(model.x1_7_3 - 1.0) + 0.5*(model.y1_7_3 - 1.0)*(model.y1_7_3 - 1.0) + \
    0.5*(model.z1_7_3 - 1.0)*(model.z1_7_3 - 1.0) + 0.5*(model.x2_7_3 - 1.0)*(model.x2_7_3 - 1.0) + \
    0.5*(model.y2_7_3 - 1.0)*(model.y2_7_3 - 1.0) + 0.5*(model.z2_7_3 - 1.0)*(model.z2_7_3 - 1.0) + \
    0.5*(model.x3_7_3 - 1.0)*(model.x3_7_3 - 1.0) + 0.5*(model.y3_7_3 - 1.0)*(model.y3_7_3 - 1.0) + \
    0.5*(model.z3_7_3 - 1.0)*(model.z3_7_3 - 1.0) + 0.5*(model.x4_7_3 - 1.0)*(model.x4_7_3 - 1.0) + \
    0.5*(model.y4_7_3 - 1.0)*(model.y4_7_3 - 1.0) + 0.5*(model.z4_7_3 - 1.0)*(model.z4_7_3 - 1.0) + \
    0.5*(model.x5_7_3 - 1.0)*(model.x5_7_3 - 1.0) + 0.5*(model.y5_7_3 - 1.0)*(model.y5_7_3 - 1.0) + \
    0.5*(model.z5_7_3 - 1.0)*(model.z5_7_3 - 1.0) + 0.5*(model.x6_7_3 - 1.0)*(model.x6_7_3 - 1.0) + \
    0.5*(model.y6_7_3 - 1.0)*(model.y6_7_3 - 1.0) + 0.5*(model.z6_7_3 - 1.0)*(model.z6_7_3 - 1.0) + \
    0.5*(model.x7_7_3 - 1.0)*(model.x7_7_3 - 1.0) + 0.5*(model.y7_7_3 - 1.0)*(model.y7_7_3 - 1.0) + \
    0.5*(model.z7_7_3 - 1.0)*(model.z7_7_3 - 1.0) + 0.5*(model.x8_7_3 - 1.0)*(model.x8_7_3 - 1.0) + \
    0.5*(model.y8_7_3 - 1.0)*(model.y8_7_3 - 1.0) + 0.5*(model.z8_7_3 - 1.0)*(model.z8_7_3 - 1.0) + \
    0.5*(model.x9_7_3 - 1.0)*(model.x9_7_3 - 1.0) + 0.5*(model.y9_7_3 - 1.0)*(model.y9_7_3 - 1.0) + \
    0.5*(model.z9_7_3 - 1.0)*(model.z9_7_3 - 1.0) + 0.5*(model.x1_8_3 - 1.0)*(model.x1_8_3 - 1.0) + \
    0.5*(model.y1_8_3 - 1.0)*(model.y1_8_3 - 1.0) + 0.5*(model.z1_8_3 - 1.0)*(model.z1_8_3 - 1.0) + \
    0.5*(model.x2_8_3 - 1.0)*(model.x2_8_3 - 1.0) + 0.5*(model.y2_8_3 - 1.0)*(model.y2_8_3 - 1.0) + \
    0.5*(model.z2_8_3 - 1.0)*(model.z2_8_3 - 1.0) + 0.5*(model.x3_8_3 - 1.0)*(model.x3_8_3 - 1.0) + \
    0.5*(model.y3_8_3 - 1.0)*(model.y3_8_3 - 1.0) + 0.5*(model.z3_8_3 - 1.0)*(model.z3_8_3 - 1.0) + \
    0.5*(model.x4_8_3 - 1.0)*(model.x4_8_3 - 1.0) + 0.5*(model.y4_8_3 - 1.0)*(model.y4_8_3 - 1.0) + \
    0.5*(model.z4_8_3 - 1.0)*(model.z4_8_3 - 1.0) + 0.5*(model.x5_8_3 - 1.0)*(model.x5_8_3 - 1.0) + \
    0.5*(model.y5_8_3 - 1.0)*(model.y5_8_3 - 1.0) + 0.5*(model.z5_8_3 - 1.0)*(model.z5_8_3 - 1.0) + \
    0.5*(model.x6_8_3 - 1.0)*(model.x6_8_3 - 1.0) + 0.5*(model.y6_8_3 - 1.0)*(model.y6_8_3 - 1.0) + \
    0.5*(model.z6_8_3 - 1.0)*(model.z6_8_3 - 1.0) + 0.5*(model.x7_8_3 - 1.0)*(model.x7_8_3 - 1.0) + \
    0.5*(model.y7_8_3 - 1.0)*(model.y7_8_3 - 1.0) + 0.5*(model.z7_8_3 - 1.0)*(model.z7_8_3 - 1.0) + \
    0.5*(model.x8_8_3 - 1.0)*(model.x8_8_3 - 1.0) + 0.5*(model.y8_8_3 - 1.0)*(model.y8_8_3 - 1.0) + \
    0.5*(model.z8_8_3 - 1.0)*(model.z8_8_3 - 1.0) + 0.5*(model.x9_8_3 - 1.0)*(model.x9_8_3 - 1.0) + \
    0.5*(model.y9_8_3 - 1.0)*(model.y9_8_3 - 1.0) + 0.5*(model.z9_8_3 - 1.0)*(model.z9_8_3 - 1.0) + \
    0.5*(model.x1_9_3 - 1.0)*(model.x1_9_3 - 1.0) + 0.5*(model.y1_9_3 - 1.0)*(model.y1_9_3 - 1.0) + \
    0.5*(model.z1_9_3 - 1.0)*(model.z1_9_3 - 1.0) + 0.5*(model.x2_9_3 - 1.0)*(model.x2_9_3 - 1.0) + \
    0.5*(model.y2_9_3 - 1.0)*(model.y2_9_3 - 1.0) + 0.5*(model.z2_9_3 - 1.0)*(model.z2_9_3 - 1.0) + \
    0.5*(model.x3_9_3 - 1.0)*(model.x3_9_3 - 1.0) + 0.5*(model.y3_9_3 - 1.0)*(model.y3_9_3 - 1.0) + \
    0.5*(model.z3_9_3 - 1.0)*(model.z3_9_3 - 1.0) + 0.5*(model.x4_9_3 - 1.0)*(model.x4_9_3 - 1.0) + \
    0.5*(model.y4_9_3 - 1.0)*(model.y4_9_3 - 1.0) + 0.5*(model.z4_9_3 - 1.0)*(model.z4_9_3 - 1.0) + \
    0.5*(model.x5_9_3 - 1.0)*(model.x5_9_3 - 1.0) + 0.5*(model.y5_9_3 - 1.0)*(model.y5_9_3 - 1.0) + \
    0.5*(model.z5_9_3 - 1.0)*(model.z5_9_3 - 1.0) + 0.5*(model.x6_9_3 - 1.0)*(model.x6_9_3 - 1.0) + \
    0.5*(model.y6_9_3 - 1.0)*(model.y6_9_3 - 1.0) + 0.5*(model.z6_9_3 - 1.0)*(model.z6_9_3 - 1.0) + \
    0.5*(model.x7_9_3 - 1.0)*(model.x7_9_3 - 1.0) + 0.5*(model.y7_9_3 - 1.0)*(model.y7_9_3 - 1.0) + \
    0.5*(model.z7_9_3 - 1.0)*(model.z7_9_3 - 1.0) + 0.5*(model.x8_9_3 - 1.0)*(model.x8_9_3 - 1.0) + \
    0.5*(model.y8_9_3 - 1.0)*(model.y8_9_3 - 1.0) + 0.5*(model.z8_9_3 - 1.0)*(model.z8_9_3 - 1.0) + \
    0.5*(model.x9_9_3 - 1.0)*(model.x9_9_3 - 1.0) + 0.5*(model.y9_9_3 - 1.0)*(model.y9_9_3 - 1.0) + \
    0.5*(model.z9_9_3 - 1.0)*(model.z9_9_3 - 1.0) + 0.5*(model.x1_1_4 - 1.0)*(model.x1_1_4 - 1.0) + \
    0.5*(model.y1_1_4 - 1.0)*(model.y1_1_4 - 1.0) + 0.5*(model.z1_1_4 - 1.0)*(model.z1_1_4 - 1.0) + \
    0.5*(model.x2_1_4 - 1.0)*(model.x2_1_4 - 1.0) + 0.5*(model.y2_1_4 - 1.0)*(model.y2_1_4 - 1.0) + \
    0.5*(model.z2_1_4 - 1.0)*(model.z2_1_4 - 1.0) + 0.5*(model.x3_1_4 - 1.0)*(model.x3_1_4 - 1.0) + \
    0.5*(model.y3_1_4 - 1.0)*(model.y3_1_4 - 1.0) + 0.5*(model.z3_1_4 - 1.0)*(model.z3_1_4 - 1.0) + \
    0.5*(model.x4_1_4 - 1.0)*(model.x4_1_4 - 1.0) + 0.5*(model.y4_1_4 - 1.0)*(model.y4_1_4 - 1.0) + \
    0.5*(model.z4_1_4 - 1.0)*(model.z4_1_4 - 1.0) + 0.5*(model.x5_1_4 - 1.0)*(model.x5_1_4 - 1.0) + \
    0.5*(model.y5_1_4 - 1.0)*(model.y5_1_4 - 1.0) + 0.5*(model.z5_1_4 - 1.0)*(model.z5_1_4 - 1.0) + \
    0.5*(model.x6_1_4 - 1.0)*(model.x6_1_4 - 1.0) + 0.5*(model.y6_1_4 - 1.0)*(model.y6_1_4 - 1.0) + \
    0.5*(model.z6_1_4 - 1.0)*(model.z6_1_4 - 1.0) + 0.5*(model.x7_1_4 - 1.0)*(model.x7_1_4 - 1.0) + \
    0.5*(model.y7_1_4 - 1.0)*(model.y7_1_4 - 1.0) + 0.5*(model.z7_1_4 - 1.0)*(model.z7_1_4 - 1.0) + \
    0.5*(model.x8_1_4 - 1.0)*(model.x8_1_4 - 1.0) + 0.5*(model.y8_1_4 - 1.0)*(model.y8_1_4 - 1.0) + \
    0.5*(model.z8_1_4 - 1.0)*(model.z8_1_4 - 1.0) + 0.5*(model.x9_1_4 - 1.0)*(model.x9_1_4 - 1.0) + \
    0.5*(model.y9_1_4 - 1.0)*(model.y9_1_4 - 1.0) + 0.5*(model.z9_1_4 - 1.0)*(model.z9_1_4 - 1.0) + \
    0.5*(model.x1_2_4 - 1.0)*(model.x1_2_4 - 1.0) + 0.5*(model.y1_2_4 - 1.0)*(model.y1_2_4 - 1.0) + \
    0.5*(model.z1_2_4 - 1.0)*(model.z1_2_4 - 1.0) + 0.5*(model.x2_2_4 - 1.0)*(model.x2_2_4 - 1.0) + \
    0.5*(model.y2_2_4 - 1.0)*(model.y2_2_4 - 1.0) + 0.5*(model.z2_2_4 - 1.0)*(model.z2_2_4 - 1.0) + \
    0.5*(model.x3_2_4 - 1.0)*(model.x3_2_4 - 1.0) + 0.5*(model.y3_2_4 - 1.0)*(model.y3_2_4 - 1.0) + \
    0.5*(model.z3_2_4 - 1.0)*(model.z3_2_4 - 1.0) + 0.5*(model.x4_2_4 - 1.0)*(model.x4_2_4 - 1.0) + \
    0.5*(model.y4_2_4 - 1.0)*(model.y4_2_4 - 1.0) + 0.5*(model.z4_2_4 - 1.0)*(model.z4_2_4 - 1.0) + \
    0.5*(model.x5_2_4 - 1.0)*(model.x5_2_4 - 1.0) + 0.5*(model.y5_2_4 - 1.0)*(model.y5_2_4 - 1.0) + \
    0.5*(model.z5_2_4 - 1.0)*(model.z5_2_4 - 1.0) + 0.5*(model.x6_2_4 - 1.0)*(model.x6_2_4 - 1.0) + \
    0.5*(model.y6_2_4 - 1.0)*(model.y6_2_4 - 1.0) + 0.5*(model.z6_2_4 - 1.0)*(model.z6_2_4 - 1.0) + \
    0.5*(model.x7_2_4 - 1.0)*(model.x7_2_4 - 1.0) + 0.5*(model.y7_2_4 - 1.0)*(model.y7_2_4 - 1.0) + \
    0.5*(model.z7_2_4 - 1.0)*(model.z7_2_4 - 1.0) + 0.5*(model.x8_2_4 - 1.0)*(model.x8_2_4 - 1.0) + \
    0.5*(model.y8_2_4 - 1.0)*(model.y8_2_4 - 1.0) + 0.5*(model.z8_2_4 - 1.0)*(model.z8_2_4 - 1.0) + \
    0.5*(model.x9_2_4 - 1.0)*(model.x9_2_4 - 1.0) + 0.5*(model.y9_2_4 - 1.0)*(model.y9_2_4 - 1.0) + \
    0.5*(model.z9_2_4 - 1.0)*(model.z9_2_4 - 1.0) + 0.5*(model.x1_3_4 - 1.0)*(model.x1_3_4 - 1.0) + \
    0.5*(model.y1_3_4 - 1.0)*(model.y1_3_4 - 1.0) + 0.5*(model.z1_3_4 - 1.0)*(model.z1_3_4 - 1.0) + \
    0.5*(model.x2_3_4 - 1.0)*(model.x2_3_4 - 1.0) + 0.5*(model.y2_3_4 - 1.0)*(model.y2_3_4 - 1.0) + \
    0.5*(model.z2_3_4 - 1.0)*(model.z2_3_4 - 1.0) + 0.5*(model.x3_3_4 - 1.0)*(model.x3_3_4 - 1.0) + \
    0.5*(model.y3_3_4 - 1.0)*(model.y3_3_4 - 1.0) + 0.5*(model.z3_3_4 - 1.0)*(model.z3_3_4 - 1.0) + \
    0.5*(model.x4_3_4 - 1.0)*(model.x4_3_4 - 1.0) + 0.5*(model.y4_3_4 - 1.0)*(model.y4_3_4 - 1.0) + \
    0.5*(model.z4_3_4 - 1.0)*(model.z4_3_4 - 1.0) + 0.5*(model.x5_3_4 - 1.0)*(model.x5_3_4 - 1.0) + \
    0.5*(model.y5_3_4 - 1.0)*(model.y5_3_4 - 1.0) + 0.5*(model.z5_3_4 - 1.0)*(model.z5_3_4 - 1.0) + \
    0.5*(model.x6_3_4 - 1.0)*(model.x6_3_4 - 1.0) + 0.5*(model.y6_3_4 - 1.0)*(model.y6_3_4 - 1.0) + \
    0.5*(model.z6_3_4 - 1.0)*(model.z6_3_4 - 1.0) + 0.5*(model.x7_3_4 - 1.0)*(model.x7_3_4 - 1.0) + \
    0.5*(model.y7_3_4 - 1.0)*(model.y7_3_4 - 1.0) + 0.5*(model.z7_3_4 - 1.0)*(model.z7_3_4 - 1.0) + \
    0.5*(model.x8_3_4 - 1.0)*(model.x8_3_4 - 1.0) + 0.5*(model.y8_3_4 - 1.0)*(model.y8_3_4 - 1.0) + \
    0.5*(model.z8_3_4 - 1.0)*(model.z8_3_4 - 1.0) + 0.5*(model.x9_3_4 - 1.0)*(model.x9_3_4 - 1.0) + \
    0.5*(model.y9_3_4 - 1.0)*(model.y9_3_4 - 1.0) + 0.5*(model.z9_3_4 - 1.0)*(model.z9_3_4 - 1.0) + \
    0.5*(model.x1_4_4 - 1.0)*(model.x1_4_4 - 1.0) + 0.5*(model.y1_4_4 - 1.0)*(model.y1_4_4 - 1.0) + \
    0.5*(model.z1_4_4 - 1.0)*(model.z1_4_4 - 1.0) + 0.5*(model.x2_4_4 - 1.0)*(model.x2_4_4 - 1.0) + \
    0.5*(model.y2_4_4 - 1.0)*(model.y2_4_4 - 1.0) + 0.5*(model.z2_4_4 - 1.0)*(model.z2_4_4 - 1.0) + \
    0.5*(model.x3_4_4 - 1.0)*(model.x3_4_4 - 1.0) + 0.5*(model.y3_4_4 - 1.0)*(model.y3_4_4 - 1.0) + \
    0.5*(model.z3_4_4 - 1.0)*(model.z3_4_4 - 1.0) + 0.5*(model.x4_4_4 - 1.0)*(model.x4_4_4 - 1.0) + \
    0.5*(model.y4_4_4 - 1.0)*(model.y4_4_4 - 1.0) + 0.5*(model.z4_4_4 - 1.0)*(model.z4_4_4 - 1.0) + \
    0.5*(model.x5_4_4 - 1.0)*(model.x5_4_4 - 1.0) + 0.5*(model.y5_4_4 - 1.0)*(model.y5_4_4 - 1.0) + \
    0.5*(model.z5_4_4 - 1.0)*(model.z5_4_4 - 1.0) + 0.5*(model.x6_4_4 - 1.0)*(model.x6_4_4 - 1.0) + \
    0.5*(model.y6_4_4 - 1.0)*(model.y6_4_4 - 1.0) + 0.5*(model.z6_4_4 - 1.0)*(model.z6_4_4 - 1.0) + \
    0.5*(model.x7_4_4 - 1.0)*(model.x7_4_4 - 1.0) + 0.5*(model.y7_4_4 - 1.0)*(model.y7_4_4 - 1.0) + \
    0.5*(model.z7_4_4 - 1.0)*(model.z7_4_4 - 1.0) + 0.5*(model.x8_4_4 - 1.0)*(model.x8_4_4 - 1.0) + \
    0.5*(model.y8_4_4 - 1.0)*(model.y8_4_4 - 1.0) + 0.5*(model.z8_4_4 - 1.0)*(model.z8_4_4 - 1.0) + \
    0.5*(model.x9_4_4 - 1.0)*(model.x9_4_4 - 1.0) + 0.5*(model.y9_4_4 - 1.0)*(model.y9_4_4 - 1.0) + \
    0.5*(model.z9_4_4 - 1.0)*(model.z9_4_4 - 1.0) + 0.5*(model.x1_5_4 - 1.0)*(model.x1_5_4 - 1.0) + \
    0.5*(model.y1_5_4 - 1.0)*(model.y1_5_4 - 1.0) + 0.5*(model.z1_5_4 - 1.0)*(model.z1_5_4 - 1.0) + \
    0.5*(model.x2_5_4 - 1.0)*(model.x2_5_4 - 1.0) + 0.5*(model.y2_5_4 - 1.0)*(model.y2_5_4 - 1.0) + \
    0.5*(model.z2_5_4 - 1.0)*(model.z2_5_4 - 1.0) + 0.5*(model.x3_5_4 - 1.0)*(model.x3_5_4 - 1.0) + \
    0.5*(model.y3_5_4 - 1.0)*(model.y3_5_4 - 1.0) + 0.5*(model.z3_5_4 - 1.0)*(model.z3_5_4 - 1.0) + \
    0.5*(model.x4_5_4 - 1.0)*(model.x4_5_4 - 1.0) + 0.5*(model.y4_5_4 - 1.0)*(model.y4_5_4 - 1.0) + \
    0.5*(model.z4_5_4 - 1.0)*(model.z4_5_4 - 1.0) + 0.5*(model.x5_5_4 - 1.0)*(model.x5_5_4 - 1.0) + \
    0.5*(model.y5_5_4 - 1.0)*(model.y5_5_4 - 1.0) + 0.5*(model.z5_5_4 - 1.0)*(model.z5_5_4 - 1.0) + \
    0.5*(model.x6_5_4 - 1.0)*(model.x6_5_4 - 1.0) + 0.5*(model.y6_5_4 - 1.0)*(model.y6_5_4 - 1.0) + \
    0.5*(model.z6_5_4 - 1.0)*(model.z6_5_4 - 1.0) + 0.5*(model.x7_5_4 - 1.0)*(model.x7_5_4 - 1.0) + \
    0.5*(model.y7_5_4 - 1.0)*(model.y7_5_4 - 1.0) + 0.5*(model.z7_5_4 - 1.0)*(model.z7_5_4 - 1.0) + \
    0.5*(model.x8_5_4 - 1.0)*(model.x8_5_4 - 1.0) + 0.5*(model.y8_5_4 - 1.0)*(model.y8_5_4 - 1.0) + \
    0.5*(model.z8_5_4 - 1.0)*(model.z8_5_4 - 1.0) + 0.5*(model.x9_5_4 - 1.0)*(model.x9_5_4 - 1.0) + \
    0.5*(model.y9_5_4 - 1.0)*(model.y9_5_4 - 1.0) + 0.5*(model.z9_5_4 - 1.0)*(model.z9_5_4 - 1.0) + \
    0.5*(model.x1_6_4 - 1.0)*(model.x1_6_4 - 1.0) + 0.5*(model.y1_6_4 - 1.0)*(model.y1_6_4 - 1.0) + \
    0.5*(model.z1_6_4 - 1.0)*(model.z1_6_4 - 1.0) + 0.5*(model.x2_6_4 - 1.0)*(model.x2_6_4 - 1.0) + \
    0.5*(model.y2_6_4 - 1.0)*(model.y2_6_4 - 1.0) + 0.5*(model.z2_6_4 - 1.0)*(model.z2_6_4 - 1.0) + \
    0.5*(model.x3_6_4 - 1.0)*(model.x3_6_4 - 1.0) + 0.5*(model.y3_6_4 - 1.0)*(model.y3_6_4 - 1.0) + \
    0.5*(model.z3_6_4 - 1.0)*(model.z3_6_4 - 1.0) + 0.5*(model.x4_6_4 - 1.0)*(model.x4_6_4 - 1.0) + \
    0.5*(model.y4_6_4 - 1.0)*(model.y4_6_4 - 1.0) + 0.5*(model.z4_6_4 - 1.0)*(model.z4_6_4 - 1.0) + \
    0.5*(model.x5_6_4 - 1.0)*(model.x5_6_4 - 1.0) + 0.5*(model.y5_6_4 - 1.0)*(model.y5_6_4 - 1.0) + \
    0.5*(model.z5_6_4 - 1.0)*(model.z5_6_4 - 1.0) + 0.5*(model.x6_6_4 - 1.0)*(model.x6_6_4 - 1.0) + \
    0.5*(model.y6_6_4 - 1.0)*(model.y6_6_4 - 1.0) + 0.5*(model.z6_6_4 - 1.0)*(model.z6_6_4 - 1.0) + \
    0.5*(model.x7_6_4 - 1.0)*(model.x7_6_4 - 1.0) + 0.5*(model.y7_6_4 - 1.0)*(model.y7_6_4 - 1.0) + \
    0.5*(model.z7_6_4 - 1.0)*(model.z7_6_4 - 1.0) + 0.5*(model.x8_6_4 - 1.0)*(model.x8_6_4 - 1.0) + \
    0.5*(model.y8_6_4 - 1.0)*(model.y8_6_4 - 1.0) + 0.5*(model.z8_6_4 - 1.0)*(model.z8_6_4 - 1.0) + \
    0.5*(model.x9_6_4 - 1.0)*(model.x9_6_4 - 1.0) + 0.5*(model.y9_6_4 - 1.0)*(model.y9_6_4 - 1.0) + \
    0.5*(model.z9_6_4 - 1.0)*(model.z9_6_4 - 1.0) + 0.5*(model.x1_7_4 - 1.0)*(model.x1_7_4 - 1.0) + \
    0.5*(model.y1_7_4 - 1.0)*(model.y1_7_4 - 1.0) + 0.5*(model.z1_7_4 - 1.0)*(model.z1_7_4 - 1.0) + \
    0.5*(model.x2_7_4 - 1.0)*(model.x2_7_4 - 1.0) + 0.5*(model.y2_7_4 - 1.0)*(model.y2_7_4 - 1.0) + \
    0.5*(model.z2_7_4 - 1.0)*(model.z2_7_4 - 1.0) + 0.5*(model.x3_7_4 - 1.0)*(model.x3_7_4 - 1.0) + \
    0.5*(model.y3_7_4 - 1.0)*(model.y3_7_4 - 1.0) + 0.5*(model.z3_7_4 - 1.0)*(model.z3_7_4 - 1.0) + \
    0.5*(model.x4_7_4 - 1.0)*(model.x4_7_4 - 1.0) + 0.5*(model.y4_7_4 - 1.0)*(model.y4_7_4 - 1.0) + \
    0.5*(model.z4_7_4 - 1.0)*(model.z4_7_4 - 1.0) + 0.5*(model.x5_7_4 - 1.0)*(model.x5_7_4 - 1.0) + \
    0.5*(model.y5_7_4 - 1.0)*(model.y5_7_4 - 1.0) + 0.5*(model.z5_7_4 - 1.0)*(model.z5_7_4 - 1.0) + \
    0.5*(model.x6_7_4 - 1.0)*(model.x6_7_4 - 1.0) + 0.5*(model.y6_7_4 - 1.0)*(model.y6_7_4 - 1.0) + \
    0.5*(model.z6_7_4 - 1.0)*(model.z6_7_4 - 1.0) + 0.5*(model.x7_7_4 - 1.0)*(model.x7_7_4 - 1.0) + \
    0.5*(model.y7_7_4 - 1.0)*(model.y7_7_4 - 1.0) + 0.5*(model.z7_7_4 - 1.0)*(model.z7_7_4 - 1.0) + \
    0.5*(model.x8_7_4 - 1.0)*(model.x8_7_4 - 1.0) + 0.5*(model.y8_7_4 - 1.0)*(model.y8_7_4 - 1.0) + \
    0.5*(model.z8_7_4 - 1.0)*(model.z8_7_4 - 1.0) + 0.5*(model.x9_7_4 - 1.0)*(model.x9_7_4 - 1.0) + \
    0.5*(model.y9_7_4 - 1.0)*(model.y9_7_4 - 1.0) + 0.5*(model.z9_7_4 - 1.0)*(model.z9_7_4 - 1.0) + \
    0.5*(model.x1_8_4 - 1.0)*(model.x1_8_4 - 1.0) + 0.5*(model.y1_8_4 - 1.0)*(model.y1_8_4 - 1.0) + \
    0.5*(model.z1_8_4 - 1.0)*(model.z1_8_4 - 1.0) + 0.5*(model.x2_8_4 - 1.0)*(model.x2_8_4 - 1.0) + \
    0.5*(model.y2_8_4 - 1.0)*(model.y2_8_4 - 1.0) + 0.5*(model.z2_8_4 - 1.0)*(model.z2_8_4 - 1.0) + \
    0.5*(model.x3_8_4 - 1.0)*(model.x3_8_4 - 1.0) + 0.5*(model.y3_8_4 - 1.0)*(model.y3_8_4 - 1.0) + \
    0.5*(model.z3_8_4 - 1.0)*(model.z3_8_4 - 1.0) + 0.5*(model.x4_8_4 - 1.0)*(model.x4_8_4 - 1.0) + \
    0.5*(model.y4_8_4 - 1.0)*(model.y4_8_4 - 1.0) + 0.5*(model.z4_8_4 - 1.0)*(model.z4_8_4 - 1.0) + \
    0.5*(model.x5_8_4 - 1.0)*(model.x5_8_4 - 1.0) + 0.5*(model.y5_8_4 - 1.0)*(model.y5_8_4 - 1.0) + \
    0.5*(model.z5_8_4 - 1.0)*(model.z5_8_4 - 1.0) + 0.5*(model.x6_8_4 - 1.0)*(model.x6_8_4 - 1.0) + \
    0.5*(model.y6_8_4 - 1.0)*(model.y6_8_4 - 1.0) + 0.5*(model.z6_8_4 - 1.0)*(model.z6_8_4 - 1.0) + \
    0.5*(model.x7_8_4 - 1.0)*(model.x7_8_4 - 1.0) + 0.5*(model.y7_8_4 - 1.0)*(model.y7_8_4 - 1.0) + \
    0.5*(model.z7_8_4 - 1.0)*(model.z7_8_4 - 1.0) + 0.5*(model.x8_8_4 - 1.0)*(model.x8_8_4 - 1.0) + \
    0.5*(model.y8_8_4 - 1.0)*(model.y8_8_4 - 1.0) + 0.5*(model.z8_8_4 - 1.0)*(model.z8_8_4 - 1.0) + \
    0.5*(model.x9_8_4 - 1.0)*(model.x9_8_4 - 1.0) + 0.5*(model.y9_8_4 - 1.0)*(model.y9_8_4 - 1.0) + \
    0.5*(model.z9_8_4 - 1.0)*(model.z9_8_4 - 1.0) + 0.5*(model.x1_9_4 - 1.0)*(model.x1_9_4 - 1.0) + \
    0.5*(model.y1_9_4 - 1.0)*(model.y1_9_4 - 1.0) + 0.5*(model.z1_9_4 - 1.0)*(model.z1_9_4 - 1.0) + \
    0.5*(model.x2_9_4 - 1.0)*(model.x2_9_4 - 1.0) + 0.5*(model.y2_9_4 - 1.0)*(model.y2_9_4 - 1.0) + \
    0.5*(model.z2_9_4 - 1.0)*(model.z2_9_4 - 1.0) + 0.5*(model.x3_9_4 - 1.0)*(model.x3_9_4 - 1.0) + \
    0.5*(model.y3_9_4 - 1.0)*(model.y3_9_4 - 1.0) + 0.5*(model.z3_9_4 - 1.0)*(model.z3_9_4 - 1.0) + \
    0.5*(model.x4_9_4 - 1.0)*(model.x4_9_4 - 1.0) + 0.5*(model.y4_9_4 - 1.0)*(model.y4_9_4 - 1.0) + \
    0.5*(model.z4_9_4 - 1.0)*(model.z4_9_4 - 1.0) + 0.5*(model.x5_9_4 - 1.0)*(model.x5_9_4 - 1.0) + \
    0.5*(model.y5_9_4 - 1.0)*(model.y5_9_4 - 1.0) + 0.5*(model.z5_9_4 - 1.0)*(model.z5_9_4 - 1.0) + \
    0.5*(model.x6_9_4 - 1.0)*(model.x6_9_4 - 1.0) + 0.5*(model.y6_9_4 - 1.0)*(model.y6_9_4 - 1.0) + \
    0.5*(model.z6_9_4 - 1.0)*(model.z6_9_4 - 1.0) + 0.5*(model.x7_9_4 - 1.0)*(model.x7_9_4 - 1.0) + \
    0.5*(model.y7_9_4 - 1.0)*(model.y7_9_4 - 1.0) + 0.5*(model.z7_9_4 - 1.0)*(model.z7_9_4 - 1.0) + \
    0.5*(model.x8_9_4 - 1.0)*(model.x8_9_4 - 1.0) + 0.5*(model.y8_9_4 - 1.0)*(model.y8_9_4 - 1.0) + \
    0.5*(model.z8_9_4 - 1.0)*(model.z8_9_4 - 1.0) + 0.5*(model.x9_9_4 - 1.0)*(model.x9_9_4 - 1.0) + \
    0.5*(model.y9_9_4 - 1.0)*(model.y9_9_4 - 1.0) + 0.5*(model.z9_9_4 - 1.0)*(model.z9_9_4 - 1.0) + \
    0.5*(model.x1_1_5 - 1.0)*(model.x1_1_5 - 1.0) + 0.5*(model.y1_1_5 - 1.0)*(model.y1_1_5 - 1.0) + \
    0.5*(model.z1_1_5 - 1.0)*(model.z1_1_5 - 1.0) + 0.5*(model.x2_1_5 - 1.0)*(model.x2_1_5 - 1.0) + \
    0.5*(model.y2_1_5 - 1.0)*(model.y2_1_5 - 1.0) + 0.5*(model.z2_1_5 - 1.0)*(model.z2_1_5 - 1.0) + \
    0.5*(model.x3_1_5 - 1.0)*(model.x3_1_5 - 1.0) + 0.5*(model.y3_1_5 - 1.0)*(model.y3_1_5 - 1.0) + \
    0.5*(model.z3_1_5 - 1.0)*(model.z3_1_5 - 1.0) + 0.5*(model.x4_1_5 - 1.0)*(model.x4_1_5 - 1.0) + \
    0.5*(model.y4_1_5 - 1.0)*(model.y4_1_5 - 1.0) + 0.5*(model.z4_1_5 - 1.0)*(model.z4_1_5 - 1.0) + \
    0.5*(model.x5_1_5 - 1.0)*(model.x5_1_5 - 1.0) + 0.5*(model.y5_1_5 - 1.0)*(model.y5_1_5 - 1.0) + \
    0.5*(model.z5_1_5 - 1.0)*(model.z5_1_5 - 1.0) + 0.5*(model.x6_1_5 - 1.0)*(model.x6_1_5 - 1.0) + \
    0.5*(model.y6_1_5 - 1.0)*(model.y6_1_5 - 1.0) + 0.5*(model.z6_1_5 - 1.0)*(model.z6_1_5 - 1.0) + \
    0.5*(model.x7_1_5 - 1.0)*(model.x7_1_5 - 1.0) + 0.5*(model.y7_1_5 - 1.0)*(model.y7_1_5 - 1.0) + \
    0.5*(model.z7_1_5 - 1.0)*(model.z7_1_5 - 1.0) + 0.5*(model.x8_1_5 - 1.0)*(model.x8_1_5 - 1.0) + \
    0.5*(model.y8_1_5 - 1.0)*(model.y8_1_5 - 1.0) + 0.5*(model.z8_1_5 - 1.0)*(model.z8_1_5 - 1.0) + \
    0.5*(model.x9_1_5 - 1.0)*(model.x9_1_5 - 1.0) + 0.5*(model.y9_1_5 - 1.0)*(model.y9_1_5 - 1.0) + \
    0.5*(model.z9_1_5 - 1.0)*(model.z9_1_5 - 1.0) + 0.5*(model.x1_2_5 - 1.0)*(model.x1_2_5 - 1.0) + \
    0.5*(model.y1_2_5 - 1.0)*(model.y1_2_5 - 1.0) + 0.5*(model.z1_2_5 - 1.0)*(model.z1_2_5 - 1.0) + \
    0.5*(model.x2_2_5 - 1.0)*(model.x2_2_5 - 1.0) + 0.5*(model.y2_2_5 - 1.0)*(model.y2_2_5 - 1.0) + \
    0.5*(model.z2_2_5 - 1.0)*(model.z2_2_5 - 1.0) + 0.5*(model.x3_2_5 - 1.0)*(model.x3_2_5 - 1.0) + \
    0.5*(model.y3_2_5 - 1.0)*(model.y3_2_5 - 1.0) + 0.5*(model.z3_2_5 - 1.0)*(model.z3_2_5 - 1.0) + \
    0.5*(model.x4_2_5 - 1.0)*(model.x4_2_5 - 1.0) + 0.5*(model.y4_2_5 - 1.0)*(model.y4_2_5 - 1.0) + \
    0.5*(model.z4_2_5 - 1.0)*(model.z4_2_5 - 1.0) + 0.5*(model.x5_2_5 - 1.0)*(model.x5_2_5 - 1.0) + \
    0.5*(model.y5_2_5 - 1.0)*(model.y5_2_5 - 1.0) + 0.5*(model.z5_2_5 - 1.0)*(model.z5_2_5 - 1.0) + \
    0.5*(model.x6_2_5 - 1.0)*(model.x6_2_5 - 1.0) + 0.5*(model.y6_2_5 - 1.0)*(model.y6_2_5 - 1.0) + \
    0.5*(model.z6_2_5 - 1.0)*(model.z6_2_5 - 1.0) + 0.5*(model.x7_2_5 - 1.0)*(model.x7_2_5 - 1.0) + \
    0.5*(model.y7_2_5 - 1.0)*(model.y7_2_5 - 1.0) + 0.5*(model.z7_2_5 - 1.0)*(model.z7_2_5 - 1.0) + \
    0.5*(model.x8_2_5 - 1.0)*(model.x8_2_5 - 1.0) + 0.5*(model.y8_2_5 - 1.0)*(model.y8_2_5 - 1.0) + \
    0.5*(model.z8_2_5 - 1.0)*(model.z8_2_5 - 1.0) + 0.5*(model.x9_2_5 - 1.0)*(model.x9_2_5 - 1.0) + \
    0.5*(model.y9_2_5 - 1.0)*(model.y9_2_5 - 1.0) + 0.5*(model.z9_2_5 - 1.0)*(model.z9_2_5 - 1.0) + \
    0.5*(model.x1_3_5 - 1.0)*(model.x1_3_5 - 1.0) + 0.5*(model.y1_3_5 - 1.0)*(model.y1_3_5 - 1.0) + \
    0.5*(model.z1_3_5 - 1.0)*(model.z1_3_5 - 1.0) + 0.5*(model.x2_3_5 - 1.0)*(model.x2_3_5 - 1.0) + \
    0.5*(model.y2_3_5 - 1.0)*(model.y2_3_5 - 1.0) + 0.5*(model.z2_3_5 - 1.0)*(model.z2_3_5 - 1.0) + \
    0.5*(model.x3_3_5 - 1.0)*(model.x3_3_5 - 1.0) + 0.5*(model.y3_3_5 - 1.0)*(model.y3_3_5 - 1.0) + \
    0.5*(model.z3_3_5 - 1.0)*(model.z3_3_5 - 1.0) + 0.5*(model.x4_3_5 - 1.0)*(model.x4_3_5 - 1.0) + \
    0.5*(model.y4_3_5 - 1.0)*(model.y4_3_5 - 1.0) + 0.5*(model.z4_3_5 - 1.0)*(model.z4_3_5 - 1.0) + \
    0.5*(model.x5_3_5 - 1.0)*(model.x5_3_5 - 1.0) + 0.5*(model.y5_3_5 - 1.0)*(model.y5_3_5 - 1.0) + \
    0.5*(model.z5_3_5 - 1.0)*(model.z5_3_5 - 1.0) + 0.5*(model.x6_3_5 - 1.0)*(model.x6_3_5 - 1.0) + \
    0.5*(model.y6_3_5 - 1.0)*(model.y6_3_5 - 1.0) + 0.5*(model.z6_3_5 - 1.0)*(model.z6_3_5 - 1.0) + \
    0.5*(model.x7_3_5 - 1.0)*(model.x7_3_5 - 1.0) + 0.5*(model.y7_3_5 - 1.0)*(model.y7_3_5 - 1.0) + \
    0.5*(model.z7_3_5 - 1.0)*(model.z7_3_5 - 1.0) + 0.5*(model.x8_3_5 - 1.0)*(model.x8_3_5 - 1.0) + \
    0.5*(model.y8_3_5 - 1.0)*(model.y8_3_5 - 1.0) + 0.5*(model.z8_3_5 - 1.0)*(model.z8_3_5 - 1.0) + \
    0.5*(model.x9_3_5 - 1.0)*(model.x9_3_5 - 1.0) + 0.5*(model.y9_3_5 - 1.0)*(model.y9_3_5 - 1.0) + \
    0.5*(model.z9_3_5 - 1.0)*(model.z9_3_5 - 1.0) + 0.5*(model.x1_4_5 - 1.0)*(model.x1_4_5 - 1.0) + \
    0.5*(model.y1_4_5 - 1.0)*(model.y1_4_5 - 1.0) + 0.5*(model.z1_4_5 - 1.0)*(model.z1_4_5 - 1.0) + \
    0.5*(model.x2_4_5 - 1.0)*(model.x2_4_5 - 1.0) + 0.5*(model.y2_4_5 - 1.0)*(model.y2_4_5 - 1.0) + \
    0.5*(model.z2_4_5 - 1.0)*(model.z2_4_5 - 1.0) + 0.5*(model.x3_4_5 - 1.0)*(model.x3_4_5 - 1.0) + \
    0.5*(model.y3_4_5 - 1.0)*(model.y3_4_5 - 1.0) + 0.5*(model.z3_4_5 - 1.0)*(model.z3_4_5 - 1.0) + \
    0.5*(model.x4_4_5 - 1.0)*(model.x4_4_5 - 1.0) + 0.5*(model.y4_4_5 - 1.0)*(model.y4_4_5 - 1.0) + \
    0.5*(model.z4_4_5 - 1.0)*(model.z4_4_5 - 1.0) + 0.5*(model.x5_4_5 - 1.0)*(model.x5_4_5 - 1.0) + \
    0.5*(model.y5_4_5 - 1.0)*(model.y5_4_5 - 1.0) + 0.5*(model.z5_4_5 - 1.0)*(model.z5_4_5 - 1.0) + \
    0.5*(model.x6_4_5 - 1.0)*(model.x6_4_5 - 1.0) + 0.5*(model.y6_4_5 - 1.0)*(model.y6_4_5 - 1.0) + \
    0.5*(model.z6_4_5 - 1.0)*(model.z6_4_5 - 1.0) + 0.5*(model.x7_4_5 - 1.0)*(model.x7_4_5 - 1.0) + \
    0.5*(model.y7_4_5 - 1.0)*(model.y7_4_5 - 1.0) + 0.5*(model.z7_4_5 - 1.0)*(model.z7_4_5 - 1.0) + \
    0.5*(model.x8_4_5 - 1.0)*(model.x8_4_5 - 1.0) + 0.5*(model.y8_4_5 - 1.0)*(model.y8_4_5 - 1.0) + \
    0.5*(model.z8_4_5 - 1.0)*(model.z8_4_5 - 1.0) + 0.5*(model.x9_4_5 - 1.0)*(model.x9_4_5 - 1.0) + \
    0.5*(model.y9_4_5 - 1.0)*(model.y9_4_5 - 1.0) + 0.5*(model.z9_4_5 - 1.0)*(model.z9_4_5 - 1.0) + \
    0.5*(model.x1_5_5 - 1.0)*(model.x1_5_5 - 1.0) + 0.5*(model.y1_5_5 - 1.0)*(model.y1_5_5 - 1.0) + \
    0.5*(model.z1_5_5 - 1.0)*(model.z1_5_5 - 1.0) + 0.5*(model.x2_5_5 - 1.0)*(model.x2_5_5 - 1.0) + \
    0.5*(model.y2_5_5 - 1.0)*(model.y2_5_5 - 1.0) + 0.5*(model.z2_5_5 - 1.0)*(model.z2_5_5 - 1.0) + \
    0.5*(model.x3_5_5 - 1.0)*(model.x3_5_5 - 1.0) + 0.5*(model.y3_5_5 - 1.0)*(model.y3_5_5 - 1.0) + \
    0.5*(model.z3_5_5 - 1.0)*(model.z3_5_5 - 1.0) + 0.5*(model.x4_5_5 - 1.0)*(model.x4_5_5 - 1.0) + \
    0.5*(model.y4_5_5 - 1.0)*(model.y4_5_5 - 1.0) + 0.5*(model.z4_5_5 - 1.0)*(model.z4_5_5 - 1.0) + \
    0.5*(model.x5_5_5 - 1.0)*(model.x5_5_5 - 1.0) + 0.5*(model.y5_5_5 - 1.0)*(model.y5_5_5 - 1.0) + \
    0.5*(model.z5_5_5 - 1.0)*(model.z5_5_5 - 1.0) + 0.5*(model.x6_5_5 - 1.0)*(model.x6_5_5 - 1.0) + \
    0.5*(model.y6_5_5 - 1.0)*(model.y6_5_5 - 1.0) + 0.5*(model.z6_5_5 - 1.0)*(model.z6_5_5 - 1.0) + \
    0.5*(model.x7_5_5 - 1.0)*(model.x7_5_5 - 1.0) + 0.5*(model.y7_5_5 - 1.0)*(model.y7_5_5 - 1.0) + \
    0.5*(model.z7_5_5 - 1.0)*(model.z7_5_5 - 1.0) + 0.5*(model.x8_5_5 - 1.0)*(model.x8_5_5 - 1.0) + \
    0.5*(model.y8_5_5 - 1.0)*(model.y8_5_5 - 1.0) + 0.5*(model.z8_5_5 - 1.0)*(model.z8_5_5 - 1.0) + \
    0.5*(model.x9_5_5 - 1.0)*(model.x9_5_5 - 1.0) + 0.5*(model.y9_5_5 - 1.0)*(model.y9_5_5 - 1.0) + \
    0.5*(model.z9_5_5 - 1.0)*(model.z9_5_5 - 1.0) + 0.5*(model.x1_6_5 - 1.0)*(model.x1_6_5 - 1.0) + \
    0.5*(model.y1_6_5 - 1.0)*(model.y1_6_5 - 1.0) + 0.5*(model.z1_6_5 - 1.0)*(model.z1_6_5 - 1.0) + \
    0.5*(model.x2_6_5 - 1.0)*(model.x2_6_5 - 1.0) + 0.5*(model.y2_6_5 - 1.0)*(model.y2_6_5 - 1.0) + \
    0.5*(model.z2_6_5 - 1.0)*(model.z2_6_5 - 1.0) + 0.5*(model.x3_6_5 - 1.0)*(model.x3_6_5 - 1.0) + \
    0.5*(model.y3_6_5 - 1.0)*(model.y3_6_5 - 1.0) + 0.5*(model.z3_6_5 - 1.0)*(model.z3_6_5 - 1.0) + \
    0.5*(model.x4_6_5 - 1.0)*(model.x4_6_5 - 1.0) + 0.5*(model.y4_6_5 - 1.0)*(model.y4_6_5 - 1.0) + \
    0.5*(model.z4_6_5 - 1.0)*(model.z4_6_5 - 1.0) + 0.5*(model.x5_6_5 - 1.0)*(model.x5_6_5 - 1.0) + \
    0.5*(model.y5_6_5 - 1.0)*(model.y5_6_5 - 1.0) + 0.5*(model.z5_6_5 - 1.0)*(model.z5_6_5 - 1.0) + \
    0.5*(model.x6_6_5 - 1.0)*(model.x6_6_5 - 1.0) + 0.5*(model.y6_6_5 - 1.0)*(model.y6_6_5 - 1.0) + \
    0.5*(model.z6_6_5 - 1.0)*(model.z6_6_5 - 1.0) + 0.5*(model.x7_6_5 - 1.0)*(model.x7_6_5 - 1.0) + \
    0.5*(model.y7_6_5 - 1.0)*(model.y7_6_5 - 1.0) + 0.5*(model.z7_6_5 - 1.0)*(model.z7_6_5 - 1.0) + \
    0.5*(model.x8_6_5 - 1.0)*(model.x8_6_5 - 1.0) + 0.5*(model.y8_6_5 - 1.0)*(model.y8_6_5 - 1.0) + \
    0.5*(model.z8_6_5 - 1.0)*(model.z8_6_5 - 1.0) + 0.5*(model.x9_6_5 - 1.0)*(model.x9_6_5 - 1.0) + \
    0.5*(model.y9_6_5 - 1.0)*(model.y9_6_5 - 1.0) + 0.5*(model.z9_6_5 - 1.0)*(model.z9_6_5 - 1.0) + \
    0.5*(model.x1_7_5 - 1.0)*(model.x1_7_5 - 1.0) + 0.5*(model.y1_7_5 - 1.0)*(model.y1_7_5 - 1.0) + \
    0.5*(model.z1_7_5 - 1.0)*(model.z1_7_5 - 1.0) + 0.5*(model.x2_7_5 - 1.0)*(model.x2_7_5 - 1.0) + \
    0.5*(model.y2_7_5 - 1.0)*(model.y2_7_5 - 1.0) + 0.5*(model.z2_7_5 - 1.0)*(model.z2_7_5 - 1.0) + \
    0.5*(model.x3_7_5 - 1.0)*(model.x3_7_5 - 1.0) + 0.5*(model.y3_7_5 - 1.0)*(model.y3_7_5 - 1.0) + \
    0.5*(model.z3_7_5 - 1.0)*(model.z3_7_5 - 1.0) + 0.5*(model.x4_7_5 - 1.0)*(model.x4_7_5 - 1.0) + \
    0.5*(model.y4_7_5 - 1.0)*(model.y4_7_5 - 1.0) + 0.5*(model.z4_7_5 - 1.0)*(model.z4_7_5 - 1.0) + \
    0.5*(model.x5_7_5 - 1.0)*(model.x5_7_5 - 1.0) + 0.5*(model.y5_7_5 - 1.0)*(model.y5_7_5 - 1.0) + \
    0.5*(model.z5_7_5 - 1.0)*(model.z5_7_5 - 1.0) + 0.5*(model.x6_7_5 - 1.0)*(model.x6_7_5 - 1.0) + \
    0.5*(model.y6_7_5 - 1.0)*(model.y6_7_5 - 1.0) + 0.5*(model.z6_7_5 - 1.0)*(model.z6_7_5 - 1.0) + \
    0.5*(model.x7_7_5 - 1.0)*(model.x7_7_5 - 1.0) + 0.5*(model.y7_7_5 - 1.0)*(model.y7_7_5 - 1.0) + \
    0.5*(model.z7_7_5 - 1.0)*(model.z7_7_5 - 1.0) + 0.5*(model.x8_7_5 - 1.0)*(model.x8_7_5 - 1.0) + \
    0.5*(model.y8_7_5 - 1.0)*(model.y8_7_5 - 1.0) + 0.5*(model.z8_7_5 - 1.0)*(model.z8_7_5 - 1.0) + \
    0.5*(model.x9_7_5 - 1.0)*(model.x9_7_5 - 1.0) + 0.5*(model.y9_7_5 - 1.0)*(model.y9_7_5 - 1.0) + \
    0.5*(model.z9_7_5 - 1.0)*(model.z9_7_5 - 1.0) + 0.5*(model.x1_8_5 - 1.0)*(model.x1_8_5 - 1.0) + \
    0.5*(model.y1_8_5 - 1.0)*(model.y1_8_5 - 1.0) + 0.5*(model.z1_8_5 - 1.0)*(model.z1_8_5 - 1.0) + \
    0.5*(model.x2_8_5 - 1.0)*(model.x2_8_5 - 1.0) + 0.5*(model.y2_8_5 - 1.0)*(model.y2_8_5 - 1.0) + \
    0.5*(model.z2_8_5 - 1.0)*(model.z2_8_5 - 1.0) + 0.5*(model.x3_8_5 - 1.0)*(model.x3_8_5 - 1.0) + \
    0.5*(model.y3_8_5 - 1.0)*(model.y3_8_5 - 1.0) + 0.5*(model.z3_8_5 - 1.0)*(model.z3_8_5 - 1.0) + \
    0.5*(model.x4_8_5 - 1.0)*(model.x4_8_5 - 1.0) + 0.5*(model.y4_8_5 - 1.0)*(model.y4_8_5 - 1.0) + \
    0.5*(model.z4_8_5 - 1.0)*(model.z4_8_5 - 1.0) + 0.5*(model.x5_8_5 - 1.0)*(model.x5_8_5 - 1.0) + \
    0.5*(model.y5_8_5 - 1.0)*(model.y5_8_5 - 1.0) + 0.5*(model.z5_8_5 - 1.0)*(model.z5_8_5 - 1.0) + \
    0.5*(model.x6_8_5 - 1.0)*(model.x6_8_5 - 1.0) + 0.5*(model.y6_8_5 - 1.0)*(model.y6_8_5 - 1.0) + \
    0.5*(model.z6_8_5 - 1.0)*(model.z6_8_5 - 1.0) + 0.5*(model.x7_8_5 - 1.0)*(model.x7_8_5 - 1.0) + \
    0.5*(model.y7_8_5 - 1.0)*(model.y7_8_5 - 1.0) + 0.5*(model.z7_8_5 - 1.0)*(model.z7_8_5 - 1.0) + \
    0.5*(model.x8_8_5 - 1.0)*(model.x8_8_5 - 1.0) + 0.5*(model.y8_8_5 - 1.0)*(model.y8_8_5 - 1.0) + \
    0.5*(model.z8_8_5 - 1.0)*(model.z8_8_5 - 1.0) + 0.5*(model.x9_8_5 - 1.0)*(model.x9_8_5 - 1.0) + \
    0.5*(model.y9_8_5 - 1.0)*(model.y9_8_5 - 1.0) + 0.5*(model.z9_8_5 - 1.0)*(model.z9_8_5 - 1.0) + \
    0.5*(model.x1_9_5 - 1.0)*(model.x1_9_5 - 1.0) + 0.5*(model.y1_9_5 - 1.0)*(model.y1_9_5 - 1.0) + \
    0.5*(model.z1_9_5 - 1.0)*(model.z1_9_5 - 1.0) + 0.5*(model.x2_9_5 - 1.0)*(model.x2_9_5 - 1.0) + \
    0.5*(model.y2_9_5 - 1.0)*(model.y2_9_5 - 1.0) + 0.5*(model.z2_9_5 - 1.0)*(model.z2_9_5 - 1.0) + \
    0.5*(model.x3_9_5 - 1.0)*(model.x3_9_5 - 1.0) + 0.5*(model.y3_9_5 - 1.0)*(model.y3_9_5 - 1.0) + \
    0.5*(model.z3_9_5 - 1.0)*(model.z3_9_5 - 1.0) + 0.5*(model.x4_9_5 - 1.0)*(model.x4_9_5 - 1.0) + \
    0.5*(model.y4_9_5 - 1.0)*(model.y4_9_5 - 1.0) + 0.5*(model.z4_9_5 - 1.0)*(model.z4_9_5 - 1.0) + \
    0.5*(model.x5_9_5 - 1.0)*(model.x5_9_5 - 1.0) + 0.5*(model.y5_9_5 - 1.0)*(model.y5_9_5 - 1.0) + \
    0.5*(model.z5_9_5 - 1.0)*(model.z5_9_5 - 1.0) + 0.5*(model.x6_9_5 - 1.0)*(model.x6_9_5 - 1.0) + \
    0.5*(model.y6_9_5 - 1.0)*(model.y6_9_5 - 1.0) + 0.5*(model.z6_9_5 - 1.0)*(model.z6_9_5 - 1.0) + \
    0.5*(model.x7_9_5 - 1.0)*(model.x7_9_5 - 1.0) + 0.5*(model.y7_9_5 - 1.0)*(model.y7_9_5 - 1.0) + \
    0.5*(model.z7_9_5 - 1.0)*(model.z7_9_5 - 1.0) + 0.5*(model.x8_9_5 - 1.0)*(model.x8_9_5 - 1.0) + \
    0.5*(model.y8_9_5 - 1.0)*(model.y8_9_5 - 1.0) + 0.5*(model.z8_9_5 - 1.0)*(model.z8_9_5 - 1.0) + \
    0.5*(model.x9_9_5 - 1.0)*(model.x9_9_5 - 1.0) + 0.5*(model.y9_9_5 - 1.0)*(model.y9_9_5 - 1.0) + \
    0.5*(model.z9_9_5 - 1.0)*(model.z9_9_5 - 1.0) + 0.5*(model.x1_1_6 - 1.0)*(model.x1_1_6 - 1.0) + \
    0.5*(model.y1_1_6 - 1.0)*(model.y1_1_6 - 1.0) + 0.5*(model.z1_1_6 - 1.0)*(model.z1_1_6 - 1.0) + \
    0.5*(model.x2_1_6 - 1.0)*(model.x2_1_6 - 1.0) + 0.5*(model.y2_1_6 - 1.0)*(model.y2_1_6 - 1.0) + \
    0.5*(model.z2_1_6 - 1.0)*(model.z2_1_6 - 1.0) + 0.5*(model.x3_1_6 - 1.0)*(model.x3_1_6 - 1.0) + \
    0.5*(model.y3_1_6 - 1.0)*(model.y3_1_6 - 1.0) + 0.5*(model.z3_1_6 - 1.0)*(model.z3_1_6 - 1.0) + \
    0.5*(model.x4_1_6 - 1.0)*(model.x4_1_6 - 1.0) + 0.5*(model.y4_1_6 - 1.0)*(model.y4_1_6 - 1.0) + \
    0.5*(model.z4_1_6 - 1.0)*(model.z4_1_6 - 1.0) + 0.5*(model.x5_1_6 - 1.0)*(model.x5_1_6 - 1.0) + \
    0.5*(model.y5_1_6 - 1.0)*(model.y5_1_6 - 1.0) + 0.5*(model.z5_1_6 - 1.0)*(model.z5_1_6 - 1.0) + \
    0.5*(model.x6_1_6 - 1.0)*(model.x6_1_6 - 1.0) + 0.5*(model.y6_1_6 - 1.0)*(model.y6_1_6 - 1.0) + \
    0.5*(model.z6_1_6 - 1.0)*(model.z6_1_6 - 1.0) + 0.5*(model.x7_1_6 - 1.0)*(model.x7_1_6 - 1.0) + \
    0.5*(model.y7_1_6 - 1.0)*(model.y7_1_6 - 1.0) + 0.5*(model.z7_1_6 - 1.0)*(model.z7_1_6 - 1.0) + \
    0.5*(model.x8_1_6 - 1.0)*(model.x8_1_6 - 1.0) + 0.5*(model.y8_1_6 - 1.0)*(model.y8_1_6 - 1.0) + \
    0.5*(model.z8_1_6 - 1.0)*(model.z8_1_6 - 1.0) + 0.5*(model.x9_1_6 - 1.0)*(model.x9_1_6 - 1.0) + \
    0.5*(model.y9_1_6 - 1.0)*(model.y9_1_6 - 1.0) + 0.5*(model.z9_1_6 - 1.0)*(model.z9_1_6 - 1.0) + \
    0.5*(model.x1_2_6 - 1.0)*(model.x1_2_6 - 1.0) + 0.5*(model.y1_2_6 - 1.0)*(model.y1_2_6 - 1.0) + \
    0.5*(model.z1_2_6 - 1.0)*(model.z1_2_6 - 1.0) + 0.5*(model.x2_2_6 - 1.0)*(model.x2_2_6 - 1.0) + \
    0.5*(model.y2_2_6 - 1.0)*(model.y2_2_6 - 1.0) + 0.5*(model.z2_2_6 - 1.0)*(model.z2_2_6 - 1.0) + \
    0.5*(model.x3_2_6 - 1.0)*(model.x3_2_6 - 1.0) + 0.5*(model.y3_2_6 - 1.0)*(model.y3_2_6 - 1.0) + \
    0.5*(model.z3_2_6 - 1.0)*(model.z3_2_6 - 1.0) + 0.5*(model.x4_2_6 - 1.0)*(model.x4_2_6 - 1.0) + \
    0.5*(model.y4_2_6 - 1.0)*(model.y4_2_6 - 1.0) + 0.5*(model.z4_2_6 - 1.0)*(model.z4_2_6 - 1.0) + \
    0.5*(model.x5_2_6 - 1.0)*(model.x5_2_6 - 1.0) + 0.5*(model.y5_2_6 - 1.0)*(model.y5_2_6 - 1.0) + \
    0.5*(model.z5_2_6 - 1.0)*(model.z5_2_6 - 1.0) + 0.5*(model.x6_2_6 - 1.0)*(model.x6_2_6 - 1.0) + \
    0.5*(model.y6_2_6 - 1.0)*(model.y6_2_6 - 1.0) + 0.5*(model.z6_2_6 - 1.0)*(model.z6_2_6 - 1.0) + \
    0.5*(model.x7_2_6 - 1.0)*(model.x7_2_6 - 1.0) + 0.5*(model.y7_2_6 - 1.0)*(model.y7_2_6 - 1.0) + \
    0.5*(model.z7_2_6 - 1.0)*(model.z7_2_6 - 1.0) + 0.5*(model.x8_2_6 - 1.0)*(model.x8_2_6 - 1.0) + \
    0.5*(model.y8_2_6 - 1.0)*(model.y8_2_6 - 1.0) + 0.5*(model.z8_2_6 - 1.0)*(model.z8_2_6 - 1.0) + \
    0.5*(model.x9_2_6 - 1.0)*(model.x9_2_6 - 1.0) + 0.5*(model.y9_2_6 - 1.0)*(model.y9_2_6 - 1.0) + \
    0.5*(model.z9_2_6 - 1.0)*(model.z9_2_6 - 1.0) + 0.5*(model.x1_3_6 - 1.0)*(model.x1_3_6 - 1.0) + \
    0.5*(model.y1_3_6 - 1.0)*(model.y1_3_6 - 1.0) + 0.5*(model.z1_3_6 - 1.0)*(model.z1_3_6 - 1.0) + \
    0.5*(model.x2_3_6 - 1.0)*(model.x2_3_6 - 1.0) + 0.5*(model.y2_3_6 - 1.0)*(model.y2_3_6 - 1.0) + \
    0.5*(model.z2_3_6 - 1.0)*(model.z2_3_6 - 1.0) + 0.5*(model.x3_3_6 - 1.0)*(model.x3_3_6 - 1.0) + \
    0.5*(model.y3_3_6 - 1.0)*(model.y3_3_6 - 1.0) + 0.5*(model.z3_3_6 - 1.0)*(model.z3_3_6 - 1.0) + \
    0.5*(model.x4_3_6 - 1.0)*(model.x4_3_6 - 1.0) + 0.5*(model.y4_3_6 - 1.0)*(model.y4_3_6 - 1.0) + \
    0.5*(model.z4_3_6 - 1.0)*(model.z4_3_6 - 1.0) + 0.5*(model.x5_3_6 - 1.0)*(model.x5_3_6 - 1.0) + \
    0.5*(model.y5_3_6 - 1.0)*(model.y5_3_6 - 1.0) + 0.5*(model.z5_3_6 - 1.0)*(model.z5_3_6 - 1.0) + \
    0.5*(model.x6_3_6 - 1.0)*(model.x6_3_6 - 1.0) + 0.5*(model.y6_3_6 - 1.0)*(model.y6_3_6 - 1.0) + \
    0.5*(model.z6_3_6 - 1.0)*(model.z6_3_6 - 1.0) + 0.5*(model.x7_3_6 - 1.0)*(model.x7_3_6 - 1.0) + \
    0.5*(model.y7_3_6 - 1.0)*(model.y7_3_6 - 1.0) + 0.5*(model.z7_3_6 - 1.0)*(model.z7_3_6 - 1.0) + \
    0.5*(model.x8_3_6 - 1.0)*(model.x8_3_6 - 1.0) + 0.5*(model.y8_3_6 - 1.0)*(model.y8_3_6 - 1.0) + \
    0.5*(model.z8_3_6 - 1.0)*(model.z8_3_6 - 1.0) + 0.5*(model.x9_3_6 - 1.0)*(model.x9_3_6 - 1.0) + \
    0.5*(model.y9_3_6 - 1.0)*(model.y9_3_6 - 1.0) + 0.5*(model.z9_3_6 - 1.0)*(model.z9_3_6 - 1.0) + \
    0.5*(model.x1_4_6 - 1.0)*(model.x1_4_6 - 1.0) + 0.5*(model.y1_4_6 - 1.0)*(model.y1_4_6 - 1.0) + \
    0.5*(model.z1_4_6 - 1.0)*(model.z1_4_6 - 1.0) + 0.5*(model.x2_4_6 - 1.0)*(model.x2_4_6 - 1.0) + \
    0.5*(model.y2_4_6 - 1.0)*(model.y2_4_6 - 1.0) + 0.5*(model.z2_4_6 - 1.0)*(model.z2_4_6 - 1.0) + \
    0.5*(model.x3_4_6 - 1.0)*(model.x3_4_6 - 1.0) + 0.5*(model.y3_4_6 - 1.0)*(model.y3_4_6 - 1.0) + \
    0.5*(model.z3_4_6 - 1.0)*(model.z3_4_6 - 1.0) + 0.5*(model.x4_4_6 - 1.0)*(model.x4_4_6 - 1.0) + \
    0.5*(model.y4_4_6 - 1.0)*(model.y4_4_6 - 1.0) + 0.5*(model.z4_4_6 - 1.0)*(model.z4_4_6 - 1.0) + \
    0.5*(model.x5_4_6 - 1.0)*(model.x5_4_6 - 1.0) + 0.5*(model.y5_4_6 - 1.0)*(model.y5_4_6 - 1.0) + \
    0.5*(model.z5_4_6 - 1.0)*(model.z5_4_6 - 1.0) + 0.5*(model.x6_4_6 - 1.0)*(model.x6_4_6 - 1.0) + \
    0.5*(model.y6_4_6 - 1.0)*(model.y6_4_6 - 1.0) + 0.5*(model.z6_4_6 - 1.0)*(model.z6_4_6 - 1.0) + \
    0.5*(model.x7_4_6 - 1.0)*(model.x7_4_6 - 1.0) + 0.5*(model.y7_4_6 - 1.0)*(model.y7_4_6 - 1.0) + \
    0.5*(model.z7_4_6 - 1.0)*(model.z7_4_6 - 1.0) + 0.5*(model.x8_4_6 - 1.0)*(model.x8_4_6 - 1.0) + \
    0.5*(model.y8_4_6 - 1.0)*(model.y8_4_6 - 1.0) + 0.5*(model.z8_4_6 - 1.0)*(model.z8_4_6 - 1.0) + \
    0.5*(model.x9_4_6 - 1.0)*(model.x9_4_6 - 1.0) + 0.5*(model.y9_4_6 - 1.0)*(model.y9_4_6 - 1.0) + \
    0.5*(model.z9_4_6 - 1.0)*(model.z9_4_6 - 1.0) + 0.5*(model.x1_5_6 - 1.0)*(model.x1_5_6 - 1.0) + \
    0.5*(model.y1_5_6 - 1.0)*(model.y1_5_6 - 1.0) + 0.5*(model.z1_5_6 - 1.0)*(model.z1_5_6 - 1.0) + \
    0.5*(model.x2_5_6 - 1.0)*(model.x2_5_6 - 1.0) + 0.5*(model.y2_5_6 - 1.0)*(model.y2_5_6 - 1.0) + \
    0.5*(model.z2_5_6 - 1.0)*(model.z2_5_6 - 1.0) + 0.5*(model.x3_5_6 - 1.0)*(model.x3_5_6 - 1.0) + \
    0.5*(model.y3_5_6 - 1.0)*(model.y3_5_6 - 1.0) + 0.5*(model.z3_5_6 - 1.0)*(model.z3_5_6 - 1.0) + \
    0.5*(model.x4_5_6 - 1.0)*(model.x4_5_6 - 1.0) + 0.5*(model.y4_5_6 - 1.0)*(model.y4_5_6 - 1.0) + \
    0.5*(model.z4_5_6 - 1.0)*(model.z4_5_6 - 1.0) + 0.5*(model.x5_5_6 - 1.0)*(model.x5_5_6 - 1.0) + \
    0.5*(model.y5_5_6 - 1.0)*(model.y5_5_6 - 1.0) + 0.5*(model.z5_5_6 - 1.0)*(model.z5_5_6 - 1.0) + \
    0.5*(model.x6_5_6 - 1.0)*(model.x6_5_6 - 1.0) + 0.5*(model.y6_5_6 - 1.0)*(model.y6_5_6 - 1.0) + \
    0.5*(model.z6_5_6 - 1.0)*(model.z6_5_6 - 1.0) + 0.5*(model.x7_5_6 - 1.0)*(model.x7_5_6 - 1.0) + \
    0.5*(model.y7_5_6 - 1.0)*(model.y7_5_6 - 1.0) + 0.5*(model.z7_5_6 - 1.0)*(model.z7_5_6 - 1.0) + \
    0.5*(model.x8_5_6 - 1.0)*(model.x8_5_6 - 1.0) + 0.5*(model.y8_5_6 - 1.0)*(model.y8_5_6 - 1.0) + \
    0.5*(model.z8_5_6 - 1.0)*(model.z8_5_6 - 1.0) + 0.5*(model.x9_5_6 - 1.0)*(model.x9_5_6 - 1.0) + \
    0.5*(model.y9_5_6 - 1.0)*(model.y9_5_6 - 1.0) + 0.5*(model.z9_5_6 - 1.0)*(model.z9_5_6 - 1.0) + \
    0.5*(model.x1_6_6 - 1.0)*(model.x1_6_6 - 1.0) + 0.5*(model.y1_6_6 - 1.0)*(model.y1_6_6 - 1.0) + \
    0.5*(model.z1_6_6 - 1.0)*(model.z1_6_6 - 1.0) + 0.5*(model.x2_6_6 - 1.0)*(model.x2_6_6 - 1.0) + \
    0.5*(model.y2_6_6 - 1.0)*(model.y2_6_6 - 1.0) + 0.5*(model.z2_6_6 - 1.0)*(model.z2_6_6 - 1.0) + \
    0.5*(model.x3_6_6 - 1.0)*(model.x3_6_6 - 1.0) + 0.5*(model.y3_6_6 - 1.0)*(model.y3_6_6 - 1.0) + \
    0.5*(model.z3_6_6 - 1.0)*(model.z3_6_6 - 1.0) + 0.5*(model.x4_6_6 - 1.0)*(model.x4_6_6 - 1.0) + \
    0.5*(model.y4_6_6 - 1.0)*(model.y4_6_6 - 1.0) + 0.5*(model.z4_6_6 - 1.0)*(model.z4_6_6 - 1.0) + \
    0.5*(model.x5_6_6 - 1.0)*(model.x5_6_6 - 1.0) + 0.5*(model.y5_6_6 - 1.0)*(model.y5_6_6 - 1.0) + \
    0.5*(model.z5_6_6 - 1.0)*(model.z5_6_6 - 1.0) + 0.5*(model.x6_6_6 - 1.0)*(model.x6_6_6 - 1.0) + \
    0.5*(model.y6_6_6 - 1.0)*(model.y6_6_6 - 1.0) + 0.5*(model.z6_6_6 - 1.0)*(model.z6_6_6 - 1.0) + \
    0.5*(model.x7_6_6 - 1.0)*(model.x7_6_6 - 1.0) + 0.5*(model.y7_6_6 - 1.0)*(model.y7_6_6 - 1.0) + \
    0.5*(model.z7_6_6 - 1.0)*(model.z7_6_6 - 1.0) + 0.5*(model.x8_6_6 - 1.0)*(model.x8_6_6 - 1.0) + \
    0.5*(model.y8_6_6 - 1.0)*(model.y8_6_6 - 1.0) + 0.5*(model.z8_6_6 - 1.0)*(model.z8_6_6 - 1.0) + \
    0.5*(model.x9_6_6 - 1.0)*(model.x9_6_6 - 1.0) + 0.5*(model.y9_6_6 - 1.0)*(model.y9_6_6 - 1.0) + \
    0.5*(model.z9_6_6 - 1.0)*(model.z9_6_6 - 1.0) + 0.5*(model.x1_7_6 - 1.0)*(model.x1_7_6 - 1.0) + \
    0.5*(model.y1_7_6 - 1.0)*(model.y1_7_6 - 1.0) + 0.5*(model.z1_7_6 - 1.0)*(model.z1_7_6 - 1.0) + \
    0.5*(model.x2_7_6 - 1.0)*(model.x2_7_6 - 1.0) + 0.5*(model.y2_7_6 - 1.0)*(model.y2_7_6 - 1.0) + \
    0.5*(model.z2_7_6 - 1.0)*(model.z2_7_6 - 1.0) + 0.5*(model.x3_7_6 - 1.0)*(model.x3_7_6 - 1.0) + \
    0.5*(model.y3_7_6 - 1.0)*(model.y3_7_6 - 1.0) + 0.5*(model.z3_7_6 - 1.0)*(model.z3_7_6 - 1.0) + \
    0.5*(model.x4_7_6 - 1.0)*(model.x4_7_6 - 1.0) + 0.5*(model.y4_7_6 - 1.0)*(model.y4_7_6 - 1.0) + \
    0.5*(model.z4_7_6 - 1.0)*(model.z4_7_6 - 1.0) + 0.5*(model.x5_7_6 - 1.0)*(model.x5_7_6 - 1.0) + \
    0.5*(model.y5_7_6 - 1.0)*(model.y5_7_6 - 1.0) + 0.5*(model.z5_7_6 - 1.0)*(model.z5_7_6 - 1.0) + \
    0.5*(model.x6_7_6 - 1.0)*(model.x6_7_6 - 1.0) + 0.5*(model.y6_7_6 - 1.0)*(model.y6_7_6 - 1.0) + \
    0.5*(model.z6_7_6 - 1.0)*(model.z6_7_6 - 1.0) + 0.5*(model.x7_7_6 - 1.0)*(model.x7_7_6 - 1.0) + \
    0.5*(model.y7_7_6 - 1.0)*(model.y7_7_6 - 1.0) + 0.5*(model.z7_7_6 - 1.0)*(model.z7_7_6 - 1.0) + \
    0.5*(model.x8_7_6 - 1.0)*(model.x8_7_6 - 1.0) + 0.5*(model.y8_7_6 - 1.0)*(model.y8_7_6 - 1.0) + \
    0.5*(model.z8_7_6 - 1.0)*(model.z8_7_6 - 1.0) + 0.5*(model.x9_7_6 - 1.0)*(model.x9_7_6 - 1.0) + \
    0.5*(model.y9_7_6 - 1.0)*(model.y9_7_6 - 1.0) + 0.5*(model.z9_7_6 - 1.0)*(model.z9_7_6 - 1.0) + \
    0.5*(model.x1_8_6 - 1.0)*(model.x1_8_6 - 1.0) + 0.5*(model.y1_8_6 - 1.0)*(model.y1_8_6 - 1.0) + \
    0.5*(model.z1_8_6 - 1.0)*(model.z1_8_6 - 1.0) + 0.5*(model.x2_8_6 - 1.0)*(model.x2_8_6 - 1.0) + \
    0.5*(model.y2_8_6 - 1.0)*(model.y2_8_6 - 1.0) + 0.5*(model.z2_8_6 - 1.0)*(model.z2_8_6 - 1.0) + \
    0.5*(model.x3_8_6 - 1.0)*(model.x3_8_6 - 1.0) + 0.5*(model.y3_8_6 - 1.0)*(model.y3_8_6 - 1.0) + \
    0.5*(model.z3_8_6 - 1.0)*(model.z3_8_6 - 1.0) + 0.5*(model.x4_8_6 - 1.0)*(model.x4_8_6 - 1.0) + \
    0.5*(model.y4_8_6 - 1.0)*(model.y4_8_6 - 1.0) + 0.5*(model.z4_8_6 - 1.0)*(model.z4_8_6 - 1.0) + \
    0.5*(model.x5_8_6 - 1.0)*(model.x5_8_6 - 1.0) + 0.5*(model.y5_8_6 - 1.0)*(model.y5_8_6 - 1.0) + \
    0.5*(model.z5_8_6 - 1.0)*(model.z5_8_6 - 1.0) + 0.5*(model.x6_8_6 - 1.0)*(model.x6_8_6 - 1.0) + \
    0.5*(model.y6_8_6 - 1.0)*(model.y6_8_6 - 1.0) + 0.5*(model.z6_8_6 - 1.0)*(model.z6_8_6 - 1.0) + \
    0.5*(model.x7_8_6 - 1.0)*(model.x7_8_6 - 1.0) + 0.5*(model.y7_8_6 - 1.0)*(model.y7_8_6 - 1.0) + \
    0.5*(model.z7_8_6 - 1.0)*(model.z7_8_6 - 1.0) + 0.5*(model.x8_8_6 - 1.0)*(model.x8_8_6 - 1.0) + \
    0.5*(model.y8_8_6 - 1.0)*(model.y8_8_6 - 1.0) + 0.5*(model.z8_8_6 - 1.0)*(model.z8_8_6 - 1.0) + \
    0.5*(model.x9_8_6 - 1.0)*(model.x9_8_6 - 1.0) + 0.5*(model.y9_8_6 - 1.0)*(model.y9_8_6 - 1.0) + \
    0.5*(model.z9_8_6 - 1.0)*(model.z9_8_6 - 1.0) + 0.5*(model.x1_9_6 - 1.0)*(model.x1_9_6 - 1.0) + \
    0.5*(model.y1_9_6 - 1.0)*(model.y1_9_6 - 1.0) + 0.5*(model.z1_9_6 - 1.0)*(model.z1_9_6 - 1.0) + \
    0.5*(model.x2_9_6 - 1.0)*(model.x2_9_6 - 1.0) + 0.5*(model.y2_9_6 - 1.0)*(model.y2_9_6 - 1.0) + \
    0.5*(model.z2_9_6 - 1.0)*(model.z2_9_6 - 1.0) + 0.5*(model.x3_9_6 - 1.0)*(model.x3_9_6 - 1.0) + \
    0.5*(model.y3_9_6 - 1.0)*(model.y3_9_6 - 1.0) + 0.5*(model.z3_9_6 - 1.0)*(model.z3_9_6 - 1.0) + \
    0.5*(model.x4_9_6 - 1.0)*(model.x4_9_6 - 1.0) + 0.5*(model.y4_9_6 - 1.0)*(model.y4_9_6 - 1.0) + \
    0.5*(model.z4_9_6 - 1.0)*(model.z4_9_6 - 1.0) + 0.5*(model.x5_9_6 - 1.0)*(model.x5_9_6 - 1.0) + \
    0.5*(model.y5_9_6 - 1.0)*(model.y5_9_6 - 1.0) + 0.5*(model.z5_9_6 - 1.0)*(model.z5_9_6 - 1.0) + \
    0.5*(model.x6_9_6 - 1.0)*(model.x6_9_6 - 1.0) + 0.5*(model.y6_9_6 - 1.0)*(model.y6_9_6 - 1.0) + \
    0.5*(model.z6_9_6 - 1.0)*(model.z6_9_6 - 1.0) + 0.5*(model.x7_9_6 - 1.0)*(model.x7_9_6 - 1.0) + \
    0.5*(model.y7_9_6 - 1.0)*(model.y7_9_6 - 1.0) + 0.5*(model.z7_9_6 - 1.0)*(model.z7_9_6 - 1.0) + \
    0.5*(model.x8_9_6 - 1.0)*(model.x8_9_6 - 1.0) + 0.5*(model.y8_9_6 - 1.0)*(model.y8_9_6 - 1.0) + \
    0.5*(model.z8_9_6 - 1.0)*(model.z8_9_6 - 1.0) + 0.5*(model.x9_9_6 - 1.0)*(model.x9_9_6 - 1.0) + \
    0.5*(model.y9_9_6 - 1.0)*(model.y9_9_6 - 1.0) + 0.5*(model.z9_9_6 - 1.0)*(model.z9_9_6 - 1.0) + \
    0.5*(model.x1_1_7 - 1.0)*(model.x1_1_7 - 1.0) + 0.5*(model.y1_1_7 - 1.0)*(model.y1_1_7 - 1.0) + \
    0.5*(model.z1_1_7 - 1.0)*(model.z1_1_7 - 1.0) + 0.5*(model.x2_1_7 - 1.0)*(model.x2_1_7 - 1.0) + \
    0.5*(model.y2_1_7 - 1.0)*(model.y2_1_7 - 1.0) + 0.5*(model.z2_1_7 - 1.0)*(model.z2_1_7 - 1.0) + \
    0.5*(model.x3_1_7 - 1.0)*(model.x3_1_7 - 1.0) + 0.5*(model.y3_1_7 - 1.0)*(model.y3_1_7 - 1.0) + \
    0.5*(model.z3_1_7 - 1.0)*(model.z3_1_7 - 1.0) + 0.5*(model.x4_1_7 - 1.0)*(model.x4_1_7 - 1.0) + \
    0.5*(model.y4_1_7 - 1.0)*(model.y4_1_7 - 1.0) + 0.5*(model.z4_1_7 - 1.0)*(model.z4_1_7 - 1.0) + \
    0.5*(model.x5_1_7 - 1.0)*(model.x5_1_7 - 1.0) + 0.5*(model.y5_1_7 - 1.0)*(model.y5_1_7 - 1.0) + \
    0.5*(model.z5_1_7 - 1.0)*(model.z5_1_7 - 1.0) + 0.5*(model.x6_1_7 - 1.0)*(model.x6_1_7 - 1.0) + \
    0.5*(model.y6_1_7 - 1.0)*(model.y6_1_7 - 1.0) + 0.5*(model.z6_1_7 - 1.0)*(model.z6_1_7 - 1.0) + \
    0.5*(model.x7_1_7 - 1.0)*(model.x7_1_7 - 1.0) + 0.5*(model.y7_1_7 - 1.0)*(model.y7_1_7 - 1.0) + \
    0.5*(model.z7_1_7 - 1.0)*(model.z7_1_7 - 1.0) + 0.5*(model.x8_1_7 - 1.0)*(model.x8_1_7 - 1.0) + \
    0.5*(model.y8_1_7 - 1.0)*(model.y8_1_7 - 1.0) + 0.5*(model.z8_1_7 - 1.0)*(model.z8_1_7 - 1.0) + \
    0.5*(model.x9_1_7 - 1.0)*(model.x9_1_7 - 1.0) + 0.5*(model.y9_1_7 - 1.0)*(model.y9_1_7 - 1.0) + \
    0.5*(model.z9_1_7 - 1.0)*(model.z9_1_7 - 1.0) + 0.5*(model.x1_2_7 - 1.0)*(model.x1_2_7 - 1.0) + \
    0.5*(model.y1_2_7 - 1.0)*(model.y1_2_7 - 1.0) + 0.5*(model.z1_2_7 - 1.0)*(model.z1_2_7 - 1.0) + \
    0.5*(model.x2_2_7 - 1.0)*(model.x2_2_7 - 1.0) + 0.5*(model.y2_2_7 - 1.0)*(model.y2_2_7 - 1.0) + \
    0.5*(model.z2_2_7 - 1.0)*(model.z2_2_7 - 1.0) + 0.5*(model.x3_2_7 - 1.0)*(model.x3_2_7 - 1.0) + \
    0.5*(model.y3_2_7 - 1.0)*(model.y3_2_7 - 1.0) + 0.5*(model.z3_2_7 - 1.0)*(model.z3_2_7 - 1.0) + \
    0.5*(model.x4_2_7 - 1.0)*(model.x4_2_7 - 1.0) + 0.5*(model.y4_2_7 - 1.0)*(model.y4_2_7 - 1.0) + \
    0.5*(model.z4_2_7 - 1.0)*(model.z4_2_7 - 1.0) + 0.5*(model.x5_2_7 - 1.0)*(model.x5_2_7 - 1.0) + \
    0.5*(model.y5_2_7 - 1.0)*(model.y5_2_7 - 1.0) + 0.5*(model.z5_2_7 - 1.0)*(model.z5_2_7 - 1.0) + \
    0.5*(model.x6_2_7 - 1.0)*(model.x6_2_7 - 1.0) + 0.5*(model.y6_2_7 - 1.0)*(model.y6_2_7 - 1.0) + \
    0.5*(model.z6_2_7 - 1.0)*(model.z6_2_7 - 1.0) + 0.5*(model.x7_2_7 - 1.0)*(model.x7_2_7 - 1.0) + \
    0.5*(model.y7_2_7 - 1.0)*(model.y7_2_7 - 1.0) + 0.5*(model.z7_2_7 - 1.0)*(model.z7_2_7 - 1.0) + \
    0.5*(model.x8_2_7 - 1.0)*(model.x8_2_7 - 1.0) + 0.5*(model.y8_2_7 - 1.0)*(model.y8_2_7 - 1.0) + \
    0.5*(model.z8_2_7 - 1.0)*(model.z8_2_7 - 1.0) + 0.5*(model.x9_2_7 - 1.0)*(model.x9_2_7 - 1.0) + \
    0.5*(model.y9_2_7 - 1.0)*(model.y9_2_7 - 1.0) + 0.5*(model.z9_2_7 - 1.0)*(model.z9_2_7 - 1.0) + \
    0.5*(model.x1_3_7 - 1.0)*(model.x1_3_7 - 1.0) + 0.5*(model.y1_3_7 - 1.0)*(model.y1_3_7 - 1.0) + \
    0.5*(model.z1_3_7 - 1.0)*(model.z1_3_7 - 1.0) + 0.5*(model.x2_3_7 - 1.0)*(model.x2_3_7 - 1.0) + \
    0.5*(model.y2_3_7 - 1.0)*(model.y2_3_7 - 1.0) + 0.5*(model.z2_3_7 - 1.0)*(model.z2_3_7 - 1.0) + \
    0.5*(model.x3_3_7 - 1.0)*(model.x3_3_7 - 1.0) + 0.5*(model.y3_3_7 - 1.0)*(model.y3_3_7 - 1.0) + \
    0.5*(model.z3_3_7 - 1.0)*(model.z3_3_7 - 1.0) + 0.5*(model.x4_3_7 - 1.0)*(model.x4_3_7 - 1.0) + \
    0.5*(model.y4_3_7 - 1.0)*(model.y4_3_7 - 1.0) + 0.5*(model.z4_3_7 - 1.0)*(model.z4_3_7 - 1.0) + \
    0.5*(model.x5_3_7 - 1.0)*(model.x5_3_7 - 1.0) + 0.5*(model.y5_3_7 - 1.0)*(model.y5_3_7 - 1.0) + \
    0.5*(model.z5_3_7 - 1.0)*(model.z5_3_7 - 1.0) + 0.5*(model.x6_3_7 - 1.0)*(model.x6_3_7 - 1.0) + \
    0.5*(model.y6_3_7 - 1.0)*(model.y6_3_7 - 1.0) + 0.5*(model.z6_3_7 - 1.0)*(model.z6_3_7 - 1.0) + \
    0.5*(model.x7_3_7 - 1.0)*(model.x7_3_7 - 1.0) + 0.5*(model.y7_3_7 - 1.0)*(model.y7_3_7 - 1.0) + \
    0.5*(model.z7_3_7 - 1.0)*(model.z7_3_7 - 1.0) + 0.5*(model.x8_3_7 - 1.0)*(model.x8_3_7 - 1.0) + \
    0.5*(model.y8_3_7 - 1.0)*(model.y8_3_7 - 1.0) + 0.5*(model.z8_3_7 - 1.0)*(model.z8_3_7 - 1.0) + \
    0.5*(model.x9_3_7 - 1.0)*(model.x9_3_7 - 1.0) + 0.5*(model.y9_3_7 - 1.0)*(model.y9_3_7 - 1.0) + \
    0.5*(model.z9_3_7 - 1.0)*(model.z9_3_7 - 1.0) + 0.5*(model.x1_4_7 - 1.0)*(model.x1_4_7 - 1.0) + \
    0.5*(model.y1_4_7 - 1.0)*(model.y1_4_7 - 1.0) + 0.5*(model.z1_4_7 - 1.0)*(model.z1_4_7 - 1.0) + \
    0.5*(model.x2_4_7 - 1.0)*(model.x2_4_7 - 1.0) + 0.5*(model.y2_4_7 - 1.0)*(model.y2_4_7 - 1.0) + \
    0.5*(model.z2_4_7 - 1.0)*(model.z2_4_7 - 1.0) + 0.5*(model.x3_4_7 - 1.0)*(model.x3_4_7 - 1.0) + \
    0.5*(model.y3_4_7 - 1.0)*(model.y3_4_7 - 1.0) + 0.5*(model.z3_4_7 - 1.0)*(model.z3_4_7 - 1.0) + \
    0.5*(model.x4_4_7 - 1.0)*(model.x4_4_7 - 1.0) + 0.5*(model.y4_4_7 - 1.0)*(model.y4_4_7 - 1.0) + \
    0.5*(model.z4_4_7 - 1.0)*(model.z4_4_7 - 1.0) + 0.5*(model.x5_4_7 - 1.0)*(model.x5_4_7 - 1.0) + \
    0.5*(model.y5_4_7 - 1.0)*(model.y5_4_7 - 1.0) + 0.5*(model.z5_4_7 - 1.0)*(model.z5_4_7 - 1.0) + \
    0.5*(model.x6_4_7 - 1.0)*(model.x6_4_7 - 1.0) + 0.5*(model.y6_4_7 - 1.0)*(model.y6_4_7 - 1.0) + \
    0.5*(model.z6_4_7 - 1.0)*(model.z6_4_7 - 1.0) + 0.5*(model.x7_4_7 - 1.0)*(model.x7_4_7 - 1.0) + \
    0.5*(model.y7_4_7 - 1.0)*(model.y7_4_7 - 1.0) + 0.5*(model.z7_4_7 - 1.0)*(model.z7_4_7 - 1.0) + \
    0.5*(model.x8_4_7 - 1.0)*(model.x8_4_7 - 1.0) + 0.5*(model.y8_4_7 - 1.0)*(model.y8_4_7 - 1.0) + \
    0.5*(model.z8_4_7 - 1.0)*(model.z8_4_7 - 1.0) + 0.5*(model.x9_4_7 - 1.0)*(model.x9_4_7 - 1.0) + \
    0.5*(model.y9_4_7 - 1.0)*(model.y9_4_7 - 1.0) + 0.5*(model.z9_4_7 - 1.0)*(model.z9_4_7 - 1.0) + \
    0.5*(model.x1_5_7 - 1.0)*(model.x1_5_7 - 1.0) + 0.5*(model.y1_5_7 - 1.0)*(model.y1_5_7 - 1.0) + \
    0.5*(model.z1_5_7 - 1.0)*(model.z1_5_7 - 1.0) + 0.5*(model.x2_5_7 - 1.0)*(model.x2_5_7 - 1.0) + \
    0.5*(model.y2_5_7 - 1.0)*(model.y2_5_7 - 1.0) + 0.5*(model.z2_5_7 - 1.0)*(model.z2_5_7 - 1.0) + \
    0.5*(model.x3_5_7 - 1.0)*(model.x3_5_7 - 1.0) + 0.5*(model.y3_5_7 - 1.0)*(model.y3_5_7 - 1.0) + \
    0.5*(model.z3_5_7 - 1.0)*(model.z3_5_7 - 1.0) + 0.5*(model.x4_5_7 - 1.0)*(model.x4_5_7 - 1.0) + \
    0.5*(model.y4_5_7 - 1.0)*(model.y4_5_7 - 1.0) + 0.5*(model.z4_5_7 - 1.0)*(model.z4_5_7 - 1.0) + \
    0.5*(model.x5_5_7 - 1.0)*(model.x5_5_7 - 1.0) + 0.5*(model.y5_5_7 - 1.0)*(model.y5_5_7 - 1.0) + \
    0.5*(model.z5_5_7 - 1.0)*(model.z5_5_7 - 1.0) + 0.5*(model.x6_5_7 - 1.0)*(model.x6_5_7 - 1.0) + \
    0.5*(model.y6_5_7 - 1.0)*(model.y6_5_7 - 1.0) + 0.5*(model.z6_5_7 - 1.0)*(model.z6_5_7 - 1.0) + \
    0.5*(model.x7_5_7 - 1.0)*(model.x7_5_7 - 1.0) + 0.5*(model.y7_5_7 - 1.0)*(model.y7_5_7 - 1.0) + \
    0.5*(model.z7_5_7 - 1.0)*(model.z7_5_7 - 1.0) + 0.5*(model.x8_5_7 - 1.0)*(model.x8_5_7 - 1.0) + \
    0.5*(model.y8_5_7 - 1.0)*(model.y8_5_7 - 1.0) + 0.5*(model.z8_5_7 - 1.0)*(model.z8_5_7 - 1.0) + \
    0.5*(model.x9_5_7 - 1.0)*(model.x9_5_7 - 1.0) + 0.5*(model.y9_5_7 - 1.0)*(model.y9_5_7 - 1.0) + \
    0.5*(model.z9_5_7 - 1.0)*(model.z9_5_7 - 1.0) + 0.5*(model.x1_6_7 - 1.0)*(model.x1_6_7 - 1.0) + \
    0.5*(model.y1_6_7 - 1.0)*(model.y1_6_7 - 1.0) + 0.5*(model.z1_6_7 - 1.0)*(model.z1_6_7 - 1.0) + \
    0.5*(model.x2_6_7 - 1.0)*(model.x2_6_7 - 1.0) + 0.5*(model.y2_6_7 - 1.0)*(model.y2_6_7 - 1.0) + \
    0.5*(model.z2_6_7 - 1.0)*(model.z2_6_7 - 1.0) + 0.5*(model.x3_6_7 - 1.0)*(model.x3_6_7 - 1.0) + \
    0.5*(model.y3_6_7 - 1.0)*(model.y3_6_7 - 1.0) + 0.5*(model.z3_6_7 - 1.0)*(model.z3_6_7 - 1.0) + \
    0.5*(model.x4_6_7 - 1.0)*(model.x4_6_7 - 1.0) + 0.5*(model.y4_6_7 - 1.0)*(model.y4_6_7 - 1.0) + \
    0.5*(model.z4_6_7 - 1.0)*(model.z4_6_7 - 1.0) + 0.5*(model.x5_6_7 - 1.0)*(model.x5_6_7 - 1.0) + \
    0.5*(model.y5_6_7 - 1.0)*(model.y5_6_7 - 1.0) + 0.5*(model.z5_6_7 - 1.0)*(model.z5_6_7 - 1.0) + \
    0.5*(model.x6_6_7 - 1.0)*(model.x6_6_7 - 1.0) + 0.5*(model.y6_6_7 - 1.0)*(model.y6_6_7 - 1.0) + \
    0.5*(model.z6_6_7 - 1.0)*(model.z6_6_7 - 1.0) + 0.5*(model.x7_6_7 - 1.0)*(model.x7_6_7 - 1.0) + \
    0.5*(model.y7_6_7 - 1.0)*(model.y7_6_7 - 1.0) + 0.5*(model.z7_6_7 - 1.0)*(model.z7_6_7 - 1.0) + \
    0.5*(model.x8_6_7 - 1.0)*(model.x8_6_7 - 1.0) + 0.5*(model.y8_6_7 - 1.0)*(model.y8_6_7 - 1.0) + \
    0.5*(model.z8_6_7 - 1.0)*(model.z8_6_7 - 1.0) + 0.5*(model.x9_6_7 - 1.0)*(model.x9_6_7 - 1.0) + \
    0.5*(model.y9_6_7 - 1.0)*(model.y9_6_7 - 1.0) + 0.5*(model.z9_6_7 - 1.0)*(model.z9_6_7 - 1.0) + \
    0.5*(model.x1_7_7 - 1.0)*(model.x1_7_7 - 1.0) + 0.5*(model.y1_7_7 - 1.0)*(model.y1_7_7 - 1.0) + \
    0.5*(model.z1_7_7 - 1.0)*(model.z1_7_7 - 1.0) + 0.5*(model.x2_7_7 - 1.0)*(model.x2_7_7 - 1.0) + \
    0.5*(model.y2_7_7 - 1.0)*(model.y2_7_7 - 1.0) + 0.5*(model.z2_7_7 - 1.0)*(model.z2_7_7 - 1.0) + \
    0.5*(model.x3_7_7 - 1.0)*(model.x3_7_7 - 1.0) + 0.5*(model.y3_7_7 - 1.0)*(model.y3_7_7 - 1.0) + \
    0.5*(model.z3_7_7 - 1.0)*(model.z3_7_7 - 1.0) + 0.5*(model.x4_7_7 - 1.0)*(model.x4_7_7 - 1.0) + \
    0.5*(model.y4_7_7 - 1.0)*(model.y4_7_7 - 1.0) + 0.5*(model.z4_7_7 - 1.0)*(model.z4_7_7 - 1.0) + \
    0.5*(model.x5_7_7 - 1.0)*(model.x5_7_7 - 1.0) + 0.5*(model.y5_7_7 - 1.0)*(model.y5_7_7 - 1.0) + \
    0.5*(model.z5_7_7 - 1.0)*(model.z5_7_7 - 1.0) + 0.5*(model.x6_7_7 - 1.0)*(model.x6_7_7 - 1.0) + \
    0.5*(model.y6_7_7 - 1.0)*(model.y6_7_7 - 1.0) + 0.5*(model.z6_7_7 - 1.0)*(model.z6_7_7 - 1.0) + \
    0.5*(model.x7_7_7 - 1.0)*(model.x7_7_7 - 1.0) + 0.5*(model.y7_7_7 - 1.0)*(model.y7_7_7 - 1.0) + \
    0.5*(model.z7_7_7 - 1.0)*(model.z7_7_7 - 1.0) + 0.5*(model.x8_7_7 - 1.0)*(model.x8_7_7 - 1.0) + \
    0.5*(model.y8_7_7 - 1.0)*(model.y8_7_7 - 1.0) + 0.5*(model.z8_7_7 - 1.0)*(model.z8_7_7 - 1.0) + \
    0.5*(model.x9_7_7 - 1.0)*(model.x9_7_7 - 1.0) + 0.5*(model.y9_7_7 - 1.0)*(model.y9_7_7 - 1.0) + \
    0.5*(model.z9_7_7 - 1.0)*(model.z9_7_7 - 1.0) + 0.5*(model.x1_8_7 - 1.0)*(model.x1_8_7 - 1.0) + \
    0.5*(model.y1_8_7 - 1.0)*(model.y1_8_7 - 1.0) + 0.5*(model.z1_8_7 - 1.0)*(model.z1_8_7 - 1.0) + \
    0.5*(model.x2_8_7 - 1.0)*(model.x2_8_7 - 1.0) + 0.5*(model.y2_8_7 - 1.0)*(model.y2_8_7 - 1.0) + \
    0.5*(model.z2_8_7 - 1.0)*(model.z2_8_7 - 1.0) + 0.5*(model.x3_8_7 - 1.0)*(model.x3_8_7 - 1.0) + \
    0.5*(model.y3_8_7 - 1.0)*(model.y3_8_7 - 1.0) + 0.5*(model.z3_8_7 - 1.0)*(model.z3_8_7 - 1.0) + \
    0.5*(model.x4_8_7 - 1.0)*(model.x4_8_7 - 1.0) + 0.5*(model.y4_8_7 - 1.0)*(model.y4_8_7 - 1.0) + \
    0.5*(model.z4_8_7 - 1.0)*(model.z4_8_7 - 1.0) + 0.5*(model.x5_8_7 - 1.0)*(model.x5_8_7 - 1.0) + \
    0.5*(model.y5_8_7 - 1.0)*(model.y5_8_7 - 1.0) + 0.5*(model.z5_8_7 - 1.0)*(model.z5_8_7 - 1.0) + \
    0.5*(model.x6_8_7 - 1.0)*(model.x6_8_7 - 1.0) + 0.5*(model.y6_8_7 - 1.0)*(model.y6_8_7 - 1.0) + \
    0.5*(model.z6_8_7 - 1.0)*(model.z6_8_7 - 1.0) + 0.5*(model.x7_8_7 - 1.0)*(model.x7_8_7 - 1.0) + \
    0.5*(model.y7_8_7 - 1.0)*(model.y7_8_7 - 1.0) + 0.5*(model.z7_8_7 - 1.0)*(model.z7_8_7 - 1.0) + \
    0.5*(model.x8_8_7 - 1.0)*(model.x8_8_7 - 1.0) + 0.5*(model.y8_8_7 - 1.0)*(model.y8_8_7 - 1.0) + \
    0.5*(model.z8_8_7 - 1.0)*(model.z8_8_7 - 1.0) + 0.5*(model.x9_8_7 - 1.0)*(model.x9_8_7 - 1.0) + \
    0.5*(model.y9_8_7 - 1.0)*(model.y9_8_7 - 1.0) + 0.5*(model.z9_8_7 - 1.0)*(model.z9_8_7 - 1.0) + \
    0.5*(model.x1_9_7 - 1.0)*(model.x1_9_7 - 1.0) + 0.5*(model.y1_9_7 - 1.0)*(model.y1_9_7 - 1.0) + \
    0.5*(model.z1_9_7 - 1.0)*(model.z1_9_7 - 1.0) + 0.5*(model.x2_9_7 - 1.0)*(model.x2_9_7 - 1.0) + \
    0.5*(model.y2_9_7 - 1.0)*(model.y2_9_7 - 1.0) + 0.5*(model.z2_9_7 - 1.0)*(model.z2_9_7 - 1.0) + \
    0.5*(model.x3_9_7 - 1.0)*(model.x3_9_7 - 1.0) + 0.5*(model.y3_9_7 - 1.0)*(model.y3_9_7 - 1.0) + \
    0.5*(model.z3_9_7 - 1.0)*(model.z3_9_7 - 1.0) + 0.5*(model.x4_9_7 - 1.0)*(model.x4_9_7 - 1.0) + \
    0.5*(model.y4_9_7 - 1.0)*(model.y4_9_7 - 1.0) + 0.5*(model.z4_9_7 - 1.0)*(model.z4_9_7 - 1.0) + \
    0.5*(model.x5_9_7 - 1.0)*(model.x5_9_7 - 1.0) + 0.5*(model.y5_9_7 - 1.0)*(model.y5_9_7 - 1.0) + \
    0.5*(model.z5_9_7 - 1.0)*(model.z5_9_7 - 1.0) + 0.5*(model.x6_9_7 - 1.0)*(model.x6_9_7 - 1.0) + \
    0.5*(model.y6_9_7 - 1.0)*(model.y6_9_7 - 1.0) + 0.5*(model.z6_9_7 - 1.0)*(model.z6_9_7 - 1.0) + \
    0.5*(model.x7_9_7 - 1.0)*(model.x7_9_7 - 1.0) + 0.5*(model.y7_9_7 - 1.0)*(model.y7_9_7 - 1.0) + \
    0.5*(model.z7_9_7 - 1.0)*(model.z7_9_7 - 1.0) + 0.5*(model.x8_9_7 - 1.0)*(model.x8_9_7 - 1.0) + \
    0.5*(model.y8_9_7 - 1.0)*(model.y8_9_7 - 1.0) + 0.5*(model.z8_9_7 - 1.0)*(model.z8_9_7 - 1.0) + \
    0.5*(model.x9_9_7 - 1.0)*(model.x9_9_7 - 1.0) + 0.5*(model.y9_9_7 - 1.0)*(model.y9_9_7 - 1.0) + \
    0.5*(model.z9_9_7 - 1.0)*(model.z9_9_7 - 1.0) + 0.5*(model.x1_1_8 - 1.0)*(model.x1_1_8 - 1.0) + \
    0.5*(model.y1_1_8 - 1.0)*(model.y1_1_8 - 1.0) + 0.5*(model.z1_1_8 - 1.0)*(model.z1_1_8 - 1.0) + \
    0.5*(model.x2_1_8 - 1.0)*(model.x2_1_8 - 1.0) + 0.5*(model.y2_1_8 - 1.0)*(model.y2_1_8 - 1.0) + \
    0.5*(model.z2_1_8 - 1.0)*(model.z2_1_8 - 1.0) + 0.5*(model.x3_1_8 - 1.0)*(model.x3_1_8 - 1.0) + \
    0.5*(model.y3_1_8 - 1.0)*(model.y3_1_8 - 1.0) + 0.5*(model.z3_1_8 - 1.0)*(model.z3_1_8 - 1.0) + \
    0.5*(model.x4_1_8 - 1.0)*(model.x4_1_8 - 1.0) + 0.5*(model.y4_1_8 - 1.0)*(model.y4_1_8 - 1.0) + \
    0.5*(model.z4_1_8 - 1.0)*(model.z4_1_8 - 1.0) + 0.5*(model.x5_1_8 - 1.0)*(model.x5_1_8 - 1.0) + \
    0.5*(model.y5_1_8 - 1.0)*(model.y5_1_8 - 1.0) + 0.5*(model.z5_1_8 - 1.0)*(model.z5_1_8 - 1.0) + \
    0.5*(model.x6_1_8 - 1.0)*(model.x6_1_8 - 1.0) + 0.5*(model.y6_1_8 - 1.0)*(model.y6_1_8 - 1.0) + \
    0.5*(model.z6_1_8 - 1.0)*(model.z6_1_8 - 1.0) + 0.5*(model.x7_1_8 - 1.0)*(model.x7_1_8 - 1.0) + \
    0.5*(model.y7_1_8 - 1.0)*(model.y7_1_8 - 1.0) + 0.5*(model.z7_1_8 - 1.0)*(model.z7_1_8 - 1.0) + \
    0.5*(model.x8_1_8 - 1.0)*(model.x8_1_8 - 1.0) + 0.5*(model.y8_1_8 - 1.0)*(model.y8_1_8 - 1.0) + \
    0.5*(model.z8_1_8 - 1.0)*(model.z8_1_8 - 1.0) + 0.5*(model.x9_1_8 - 1.0)*(model.x9_1_8 - 1.0) + \
    0.5*(model.y9_1_8 - 1.0)*(model.y9_1_8 - 1.0) + 0.5*(model.z9_1_8 - 1.0)*(model.z9_1_8 - 1.0) + \
    0.5*(model.x1_2_8 - 1.0)*(model.x1_2_8 - 1.0) + 0.5*(model.y1_2_8 - 1.0)*(model.y1_2_8 - 1.0) + \
    0.5*(model.z1_2_8 - 1.0)*(model.z1_2_8 - 1.0) + 0.5*(model.x2_2_8 - 1.0)*(model.x2_2_8 - 1.0) + \
    0.5*(model.y2_2_8 - 1.0)*(model.y2_2_8 - 1.0) + 0.5*(model.z2_2_8 - 1.0)*(model.z2_2_8 - 1.0) + \
    0.5*(model.x3_2_8 - 1.0)*(model.x3_2_8 - 1.0) + 0.5*(model.y3_2_8 - 1.0)*(model.y3_2_8 - 1.0) + \
    0.5*(model.z3_2_8 - 1.0)*(model.z3_2_8 - 1.0) + 0.5*(model.x4_2_8 - 1.0)*(model.x4_2_8 - 1.0) + \
    0.5*(model.y4_2_8 - 1.0)*(model.y4_2_8 - 1.0) + 0.5*(model.z4_2_8 - 1.0)*(model.z4_2_8 - 1.0) + \
    0.5*(model.x5_2_8 - 1.0)*(model.x5_2_8 - 1.0) + 0.5*(model.y5_2_8 - 1.0)*(model.y5_2_8 - 1.0) + \
    0.5*(model.z5_2_8 - 1.0)*(model.z5_2_8 - 1.0) + 0.5*(model.x6_2_8 - 1.0)*(model.x6_2_8 - 1.0) + \
    0.5*(model.y6_2_8 - 1.0)*(model.y6_2_8 - 1.0) + 0.5*(model.z6_2_8 - 1.0)*(model.z6_2_8 - 1.0) + \
    0.5*(model.x7_2_8 - 1.0)*(model.x7_2_8 - 1.0) + 0.5*(model.y7_2_8 - 1.0)*(model.y7_2_8 - 1.0) + \
    0.5*(model.z7_2_8 - 1.0)*(model.z7_2_8 - 1.0) + 0.5*(model.x8_2_8 - 1.0)*(model.x8_2_8 - 1.0) + \
    0.5*(model.y8_2_8 - 1.0)*(model.y8_2_8 - 1.0) + 0.5*(model.z8_2_8 - 1.0)*(model.z8_2_8 - 1.0) + \
    0.5*(model.x9_2_8 - 1.0)*(model.x9_2_8 - 1.0) + 0.5*(model.y9_2_8 - 1.0)*(model.y9_2_8 - 1.0) + \
    0.5*(model.z9_2_8 - 1.0)*(model.z9_2_8 - 1.0) + 0.5*(model.x1_3_8 - 1.0)*(model.x1_3_8 - 1.0) + \
    0.5*(model.y1_3_8 - 1.0)*(model.y1_3_8 - 1.0) + 0.5*(model.z1_3_8 - 1.0)*(model.z1_3_8 - 1.0) + \
    0.5*(model.x2_3_8 - 1.0)*(model.x2_3_8 - 1.0) + 0.5*(model.y2_3_8 - 1.0)*(model.y2_3_8 - 1.0) + \
    0.5*(model.z2_3_8 - 1.0)*(model.z2_3_8 - 1.0) + 0.5*(model.x3_3_8 - 1.0)*(model.x3_3_8 - 1.0) + \
    0.5*(model.y3_3_8 - 1.0)*(model.y3_3_8 - 1.0) + 0.5*(model.z3_3_8 - 1.0)*(model.z3_3_8 - 1.0) + \
    0.5*(model.x4_3_8 - 1.0)*(model.x4_3_8 - 1.0) + 0.5*(model.y4_3_8 - 1.0)*(model.y4_3_8 - 1.0) + \
    0.5*(model.z4_3_8 - 1.0)*(model.z4_3_8 - 1.0) + 0.5*(model.x5_3_8 - 1.0)*(model.x5_3_8 - 1.0) + \
    0.5*(model.y5_3_8 - 1.0)*(model.y5_3_8 - 1.0) + 0.5*(model.z5_3_8 - 1.0)*(model.z5_3_8 - 1.0) + \
    0.5*(model.x6_3_8 - 1.0)*(model.x6_3_8 - 1.0) + 0.5*(model.y6_3_8 - 1.0)*(model.y6_3_8 - 1.0) + \
    0.5*(model.z6_3_8 - 1.0)*(model.z6_3_8 - 1.0) + 0.5*(model.x7_3_8 - 1.0)*(model.x7_3_8 - 1.0) + \
    0.5*(model.y7_3_8 - 1.0)*(model.y7_3_8 - 1.0) + 0.5*(model.z7_3_8 - 1.0)*(model.z7_3_8 - 1.0) + \
    0.5*(model.x8_3_8 - 1.0)*(model.x8_3_8 - 1.0) + 0.5*(model.y8_3_8 - 1.0)*(model.y8_3_8 - 1.0) + \
    0.5*(model.z8_3_8 - 1.0)*(model.z8_3_8 - 1.0) + 0.5*(model.x9_3_8 - 1.0)*(model.x9_3_8 - 1.0) + \
    0.5*(model.y9_3_8 - 1.0)*(model.y9_3_8 - 1.0) + 0.5*(model.z9_3_8 - 1.0)*(model.z9_3_8 - 1.0) + \
    0.5*(model.x1_4_8 - 1.0)*(model.x1_4_8 - 1.0) + 0.5*(model.y1_4_8 - 1.0)*(model.y1_4_8 - 1.0) + \
    0.5*(model.z1_4_8 - 1.0)*(model.z1_4_8 - 1.0) + 0.5*(model.x2_4_8 - 1.0)*(model.x2_4_8 - 1.0) + \
    0.5*(model.y2_4_8 - 1.0)*(model.y2_4_8 - 1.0) + 0.5*(model.z2_4_8 - 1.0)*(model.z2_4_8 - 1.0) + \
    0.5*(model.x3_4_8 - 1.0)*(model.x3_4_8 - 1.0) + 0.5*(model.y3_4_8 - 1.0)*(model.y3_4_8 - 1.0) + \
    0.5*(model.z3_4_8 - 1.0)*(model.z3_4_8 - 1.0) + 0.5*(model.x4_4_8 - 1.0)*(model.x4_4_8 - 1.0) + \
    0.5*(model.y4_4_8 - 1.0)*(model.y4_4_8 - 1.0) + 0.5*(model.z4_4_8 - 1.0)*(model.z4_4_8 - 1.0) + \
    0.5*(model.x5_4_8 - 1.0)*(model.x5_4_8 - 1.0) + 0.5*(model.y5_4_8 - 1.0)*(model.y5_4_8 - 1.0) + \
    0.5*(model.z5_4_8 - 1.0)*(model.z5_4_8 - 1.0) + 0.5*(model.x6_4_8 - 1.0)*(model.x6_4_8 - 1.0) + \
    0.5*(model.y6_4_8 - 1.0)*(model.y6_4_8 - 1.0) + 0.5*(model.z6_4_8 - 1.0)*(model.z6_4_8 - 1.0) + \
    0.5*(model.x7_4_8 - 1.0)*(model.x7_4_8 - 1.0) + 0.5*(model.y7_4_8 - 1.0)*(model.y7_4_8 - 1.0) + \
    0.5*(model.z7_4_8 - 1.0)*(model.z7_4_8 - 1.0) + 0.5*(model.x8_4_8 - 1.0)*(model.x8_4_8 - 1.0) + \
    0.5*(model.y8_4_8 - 1.0)*(model.y8_4_8 - 1.0) + 0.5*(model.z8_4_8 - 1.0)*(model.z8_4_8 - 1.0) + \
    0.5*(model.x9_4_8 - 1.0)*(model.x9_4_8 - 1.0) + 0.5*(model.y9_4_8 - 1.0)*(model.y9_4_8 - 1.0) + \
    0.5*(model.z9_4_8 - 1.0)*(model.z9_4_8 - 1.0) + 0.5*(model.x1_5_8 - 1.0)*(model.x1_5_8 - 1.0) + \
    0.5*(model.y1_5_8 - 1.0)*(model.y1_5_8 - 1.0) + 0.5*(model.z1_5_8 - 1.0)*(model.z1_5_8 - 1.0) + \
    0.5*(model.x2_5_8 - 1.0)*(model.x2_5_8 - 1.0) + 0.5*(model.y2_5_8 - 1.0)*(model.y2_5_8 - 1.0) + \
    0.5*(model.z2_5_8 - 1.0)*(model.z2_5_8 - 1.0) + 0.5*(model.x3_5_8 - 1.0)*(model.x3_5_8 - 1.0) + \
    0.5*(model.y3_5_8 - 1.0)*(model.y3_5_8 - 1.0) + 0.5*(model.z3_5_8 - 1.0)*(model.z3_5_8 - 1.0) + \
    0.5*(model.x4_5_8 - 1.0)*(model.x4_5_8 - 1.0) + 0.5*(model.y4_5_8 - 1.0)*(model.y4_5_8 - 1.0) + \
    0.5*(model.z4_5_8 - 1.0)*(model.z4_5_8 - 1.0) + 0.5*(model.x5_5_8 - 1.0)*(model.x5_5_8 - 1.0) + \
    0.5*(model.y5_5_8 - 1.0)*(model.y5_5_8 - 1.0) + 0.5*(model.z5_5_8 - 1.0)*(model.z5_5_8 - 1.0) + \
    0.5*(model.x6_5_8 - 1.0)*(model.x6_5_8 - 1.0) + 0.5*(model.y6_5_8 - 1.0)*(model.y6_5_8 - 1.0) + \
    0.5*(model.z6_5_8 - 1.0)*(model.z6_5_8 - 1.0) + 0.5*(model.x7_5_8 - 1.0)*(model.x7_5_8 - 1.0) + \
    0.5*(model.y7_5_8 - 1.0)*(model.y7_5_8 - 1.0) + 0.5*(model.z7_5_8 - 1.0)*(model.z7_5_8 - 1.0) + \
    0.5*(model.x8_5_8 - 1.0)*(model.x8_5_8 - 1.0) + 0.5*(model.y8_5_8 - 1.0)*(model.y8_5_8 - 1.0) + \
    0.5*(model.z8_5_8 - 1.0)*(model.z8_5_8 - 1.0) + 0.5*(model.x9_5_8 - 1.0)*(model.x9_5_8 - 1.0) + \
    0.5*(model.y9_5_8 - 1.0)*(model.y9_5_8 - 1.0) + 0.5*(model.z9_5_8 - 1.0)*(model.z9_5_8 - 1.0) + \
    0.5*(model.x1_6_8 - 1.0)*(model.x1_6_8 - 1.0) + 0.5*(model.y1_6_8 - 1.0)*(model.y1_6_8 - 1.0) + \
    0.5*(model.z1_6_8 - 1.0)*(model.z1_6_8 - 1.0) + 0.5*(model.x2_6_8 - 1.0)*(model.x2_6_8 - 1.0) + \
    0.5*(model.y2_6_8 - 1.0)*(model.y2_6_8 - 1.0) + 0.5*(model.z2_6_8 - 1.0)*(model.z2_6_8 - 1.0) + \
    0.5*(model.x3_6_8 - 1.0)*(model.x3_6_8 - 1.0) + 0.5*(model.y3_6_8 - 1.0)*(model.y3_6_8 - 1.0) + \
    0.5*(model.z3_6_8 - 1.0)*(model.z3_6_8 - 1.0) + 0.5*(model.x4_6_8 - 1.0)*(model.x4_6_8 - 1.0) + \
    0.5*(model.y4_6_8 - 1.0)*(model.y4_6_8 - 1.0) + 0.5*(model.z4_6_8 - 1.0)*(model.z4_6_8 - 1.0) + \
    0.5*(model.x5_6_8 - 1.0)*(model.x5_6_8 - 1.0) + 0.5*(model.y5_6_8 - 1.0)*(model.y5_6_8 - 1.0) + \
    0.5*(model.z5_6_8 - 1.0)*(model.z5_6_8 - 1.0) + 0.5*(model.x6_6_8 - 1.0)*(model.x6_6_8 - 1.0) + \
    0.5*(model.y6_6_8 - 1.0)*(model.y6_6_8 - 1.0) + 0.5*(model.z6_6_8 - 1.0)*(model.z6_6_8 - 1.0) + \
    0.5*(model.x7_6_8 - 1.0)*(model.x7_6_8 - 1.0) + 0.5*(model.y7_6_8 - 1.0)*(model.y7_6_8 - 1.0) + \
    0.5*(model.z7_6_8 - 1.0)*(model.z7_6_8 - 1.0) + 0.5*(model.x8_6_8 - 1.0)*(model.x8_6_8 - 1.0) + \
    0.5*(model.y8_6_8 - 1.0)*(model.y8_6_8 - 1.0) + 0.5*(model.z8_6_8 - 1.0)*(model.z8_6_8 - 1.0) + \
    0.5*(model.x9_6_8 - 1.0)*(model.x9_6_8 - 1.0) + 0.5*(model.y9_6_8 - 1.0)*(model.y9_6_8 - 1.0) + \
    0.5*(model.z9_6_8 - 1.0)*(model.z9_6_8 - 1.0) + 0.5*(model.x1_7_8 - 1.0)*(model.x1_7_8 - 1.0) + \
    0.5*(model.y1_7_8 - 1.0)*(model.y1_7_8 - 1.0) + 0.5*(model.z1_7_8 - 1.0)*(model.z1_7_8 - 1.0) + \
    0.5*(model.x2_7_8 - 1.0)*(model.x2_7_8 - 1.0) + 0.5*(model.y2_7_8 - 1.0)*(model.y2_7_8 - 1.0) + \
    0.5*(model.z2_7_8 - 1.0)*(model.z2_7_8 - 1.0) + 0.5*(model.x3_7_8 - 1.0)*(model.x3_7_8 - 1.0) + \
    0.5*(model.y3_7_8 - 1.0)*(model.y3_7_8 - 1.0) + 0.5*(model.z3_7_8 - 1.0)*(model.z3_7_8 - 1.0) + \
    0.5*(model.x4_7_8 - 1.0)*(model.x4_7_8 - 1.0) + 0.5*(model.y4_7_8 - 1.0)*(model.y4_7_8 - 1.0) + \
    0.5*(model.z4_7_8 - 1.0)*(model.z4_7_8 - 1.0) + 0.5*(model.x5_7_8 - 1.0)*(model.x5_7_8 - 1.0) + \
    0.5*(model.y5_7_8 - 1.0)*(model.y5_7_8 - 1.0) + 0.5*(model.z5_7_8 - 1.0)*(model.z5_7_8 - 1.0) + \
    0.5*(model.x6_7_8 - 1.0)*(model.x6_7_8 - 1.0) + 0.5*(model.y6_7_8 - 1.0)*(model.y6_7_8 - 1.0) + \
    0.5*(model.z6_7_8 - 1.0)*(model.z6_7_8 - 1.0) + 0.5*(model.x7_7_8 - 1.0)*(model.x7_7_8 - 1.0) + \
    0.5*(model.y7_7_8 - 1.0)*(model.y7_7_8 - 1.0) + 0.5*(model.z7_7_8 - 1.0)*(model.z7_7_8 - 1.0) + \
    0.5*(model.x8_7_8 - 1.0)*(model.x8_7_8 - 1.0) + 0.5*(model.y8_7_8 - 1.0)*(model.y8_7_8 - 1.0) + \
    0.5*(model.z8_7_8 - 1.0)*(model.z8_7_8 - 1.0) + 0.5*(model.x9_7_8 - 1.0)*(model.x9_7_8 - 1.0) + \
    0.5*(model.y9_7_8 - 1.0)*(model.y9_7_8 - 1.0) + 0.5*(model.z9_7_8 - 1.0)*(model.z9_7_8 - 1.0) + \
    0.5*(model.x1_8_8 - 1.0)*(model.x1_8_8 - 1.0) + 0.5*(model.y1_8_8 - 1.0)*(model.y1_8_8 - 1.0) + \
    0.5*(model.z1_8_8 - 1.0)*(model.z1_8_8 - 1.0) + 0.5*(model.x2_8_8 - 1.0)*(model.x2_8_8 - 1.0) + \
    0.5*(model.y2_8_8 - 1.0)*(model.y2_8_8 - 1.0) + 0.5*(model.z2_8_8 - 1.0)*(model.z2_8_8 - 1.0) + \
    0.5*(model.x3_8_8 - 1.0)*(model.x3_8_8 - 1.0) + 0.5*(model.y3_8_8 - 1.0)*(model.y3_8_8 - 1.0) + \
    0.5*(model.z3_8_8 - 1.0)*(model.z3_8_8 - 1.0) + 0.5*(model.x4_8_8 - 1.0)*(model.x4_8_8 - 1.0) + \
    0.5*(model.y4_8_8 - 1.0)*(model.y4_8_8 - 1.0) + 0.5*(model.z4_8_8 - 1.0)*(model.z4_8_8 - 1.0) + \
    0.5*(model.x5_8_8 - 1.0)*(model.x5_8_8 - 1.0) + 0.5*(model.y5_8_8 - 1.0)*(model.y5_8_8 - 1.0) + \
    0.5*(model.z5_8_8 - 1.0)*(model.z5_8_8 - 1.0) + 0.5*(model.x6_8_8 - 1.0)*(model.x6_8_8 - 1.0) + \
    0.5*(model.y6_8_8 - 1.0)*(model.y6_8_8 - 1.0) + 0.5*(model.z6_8_8 - 1.0)*(model.z6_8_8 - 1.0) + \
    0.5*(model.x7_8_8 - 1.0)*(model.x7_8_8 - 1.0) + 0.5*(model.y7_8_8 - 1.0)*(model.y7_8_8 - 1.0) + \
    0.5*(model.z7_8_8 - 1.0)*(model.z7_8_8 - 1.0) + 0.5*(model.x8_8_8 - 1.0)*(model.x8_8_8 - 1.0) + \
    0.5*(model.y8_8_8 - 1.0)*(model.y8_8_8 - 1.0) + 0.5*(model.z8_8_8 - 1.0)*(model.z8_8_8 - 1.0) + \
    0.5*(model.x9_8_8 - 1.0)*(model.x9_8_8 - 1.0) + 0.5*(model.y9_8_8 - 1.0)*(model.y9_8_8 - 1.0) + \
    0.5*(model.z9_8_8 - 1.0)*(model.z9_8_8 - 1.0) + 0.5*(model.x1_9_8 - 1.0)*(model.x1_9_8 - 1.0) + \
    0.5*(model.y1_9_8 - 1.0)*(model.y1_9_8 - 1.0) + 0.5*(model.z1_9_8 - 1.0)*(model.z1_9_8 - 1.0) + \
    0.5*(model.x2_9_8 - 1.0)*(model.x2_9_8 - 1.0) + 0.5*(model.y2_9_8 - 1.0)*(model.y2_9_8 - 1.0) + \
    0.5*(model.z2_9_8 - 1.0)*(model.z2_9_8 - 1.0) + 0.5*(model.x3_9_8 - 1.0)*(model.x3_9_8 - 1.0) + \
    0.5*(model.y3_9_8 - 1.0)*(model.y3_9_8 - 1.0) + 0.5*(model.z3_9_8 - 1.0)*(model.z3_9_8 - 1.0) + \
    0.5*(model.x4_9_8 - 1.0)*(model.x4_9_8 - 1.0) + 0.5*(model.y4_9_8 - 1.0)*(model.y4_9_8 - 1.0) + \
    0.5*(model.z4_9_8 - 1.0)*(model.z4_9_8 - 1.0) + 0.5*(model.x5_9_8 - 1.0)*(model.x5_9_8 - 1.0) + \
    0.5*(model.y5_9_8 - 1.0)*(model.y5_9_8 - 1.0) + 0.5*(model.z5_9_8 - 1.0)*(model.z5_9_8 - 1.0) + \
    0.5*(model.x6_9_8 - 1.0)*(model.x6_9_8 - 1.0) + 0.5*(model.y6_9_8 - 1.0)*(model.y6_9_8 - 1.0) + \
    0.5*(model.z6_9_8 - 1.0)*(model.z6_9_8 - 1.0) + 0.5*(model.x7_9_8 - 1.0)*(model.x7_9_8 - 1.0) + \
    0.5*(model.y7_9_8 - 1.0)*(model.y7_9_8 - 1.0) + 0.5*(model.z7_9_8 - 1.0)*(model.z7_9_8 - 1.0) + \
    0.5*(model.x8_9_8 - 1.0)*(model.x8_9_8 - 1.0) + 0.5*(model.y8_9_8 - 1.0)*(model.y8_9_8 - 1.0) + \
    0.5*(model.z8_9_8 - 1.0)*(model.z8_9_8 - 1.0) + 0.5*(model.x9_9_8 - 1.0)*(model.x9_9_8 - 1.0) + \
    0.5*(model.y9_9_8 - 1.0)*(model.y9_9_8 - 1.0) + 0.5*(model.z9_9_8 - 1.0)*(model.z9_9_8 - 1.0) + \
    0.5*(model.x1_1_9 - 1.0)*(model.x1_1_9 - 1.0) + 0.5*(model.y1_1_9 - 1.0)*(model.y1_1_9 - 1.0) + \
    0.5*(model.z1_1_9 - 1.0)*(model.z1_1_9 - 1.0) + 0.5*(model.x2_1_9 - 1.0)*(model.x2_1_9 - 1.0) + \
    0.5*(model.y2_1_9 - 1.0)*(model.y2_1_9 - 1.0) + 0.5*(model.z2_1_9 - 1.0)*(model.z2_1_9 - 1.0) + \
    0.5*(model.x3_1_9 - 1.0)*(model.x3_1_9 - 1.0) + 0.5*(model.y3_1_9 - 1.0)*(model.y3_1_9 - 1.0) + \
    0.5*(model.z3_1_9 - 1.0)*(model.z3_1_9 - 1.0) + 0.5*(model.x4_1_9 - 1.0)*(model.x4_1_9 - 1.0) + \
    0.5*(model.y4_1_9 - 1.0)*(model.y4_1_9 - 1.0) + 0.5*(model.z4_1_9 - 1.0)*(model.z4_1_9 - 1.0) + \
    0.5*(model.x5_1_9 - 1.0)*(model.x5_1_9 - 1.0) + 0.5*(model.y5_1_9 - 1.0)*(model.y5_1_9 - 1.0) + \
    0.5*(model.z5_1_9 - 1.0)*(model.z5_1_9 - 1.0) + 0.5*(model.x6_1_9 - 1.0)*(model.x6_1_9 - 1.0) + \
    0.5*(model.y6_1_9 - 1.0)*(model.y6_1_9 - 1.0) + 0.5*(model.z6_1_9 - 1.0)*(model.z6_1_9 - 1.0) + \
    0.5*(model.x7_1_9 - 1.0)*(model.x7_1_9 - 1.0) + 0.5*(model.y7_1_9 - 1.0)*(model.y7_1_9 - 1.0) + \
    0.5*(model.z7_1_9 - 1.0)*(model.z7_1_9 - 1.0) + 0.5*(model.x8_1_9 - 1.0)*(model.x8_1_9 - 1.0) + \
    0.5*(model.y8_1_9 - 1.0)*(model.y8_1_9 - 1.0) + 0.5*(model.z8_1_9 - 1.0)*(model.z8_1_9 - 1.0) + \
    0.5*(model.x9_1_9 - 1.0)*(model.x9_1_9 - 1.0) + 0.5*(model.y9_1_9 - 1.0)*(model.y9_1_9 - 1.0) + \
    0.5*(model.z9_1_9 - 1.0)*(model.z9_1_9 - 1.0) + 0.5*(model.x1_2_9 - 1.0)*(model.x1_2_9 - 1.0) + \
    0.5*(model.y1_2_9 - 1.0)*(model.y1_2_9 - 1.0) + 0.5*(model.z1_2_9 - 1.0)*(model.z1_2_9 - 1.0) + \
    0.5*(model.x2_2_9 - 1.0)*(model.x2_2_9 - 1.0) + 0.5*(model.y2_2_9 - 1.0)*(model.y2_2_9 - 1.0) + \
    0.5*(model.z2_2_9 - 1.0)*(model.z2_2_9 - 1.0) + 0.5*(model.x3_2_9 - 1.0)*(model.x3_2_9 - 1.0) + \
    0.5*(model.y3_2_9 - 1.0)*(model.y3_2_9 - 1.0) + 0.5*(model.z3_2_9 - 1.0)*(model.z3_2_9 - 1.0) + \
    0.5*(model.x4_2_9 - 1.0)*(model.x4_2_9 - 1.0) + 0.5*(model.y4_2_9 - 1.0)*(model.y4_2_9 - 1.0) + \
    0.5*(model.z4_2_9 - 1.0)*(model.z4_2_9 - 1.0) + 0.5*(model.x5_2_9 - 1.0)*(model.x5_2_9 - 1.0) + \
    0.5*(model.y5_2_9 - 1.0)*(model.y5_2_9 - 1.0) + 0.5*(model.z5_2_9 - 1.0)*(model.z5_2_9 - 1.0) + \
    0.5*(model.x6_2_9 - 1.0)*(model.x6_2_9 - 1.0) + 0.5*(model.y6_2_9 - 1.0)*(model.y6_2_9 - 1.0) + \
    0.5*(model.z6_2_9 - 1.0)*(model.z6_2_9 - 1.0) + 0.5*(model.x7_2_9 - 1.0)*(model.x7_2_9 - 1.0) + \
    0.5*(model.y7_2_9 - 1.0)*(model.y7_2_9 - 1.0) + 0.5*(model.z7_2_9 - 1.0)*(model.z7_2_9 - 1.0) + \
    0.5*(model.x8_2_9 - 1.0)*(model.x8_2_9 - 1.0) + 0.5*(model.y8_2_9 - 1.0)*(model.y8_2_9 - 1.0) + \
    0.5*(model.z8_2_9 - 1.0)*(model.z8_2_9 - 1.0) + 0.5*(model.x9_2_9 - 1.0)*(model.x9_2_9 - 1.0) + \
    0.5*(model.y9_2_9 - 1.0)*(model.y9_2_9 - 1.0) + 0.5*(model.z9_2_9 - 1.0)*(model.z9_2_9 - 1.0) + \
    0.5*(model.x1_3_9 - 1.0)*(model.x1_3_9 - 1.0) + 0.5*(model.y1_3_9 - 1.0)*(model.y1_3_9 - 1.0) + \
    0.5*(model.z1_3_9 - 1.0)*(model.z1_3_9 - 1.0) + 0.5*(model.x2_3_9 - 1.0)*(model.x2_3_9 - 1.0) + \
    0.5*(model.y2_3_9 - 1.0)*(model.y2_3_9 - 1.0) + 0.5*(model.z2_3_9 - 1.0)*(model.z2_3_9 - 1.0) + \
    0.5*(model.x3_3_9 - 1.0)*(model.x3_3_9 - 1.0) + 0.5*(model.y3_3_9 - 1.0)*(model.y3_3_9 - 1.0) + \
    0.5*(model.z3_3_9 - 1.0)*(model.z3_3_9 - 1.0) + 0.5*(model.x4_3_9 - 1.0)*(model.x4_3_9 - 1.0) + \
    0.5*(model.y4_3_9 - 1.0)*(model.y4_3_9 - 1.0) + 0.5*(model.z4_3_9 - 1.0)*(model.z4_3_9 - 1.0) + \
    0.5*(model.x5_3_9 - 1.0)*(model.x5_3_9 - 1.0) + 0.5*(model.y5_3_9 - 1.0)*(model.y5_3_9 - 1.0) + \
    0.5*(model.z5_3_9 - 1.0)*(model.z5_3_9 - 1.0) + 0.5*(model.x6_3_9 - 1.0)*(model.x6_3_9 - 1.0) + \
    0.5*(model.y6_3_9 - 1.0)*(model.y6_3_9 - 1.0) + 0.5*(model.z6_3_9 - 1.0)*(model.z6_3_9 - 1.0) + \
    0.5*(model.x7_3_9 - 1.0)*(model.x7_3_9 - 1.0) + 0.5*(model.y7_3_9 - 1.0)*(model.y7_3_9 - 1.0) + \
    0.5*(model.z7_3_9 - 1.0)*(model.z7_3_9 - 1.0) + 0.5*(model.x8_3_9 - 1.0)*(model.x8_3_9 - 1.0) + \
    0.5*(model.y8_3_9 - 1.0)*(model.y8_3_9 - 1.0) + 0.5*(model.z8_3_9 - 1.0)*(model.z8_3_9 - 1.0) + \
    0.5*(model.x9_3_9 - 1.0)*(model.x9_3_9 - 1.0) + 0.5*(model.y9_3_9 - 1.0)*(model.y9_3_9 - 1.0) + \
    0.5*(model.z9_3_9 - 1.0)*(model.z9_3_9 - 1.0) + 0.5*(model.x1_4_9 - 1.0)*(model.x1_4_9 - 1.0) + \
    0.5*(model.y1_4_9 - 1.0)*(model.y1_4_9 - 1.0) + 0.5*(model.z1_4_9 - 1.0)*(model.z1_4_9 - 1.0) + \
    0.5*(model.x2_4_9 - 1.0)*(model.x2_4_9 - 1.0) + 0.5*(model.y2_4_9 - 1.0)*(model.y2_4_9 - 1.0) + \
    0.5*(model.z2_4_9 - 1.0)*(model.z2_4_9 - 1.0) + 0.5*(model.x3_4_9 - 1.0)*(model.x3_4_9 - 1.0) + \
    0.5*(model.y3_4_9 - 1.0)*(model.y3_4_9 - 1.0) + 0.5*(model.z3_4_9 - 1.0)*(model.z3_4_9 - 1.0) + \
    0.5*(model.x4_4_9 - 1.0)*(model.x4_4_9 - 1.0) + 0.5*(model.y4_4_9 - 1.0)*(model.y4_4_9 - 1.0) + \
    0.5*(model.z4_4_9 - 1.0)*(model.z4_4_9 - 1.0) + 0.5*(model.x5_4_9 - 1.0)*(model.x5_4_9 - 1.0) + \
    0.5*(model.y5_4_9 - 1.0)*(model.y5_4_9 - 1.0) + 0.5*(model.z5_4_9 - 1.0)*(model.z5_4_9 - 1.0) + \
    0.5*(model.x6_4_9 - 1.0)*(model.x6_4_9 - 1.0) + 0.5*(model.y6_4_9 - 1.0)*(model.y6_4_9 - 1.0) + \
    0.5*(model.z6_4_9 - 1.0)*(model.z6_4_9 - 1.0) + 0.5*(model.x7_4_9 - 1.0)*(model.x7_4_9 - 1.0) + \
    0.5*(model.y7_4_9 - 1.0)*(model.y7_4_9 - 1.0) + 0.5*(model.z7_4_9 - 1.0)*(model.z7_4_9 - 1.0) + \
    0.5*(model.x8_4_9 - 1.0)*(model.x8_4_9 - 1.0) + 0.5*(model.y8_4_9 - 1.0)*(model.y8_4_9 - 1.0) + \
    0.5*(model.z8_4_9 - 1.0)*(model.z8_4_9 - 1.0) + 0.5*(model.x9_4_9 - 1.0)*(model.x9_4_9 - 1.0) + \
    0.5*(model.y9_4_9 - 1.0)*(model.y9_4_9 - 1.0) + 0.5*(model.z9_4_9 - 1.0)*(model.z9_4_9 - 1.0) + \
    0.5*(model.x1_5_9 - 1.0)*(model.x1_5_9 - 1.0) + 0.5*(model.y1_5_9 - 1.0)*(model.y1_5_9 - 1.0) + \
    0.5*(model.z1_5_9 - 1.0)*(model.z1_5_9 - 1.0) + 0.5*(model.x2_5_9 - 1.0)*(model.x2_5_9 - 1.0) + \
    0.5*(model.y2_5_9 - 1.0)*(model.y2_5_9 - 1.0) + 0.5*(model.z2_5_9 - 1.0)*(model.z2_5_9 - 1.0) + \
    0.5*(model.x3_5_9 - 1.0)*(model.x3_5_9 - 1.0) + 0.5*(model.y3_5_9 - 1.0)*(model.y3_5_9 - 1.0) + \
    0.5*(model.z3_5_9 - 1.0)*(model.z3_5_9 - 1.0) + 0.5*(model.x4_5_9 - 1.0)*(model.x4_5_9 - 1.0) + \
    0.5*(model.y4_5_9 - 1.0)*(model.y4_5_9 - 1.0) + 0.5*(model.z4_5_9 - 1.0)*(model.z4_5_9 - 1.0) + \
    0.5*(model.x5_5_9 - 1.0)*(model.x5_5_9 - 1.0) + 0.5*(model.y5_5_9 - 1.0)*(model.y5_5_9 - 1.0) + \
    0.5*(model.z5_5_9 - 1.0)*(model.z5_5_9 - 1.0) + 0.5*(model.x6_5_9 - 1.0)*(model.x6_5_9 - 1.0) + \
    0.5*(model.y6_5_9 - 1.0)*(model.y6_5_9 - 1.0) + 0.5*(model.z6_5_9 - 1.0)*(model.z6_5_9 - 1.0) + \
    0.5*(model.x7_5_9 - 1.0)*(model.x7_5_9 - 1.0) + 0.5*(model.y7_5_9 - 1.0)*(model.y7_5_9 - 1.0) + \
    0.5*(model.z7_5_9 - 1.0)*(model.z7_5_9 - 1.0) + 0.5*(model.x8_5_9 - 1.0)*(model.x8_5_9 - 1.0) + \
    0.5*(model.y8_5_9 - 1.0)*(model.y8_5_9 - 1.0) + 0.5*(model.z8_5_9 - 1.0)*(model.z8_5_9 - 1.0) + \
    0.5*(model.x9_5_9 - 1.0)*(model.x9_5_9 - 1.0) + 0.5*(model.y9_5_9 - 1.0)*(model.y9_5_9 - 1.0) + \
    0.5*(model.z9_5_9 - 1.0)*(model.z9_5_9 - 1.0) + 0.5*(model.x1_6_9 - 1.0)*(model.x1_6_9 - 1.0) + \
    0.5*(model.y1_6_9 - 1.0)*(model.y1_6_9 - 1.0) + 0.5*(model.z1_6_9 - 1.0)*(model.z1_6_9 - 1.0) + \
    0.5*(model.x2_6_9 - 1.0)*(model.x2_6_9 - 1.0) + 0.5*(model.y2_6_9 - 1.0)*(model.y2_6_9 - 1.0) + \
    0.5*(model.z2_6_9 - 1.0)*(model.z2_6_9 - 1.0) + 0.5*(model.x3_6_9 - 1.0)*(model.x3_6_9 - 1.0) + \
    0.5*(model.y3_6_9 - 1.0)*(model.y3_6_9 - 1.0) + 0.5*(model.z3_6_9 - 1.0)*(model.z3_6_9 - 1.0) + \
    0.5*(model.x4_6_9 - 1.0)*(model.x4_6_9 - 1.0) + 0.5*(model.y4_6_9 - 1.0)*(model.y4_6_9 - 1.0) + \
    0.5*(model.z4_6_9 - 1.0)*(model.z4_6_9 - 1.0) + 0.5*(model.x5_6_9 - 1.0)*(model.x5_6_9 - 1.0) + \
    0.5*(model.y5_6_9 - 1.0)*(model.y5_6_9 - 1.0) + 0.5*(model.z5_6_9 - 1.0)*(model.z5_6_9 - 1.0) + \
    0.5*(model.x6_6_9 - 1.0)*(model.x6_6_9 - 1.0) + 0.5*(model.y6_6_9 - 1.0)*(model.y6_6_9 - 1.0) + \
    0.5*(model.z6_6_9 - 1.0)*(model.z6_6_9 - 1.0) + 0.5*(model.x7_6_9 - 1.0)*(model.x7_6_9 - 1.0) + \
    0.5*(model.y7_6_9 - 1.0)*(model.y7_6_9 - 1.0) + 0.5*(model.z7_6_9 - 1.0)*(model.z7_6_9 - 1.0) + \
    0.5*(model.x8_6_9 - 1.0)*(model.x8_6_9 - 1.0) + 0.5*(model.y8_6_9 - 1.0)*(model.y8_6_9 - 1.0) + \
    0.5*(model.z8_6_9 - 1.0)*(model.z8_6_9 - 1.0) + 0.5*(model.x9_6_9 - 1.0)*(model.x9_6_9 - 1.0) + \
    0.5*(model.y9_6_9 - 1.0)*(model.y9_6_9 - 1.0) + 0.5*(model.z9_6_9 - 1.0)*(model.z9_6_9 - 1.0) + \
    0.5*(model.x1_7_9 - 1.0)*(model.x1_7_9 - 1.0) + 0.5*(model.y1_7_9 - 1.0)*(model.y1_7_9 - 1.0) + \
    0.5*(model.z1_7_9 - 1.0)*(model.z1_7_9 - 1.0) + 0.5*(model.x2_7_9 - 1.0)*(model.x2_7_9 - 1.0) + \
    0.5*(model.y2_7_9 - 1.0)*(model.y2_7_9 - 1.0) + 0.5*(model.z2_7_9 - 1.0)*(model.z2_7_9 - 1.0) + \
    0.5*(model.x3_7_9 - 1.0)*(model.x3_7_9 - 1.0) + 0.5*(model.y3_7_9 - 1.0)*(model.y3_7_9 - 1.0) + \
    0.5*(model.z3_7_9 - 1.0)*(model.z3_7_9 - 1.0) + 0.5*(model.x4_7_9 - 1.0)*(model.x4_7_9 - 1.0) + \
    0.5*(model.y4_7_9 - 1.0)*(model.y4_7_9 - 1.0) + 0.5*(model.z4_7_9 - 1.0)*(model.z4_7_9 - 1.0) + \
    0.5*(model.x5_7_9 - 1.0)*(model.x5_7_9 - 1.0) + 0.5*(model.y5_7_9 - 1.0)*(model.y5_7_9 - 1.0) + \
    0.5*(model.z5_7_9 - 1.0)*(model.z5_7_9 - 1.0) + 0.5*(model.x6_7_9 - 1.0)*(model.x6_7_9 - 1.0) + \
    0.5*(model.y6_7_9 - 1.0)*(model.y6_7_9 - 1.0) + 0.5*(model.z6_7_9 - 1.0)*(model.z6_7_9 - 1.0) + \
    0.5*(model.x7_7_9 - 1.0)*(model.x7_7_9 - 1.0) + 0.5*(model.y7_7_9 - 1.0)*(model.y7_7_9 - 1.0) + \
    0.5*(model.z7_7_9 - 1.0)*(model.z7_7_9 - 1.0) + 0.5*(model.x8_7_9 - 1.0)*(model.x8_7_9 - 1.0) + \
    0.5*(model.y8_7_9 - 1.0)*(model.y8_7_9 - 1.0) + 0.5*(model.z8_7_9 - 1.0)*(model.z8_7_9 - 1.0) + \
    0.5*(model.x9_7_9 - 1.0)*(model.x9_7_9 - 1.0) + 0.5*(model.y9_7_9 - 1.0)*(model.y9_7_9 - 1.0) + \
    0.5*(model.z9_7_9 - 1.0)*(model.z9_7_9 - 1.0) + 0.5*(model.x1_8_9 - 1.0)*(model.x1_8_9 - 1.0) + \
    0.5*(model.y1_8_9 - 1.0)*(model.y1_8_9 - 1.0) + 0.5*(model.z1_8_9 - 1.0)*(model.z1_8_9 - 1.0) + \
    0.5*(model.x2_8_9 - 1.0)*(model.x2_8_9 - 1.0) + 0.5*(model.y2_8_9 - 1.0)*(model.y2_8_9 - 1.0) + \
    0.5*(model.z2_8_9 - 1.0)*(model.z2_8_9 - 1.0) + 0.5*(model.x3_8_9 - 1.0)*(model.x3_8_9 - 1.0) + \
    0.5*(model.y3_8_9 - 1.0)*(model.y3_8_9 - 1.0) + 0.5*(model.z3_8_9 - 1.0)*(model.z3_8_9 - 1.0) + \
    0.5*(model.x4_8_9 - 1.0)*(model.x4_8_9 - 1.0) + 0.5*(model.y4_8_9 - 1.0)*(model.y4_8_9 - 1.0) + \
    0.5*(model.z4_8_9 - 1.0)*(model.z4_8_9 - 1.0) + 0.5*(model.x5_8_9 - 1.0)*(model.x5_8_9 - 1.0) + \
    0.5*(model.y5_8_9 - 1.0)*(model.y5_8_9 - 1.0) + 0.5*(model.z5_8_9 - 1.0)*(model.z5_8_9 - 1.0) + \
    0.5*(model.x6_8_9 - 1.0)*(model.x6_8_9 - 1.0) + 0.5*(model.y6_8_9 - 1.0)*(model.y6_8_9 - 1.0) + \
    0.5*(model.z6_8_9 - 1.0)*(model.z6_8_9 - 1.0) + 0.5*(model.x7_8_9 - 1.0)*(model.x7_8_9 - 1.0) + \
    0.5*(model.y7_8_9 - 1.0)*(model.y7_8_9 - 1.0) + 0.5*(model.z7_8_9 - 1.0)*(model.z7_8_9 - 1.0) + \
    0.5*(model.x8_8_9 - 1.0)*(model.x8_8_9 - 1.0) + 0.5*(model.y8_8_9 - 1.0)*(model.y8_8_9 - 1.0) + \
    0.5*(model.z8_8_9 - 1.0)*(model.z8_8_9 - 1.0) + 0.5*(model.x9_8_9 - 1.0)*(model.x9_8_9 - 1.0) + \
    0.5*(model.y9_8_9 - 1.0)*(model.y9_8_9 - 1.0) + 0.5*(model.z9_8_9 - 1.0)*(model.z9_8_9 - 1.0) + \
    0.5*(model.x1_9_9 - 1.0)*(model.x1_9_9 - 1.0) + 0.5*(model.y1_9_9 - 1.0)*(model.y1_9_9 - 1.0) + \
    0.5*(model.z1_9_9 - 1.0)*(model.z1_9_9 - 1.0) + 0.5*(model.x2_9_9 - 1.0)*(model.x2_9_9 - 1.0) + \
    0.5*(model.y2_9_9 - 1.0)*(model.y2_9_9 - 1.0) + 0.5*(model.z2_9_9 - 1.0)*(model.z2_9_9 - 1.0) + \
    0.5*(model.x3_9_9 - 1.0)*(model.x3_9_9 - 1.0) + 0.5*(model.y3_9_9 - 1.0)*(model.y3_9_9 - 1.0) + \
    0.5*(model.z3_9_9 - 1.0)*(model.z3_9_9 - 1.0) + 0.5*(model.x4_9_9 - 1.0)*(model.x4_9_9 - 1.0) + \
    0.5*(model.y4_9_9 - 1.0)*(model.y4_9_9 - 1.0) + 0.5*(model.z4_9_9 - 1.0)*(model.z4_9_9 - 1.0) + \
    0.5*(model.x5_9_9 - 1.0)*(model.x5_9_9 - 1.0) + 0.5*(model.y5_9_9 - 1.0)*(model.y5_9_9 - 1.0) + \
    0.5*(model.z5_9_9 - 1.0)*(model.z5_9_9 - 1.0) + 0.5*(model.x6_9_9 - 1.0)*(model.x6_9_9 - 1.0) + \
    0.5*(model.y6_9_9 - 1.0)*(model.y6_9_9 - 1.0) + 0.5*(model.z6_9_9 - 1.0)*(model.z6_9_9 - 1.0) + \
    0.5*(model.x7_9_9 - 1.0)*(model.x7_9_9 - 1.0) + 0.5*(model.y7_9_9 - 1.0)*(model.y7_9_9 - 1.0) + \
    0.5*(model.z7_9_9 - 1.0)*(model.z7_9_9 - 1.0) + 0.5*(model.x8_9_9 - 1.0)*(model.x8_9_9 - 1.0) + \
    0.5*(model.y8_9_9 - 1.0)*(model.y8_9_9 - 1.0) + 0.5*(model.z8_9_9 - 1.0)*(model.z8_9_9 - 1.0) + \
    0.5*(model.x9_9_9 - 1.0)*(model.x9_9_9 - 1.0) + 0.5*(model.y9_9_9 - 1.0)*(model.y9_9_9 - 1.0) + \
    0.5*(model.z9_9_9 - 1.0)*(model.z9_9_9 - 1.0) + 0.5*(model.y10_1_1 - 1.0)*(model.y10_1_1 - 1.0) + \
    0.5*(model.z10_1_1 - 1.0)*(model.z10_1_1 - 1.0) + 0.5*(model.y10_2_1 - 1.0)*(model.y10_2_1 - 1.0) \
    + 0.5*(model.z10_2_1 - 1.0)*(model.z10_2_1 - 1.0) + 0.5*(model.y10_3_1 - 1.0)*(model.y10_3_1 - \
    1.0) + 0.5*(model.z10_3_1 - 1.0)*(model.z10_3_1 - 1.0) + 0.5*(model.y10_4_1 - 1.0)*(model.y10_4_1 \
    - 1.0) + 0.5*(model.z10_4_1 - 1.0)*(model.z10_4_1 - 1.0) + 0.5*(model.y10_5_1 - \
    1.0)*(model.y10_5_1 - 1.0) + 0.5*(model.z10_5_1 - 1.0)*(model.z10_5_1 - 1.0) + 0.5*(model.y10_6_1 \
    - 1.0)*(model.y10_6_1 - 1.0) + 0.5*(model.z10_6_1 - 1.0)*(model.z10_6_1 - 1.0) + \
    0.5*(model.y10_7_1 - 1.0)*(model.y10_7_1 - 1.0) + 0.5*(model.z10_7_1 - 1.0)*(model.z10_7_1 - 1.0) \
    + 0.5*(model.y10_8_1 - 1.0)*(model.y10_8_1 - 1.0) + 0.5*(model.z10_8_1 - 1.0)*(model.z10_8_1 - \
    1.0) + 0.5*(model.y10_9_1 - 1.0)*(model.y10_9_1 - 1.0) + 0.5*(model.z10_9_1 - 1.0)*(model.z10_9_1 \
    - 1.0) + 0.5*(model.y10_1_2 - 1.0)*(model.y10_1_2 - 1.0) + 0.5*(model.z10_1_2 - \
    1.0)*(model.z10_1_2 - 1.0) + 0.5*(model.y10_2_2 - 1.0)*(model.y10_2_2 - 1.0) + 0.5*(model.z10_2_2 \
    - 1.0)*(model.z10_2_2 - 1.0) + 0.5*(model.y10_3_2 - 1.0)*(model.y10_3_2 - 1.0) + \
    0.5*(model.z10_3_2 - 1.0)*(model.z10_3_2 - 1.0) + 0.5*(model.y10_4_2 - 1.0)*(model.y10_4_2 - 1.0) \
    + 0.5*(model.z10_4_2 - 1.0)*(model.z10_4_2 - 1.0) + 0.5*(model.y10_5_2 - 1.0)*(model.y10_5_2 - \
    1.0) + 0.5*(model.z10_5_2 - 1.0)*(model.z10_5_2 - 1.0) + 0.5*(model.y10_6_2 - 1.0)*(model.y10_6_2 \
    - 1.0) + 0.5*(model.z10_6_2 - 1.0)*(model.z10_6_2 - 1.0) + 0.5*(model.y10_7_2 - \
    1.0)*(model.y10_7_2 - 1.0) + 0.5*(model.z10_7_2 - 1.0)*(model.z10_7_2 - 1.0) + 0.5*(model.y10_8_2 \
    - 1.0)*(model.y10_8_2 - 1.0) + 0.5*(model.z10_8_2 - 1.0)*(model.z10_8_2 - 1.0) + \
    0.5*(model.y10_9_2 - 1.0)*(model.y10_9_2 - 1.0) + 0.5*(model.z10_9_2 - 1.0)*(model.z10_9_2 - 1.0) \
    + 0.5*(model.y10_1_3 - 1.0)*(model.y10_1_3 - 1.0) + 0.5*(model.z10_1_3 - 1.0)*(model.z10_1_3 - \
    1.0) + 0.5*(model.y10_2_3 - 1.0)*(model.y10_2_3 - 1.0) + 0.5*(model.z10_2_3 - 1.0)*(model.z10_2_3 \
    - 1.0) + 0.5*(model.y10_3_3 - 1.0)*(model.y10_3_3 - 1.0) + 0.5*(model.z10_3_3 - \
    1.0)*(model.z10_3_3 - 1.0) + 0.5*(model.y10_4_3 - 1.0)*(model.y10_4_3 - 1.0) + 0.5*(model.z10_4_3 \
    - 1.0)*(model.z10_4_3 - 1.0) + 0.5*(model.y10_5_3 - 1.0)*(model.y10_5_3 - 1.0) + \
    0.5*(model.z10_5_3 - 1.0)*(model.z10_5_3 - 1.0) + 0.5*(model.y10_6_3 - 1.0)*(model.y10_6_3 - 1.0) \
    + 0.5*(model.z10_6_3 - 1.0)*(model.z10_6_3 - 1.0) + 0.5*(model.y10_7_3 - 1.0)*(model.y10_7_3 - \
    1.0) + 0.5*(model.z10_7_3 - 1.0)*(model.z10_7_3 - 1.0) + 0.5*(model.y10_8_3 - 1.0)*(model.y10_8_3 \
    - 1.0) + 0.5*(model.z10_8_3 - 1.0)*(model.z10_8_3 - 1.0) + 0.5*(model.y10_9_3 - \
    1.0)*(model.y10_9_3 - 1.0) + 0.5*(model.z10_9_3 - 1.0)*(model.z10_9_3 - 1.0) + 0.5*(model.y10_1_4 \
    - 1.0)*(model.y10_1_4 - 1.0) + 0.5*(model.z10_1_4 - 1.0)*(model.z10_1_4 - 1.0) + \
    0.5*(model.y10_2_4 - 1.0)*(model.y10_2_4 - 1.0) + 0.5*(model.z10_2_4 - 1.0)*(model.z10_2_4 - 1.0) \
    + 0.5*(model.y10_3_4 - 1.0)*(model.y10_3_4 - 1.0) + 0.5*(model.z10_3_4 - 1.0)*(model.z10_3_4 - \
    1.0) + 0.5*(model.y10_4_4 - 1.0)*(model.y10_4_4 - 1.0) + 0.5*(model.z10_4_4 - 1.0)*(model.z10_4_4 \
    - 1.0) + 0.5*(model.y10_5_4 - 1.0)*(model.y10_5_4 - 1.0) + 0.5*(model.z10_5_4 - \
    1.0)*(model.z10_5_4 - 1.0) + 0.5*(model.y10_6_4 - 1.0)*(model.y10_6_4 - 1.0) + 0.5*(model.z10_6_4 \
    - 1.0)*(model.z10_6_4 - 1.0) + 0.5*(model.y10_7_4 - 1.0)*(model.y10_7_4 - 1.0) + \
    0.5*(model.z10_7_4 - 1.0)*(model.z10_7_4 - 1.0) + 0.5*(model.y10_8_4 - 1.0)*(model.y10_8_4 - 1.0) \
    + 0.5*(model.z10_8_4 - 1.0)*(model.z10_8_4 - 1.0) + 0.5*(model.y10_9_4 - 1.0)*(model.y10_9_4 - \
    1.0) + 0.5*(model.z10_9_4 - 1.0)*(model.z10_9_4 - 1.0) + 0.5*(model.y10_1_5 - 1.0)*(model.y10_1_5 \
    - 1.0) + 0.5*(model.z10_1_5 - 1.0)*(model.z10_1_5 - 1.0) + 0.5*(model.y10_2_5 - \
    1.0)*(model.y10_2_5 - 1.0) + 0.5*(model.z10_2_5 - 1.0)*(model.z10_2_5 - 1.0) + 0.5*(model.y10_3_5 \
    - 1.0)*(model.y10_3_5 - 1.0) + 0.5*(model.z10_3_5 - 1.0)*(model.z10_3_5 - 1.0) + \
    0.5*(model.y10_4_5 - 1.0)*(model.y10_4_5 - 1.0) + 0.5*(model.z10_4_5 - 1.0)*(model.z10_4_5 - 1.0) \
    + 0.5*(model.y10_5_5 - 1.0)*(model.y10_5_5 - 1.0) + 0.5*(model.z10_5_5 - 1.0)*(model.z10_5_5 - \
    1.0) + 0.5*(model.y10_6_5 - 1.0)*(model.y10_6_5 - 1.0) + 0.5*(model.z10_6_5 - 1.0)*(model.z10_6_5 \
    - 1.0) + 0.5*(model.y10_7_5 - 1.0)*(model.y10_7_5 - 1.0) + 0.5*(model.z10_7_5 - \
    1.0)*(model.z10_7_5 - 1.0) + 0.5*(model.y10_8_5 - 1.0)*(model.y10_8_5 - 1.0) + 0.5*(model.z10_8_5 \
    - 1.0)*(model.z10_8_5 - 1.0) + 0.5*(model.y10_9_5 - 1.0)*(model.y10_9_5 - 1.0) + \
    0.5*(model.z10_9_5 - 1.0)*(model.z10_9_5 - 1.0) + 0.5*(model.y10_1_6 - 1.0)*(model.y10_1_6 - 1.0) \
    + 0.5*(model.z10_1_6 - 1.0)*(model.z10_1_6 - 1.0) + 0.5*(model.y10_2_6 - 1.0)*(model.y10_2_6 - \
    1.0) + 0.5*(model.z10_2_6 - 1.0)*(model.z10_2_6 - 1.0) + 0.5*(model.y10_3_6 - 1.0)*(model.y10_3_6 \
    - 1.0) + 0.5*(model.z10_3_6 - 1.0)*(model.z10_3_6 - 1.0) + 0.5*(model.y10_4_6 - \
    1.0)*(model.y10_4_6 - 1.0) + 0.5*(model.z10_4_6 - 1.0)*(model.z10_4_6 - 1.0) + 0.5*(model.y10_5_6 \
    - 1.0)*(model.y10_5_6 - 1.0) + 0.5*(model.z10_5_6 - 1.0)*(model.z10_5_6 - 1.0) + \
    0.5*(model.y10_6_6 - 1.0)*(model.y10_6_6 - 1.0) + 0.5*(model.z10_6_6 - 1.0)*(model.z10_6_6 - 1.0) \
    + 0.5*(model.y10_7_6 - 1.0)*(model.y10_7_6 - 1.0) + 0.5*(model.z10_7_6 - 1.0)*(model.z10_7_6 - \
    1.0) + 0.5*(model.y10_8_6 - 1.0)*(model.y10_8_6 - 1.0) + 0.5*(model.z10_8_6 - 1.0)*(model.z10_8_6 \
    - 1.0) + 0.5*(model.y10_9_6 - 1.0)*(model.y10_9_6 - 1.0) + 0.5*(model.z10_9_6 - \
    1.0)*(model.z10_9_6 - 1.0) + 0.5*(model.y10_1_7 - 1.0)*(model.y10_1_7 - 1.0) + 0.5*(model.z10_1_7 \
    - 1.0)*(model.z10_1_7 - 1.0) + 0.5*(model.y10_2_7 - 1.0)*(model.y10_2_7 - 1.0) + \
    0.5*(model.z10_2_7 - 1.0)*(model.z10_2_7 - 1.0) + 0.5*(model.y10_3_7 - 1.0)*(model.y10_3_7 - 1.0) \
    + 0.5*(model.z10_3_7 - 1.0)*(model.z10_3_7 - 1.0) + 0.5*(model.y10_4_7 - 1.0)*(model.y10_4_7 - \
    1.0) + 0.5*(model.z10_4_7 - 1.0)*(model.z10_4_7 - 1.0) + 0.5*(model.y10_5_7 - 1.0)*(model.y10_5_7 \
    - 1.0) + 0.5*(model.z10_5_7 - 1.0)*(model.z10_5_7 - 1.0) + 0.5*(model.y10_6_7 - \
    1.0)*(model.y10_6_7 - 1.0) + 0.5*(model.z10_6_7 - 1.0)*(model.z10_6_7 - 1.0) + 0.5*(model.y10_7_7 \
    - 1.0)*(model.y10_7_7 - 1.0) + 0.5*(model.z10_7_7 - 1.0)*(model.z10_7_7 - 1.0) + \
    0.5*(model.y10_8_7 - 1.0)*(model.y10_8_7 - 1.0) + 0.5*(model.z10_8_7 - 1.0)*(model.z10_8_7 - 1.0) \
    + 0.5*(model.y10_9_7 - 1.0)*(model.y10_9_7 - 1.0) + 0.5*(model.z10_9_7 - 1.0)*(model.z10_9_7 - \
    1.0) + 0.5*(model.y10_1_8 - 1.0)*(model.y10_1_8 - 1.0) + 0.5*(model.z10_1_8 - 1.0)*(model.z10_1_8 \
    - 1.0) + 0.5*(model.y10_2_8 - 1.0)*(model.y10_2_8 - 1.0) + 0.5*(model.z10_2_8 - \
    1.0)*(model.z10_2_8 - 1.0) + 0.5*(model.y10_3_8 - 1.0)*(model.y10_3_8 - 1.0) + 0.5*(model.z10_3_8 \
    - 1.0)*(model.z10_3_8 - 1.0) + 0.5*(model.y10_4_8 - 1.0)*(model.y10_4_8 - 1.0) + \
    0.5*(model.z10_4_8 - 1.0)*(model.z10_4_8 - 1.0) + 0.5*(model.y10_5_8 - 1.0)*(model.y10_5_8 - 1.0) \
    + 0.5*(model.z10_5_8 - 1.0)*(model.z10_5_8 - 1.0) + 0.5*(model.y10_6_8 - 1.0)*(model.y10_6_8 - \
    1.0) + 0.5*(model.z10_6_8 - 1.0)*(model.z10_6_8 - 1.0) + 0.5*(model.y10_7_8 - 1.0)*(model.y10_7_8 \
    - 1.0) + 0.5*(model.z10_7_8 - 1.0)*(model.z10_7_8 - 1.0) + 0.5*(model.y10_8_8 - \
    1.0)*(model.y10_8_8 - 1.0) + 0.5*(model.z10_8_8 - 1.0)*(model.z10_8_8 - 1.0) + 0.5*(model.y10_9_8 \
    - 1.0)*(model.y10_9_8 - 1.0) + 0.5*(model.z10_9_8 - 1.0)*(model.z10_9_8 - 1.0) + \
    0.5*(model.y10_1_9 - 1.0)*(model.y10_1_9 - 1.0) + 0.5*(model.z10_1_9 - 1.0)*(model.z10_1_9 - 1.0) \
    + 0.5*(model.y10_2_9 - 1.0)*(model.y10_2_9 - 1.0) + 0.5*(model.z10_2_9 - 1.0)*(model.z10_2_9 - \
    1.0) + 0.5*(model.y10_3_9 - 1.0)*(model.y10_3_9 - 1.0) + 0.5*(model.z10_3_9 - 1.0)*(model.z10_3_9 \
    - 1.0) + 0.5*(model.y10_4_9 - 1.0)*(model.y10_4_9 - 1.0) + 0.5*(model.z10_4_9 - \
    1.0)*(model.z10_4_9 - 1.0) + 0.5*(model.y10_5_9 - 1.0)*(model.y10_5_9 - 1.0) + 0.5*(model.z10_5_9 \
    - 1.0)*(model.z10_5_9 - 1.0) + 0.5*(model.y10_6_9 - 1.0)*(model.y10_6_9 - 1.0) + \
    0.5*(model.z10_6_9 - 1.0)*(model.z10_6_9 - 1.0) + 0.5*(model.y10_7_9 - 1.0)*(model.y10_7_9 - 1.0) \
    + 0.5*(model.z10_7_9 - 1.0)*(model.z10_7_9 - 1.0) + 0.5*(model.y10_8_9 - 1.0)*(model.y10_8_9 - \
    1.0) + 0.5*(model.z10_8_9 - 1.0)*(model.z10_8_9 - 1.0) + 0.5*(model.y10_9_9 - 1.0)*(model.y10_9_9 \
    - 1.0) + 0.5*(model.z10_9_9 - 1.0)*(model.z10_9_9 - 1.0) + 0.5*(model.x1_10_1 - \
    1.0)*(model.x1_10_1 - 1.0) + 0.5*(model.z1_10_1 - 1.0)*(model.z1_10_1 - 1.0) + 0.5*(model.x2_10_1 \
    - 1.0)*(model.x2_10_1 - 1.0) + 0.5*(model.z2_10_1 - 1.0)*(model.z2_10_1 - 1.0) + \
    0.5*(model.x3_10_1 - 1.0)*(model.x3_10_1 - 1.0) + 0.5*(model.z3_10_1 - 1.0)*(model.z3_10_1 - 1.0) \
    + 0.5*(model.x4_10_1 - 1.0)*(model.x4_10_1 - 1.0) + 0.5*(model.z4_10_1 - 1.0)*(model.z4_10_1 - \
    1.0) + 0.5*(model.x5_10_1 - 1.0)*(model.x5_10_1 - 1.0) + 0.5*(model.z5_10_1 - 1.0)*(model.z5_10_1 \
    - 1.0) + 0.5*(model.x6_10_1 - 1.0)*(model.x6_10_1 - 1.0) + 0.5*(model.z6_10_1 - \
    1.0)*(model.z6_10_1 - 1.0) + 0.5*(model.x7_10_1 - 1.0)*(model.x7_10_1 - 1.0) + 0.5*(model.z7_10_1 \
    - 1.0)*(model.z7_10_1 - 1.0) + 0.5*(model.x8_10_1 - 1.0)*(model.x8_10_1 - 1.0) + \
    0.5*(model.z8_10_1 - 1.0)*(model.z8_10_1 - 1.0) + 0.5*(model.x9_10_1 - 1.0)*(model.x9_10_1 - 1.0) \
    + 0.5*(model.z9_10_1 - 1.0)*(model.z9_10_1 - 1.0) + 0.5*(model.x1_10_2 - 1.0)*(model.x1_10_2 - \
    1.0) + 0.5*(model.z1_10_2 - 1.0)*(model.z1_10_2 - 1.0) + 0.5*(model.x2_10_2 - 1.0)*(model.x2_10_2 \
    - 1.0) + 0.5*(model.z2_10_2 - 1.0)*(model.z2_10_2 - 1.0) + 0.5*(model.x3_10_2 - \
    1.0)*(model.x3_10_2 - 1.0) + 0.5*(model.z3_10_2 - 1.0)*(model.z3_10_2 - 1.0) + 0.5*(model.x4_10_2 \
    - 1.0)*(model.x4_10_2 - 1.0) + 0.5*(model.z4_10_2 - 1.0)*(model.z4_10_2 - 1.0) + \
    0.5*(model.x5_10_2 - 1.0)*(model.x5_10_2 - 1.0) + 0.5*(model.z5_10_2 - 1.0)*(model.z5_10_2 - 1.0) \
    + 0.5*(model.x6_10_2 - 1.0)*(model.x6_10_2 - 1.0) + 0.5*(model.z6_10_2 - 1.0)*(model.z6_10_2 - \
    1.0) + 0.5*(model.x7_10_2 - 1.0)*(model.x7_10_2 - 1.0) + 0.5*(model.z7_10_2 - 1.0)*(model.z7_10_2 \
    - 1.0) + 0.5*(model.x8_10_2 - 1.0)*(model.x8_10_2 - 1.0) + 0.5*(model.z8_10_2 - \
    1.0)*(model.z8_10_2 - 1.0) + 0.5*(model.x9_10_2 - 1.0)*(model.x9_10_2 - 1.0) + 0.5*(model.z9_10_2 \
    - 1.0)*(model.z9_10_2 - 1.0) + 0.5*(model.x1_10_3 - 1.0)*(model.x1_10_3 - 1.0) + \
    0.5*(model.z1_10_3 - 1.0)*(model.z1_10_3 - 1.0) + 0.5*(model.x2_10_3 - 1.0)*(model.x2_10_3 - 1.0) \
    + 0.5*(model.z2_10_3 - 1.0)*(model.z2_10_3 - 1.0) + 0.5*(model.x3_10_3 - 1.0)*(model.x3_10_3 - \
    1.0) + 0.5*(model.z3_10_3 - 1.0)*(model.z3_10_3 - 1.0) + 0.5*(model.x4_10_3 - 1.0)*(model.x4_10_3 \
    - 1.0) + 0.5*(model.z4_10_3 - 1.0)*(model.z4_10_3 - 1.0) + 0.5*(model.x5_10_3 - \
    1.0)*(model.x5_10_3 - 1.0) + 0.5*(model.z5_10_3 - 1.0)*(model.z5_10_3 - 1.0) + 0.5*(model.x6_10_3 \
    - 1.0)*(model.x6_10_3 - 1.0) + 0.5*(model.z6_10_3 - 1.0)*(model.z6_10_3 - 1.0) + \
    0.5*(model.x7_10_3 - 1.0)*(model.x7_10_3 - 1.0) + 0.5*(model.z7_10_3 - 1.0)*(model.z7_10_3 - 1.0) \
    + 0.5*(model.x8_10_3 - 1.0)*(model.x8_10_3 - 1.0) + 0.5*(model.z8_10_3 - 1.0)*(model.z8_10_3 - \
    1.0) + 0.5*(model.x9_10_3 - 1.0)*(model.x9_10_3 - 1.0) + 0.5*(model.z9_10_3 - 1.0)*(model.z9_10_3 \
    - 1.0) + 0.5*(model.x1_10_4 - 1.0)*(model.x1_10_4 - 1.0) + 0.5*(model.z1_10_4 - \
    1.0)*(model.z1_10_4 - 1.0) + 0.5*(model.x2_10_4 - 1.0)*(model.x2_10_4 - 1.0) + 0.5*(model.z2_10_4 \
    - 1.0)*(model.z2_10_4 - 1.0) + 0.5*(model.x3_10_4 - 1.0)*(model.x3_10_4 - 1.0) + \
    0.5*(model.z3_10_4 - 1.0)*(model.z3_10_4 - 1.0) + 0.5*(model.x4_10_4 - 1.0)*(model.x4_10_4 - 1.0) \
    + 0.5*(model.z4_10_4 - 1.0)*(model.z4_10_4 - 1.0) + 0.5*(model.x5_10_4 - 1.0)*(model.x5_10_4 - \
    1.0) + 0.5*(model.z5_10_4 - 1.0)*(model.z5_10_4 - 1.0) + 0.5*(model.x6_10_4 - 1.0)*(model.x6_10_4 \
    - 1.0) + 0.5*(model.z6_10_4 - 1.0)*(model.z6_10_4 - 1.0) + 0.5*(model.x7_10_4 - \
    1.0)*(model.x7_10_4 - 1.0) + 0.5*(model.z7_10_4 - 1.0)*(model.z7_10_4 - 1.0) + 0.5*(model.x8_10_4 \
    - 1.0)*(model.x8_10_4 - 1.0) + 0.5*(model.z8_10_4 - 1.0)*(model.z8_10_4 - 1.0) + \
    0.5*(model.x9_10_4 - 1.0)*(model.x9_10_4 - 1.0) + 0.5*(model.z9_10_4 - 1.0)*(model.z9_10_4 - 1.0) \
    + 0.5*(model.x1_10_5 - 1.0)*(model.x1_10_5 - 1.0) + 0.5*(model.z1_10_5 - 1.0)*(model.z1_10_5 - \
    1.0) + 0.5*(model.x2_10_5 - 1.0)*(model.x2_10_5 - 1.0) + 0.5*(model.z2_10_5 - 1.0)*(model.z2_10_5 \
    - 1.0) + 0.5*(model.x3_10_5 - 1.0)*(model.x3_10_5 - 1.0) + 0.5*(model.z3_10_5 - \
    1.0)*(model.z3_10_5 - 1.0) + 0.5*(model.x4_10_5 - 1.0)*(model.x4_10_5 - 1.0) + 0.5*(model.z4_10_5 \
    - 1.0)*(model.z4_10_5 - 1.0) + 0.5*(model.x5_10_5 - 1.0)*(model.x5_10_5 - 1.0) + \
    0.5*(model.z5_10_5 - 1.0)*(model.z5_10_5 - 1.0) + 0.5*(model.x6_10_5 - 1.0)*(model.x6_10_5 - 1.0) \
    + 0.5*(model.z6_10_5 - 1.0)*(model.z6_10_5 - 1.0) + 0.5*(model.x7_10_5 - 1.0)*(model.x7_10_5 - \
    1.0) + 0.5*(model.z7_10_5 - 1.0)*(model.z7_10_5 - 1.0) + 0.5*(model.x8_10_5 - 1.0)*(model.x8_10_5 \
    - 1.0) + 0.5*(model.z8_10_5 - 1.0)*(model.z8_10_5 - 1.0) + 0.5*(model.x9_10_5 - \
    1.0)*(model.x9_10_5 - 1.0) + 0.5*(model.z9_10_5 - 1.0)*(model.z9_10_5 - 1.0) + 0.5*(model.x1_10_6 \
    - 1.0)*(model.x1_10_6 - 1.0) + 0.5*(model.z1_10_6 - 1.0)*(model.z1_10_6 - 1.0) + \
    0.5*(model.x2_10_6 - 1.0)*(model.x2_10_6 - 1.0) + 0.5*(model.z2_10_6 - 1.0)*(model.z2_10_6 - 1.0) \
    + 0.5*(model.x3_10_6 - 1.0)*(model.x3_10_6 - 1.0) + 0.5*(model.z3_10_6 - 1.0)*(model.z3_10_6 - \
    1.0) + 0.5*(model.x4_10_6 - 1.0)*(model.x4_10_6 - 1.0) + 0.5*(model.z4_10_6 - 1.0)*(model.z4_10_6 \
    - 1.0) + 0.5*(model.x5_10_6 - 1.0)*(model.x5_10_6 - 1.0) + 0.5*(model.z5_10_6 - \
    1.0)*(model.z5_10_6 - 1.0) + 0.5*(model.x6_10_6 - 1.0)*(model.x6_10_6 - 1.0) + 0.5*(model.z6_10_6 \
    - 1.0)*(model.z6_10_6 - 1.0) + 0.5*(model.x7_10_6 - 1.0)*(model.x7_10_6 - 1.0) + \
    0.5*(model.z7_10_6 - 1.0)*(model.z7_10_6 - 1.0) + 0.5*(model.x8_10_6 - 1.0)*(model.x8_10_6 - 1.0) \
    + 0.5*(model.z8_10_6 - 1.0)*(model.z8_10_6 - 1.0) + 0.5*(model.x9_10_6 - 1.0)*(model.x9_10_6 - \
    1.0) + 0.5*(model.z9_10_6 - 1.0)*(model.z9_10_6 - 1.0) + 0.5*(model.x1_10_7 - 1.0)*(model.x1_10_7 \
    - 1.0) + 0.5*(model.z1_10_7 - 1.0)*(model.z1_10_7 - 1.0) + 0.5*(model.x2_10_7 - \
    1.0)*(model.x2_10_7 - 1.0) + 0.5*(model.z2_10_7 - 1.0)*(model.z2_10_7 - 1.0) + 0.5*(model.x3_10_7 \
    - 1.0)*(model.x3_10_7 - 1.0) + 0.5*(model.z3_10_7 - 1.0)*(model.z3_10_7 - 1.0) + \
    0.5*(model.x4_10_7 - 1.0)*(model.x4_10_7 - 1.0) + 0.5*(model.z4_10_7 - 1.0)*(model.z4_10_7 - 1.0) \
    + 0.5*(model.x5_10_7 - 1.0)*(model.x5_10_7 - 1.0) + 0.5*(model.z5_10_7 - 1.0)*(model.z5_10_7 - \
    1.0) + 0.5*(model.x6_10_7 - 1.0)*(model.x6_10_7 - 1.0) + 0.5*(model.z6_10_7 - 1.0)*(model.z6_10_7 \
    - 1.0) + 0.5*(model.x7_10_7 - 1.0)*(model.x7_10_7 - 1.0) + 0.5*(model.z7_10_7 - \
    1.0)*(model.z7_10_7 - 1.0) + 0.5*(model.x8_10_7 - 1.0)*(model.x8_10_7 - 1.0) + 0.5*(model.z8_10_7 \
    - 1.0)*(model.z8_10_7 - 1.0) + 0.5*(model.x9_10_7 - 1.0)*(model.x9_10_7 - 1.0) + \
    0.5*(model.z9_10_7 - 1.0)*(model.z9_10_7 - 1.0) + 0.5*(model.x1_10_8 - 1.0)*(model.x1_10_8 - 1.0) \
    + 0.5*(model.z1_10_8 - 1.0)*(model.z1_10_8 - 1.0) + 0.5*(model.x2_10_8 - 1.0)*(model.x2_10_8 - \
    1.0) + 0.5*(model.z2_10_8 - 1.0)*(model.z2_10_8 - 1.0) + 0.5*(model.x3_10_8 - 1.0)*(model.x3_10_8 \
    - 1.0) + 0.5*(model.z3_10_8 - 1.0)*(model.z3_10_8 - 1.0) + 0.5*(model.x4_10_8 - \
    1.0)*(model.x4_10_8 - 1.0) + 0.5*(model.z4_10_8 - 1.0)*(model.z4_10_8 - 1.0) + 0.5*(model.x5_10_8 \
    - 1.0)*(model.x5_10_8 - 1.0) + 0.5*(model.z5_10_8 - 1.0)*(model.z5_10_8 - 1.0) + \
    0.5*(model.x6_10_8 - 1.0)*(model.x6_10_8 - 1.0) + 0.5*(model.z6_10_8 - 1.0)*(model.z6_10_8 - 1.0) \
    + 0.5*(model.x7_10_8 - 1.0)*(model.x7_10_8 - 1.0) + 0.5*(model.z7_10_8 - 1.0)*(model.z7_10_8 - \
    1.0) + 0.5*(model.x8_10_8 - 1.0)*(model.x8_10_8 - 1.0) + 0.5*(model.z8_10_8 - 1.0)*(model.z8_10_8 \
    - 1.0) + 0.5*(model.x9_10_8 - 1.0)*(model.x9_10_8 - 1.0) + 0.5*(model.z9_10_8 - \
    1.0)*(model.z9_10_8 - 1.0) + 0.5*(model.x1_10_9 - 1.0)*(model.x1_10_9 - 1.0) + 0.5*(model.z1_10_9 \
    - 1.0)*(model.z1_10_9 - 1.0) + 0.5*(model.x2_10_9 - 1.0)*(model.x2_10_9 - 1.0) + \
    0.5*(model.z2_10_9 - 1.0)*(model.z2_10_9 - 1.0) + 0.5*(model.x3_10_9 - 1.0)*(model.x3_10_9 - 1.0) \
    + 0.5*(model.z3_10_9 - 1.0)*(model.z3_10_9 - 1.0) + 0.5*(model.x4_10_9 - 1.0)*(model.x4_10_9 - \
    1.0) + 0.5*(model.z4_10_9 - 1.0)*(model.z4_10_9 - 1.0) + 0.5*(model.x5_10_9 - 1.0)*(model.x5_10_9 \
    - 1.0) + 0.5*(model.z5_10_9 - 1.0)*(model.z5_10_9 - 1.0) + 0.5*(model.x6_10_9 - \
    1.0)*(model.x6_10_9 - 1.0) + 0.5*(model.z6_10_9 - 1.0)*(model.z6_10_9 - 1.0) + 0.5*(model.x7_10_9 \
    - 1.0)*(model.x7_10_9 - 1.0) + 0.5*(model.z7_10_9 - 1.0)*(model.z7_10_9 - 1.0) + \
    0.5*(model.x8_10_9 - 1.0)*(model.x8_10_9 - 1.0) + 0.5*(model.z8_10_9 - 1.0)*(model.z8_10_9 - 1.0) \
    + 0.5*(model.x9_10_9 - 1.0)*(model.x9_10_9 - 1.0) + 0.5*(model.z9_10_9 - 1.0)*(model.z9_10_9 - \
    1.0) + 0.5*(model.x1_1_10 - 1.0)*(model.x1_1_10 - 1.0) + 0.5*(model.y1_1_10 - 1.0)*(model.y1_1_10 \
    - 1.0) + 0.5*(model.x2_1_10 - 1.0)*(model.x2_1_10 - 1.0) + 0.5*(model.y2_1_10 - \
    1.0)*(model.y2_1_10 - 1.0) + 0.5*(model.x3_1_10 - 1.0)*(model.x3_1_10 - 1.0) + 0.5*(model.y3_1_10 \
    - 1.0)*(model.y3_1_10 - 1.0) + 0.5*(model.x4_1_10 - 1.0)*(model.x4_1_10 - 1.0) + \
    0.5*(model.y4_1_10 - 1.0)*(model.y4_1_10 - 1.0) + 0.5*(model.x5_1_10 - 1.0)*(model.x5_1_10 - 1.0) \
    + 0.5*(model.y5_1_10 - 1.0)*(model.y5_1_10 - 1.0) + 0.5*(model.x6_1_10 - 1.0)*(model.x6_1_10 - \
    1.0) + 0.5*(model.y6_1_10 - 1.0)*(model.y6_1_10 - 1.0) + 0.5*(model.x7_1_10 - 1.0)*(model.x7_1_10 \
    - 1.0) + 0.5*(model.y7_1_10 - 1.0)*(model.y7_1_10 - 1.0) + 0.5*(model.x8_1_10 - \
    1.0)*(model.x8_1_10 - 1.0) + 0.5*(model.y8_1_10 - 1.0)*(model.y8_1_10 - 1.0) + 0.5*(model.x9_1_10 \
    - 1.0)*(model.x9_1_10 - 1.0) + 0.5*(model.y9_1_10 - 1.0)*(model.y9_1_10 - 1.0) + \
    0.5*(model.x1_2_10 - 1.0)*(model.x1_2_10 - 1.0) + 0.5*(model.y1_2_10 - 1.0)*(model.y1_2_10 - 1.0) \
    + 0.5*(model.x2_2_10 - 1.0)*(model.x2_2_10 - 1.0) + 0.5*(model.y2_2_10 - 1.0)*(model.y2_2_10 - \
    1.0) + 0.5*(model.x3_2_10 - 1.0)*(model.x3_2_10 - 1.0) + 0.5*(model.y3_2_10 - 1.0)*(model.y3_2_10 \
    - 1.0) + 0.5*(model.x4_2_10 - 1.0)*(model.x4_2_10 - 1.0) + 0.5*(model.y4_2_10 - \
    1.0)*(model.y4_2_10 - 1.0) + 0.5*(model.x5_2_10 - 1.0)*(model.x5_2_10 - 1.0) + 0.5*(model.y5_2_10 \
    - 1.0)*(model.y5_2_10 - 1.0) + 0.5*(model.x6_2_10 - 1.0)*(model.x6_2_10 - 1.0) + \
    0.5*(model.y6_2_10 - 1.0)*(model.y6_2_10 - 1.0) + 0.5*(model.x7_2_10 - 1.0)*(model.x7_2_10 - 1.0) \
    + 0.5*(model.y7_2_10 - 1.0)*(model.y7_2_10 - 1.0) + 0.5*(model.x8_2_10 - 1.0)*(model.x8_2_10 - \
    1.0) + 0.5*(model.y8_2_10 - 1.0)*(model.y8_2_10 - 1.0) + 0.5*(model.x9_2_10 - 1.0)*(model.x9_2_10 \
    - 1.0) + 0.5*(model.y9_2_10 - 1.0)*(model.y9_2_10 - 1.0) + 0.5*(model.x1_3_10 - \
    1.0)*(model.x1_3_10 - 1.0) + 0.5*(model.y1_3_10 - 1.0)*(model.y1_3_10 - 1.0) + 0.5*(model.x2_3_10 \
    - 1.0)*(model.x2_3_10 - 1.0) + 0.5*(model.y2_3_10 - 1.0)*(model.y2_3_10 - 1.0) + \
    0.5*(model.x3_3_10 - 1.0)*(model.x3_3_10 - 1.0) + 0.5*(model.y3_3_10 - 1.0)*(model.y3_3_10 - 1.0) \
    + 0.5*(model.x4_3_10 - 1.0)*(model.x4_3_10 - 1.0) + 0.5*(model.y4_3_10 - 1.0)*(model.y4_3_10 - \
    1.0) + 0.5*(model.x5_3_10 - 1.0)*(model.x5_3_10 - 1.0) + 0.5*(model.y5_3_10 - 1.0)*(model.y5_3_10 \
    - 1.0) + 0.5*(model.x6_3_10 - 1.0)*(model.x6_3_10 - 1.0) + 0.5*(model.y6_3_10 - \
    1.0)*(model.y6_3_10 - 1.0) + 0.5*(model.x7_3_10 - 1.0)*(model.x7_3_10 - 1.0) + 0.5*(model.y7_3_10 \
    - 1.0)*(model.y7_3_10 - 1.0) + 0.5*(model.x8_3_10 - 1.0)*(model.x8_3_10 - 1.0) + \
    0.5*(model.y8_3_10 - 1.0)*(model.y8_3_10 - 1.0) + 0.5*(model.x9_3_10 - 1.0)*(model.x9_3_10 - 1.0) \
    + 0.5*(model.y9_3_10 - 1.0)*(model.y9_3_10 - 1.0) + 0.5*(model.x1_4_10 - 1.0)*(model.x1_4_10 - \
    1.0) + 0.5*(model.y1_4_10 - 1.0)*(model.y1_4_10 - 1.0) + 0.5*(model.x2_4_10 - 1.0)*(model.x2_4_10 \
    - 1.0) + 0.5*(model.y2_4_10 - 1.0)*(model.y2_4_10 - 1.0) + 0.5*(model.x3_4_10 - \
    1.0)*(model.x3_4_10 - 1.0) + 0.5*(model.y3_4_10 - 1.0)*(model.y3_4_10 - 1.0) + 0.5*(model.x4_4_10 \
    - 1.0)*(model.x4_4_10 - 1.0) + 0.5*(model.y4_4_10 - 1.0)*(model.y4_4_10 - 1.0) + \
    0.5*(model.x5_4_10 - 1.0)*(model.x5_4_10 - 1.0) + 0.5*(model.y5_4_10 - 1.0)*(model.y5_4_10 - 1.0) \
    + 0.5*(model.x6_4_10 - 1.0)*(model.x6_4_10 - 1.0) + 0.5*(model.y6_4_10 - 1.0)*(model.y6_4_10 - \
    1.0) + 0.5*(model.x7_4_10 - 1.0)*(model.x7_4_10 - 1.0) + 0.5*(model.y7_4_10 - 1.0)*(model.y7_4_10 \
    - 1.0) + 0.5*(model.x8_4_10 - 1.0)*(model.x8_4_10 - 1.0) + 0.5*(model.y8_4_10 - \
    1.0)*(model.y8_4_10 - 1.0) + 0.5*(model.x9_4_10 - 1.0)*(model.x9_4_10 - 1.0) + 0.5*(model.y9_4_10 \
    - 1.0)*(model.y9_4_10 - 1.0) + 0.5*(model.x1_5_10 - 1.0)*(model.x1_5_10 - 1.0) + \
    0.5*(model.y1_5_10 - 1.0)*(model.y1_5_10 - 1.0) + 0.5*(model.x2_5_10 - 1.0)*(model.x2_5_10 - 1.0) \
    + 0.5*(model.y2_5_10 - 1.0)*(model.y2_5_10 - 1.0) + 0.5*(model.x3_5_10 - 1.0)*(model.x3_5_10 - \
    1.0) + 0.5*(model.y3_5_10 - 1.0)*(model.y3_5_10 - 1.0) + 0.5*(model.x4_5_10 - 1.0)*(model.x4_5_10 \
    - 1.0) + 0.5*(model.y4_5_10 - 1.0)*(model.y4_5_10 - 1.0) + 0.5*(model.x5_5_10 - \
    1.0)*(model.x5_5_10 - 1.0) + 0.5*(model.y5_5_10 - 1.0)*(model.y5_5_10 - 1.0) + 0.5*(model.x6_5_10 \
    - 1.0)*(model.x6_5_10 - 1.0) + 0.5*(model.y6_5_10 - 1.0)*(model.y6_5_10 - 1.0) + \
    0.5*(model.x7_5_10 - 1.0)*(model.x7_5_10 - 1.0) + 0.5*(model.y7_5_10 - 1.0)*(model.y7_5_10 - 1.0) \
    + 0.5*(model.x8_5_10 - 1.0)*(model.x8_5_10 - 1.0) + 0.5*(model.y8_5_10 - 1.0)*(model.y8_5_10 - \
    1.0) + 0.5*(model.x9_5_10 - 1.0)*(model.x9_5_10 - 1.0) + 0.5*(model.y9_5_10 - 1.0)*(model.y9_5_10 \
    - 1.0) + 0.5*(model.x1_6_10 - 1.0)*(model.x1_6_10 - 1.0) + 0.5*(model.y1_6_10 - \
    1.0)*(model.y1_6_10 - 1.0) + 0.5*(model.x2_6_10 - 1.0)*(model.x2_6_10 - 1.0) + 0.5*(model.y2_6_10 \
    - 1.0)*(model.y2_6_10 - 1.0) + 0.5*(model.x3_6_10 - 1.0)*(model.x3_6_10 - 1.0) + \
    0.5*(model.y3_6_10 - 1.0)*(model.y3_6_10 - 1.0) + 0.5*(model.x4_6_10 - 1.0)*(model.x4_6_10 - 1.0) \
    + 0.5*(model.y4_6_10 - 1.0)*(model.y4_6_10 - 1.0) + 0.5*(model.x5_6_10 - 1.0)*(model.x5_6_10 - \
    1.0) + 0.5*(model.y5_6_10 - 1.0)*(model.y5_6_10 - 1.0) + 0.5*(model.x6_6_10 - 1.0)*(model.x6_6_10 \
    - 1.0) + 0.5*(model.y6_6_10 - 1.0)*(model.y6_6_10 - 1.0) + 0.5*(model.x7_6_10 - \
    1.0)*(model.x7_6_10 - 1.0) + 0.5*(model.y7_6_10 - 1.0)*(model.y7_6_10 - 1.0) + 0.5*(model.x8_6_10 \
    - 1.0)*(model.x8_6_10 - 1.0) + 0.5*(model.y8_6_10 - 1.0)*(model.y8_6_10 - 1.0) + \
    0.5*(model.x9_6_10 - 1.0)*(model.x9_6_10 - 1.0) + 0.5*(model.y9_6_10 - 1.0)*(model.y9_6_10 - 1.0) \
    + 0.5*(model.x1_7_10 - 1.0)*(model.x1_7_10 - 1.0) + 0.5*(model.y1_7_10 - 1.0)*(model.y1_7_10 - \
    1.0) + 0.5*(model.x2_7_10 - 1.0)*(model.x2_7_10 - 1.0) + 0.5*(model.y2_7_10 - 1.0)*(model.y2_7_10 \
    - 1.0) + 0.5*(model.x3_7_10 - 1.0)*(model.x3_7_10 - 1.0) + 0.5*(model.y3_7_10 - \
    1.0)*(model.y3_7_10 - 1.0) + 0.5*(model.x4_7_10 - 1.0)*(model.x4_7_10 - 1.0) + 0.5*(model.y4_7_10 \
    - 1.0)*(model.y4_7_10 - 1.0) + 0.5*(model.x5_7_10 - 1.0)*(model.x5_7_10 - 1.0) + \
    0.5*(model.y5_7_10 - 1.0)*(model.y5_7_10 - 1.0) + 0.5*(model.x6_7_10 - 1.0)*(model.x6_7_10 - 1.0) \
    + 0.5*(model.y6_7_10 - 1.0)*(model.y6_7_10 - 1.0) + 0.5*(model.x7_7_10 - 1.0)*(model.x7_7_10 - \
    1.0) + 0.5*(model.y7_7_10 - 1.0)*(model.y7_7_10 - 1.0) + 0.5*(model.x8_7_10 - 1.0)*(model.x8_7_10 \
    - 1.0) + 0.5*(model.y8_7_10 - 1.0)*(model.y8_7_10 - 1.0) + 0.5*(model.x9_7_10 - \
    1.0)*(model.x9_7_10 - 1.0) + 0.5*(model.y9_7_10 - 1.0)*(model.y9_7_10 - 1.0) + 0.5*(model.x1_8_10 \
    - 1.0)*(model.x1_8_10 - 1.0) + 0.5*(model.y1_8_10 - 1.0)*(model.y1_8_10 - 1.0) + \
    0.5*(model.x2_8_10 - 1.0)*(model.x2_8_10 - 1.0) + 0.5*(model.y2_8_10 - 1.0)*(model.y2_8_10 - 1.0) \
    + 0.5*(model.x3_8_10 - 1.0)*(model.x3_8_10 - 1.0) + 0.5*(model.y3_8_10 - 1.0)*(model.y3_8_10 - \
    1.0) + 0.5*(model.x4_8_10 - 1.0)*(model.x4_8_10 - 1.0) + 0.5*(model.y4_8_10 - 1.0)*(model.y4_8_10 \
    - 1.0) + 0.5*(model.x5_8_10 - 1.0)*(model.x5_8_10 - 1.0) + 0.5*(model.y5_8_10 - \
    1.0)*(model.y5_8_10 - 1.0) + 0.5*(model.x6_8_10 - 1.0)*(model.x6_8_10 - 1.0) + 0.5*(model.y6_8_10 \
    - 1.0)*(model.y6_8_10 - 1.0) + 0.5*(model.x7_8_10 - 1.0)*(model.x7_8_10 - 1.0) + \
    0.5*(model.y7_8_10 - 1.0)*(model.y7_8_10 - 1.0) + 0.5*(model.x8_8_10 - 1.0)*(model.x8_8_10 - 1.0) \
    + 0.5*(model.y8_8_10 - 1.0)*(model.y8_8_10 - 1.0) + 0.5*(model.x9_8_10 - 1.0)*(model.x9_8_10 - \
    1.0) + 0.5*(model.y9_8_10 - 1.0)*(model.y9_8_10 - 1.0) + 0.5*(model.x1_9_10 - 1.0)*(model.x1_9_10 \
    - 1.0) + 0.5*(model.y1_9_10 - 1.0)*(model.y1_9_10 - 1.0) + 0.5*(model.x2_9_10 - \
    1.0)*(model.x2_9_10 - 1.0) + 0.5*(model.y2_9_10 - 1.0)*(model.y2_9_10 - 1.0) + 0.5*(model.x3_9_10 \
    - 1.0)*(model.x3_9_10 - 1.0) + 0.5*(model.y3_9_10 - 1.0)*(model.y3_9_10 - 1.0) + \
    0.5*(model.x4_9_10 - 1.0)*(model.x4_9_10 - 1.0) + 0.5*(model.y4_9_10 - 1.0)*(model.y4_9_10 - 1.0) \
    + 0.5*(model.x5_9_10 - 1.0)*(model.x5_9_10 - 1.0) + 0.5*(model.y5_9_10 - 1.0)*(model.y5_9_10 - \
    1.0) + 0.5*(model.x6_9_10 - 1.0)*(model.x6_9_10 - 1.0) + 0.5*(model.y6_9_10 - 1.0)*(model.y6_9_10 \
    - 1.0) + 0.5*(model.x7_9_10 - 1.0)*(model.x7_9_10 - 1.0) + 0.5*(model.y7_9_10 - \
    1.0)*(model.y7_9_10 - 1.0) + 0.5*(model.x8_9_10 - 1.0)*(model.x8_9_10 - 1.0) + 0.5*(model.y8_9_10 \
    - 1.0)*(model.y8_9_10 - 1.0) + 0.5*(model.x9_9_10 - 1.0)*(model.x9_9_10 - 1.0) + \
    0.5*(model.y9_9_10 - 1.0)*(model.y9_9_10 - 1.0) + 0.5*(model.y0_1_1 - 1.0)*(model.y0_1_1 - 1.0) + \
    0.5*(model.z0_1_1 - 1.0)*(model.z0_1_1 - 1.0) + 0.5*(model.y11_1_1 - 1.0)*(model.y11_1_1 - 1.0) + \
    0.5*(model.z11_1_1 - 1.0)*(model.z11_1_1 - 1.0) + 0.5*(model.y0_2_1 - 1.0)*(model.y0_2_1 - 1.0) + \
    0.5*(model.z0_2_1 - 1.0)*(model.z0_2_1 - 1.0) + 0.5*(model.y11_2_1 - 1.0)*(model.y11_2_1 - 1.0) + \
    0.5*(model.z11_2_1 - 1.0)*(model.z11_2_1 - 1.0) + 0.5*(model.y0_3_1 - 1.0)*(model.y0_3_1 - 1.0) + \
    0.5*(model.z0_3_1 - 1.0)*(model.z0_3_1 - 1.0) + 0.5*(model.y11_3_1 - 1.0)*(model.y11_3_1 - 1.0) + \
    0.5*(model.z11_3_1 - 1.0)*(model.z11_3_1 - 1.0) + 0.5*(model.y0_4_1 - 1.0)*(model.y0_4_1 - 1.0) + \
    0.5*(model.z0_4_1 - 1.0)*(model.z0_4_1 - 1.0) + 0.5*(model.y11_4_1 - 1.0)*(model.y11_4_1 - 1.0) + \
    0.5*(model.z11_4_1 - 1.0)*(model.z11_4_1 - 1.0) + 0.5*(model.y0_5_1 - 1.0)*(model.y0_5_1 - 1.0) + \
    0.5*(model.z0_5_1 - 1.0)*(model.z0_5_1 - 1.0) + 0.5*(model.y11_5_1 - 1.0)*(model.y11_5_1 - 1.0) + \
    0.5*(model.z11_5_1 - 1.0)*(model.z11_5_1 - 1.0) + 0.5*(model.y0_6_1 - 1.0)*(model.y0_6_1 - 1.0) + \
    0.5*(model.z0_6_1 - 1.0)*(model.z0_6_1 - 1.0) + 0.5*(model.y11_6_1 - 1.0)*(model.y11_6_1 - 1.0) + \
    0.5*(model.z11_6_1 - 1.0)*(model.z11_6_1 - 1.0) + 0.5*(model.y0_7_1 - 1.0)*(model.y0_7_1 - 1.0) + \
    0.5*(model.z0_7_1 - 1.0)*(model.z0_7_1 - 1.0) + 0.5*(model.y11_7_1 - 1.0)*(model.y11_7_1 - 1.0) + \
    0.5*(model.z11_7_1 - 1.0)*(model.z11_7_1 - 1.0) + 0.5*(model.y0_8_1 - 1.0)*(model.y0_8_1 - 1.0) + \
    0.5*(model.z0_8_1 - 1.0)*(model.z0_8_1 - 1.0) + 0.5*(model.y11_8_1 - 1.0)*(model.y11_8_1 - 1.0) + \
    0.5*(model.z11_8_1 - 1.0)*(model.z11_8_1 - 1.0) + 0.5*(model.y0_9_1 - 1.0)*(model.y0_9_1 - 1.0) + \
    0.5*(model.z0_9_1 - 1.0)*(model.z0_9_1 - 1.0) + 0.5*(model.y11_9_1 - 1.0)*(model.y11_9_1 - 1.0) + \
    0.5*(model.z11_9_1 - 1.0)*(model.z11_9_1 - 1.0) + 0.5*(model.y0_10_1 - 1.0)*(model.y0_10_1 - 1.0) \
    + 0.5*(model.z0_10_1 - 1.0)*(model.z0_10_1 - 1.0) + 0.5*(model.y11_10_1 - 1.0)*(model.y11_10_1 - \
    1.0) + 0.5*(model.z11_10_1 - 1.0)*(model.z11_10_1 - 1.0) + 0.5*(model.y0_1_2 - 1.0)*(model.y0_1_2 \
    - 1.0) + 0.5*(model.z0_1_2 - 1.0)*(model.z0_1_2 - 1.0) + 0.5*(model.y11_1_2 - 1.0)*(model.y11_1_2 \
    - 1.0) + 0.5*(model.z11_1_2 - 1.0)*(model.z11_1_2 - 1.0) + 0.5*(model.y0_2_2 - 1.0)*(model.y0_2_2 \
    - 1.0) + 0.5*(model.z0_2_2 - 1.0)*(model.z0_2_2 - 1.0) + 0.5*(model.y11_2_2 - 1.0)*(model.y11_2_2 \
    - 1.0) + 0.5*(model.z11_2_2 - 1.0)*(model.z11_2_2 - 1.0) + 0.5*(model.y0_3_2 - 1.0)*(model.y0_3_2 \
    - 1.0) + 0.5*(model.z0_3_2 - 1.0)*(model.z0_3_2 - 1.0) + 0.5*(model.y11_3_2 - 1.0)*(model.y11_3_2 \
    - 1.0) + 0.5*(model.z11_3_2 - 1.0)*(model.z11_3_2 - 1.0) + 0.5*(model.y0_4_2 - 1.0)*(model.y0_4_2 \
    - 1.0) + 0.5*(model.z0_4_2 - 1.0)*(model.z0_4_2 - 1.0) + 0.5*(model.y11_4_2 - 1.0)*(model.y11_4_2 \
    - 1.0) + 0.5*(model.z11_4_2 - 1.0)*(model.z11_4_2 - 1.0) + 0.5*(model.y0_5_2 - 1.0)*(model.y0_5_2 \
    - 1.0) + 0.5*(model.z0_5_2 - 1.0)*(model.z0_5_2 - 1.0) + 0.5*(model.y11_5_2 - 1.0)*(model.y11_5_2 \
    - 1.0) + 0.5*(model.z11_5_2 - 1.0)*(model.z11_5_2 - 1.0) + 0.5*(model.y0_6_2 - 1.0)*(model.y0_6_2 \
    - 1.0) + 0.5*(model.z0_6_2 - 1.0)*(model.z0_6_2 - 1.0) + 0.5*(model.y11_6_2 - 1.0)*(model.y11_6_2 \
    - 1.0) + 0.5*(model.z11_6_2 - 1.0)*(model.z11_6_2 - 1.0) + 0.5*(model.y0_7_2 - 1.0)*(model.y0_7_2 \
    - 1.0) + 0.5*(model.z0_7_2 - 1.0)*(model.z0_7_2 - 1.0) + 0.5*(model.y11_7_2 - 1.0)*(model.y11_7_2 \
    - 1.0) + 0.5*(model.z11_7_2 - 1.0)*(model.z11_7_2 - 1.0) + 0.5*(model.y0_8_2 - 1.0)*(model.y0_8_2 \
    - 1.0) + 0.5*(model.z0_8_2 - 1.0)*(model.z0_8_2 - 1.0) + 0.5*(model.y11_8_2 - 1.0)*(model.y11_8_2 \
    - 1.0) + 0.5*(model.z11_8_2 - 1.0)*(model.z11_8_2 - 1.0) + 0.5*(model.y0_9_2 - 1.0)*(model.y0_9_2 \
    - 1.0) + 0.5*(model.z0_9_2 - 1.0)*(model.z0_9_2 - 1.0) + 0.5*(model.y11_9_2 - 1.0)*(model.y11_9_2 \
    - 1.0) + 0.5*(model.z11_9_2 - 1.0)*(model.z11_9_2 - 1.0) + 0.5*(model.y0_10_2 - \
    1.0)*(model.y0_10_2 - 1.0) + 0.5*(model.z0_10_2 - 1.0)*(model.z0_10_2 - 1.0) + \
    0.5*(model.y11_10_2 - 1.0)*(model.y11_10_2 - 1.0) + 0.5*(model.z11_10_2 - 1.0)*(model.z11_10_2 - \
    1.0) + 0.5*(model.y0_1_3 - 1.0)*(model.y0_1_3 - 1.0) + 0.5*(model.z0_1_3 - 1.0)*(model.z0_1_3 - \
    1.0) + 0.5*(model.y11_1_3 - 1.0)*(model.y11_1_3 - 1.0) + 0.5*(model.z11_1_3 - 1.0)*(model.z11_1_3 \
    - 1.0) + 0.5*(model.y0_2_3 - 1.0)*(model.y0_2_3 - 1.0) + 0.5*(model.z0_2_3 - 1.0)*(model.z0_2_3 - \
    1.0) + 0.5*(model.y11_2_3 - 1.0)*(model.y11_2_3 - 1.0) + 0.5*(model.z11_2_3 - 1.0)*(model.z11_2_3 \
    - 1.0) + 0.5*(model.y0_3_3 - 1.0)*(model.y0_3_3 - 1.0) + 0.5*(model.z0_3_3 - 1.0)*(model.z0_3_3 - \
    1.0) + 0.5*(model.y11_3_3 - 1.0)*(model.y11_3_3 - 1.0) + 0.5*(model.z11_3_3 - 1.0)*(model.z11_3_3 \
    - 1.0) + 0.5*(model.y0_4_3 - 1.0)*(model.y0_4_3 - 1.0) + 0.5*(model.z0_4_3 - 1.0)*(model.z0_4_3 - \
    1.0) + 0.5*(model.y11_4_3 - 1.0)*(model.y11_4_3 - 1.0) + 0.5*(model.z11_4_3 - 1.0)*(model.z11_4_3 \
    - 1.0) + 0.5*(model.y0_5_3 - 1.0)*(model.y0_5_3 - 1.0) + 0.5*(model.z0_5_3 - 1.0)*(model.z0_5_3 - \
    1.0) + 0.5*(model.y11_5_3 - 1.0)*(model.y11_5_3 - 1.0) + 0.5*(model.z11_5_3 - 1.0)*(model.z11_5_3 \
    - 1.0) + 0.5*(model.y0_6_3 - 1.0)*(model.y0_6_3 - 1.0) + 0.5*(model.z0_6_3 - 1.0)*(model.z0_6_3 - \
    1.0) + 0.5*(model.y11_6_3 - 1.0)*(model.y11_6_3 - 1.0) + 0.5*(model.z11_6_3 - 1.0)*(model.z11_6_3 \
    - 1.0) + 0.5*(model.y0_7_3 - 1.0)*(model.y0_7_3 - 1.0) + 0.5*(model.z0_7_3 - 1.0)*(model.z0_7_3 - \
    1.0) + 0.5*(model.y11_7_3 - 1.0)*(model.y11_7_3 - 1.0) + 0.5*(model.z11_7_3 - 1.0)*(model.z11_7_3 \
    - 1.0) + 0.5*(model.y0_8_3 - 1.0)*(model.y0_8_3 - 1.0) + 0.5*(model.z0_8_3 - 1.0)*(model.z0_8_3 - \
    1.0) + 0.5*(model.y11_8_3 - 1.0)*(model.y11_8_3 - 1.0) + 0.5*(model.z11_8_3 - 1.0)*(model.z11_8_3 \
    - 1.0) + 0.5*(model.y0_9_3 - 1.0)*(model.y0_9_3 - 1.0) + 0.5*(model.z0_9_3 - 1.0)*(model.z0_9_3 - \
    1.0) + 0.5*(model.y11_9_3 - 1.0)*(model.y11_9_3 - 1.0) + 0.5*(model.z11_9_3 - 1.0)*(model.z11_9_3 \
    - 1.0) + 0.5*(model.y0_10_3 - 1.0)*(model.y0_10_3 - 1.0) + 0.5*(model.z0_10_3 - \
    1.0)*(model.z0_10_3 - 1.0) + 0.5*(model.y11_10_3 - 1.0)*(model.y11_10_3 - 1.0) + \
    0.5*(model.z11_10_3 - 1.0)*(model.z11_10_3 - 1.0) + 0.5*(model.y0_1_4 - 1.0)*(model.y0_1_4 - 1.0) \
    + 0.5*(model.z0_1_4 - 1.0)*(model.z0_1_4 - 1.0) + 0.5*(model.y11_1_4 - 1.0)*(model.y11_1_4 - 1.0) \
    + 0.5*(model.z11_1_4 - 1.0)*(model.z11_1_4 - 1.0) + 0.5*(model.y0_2_4 - 1.0)*(model.y0_2_4 - 1.0) \
    + 0.5*(model.z0_2_4 - 1.0)*(model.z0_2_4 - 1.0) + 0.5*(model.y11_2_4 - 1.0)*(model.y11_2_4 - 1.0) \
    + 0.5*(model.z11_2_4 - 1.0)*(model.z11_2_4 - 1.0) + 0.5*(model.y0_3_4 - 1.0)*(model.y0_3_4 - 1.0) \
    + 0.5*(model.z0_3_4 - 1.0)*(model.z0_3_4 - 1.0) + 0.5*(model.y11_3_4 - 1.0)*(model.y11_3_4 - 1.0) \
    + 0.5*(model.z11_3_4 - 1.0)*(model.z11_3_4 - 1.0) + 0.5*(model.y0_4_4 - 1.0)*(model.y0_4_4 - 1.0) \
    + 0.5*(model.z0_4_4 - 1.0)*(model.z0_4_4 - 1.0) + 0.5*(model.y11_4_4 - 1.0)*(model.y11_4_4 - 1.0) \
    + 0.5*(model.z11_4_4 - 1.0)*(model.z11_4_4 - 1.0) + 0.5*(model.y0_5_4 - 1.0)*(model.y0_5_4 - 1.0) \
    + 0.5*(model.z0_5_4 - 1.0)*(model.z0_5_4 - 1.0) + 0.5*(model.y11_5_4 - 1.0)*(model.y11_5_4 - 1.0) \
    + 0.5*(model.z11_5_4 - 1.0)*(model.z11_5_4 - 1.0) + 0.5*(model.y0_6_4 - 1.0)*(model.y0_6_4 - 1.0) \
    + 0.5*(model.z0_6_4 - 1.0)*(model.z0_6_4 - 1.0) + 0.5*(model.y11_6_4 - 1.0)*(model.y11_6_4 - 1.0) \
    + 0.5*(model.z11_6_4 - 1.0)*(model.z11_6_4 - 1.0) + 0.5*(model.y0_7_4 - 1.0)*(model.y0_7_4 - 1.0) \
    + 0.5*(model.z0_7_4 - 1.0)*(model.z0_7_4 - 1.0) + 0.5*(model.y11_7_4 - 1.0)*(model.y11_7_4 - 1.0) \
    + 0.5*(model.z11_7_4 - 1.0)*(model.z11_7_4 - 1.0) + 0.5*(model.y0_8_4 - 1.0)*(model.y0_8_4 - 1.0) \
    + 0.5*(model.z0_8_4 - 1.0)*(model.z0_8_4 - 1.0) + 0.5*(model.y11_8_4 - 1.0)*(model.y11_8_4 - 1.0) \
    + 0.5*(model.z11_8_4 - 1.0)*(model.z11_8_4 - 1.0) + 0.5*(model.y0_9_4 - 1.0)*(model.y0_9_4 - 1.0) \
    + 0.5*(model.z0_9_4 - 1.0)*(model.z0_9_4 - 1.0) + 0.5*(model.y11_9_4 - 1.0)*(model.y11_9_4 - 1.0) \
    + 0.5*(model.z11_9_4 - 1.0)*(model.z11_9_4 - 1.0) + 0.5*(model.y0_10_4 - 1.0)*(model.y0_10_4 - \
    1.0) + 0.5*(model.z0_10_4 - 1.0)*(model.z0_10_4 - 1.0) + 0.5*(model.y11_10_4 - \
    1.0)*(model.y11_10_4 - 1.0) + 0.5*(model.z11_10_4 - 1.0)*(model.z11_10_4 - 1.0) + \
    0.5*(model.y0_1_5 - 1.0)*(model.y0_1_5 - 1.0) + 0.5*(model.z0_1_5 - 1.0)*(model.z0_1_5 - 1.0) + \
    0.5*(model.y11_1_5 - 1.0)*(model.y11_1_5 - 1.0) + 0.5*(model.z11_1_5 - 1.0)*(model.z11_1_5 - 1.0) \
    + 0.5*(model.y0_2_5 - 1.0)*(model.y0_2_5 - 1.0) + 0.5*(model.z0_2_5 - 1.0)*(model.z0_2_5 - 1.0) + \
    0.5*(model.y11_2_5 - 1.0)*(model.y11_2_5 - 1.0) + 0.5*(model.z11_2_5 - 1.0)*(model.z11_2_5 - 1.0) \
    + 0.5*(model.y0_3_5 - 1.0)*(model.y0_3_5 - 1.0) + 0.5*(model.z0_3_5 - 1.0)*(model.z0_3_5 - 1.0) + \
    0.5*(model.y11_3_5 - 1.0)*(model.y11_3_5 - 1.0) + 0.5*(model.z11_3_5 - 1.0)*(model.z11_3_5 - 1.0) \
    + 0.5*(model.y0_4_5 - 1.0)*(model.y0_4_5 - 1.0) + 0.5*(model.z0_4_5 - 1.0)*(model.z0_4_5 - 1.0) + \
    0.5*(model.y11_4_5 - 1.0)*(model.y11_4_5 - 1.0) + 0.5*(model.z11_4_5 - 1.0)*(model.z11_4_5 - 1.0) \
    + 0.5*(model.y0_5_5 - 1.0)*(model.y0_5_5 - 1.0) + 0.5*(model.z0_5_5 - 1.0)*(model.z0_5_5 - 1.0) + \
    0.5*(model.y11_5_5 - 1.0)*(model.y11_5_5 - 1.0) + 0.5*(model.z11_5_5 - 1.0)*(model.z11_5_5 - 1.0) \
    + 0.5*(model.y0_6_5 - 1.0)*(model.y0_6_5 - 1.0) + 0.5*(model.z0_6_5 - 1.0)*(model.z0_6_5 - 1.0) + \
    0.5*(model.y11_6_5 - 1.0)*(model.y11_6_5 - 1.0) + 0.5*(model.z11_6_5 - 1.0)*(model.z11_6_5 - 1.0) \
    + 0.5*(model.y0_7_5 - 1.0)*(model.y0_7_5 - 1.0) + 0.5*(model.z0_7_5 - 1.0)*(model.z0_7_5 - 1.0) + \
    0.5*(model.y11_7_5 - 1.0)*(model.y11_7_5 - 1.0) + 0.5*(model.z11_7_5 - 1.0)*(model.z11_7_5 - 1.0) \
    + 0.5*(model.y0_8_5 - 1.0)*(model.y0_8_5 - 1.0) + 0.5*(model.z0_8_5 - 1.0)*(model.z0_8_5 - 1.0) + \
    0.5*(model.y11_8_5 - 1.0)*(model.y11_8_5 - 1.0) + 0.5*(model.z11_8_5 - 1.0)*(model.z11_8_5 - 1.0) \
    + 0.5*(model.y0_9_5 - 1.0)*(model.y0_9_5 - 1.0) + 0.5*(model.z0_9_5 - 1.0)*(model.z0_9_5 - 1.0) + \
    0.5*(model.y11_9_5 - 1.0)*(model.y11_9_5 - 1.0) + 0.5*(model.z11_9_5 - 1.0)*(model.z11_9_5 - 1.0) \
    + 0.5*(model.y0_10_5 - 1.0)*(model.y0_10_5 - 1.0) + 0.5*(model.z0_10_5 - 1.0)*(model.z0_10_5 - \
    1.0) + 0.5*(model.y11_10_5 - 1.0)*(model.y11_10_5 - 1.0) + 0.5*(model.z11_10_5 - \
    1.0)*(model.z11_10_5 - 1.0) + 0.5*(model.y0_1_6 - 1.0)*(model.y0_1_6 - 1.0) + 0.5*(model.z0_1_6 - \
    1.0)*(model.z0_1_6 - 1.0) + 0.5*(model.y11_1_6 - 1.0)*(model.y11_1_6 - 1.0) + 0.5*(model.z11_1_6 \
    - 1.0)*(model.z11_1_6 - 1.0) + 0.5*(model.y0_2_6 - 1.0)*(model.y0_2_6 - 1.0) + 0.5*(model.z0_2_6 \
    - 1.0)*(model.z0_2_6 - 1.0) + 0.5*(model.y11_2_6 - 1.0)*(model.y11_2_6 - 1.0) + \
    0.5*(model.z11_2_6 - 1.0)*(model.z11_2_6 - 1.0) + 0.5*(model.y0_3_6 - 1.0)*(model.y0_3_6 - 1.0) + \
    0.5*(model.z0_3_6 - 1.0)*(model.z0_3_6 - 1.0) + 0.5*(model.y11_3_6 - 1.0)*(model.y11_3_6 - 1.0) + \
    0.5*(model.z11_3_6 - 1.0)*(model.z11_3_6 - 1.0) + 0.5*(model.y0_4_6 - 1.0)*(model.y0_4_6 - 1.0) + \
    0.5*(model.z0_4_6 - 1.0)*(model.z0_4_6 - 1.0) + 0.5*(model.y11_4_6 - 1.0)*(model.y11_4_6 - 1.0) + \
    0.5*(model.z11_4_6 - 1.0)*(model.z11_4_6 - 1.0) + 0.5*(model.y0_5_6 - 1.0)*(model.y0_5_6 - 1.0) + \
    0.5*(model.z0_5_6 - 1.0)*(model.z0_5_6 - 1.0) + 0.5*(model.y11_5_6 - 1.0)*(model.y11_5_6 - 1.0) + \
    0.5*(model.z11_5_6 - 1.0)*(model.z11_5_6 - 1.0) + 0.5*(model.y0_6_6 - 1.0)*(model.y0_6_6 - 1.0) + \
    0.5*(model.z0_6_6 - 1.0)*(model.z0_6_6 - 1.0) + 0.5*(model.y11_6_6 - 1.0)*(model.y11_6_6 - 1.0) + \
    0.5*(model.z11_6_6 - 1.0)*(model.z11_6_6 - 1.0) + 0.5*(model.y0_7_6 - 1.0)*(model.y0_7_6 - 1.0) + \
    0.5*(model.z0_7_6 - 1.0)*(model.z0_7_6 - 1.0) + 0.5*(model.y11_7_6 - 1.0)*(model.y11_7_6 - 1.0) + \
    0.5*(model.z11_7_6 - 1.0)*(model.z11_7_6 - 1.0) + 0.5*(model.y0_8_6 - 1.0)*(model.y0_8_6 - 1.0) + \
    0.5*(model.z0_8_6 - 1.0)*(model.z0_8_6 - 1.0) + 0.5*(model.y11_8_6 - 1.0)*(model.y11_8_6 - 1.0) + \
    0.5*(model.z11_8_6 - 1.0)*(model.z11_8_6 - 1.0) + 0.5*(model.y0_9_6 - 1.0)*(model.y0_9_6 - 1.0) + \
    0.5*(model.z0_9_6 - 1.0)*(model.z0_9_6 - 1.0) + 0.5*(model.y11_9_6 - 1.0)*(model.y11_9_6 - 1.0) + \
    0.5*(model.z11_9_6 - 1.0)*(model.z11_9_6 - 1.0) + 0.5*(model.y0_10_6 - 1.0)*(model.y0_10_6 - 1.0) \
    + 0.5*(model.z0_10_6 - 1.0)*(model.z0_10_6 - 1.0) + 0.5*(model.y11_10_6 - 1.0)*(model.y11_10_6 - \
    1.0) + 0.5*(model.z11_10_6 - 1.0)*(model.z11_10_6 - 1.0) + 0.5*(model.y0_1_7 - 1.0)*(model.y0_1_7 \
    - 1.0) + 0.5*(model.z0_1_7 - 1.0)*(model.z0_1_7 - 1.0) + 0.5*(model.y11_1_7 - 1.0)*(model.y11_1_7 \
    - 1.0) + 0.5*(model.z11_1_7 - 1.0)*(model.z11_1_7 - 1.0) + 0.5*(model.y0_2_7 - 1.0)*(model.y0_2_7 \
    - 1.0) + 0.5*(model.z0_2_7 - 1.0)*(model.z0_2_7 - 1.0) + 0.5*(model.y11_2_7 - 1.0)*(model.y11_2_7 \
    - 1.0) + 0.5*(model.z11_2_7 - 1.0)*(model.z11_2_7 - 1.0) + 0.5*(model.y0_3_7 - 1.0)*(model.y0_3_7 \
    - 1.0) + 0.5*(model.z0_3_7 - 1.0)*(model.z0_3_7 - 1.0) + 0.5*(model.y11_3_7 - 1.0)*(model.y11_3_7 \
    - 1.0) + 0.5*(model.z11_3_7 - 1.0)*(model.z11_3_7 - 1.0) + 0.5*(model.y0_4_7 - 1.0)*(model.y0_4_7 \
    - 1.0) + 0.5*(model.z0_4_7 - 1.0)*(model.z0_4_7 - 1.0) + 0.5*(model.y11_4_7 - 1.0)*(model.y11_4_7 \
    - 1.0) + 0.5*(model.z11_4_7 - 1.0)*(model.z11_4_7 - 1.0) + 0.5*(model.y0_5_7 - 1.0)*(model.y0_5_7 \
    - 1.0) + 0.5*(model.z0_5_7 - 1.0)*(model.z0_5_7 - 1.0) + 0.5*(model.y11_5_7 - 1.0)*(model.y11_5_7 \
    - 1.0) + 0.5*(model.z11_5_7 - 1.0)*(model.z11_5_7 - 1.0) + 0.5*(model.y0_6_7 - 1.0)*(model.y0_6_7 \
    - 1.0) + 0.5*(model.z0_6_7 - 1.0)*(model.z0_6_7 - 1.0) + 0.5*(model.y11_6_7 - 1.0)*(model.y11_6_7 \
    - 1.0) + 0.5*(model.z11_6_7 - 1.0)*(model.z11_6_7 - 1.0) + 0.5*(model.y0_7_7 - 1.0)*(model.y0_7_7 \
    - 1.0) + 0.5*(model.z0_7_7 - 1.0)*(model.z0_7_7 - 1.0) + 0.5*(model.y11_7_7 - 1.0)*(model.y11_7_7 \
    - 1.0) + 0.5*(model.z11_7_7 - 1.0)*(model.z11_7_7 - 1.0) + 0.5*(model.y0_8_7 - 1.0)*(model.y0_8_7 \
    - 1.0) + 0.5*(model.z0_8_7 - 1.0)*(model.z0_8_7 - 1.0) + 0.5*(model.y11_8_7 - 1.0)*(model.y11_8_7 \
    - 1.0) + 0.5*(model.z11_8_7 - 1.0)*(model.z11_8_7 - 1.0) + 0.5*(model.y0_9_7 - 1.0)*(model.y0_9_7 \
    - 1.0) + 0.5*(model.z0_9_7 - 1.0)*(model.z0_9_7 - 1.0) + 0.5*(model.y11_9_7 - 1.0)*(model.y11_9_7 \
    - 1.0) + 0.5*(model.z11_9_7 - 1.0)*(model.z11_9_7 - 1.0) + 0.5*(model.y0_10_7 - \
    1.0)*(model.y0_10_7 - 1.0) + 0.5*(model.z0_10_7 - 1.0)*(model.z0_10_7 - 1.0) + \
    0.5*(model.y11_10_7 - 1.0)*(model.y11_10_7 - 1.0) + 0.5*(model.z11_10_7 - 1.0)*(model.z11_10_7 - \
    1.0) + 0.5*(model.y0_1_8 - 1.0)*(model.y0_1_8 - 1.0) + 0.5*(model.z0_1_8 - 1.0)*(model.z0_1_8 - \
    1.0) + 0.5*(model.y11_1_8 - 1.0)*(model.y11_1_8 - 1.0) + 0.5*(model.z11_1_8 - 1.0)*(model.z11_1_8 \
    - 1.0) + 0.5*(model.y0_2_8 - 1.0)*(model.y0_2_8 - 1.0) + 0.5*(model.z0_2_8 - 1.0)*(model.z0_2_8 - \
    1.0) + 0.5*(model.y11_2_8 - 1.0)*(model.y11_2_8 - 1.0) + 0.5*(model.z11_2_8 - 1.0)*(model.z11_2_8 \
    - 1.0) + 0.5*(model.y0_3_8 - 1.0)*(model.y0_3_8 - 1.0) + 0.5*(model.z0_3_8 - 1.0)*(model.z0_3_8 - \
    1.0) + 0.5*(model.y11_3_8 - 1.0)*(model.y11_3_8 - 1.0) + 0.5*(model.z11_3_8 - 1.0)*(model.z11_3_8 \
    - 1.0) + 0.5*(model.y0_4_8 - 1.0)*(model.y0_4_8 - 1.0) + 0.5*(model.z0_4_8 - 1.0)*(model.z0_4_8 - \
    1.0) + 0.5*(model.y11_4_8 - 1.0)*(model.y11_4_8 - 1.0) + 0.5*(model.z11_4_8 - 1.0)*(model.z11_4_8 \
    - 1.0) + 0.5*(model.y0_5_8 - 1.0)*(model.y0_5_8 - 1.0) + 0.5*(model.z0_5_8 - 1.0)*(model.z0_5_8 - \
    1.0) + 0.5*(model.y11_5_8 - 1.0)*(model.y11_5_8 - 1.0) + 0.5*(model.z11_5_8 - 1.0)*(model.z11_5_8 \
    - 1.0) + 0.5*(model.y0_6_8 - 1.0)*(model.y0_6_8 - 1.0) + 0.5*(model.z0_6_8 - 1.0)*(model.z0_6_8 - \
    1.0) + 0.5*(model.y11_6_8 - 1.0)*(model.y11_6_8 - 1.0) + 0.5*(model.z11_6_8 - 1.0)*(model.z11_6_8 \
    - 1.0) + 0.5*(model.y0_7_8 - 1.0)*(model.y0_7_8 - 1.0) + 0.5*(model.z0_7_8 - 1.0)*(model.z0_7_8 - \
    1.0) + 0.5*(model.y11_7_8 - 1.0)*(model.y11_7_8 - 1.0) + 0.5*(model.z11_7_8 - 1.0)*(model.z11_7_8 \
    - 1.0) + 0.5*(model.y0_8_8 - 1.0)*(model.y0_8_8 - 1.0) + 0.5*(model.z0_8_8 - 1.0)*(model.z0_8_8 - \
    1.0) + 0.5*(model.y11_8_8 - 1.0)*(model.y11_8_8 - 1.0) + 0.5*(model.z11_8_8 - 1.0)*(model.z11_8_8 \
    - 1.0) + 0.5*(model.y0_9_8 - 1.0)*(model.y0_9_8 - 1.0) + 0.5*(model.z0_9_8 - 1.0)*(model.z0_9_8 - \
    1.0) + 0.5*(model.y11_9_8 - 1.0)*(model.y11_9_8 - 1.0) + 0.5*(model.z11_9_8 - 1.0)*(model.z11_9_8 \
    - 1.0) + 0.5*(model.y0_10_8 - 1.0)*(model.y0_10_8 - 1.0) + 0.5*(model.z0_10_8 - \
    1.0)*(model.z0_10_8 - 1.0) + 0.5*(model.y11_10_8 - 1.0)*(model.y11_10_8 - 1.0) + \
    0.5*(model.z11_10_8 - 1.0)*(model.z11_10_8 - 1.0) + 0.5*(model.y0_1_9 - 1.0)*(model.y0_1_9 - 1.0) \
    + 0.5*(model.z0_1_9 - 1.0)*(model.z0_1_9 - 1.0) + 0.5*(model.y11_1_9 - 1.0)*(model.y11_1_9 - 1.0) \
    + 0.5*(model.z11_1_9 - 1.0)*(model.z11_1_9 - 1.0) + 0.5*(model.y0_2_9 - 1.0)*(model.y0_2_9 - 1.0) \
    + 0.5*(model.z0_2_9 - 1.0)*(model.z0_2_9 - 1.0) + 0.5*(model.y11_2_9 - 1.0)*(model.y11_2_9 - 1.0) \
    + 0.5*(model.z11_2_9 - 1.0)*(model.z11_2_9 - 1.0) + 0.5*(model.y0_3_9 - 1.0)*(model.y0_3_9 - 1.0) \
    + 0.5*(model.z0_3_9 - 1.0)*(model.z0_3_9 - 1.0) + 0.5*(model.y11_3_9 - 1.0)*(model.y11_3_9 - 1.0) \
    + 0.5*(model.z11_3_9 - 1.0)*(model.z11_3_9 - 1.0) + 0.5*(model.y0_4_9 - 1.0)*(model.y0_4_9 - 1.0) \
    + 0.5*(model.z0_4_9 - 1.0)*(model.z0_4_9 - 1.0) + 0.5*(model.y11_4_9 - 1.0)*(model.y11_4_9 - 1.0) \
    + 0.5*(model.z11_4_9 - 1.0)*(model.z11_4_9 - 1.0) + 0.5*(model.y0_5_9 - 1.0)*(model.y0_5_9 - 1.0) \
    + 0.5*(model.z0_5_9 - 1.0)*(model.z0_5_9 - 1.0) + 0.5*(model.y11_5_9 - 1.0)*(model.y11_5_9 - 1.0) \
    + 0.5*(model.z11_5_9 - 1.0)*(model.z11_5_9 - 1.0) + 0.5*(model.y0_6_9 - 1.0)*(model.y0_6_9 - 1.0) \
    + 0.5*(model.z0_6_9 - 1.0)*(model.z0_6_9 - 1.0) + 0.5*(model.y11_6_9 - 1.0)*(model.y11_6_9 - 1.0) \
    + 0.5*(model.z11_6_9 - 1.0)*(model.z11_6_9 - 1.0) + 0.5*(model.y0_7_9 - 1.0)*(model.y0_7_9 - 1.0) \
    + 0.5*(model.z0_7_9 - 1.0)*(model.z0_7_9 - 1.0) + 0.5*(model.y11_7_9 - 1.0)*(model.y11_7_9 - 1.0) \
    + 0.5*(model.z11_7_9 - 1.0)*(model.z11_7_9 - 1.0) + 0.5*(model.y0_8_9 - 1.0)*(model.y0_8_9 - 1.0) \
    + 0.5*(model.z0_8_9 - 1.0)*(model.z0_8_9 - 1.0) + 0.5*(model.y11_8_9 - 1.0)*(model.y11_8_9 - 1.0) \
    + 0.5*(model.z11_8_9 - 1.0)*(model.z11_8_9 - 1.0) + 0.5*(model.y0_9_9 - 1.0)*(model.y0_9_9 - 1.0) \
    + 0.5*(model.z0_9_9 - 1.0)*(model.z0_9_9 - 1.0) + 0.5*(model.y11_9_9 - 1.0)*(model.y11_9_9 - 1.0) \
    + 0.5*(model.z11_9_9 - 1.0)*(model.z11_9_9 - 1.0) + 0.5*(model.y0_10_9 - 1.0)*(model.y0_10_9 - \
    1.0) + 0.5*(model.z0_10_9 - 1.0)*(model.z0_10_9 - 1.0) + 0.5*(model.y11_10_9 - \
    1.0)*(model.y11_10_9 - 1.0) + 0.5*(model.z11_10_9 - 1.0)*(model.z11_10_9 - 1.0) + \
    0.5*(model.y0_1_10 - 1.0)*(model.y0_1_10 - 1.0) + 0.5*(model.z0_1_10 - 1.0)*(model.z0_1_10 - 1.0) \
    + 0.5*(model.y11_1_10 - 1.0)*(model.y11_1_10 - 1.0) + 0.5*(model.z11_1_10 - 1.0)*(model.z11_1_10 \
    - 1.0) + 0.5*(model.y0_2_10 - 1.0)*(model.y0_2_10 - 1.0) + 0.5*(model.z0_2_10 - \
    1.0)*(model.z0_2_10 - 1.0) + 0.5*(model.y11_2_10 - 1.0)*(model.y11_2_10 - 1.0) + \
    0.5*(model.z11_2_10 - 1.0)*(model.z11_2_10 - 1.0) + 0.5*(model.y0_3_10 - 1.0)*(model.y0_3_10 - \
    1.0) + 0.5*(model.z0_3_10 - 1.0)*(model.z0_3_10 - 1.0) + 0.5*(model.y11_3_10 - \
    1.0)*(model.y11_3_10 - 1.0) + 0.5*(model.z11_3_10 - 1.0)*(model.z11_3_10 - 1.0) + \
    0.5*(model.y0_4_10 - 1.0)*(model.y0_4_10 - 1.0) + 0.5*(model.z0_4_10 - 1.0)*(model.z0_4_10 - 1.0) \
    + 0.5*(model.y11_4_10 - 1.0)*(model.y11_4_10 - 1.0) + 0.5*(model.z11_4_10 - 1.0)*(model.z11_4_10 \
    - 1.0) + 0.5*(model.y0_5_10 - 1.0)*(model.y0_5_10 - 1.0) + 0.5*(model.z0_5_10 - \
    1.0)*(model.z0_5_10 - 1.0) + 0.5*(model.y11_5_10 - 1.0)*(model.y11_5_10 - 1.0) + \
    0.5*(model.z11_5_10 - 1.0)*(model.z11_5_10 - 1.0) + 0.5*(model.y0_6_10 - 1.0)*(model.y0_6_10 - \
    1.0) + 0.5*(model.z0_6_10 - 1.0)*(model.z0_6_10 - 1.0) + 0.5*(model.y11_6_10 - \
    1.0)*(model.y11_6_10 - 1.0) + 0.5*(model.z11_6_10 - 1.0)*(model.z11_6_10 - 1.0) + \
    0.5*(model.y0_7_10 - 1.0)*(model.y0_7_10 - 1.0) + 0.5*(model.z0_7_10 - 1.0)*(model.z0_7_10 - 1.0) \
    + 0.5*(model.y11_7_10 - 1.0)*(model.y11_7_10 - 1.0) + 0.5*(model.z11_7_10 - 1.0)*(model.z11_7_10 \
    - 1.0) + 0.5*(model.y0_8_10 - 1.0)*(model.y0_8_10 - 1.0) + 0.5*(model.z0_8_10 - \
    1.0)*(model.z0_8_10 - 1.0) + 0.5*(model.y11_8_10 - 1.0)*(model.y11_8_10 - 1.0) + \
    0.5*(model.z11_8_10 - 1.0)*(model.z11_8_10 - 1.0) + 0.5*(model.y0_9_10 - 1.0)*(model.y0_9_10 - \
    1.0) + 0.5*(model.z0_9_10 - 1.0)*(model.z0_9_10 - 1.0) + 0.5*(model.y11_9_10 - \
    1.0)*(model.y11_9_10 - 1.0) + 0.5*(model.z11_9_10 - 1.0)*(model.z11_9_10 - 1.0) + \
    0.5*(model.y0_10_10 - 1.0)*(model.y0_10_10 - 1.0) + 0.5*(model.z0_10_10 - 1.0)*(model.z0_10_10 - \
    1.0) + 0.5*(model.y11_10_10 - 1.0)*(model.y11_10_10 - 1.0) + 0.5*(model.z11_10_10 - \
    1.0)*(model.z11_10_10 - 1.0) + 0.5*(model.x1_0_1 - 1.0)*(model.x1_0_1 - 1.0) + 0.5*(model.z1_0_1 \
    - 1.0)*(model.z1_0_1 - 1.0) + 0.5*(model.x1_11_1 - 1.0)*(model.x1_11_1 - 1.0) + \
    0.5*(model.z1_11_1 - 1.0)*(model.z1_11_1 - 1.0) + 0.5*(model.x2_0_1 - 1.0)*(model.x2_0_1 - 1.0) + \
    0.5*(model.z2_0_1 - 1.0)*(model.z2_0_1 - 1.0) + 0.5*(model.x2_11_1 - 1.0)*(model.x2_11_1 - 1.0) + \
    0.5*(model.z2_11_1 - 1.0)*(model.z2_11_1 - 1.0) + 0.5*(model.x3_0_1 - 1.0)*(model.x3_0_1 - 1.0) + \
    0.5*(model.z3_0_1 - 1.0)*(model.z3_0_1 - 1.0) + 0.5*(model.x3_11_1 - 1.0)*(model.x3_11_1 - 1.0) + \
    0.5*(model.z3_11_1 - 1.0)*(model.z3_11_1 - 1.0) + 0.5*(model.x4_0_1 - 1.0)*(model.x4_0_1 - 1.0) + \
    0.5*(model.z4_0_1 - 1.0)*(model.z4_0_1 - 1.0) + 0.5*(model.x4_11_1 - 1.0)*(model.x4_11_1 - 1.0) + \
    0.5*(model.z4_11_1 - 1.0)*(model.z4_11_1 - 1.0) + 0.5*(model.x5_0_1 - 1.0)*(model.x5_0_1 - 1.0) + \
    0.5*(model.z5_0_1 - 1.0)*(model.z5_0_1 - 1.0) + 0.5*(model.x5_11_1 - 1.0)*(model.x5_11_1 - 1.0) + \
    0.5*(model.z5_11_1 - 1.0)*(model.z5_11_1 - 1.0) + 0.5*(model.x6_0_1 - 1.0)*(model.x6_0_1 - 1.0) + \
    0.5*(model.z6_0_1 - 1.0)*(model.z6_0_1 - 1.0) + 0.5*(model.x6_11_1 - 1.0)*(model.x6_11_1 - 1.0) + \
    0.5*(model.z6_11_1 - 1.0)*(model.z6_11_1 - 1.0) + 0.5*(model.x7_0_1 - 1.0)*(model.x7_0_1 - 1.0) + \
    0.5*(model.z7_0_1 - 1.0)*(model.z7_0_1 - 1.0) + 0.5*(model.x7_11_1 - 1.0)*(model.x7_11_1 - 1.0) + \
    0.5*(model.z7_11_1 - 1.0)*(model.z7_11_1 - 1.0) + 0.5*(model.x8_0_1 - 1.0)*(model.x8_0_1 - 1.0) + \
    0.5*(model.z8_0_1 - 1.0)*(model.z8_0_1 - 1.0) + 0.5*(model.x8_11_1 - 1.0)*(model.x8_11_1 - 1.0) + \
    0.5*(model.z8_11_1 - 1.0)*(model.z8_11_1 - 1.0) + 0.5*(model.x9_0_1 - 1.0)*(model.x9_0_1 - 1.0) + \
    0.5*(model.z9_0_1 - 1.0)*(model.z9_0_1 - 1.0) + 0.5*(model.x9_11_1 - 1.0)*(model.x9_11_1 - 1.0) + \
    0.5*(model.z9_11_1 - 1.0)*(model.z9_11_1 - 1.0) + 0.5*(model.x10_0_1 - 1.0)*(model.x10_0_1 - 1.0) \
    + 0.5*(model.z10_0_1 - 1.0)*(model.z10_0_1 - 1.0) + 0.5*(model.x10_11_1 - 1.0)*(model.x10_11_1 - \
    1.0) + 0.5*(model.z10_11_1 - 1.0)*(model.z10_11_1 - 1.0) + 0.5*(model.x1_0_2 - 1.0)*(model.x1_0_2 \
    - 1.0) + 0.5*(model.z1_0_2 - 1.0)*(model.z1_0_2 - 1.0) + 0.5*(model.x1_11_2 - 1.0)*(model.x1_11_2 \
    - 1.0) + 0.5*(model.z1_11_2 - 1.0)*(model.z1_11_2 - 1.0) + 0.5*(model.x2_0_2 - 1.0)*(model.x2_0_2 \
    - 1.0) + 0.5*(model.z2_0_2 - 1.0)*(model.z2_0_2 - 1.0) + 0.5*(model.x2_11_2 - 1.0)*(model.x2_11_2 \
    - 1.0) + 0.5*(model.z2_11_2 - 1.0)*(model.z2_11_2 - 1.0) + 0.5*(model.x3_0_2 - 1.0)*(model.x3_0_2 \
    - 1.0) + 0.5*(model.z3_0_2 - 1.0)*(model.z3_0_2 - 1.0) + 0.5*(model.x3_11_2 - 1.0)*(model.x3_11_2 \
    - 1.0) + 0.5*(model.z3_11_2 - 1.0)*(model.z3_11_2 - 1.0) + 0.5*(model.x4_0_2 - 1.0)*(model.x4_0_2 \
    - 1.0) + 0.5*(model.z4_0_2 - 1.0)*(model.z4_0_2 - 1.0) + 0.5*(model.x4_11_2 - 1.0)*(model.x4_11_2 \
    - 1.0) + 0.5*(model.z4_11_2 - 1.0)*(model.z4_11_2 - 1.0) + 0.5*(model.x5_0_2 - 1.0)*(model.x5_0_2 \
    - 1.0) + 0.5*(model.z5_0_2 - 1.0)*(model.z5_0_2 - 1.0) + 0.5*(model.x5_11_2 - 1.0)*(model.x5_11_2 \
    - 1.0) + 0.5*(model.z5_11_2 - 1.0)*(model.z5_11_2 - 1.0) + 0.5*(model.x6_0_2 - 1.0)*(model.x6_0_2 \
    - 1.0) + 0.5*(model.z6_0_2 - 1.0)*(model.z6_0_2 - 1.0) + 0.5*(model.x6_11_2 - 1.0)*(model.x6_11_2 \
    - 1.0) + 0.5*(model.z6_11_2 - 1.0)*(model.z6_11_2 - 1.0) + 0.5*(model.x7_0_2 - 1.0)*(model.x7_0_2 \
    - 1.0) + 0.5*(model.z7_0_2 - 1.0)*(model.z7_0_2 - 1.0) + 0.5*(model.x7_11_2 - 1.0)*(model.x7_11_2 \
    - 1.0) + 0.5*(model.z7_11_2 - 1.0)*(model.z7_11_2 - 1.0) + 0.5*(model.x8_0_2 - 1.0)*(model.x8_0_2 \
    - 1.0) + 0.5*(model.z8_0_2 - 1.0)*(model.z8_0_2 - 1.0) + 0.5*(model.x8_11_2 - 1.0)*(model.x8_11_2 \
    - 1.0) + 0.5*(model.z8_11_2 - 1.0)*(model.z8_11_2 - 1.0) + 0.5*(model.x9_0_2 - 1.0)*(model.x9_0_2 \
    - 1.0) + 0.5*(model.z9_0_2 - 1.0)*(model.z9_0_2 - 1.0) + 0.5*(model.x9_11_2 - 1.0)*(model.x9_11_2 \
    - 1.0) + 0.5*(model.z9_11_2 - 1.0)*(model.z9_11_2 - 1.0) + 0.5*(model.x10_0_2 - \
    1.0)*(model.x10_0_2 - 1.0) + 0.5*(model.z10_0_2 - 1.0)*(model.z10_0_2 - 1.0) + \
    0.5*(model.x10_11_2 - 1.0)*(model.x10_11_2 - 1.0) + 0.5*(model.z10_11_2 - 1.0)*(model.z10_11_2 - \
    1.0) + 0.5*(model.x1_0_3 - 1.0)*(model.x1_0_3 - 1.0) + 0.5*(model.z1_0_3 - 1.0)*(model.z1_0_3 - \
    1.0) + 0.5*(model.x1_11_3 - 1.0)*(model.x1_11_3 - 1.0) + 0.5*(model.z1_11_3 - 1.0)*(model.z1_11_3 \
    - 1.0) + 0.5*(model.x2_0_3 - 1.0)*(model.x2_0_3 - 1.0) + 0.5*(model.z2_0_3 - 1.0)*(model.z2_0_3 - \
    1.0) + 0.5*(model.x2_11_3 - 1.0)*(model.x2_11_3 - 1.0) + 0.5*(model.z2_11_3 - 1.0)*(model.z2_11_3 \
    - 1.0) + 0.5*(model.x3_0_3 - 1.0)*(model.x3_0_3 - 1.0) + 0.5*(model.z3_0_3 - 1.0)*(model.z3_0_3 - \
    1.0) + 0.5*(model.x3_11_3 - 1.0)*(model.x3_11_3 - 1.0) + 0.5*(model.z3_11_3 - 1.0)*(model.z3_11_3 \
    - 1.0) + 0.5*(model.x4_0_3 - 1.0)*(model.x4_0_3 - 1.0) + 0.5*(model.z4_0_3 - 1.0)*(model.z4_0_3 - \
    1.0) + 0.5*(model.x4_11_3 - 1.0)*(model.x4_11_3 - 1.0) + 0.5*(model.z4_11_3 - 1.0)*(model.z4_11_3 \
    - 1.0) + 0.5*(model.x5_0_3 - 1.0)*(model.x5_0_3 - 1.0) + 0.5*(model.z5_0_3 - 1.0)*(model.z5_0_3 - \
    1.0) + 0.5*(model.x5_11_3 - 1.0)*(model.x5_11_3 - 1.0) + 0.5*(model.z5_11_3 - 1.0)*(model.z5_11_3 \
    - 1.0) + 0.5*(model.x6_0_3 - 1.0)*(model.x6_0_3 - 1.0) + 0.5*(model.z6_0_3 - 1.0)*(model.z6_0_3 - \
    1.0) + 0.5*(model.x6_11_3 - 1.0)*(model.x6_11_3 - 1.0) + 0.5*(model.z6_11_3 - 1.0)*(model.z6_11_3 \
    - 1.0) + 0.5*(model.x7_0_3 - 1.0)*(model.x7_0_3 - 1.0) + 0.5*(model.z7_0_3 - 1.0)*(model.z7_0_3 - \
    1.0) + 0.5*(model.x7_11_3 - 1.0)*(model.x7_11_3 - 1.0) + 0.5*(model.z7_11_3 - 1.0)*(model.z7_11_3 \
    - 1.0) + 0.5*(model.x8_0_3 - 1.0)*(model.x8_0_3 - 1.0) + 0.5*(model.z8_0_3 - 1.0)*(model.z8_0_3 - \
    1.0) + 0.5*(model.x8_11_3 - 1.0)*(model.x8_11_3 - 1.0) + 0.5*(model.z8_11_3 - 1.0)*(model.z8_11_3 \
    - 1.0) + 0.5*(model.x9_0_3 - 1.0)*(model.x9_0_3 - 1.0) + 0.5*(model.z9_0_3 - 1.0)*(model.z9_0_3 - \
    1.0) + 0.5*(model.x9_11_3 - 1.0)*(model.x9_11_3 - 1.0) + 0.5*(model.z9_11_3 - 1.0)*(model.z9_11_3 \
    - 1.0) + 0.5*(model.x10_0_3 - 1.0)*(model.x10_0_3 - 1.0) + 0.5*(model.z10_0_3 - \
    1.0)*(model.z10_0_3 - 1.0) + 0.5*(model.x10_11_3 - 1.0)*(model.x10_11_3 - 1.0) + \
    0.5*(model.z10_11_3 - 1.0)*(model.z10_11_3 - 1.0) + 0.5*(model.x1_0_4 - 1.0)*(model.x1_0_4 - 1.0) \
    + 0.5*(model.z1_0_4 - 1.0)*(model.z1_0_4 - 1.0) + 0.5*(model.x1_11_4 - 1.0)*(model.x1_11_4 - 1.0) \
    + 0.5*(model.z1_11_4 - 1.0)*(model.z1_11_4 - 1.0) + 0.5*(model.x2_0_4 - 1.0)*(model.x2_0_4 - 1.0) \
    + 0.5*(model.z2_0_4 - 1.0)*(model.z2_0_4 - 1.0) + 0.5*(model.x2_11_4 - 1.0)*(model.x2_11_4 - 1.0) \
    + 0.5*(model.z2_11_4 - 1.0)*(model.z2_11_4 - 1.0) + 0.5*(model.x3_0_4 - 1.0)*(model.x3_0_4 - 1.0) \
    + 0.5*(model.z3_0_4 - 1.0)*(model.z3_0_4 - 1.0) + 0.5*(model.x3_11_4 - 1.0)*(model.x3_11_4 - 1.0) \
    + 0.5*(model.z3_11_4 - 1.0)*(model.z3_11_4 - 1.0) + 0.5*(model.x4_0_4 - 1.0)*(model.x4_0_4 - 1.0) \
    + 0.5*(model.z4_0_4 - 1.0)*(model.z4_0_4 - 1.0) + 0.5*(model.x4_11_4 - 1.0)*(model.x4_11_4 - 1.0) \
    + 0.5*(model.z4_11_4 - 1.0)*(model.z4_11_4 - 1.0) + 0.5*(model.x5_0_4 - 1.0)*(model.x5_0_4 - 1.0) \
    + 0.5*(model.z5_0_4 - 1.0)*(model.z5_0_4 - 1.0) + 0.5*(model.x5_11_4 - 1.0)*(model.x5_11_4 - 1.0) \
    + 0.5*(model.z5_11_4 - 1.0)*(model.z5_11_4 - 1.0) + 0.5*(model.x6_0_4 - 1.0)*(model.x6_0_4 - 1.0) \
    + 0.5*(model.z6_0_4 - 1.0)*(model.z6_0_4 - 1.0) + 0.5*(model.x6_11_4 - 1.0)*(model.x6_11_4 - 1.0) \
    + 0.5*(model.z6_11_4 - 1.0)*(model.z6_11_4 - 1.0) + 0.5*(model.x7_0_4 - 1.0)*(model.x7_0_4 - 1.0) \
    + 0.5*(model.z7_0_4 - 1.0)*(model.z7_0_4 - 1.0) + 0.5*(model.x7_11_4 - 1.0)*(model.x7_11_4 - 1.0) \
    + 0.5*(model.z7_11_4 - 1.0)*(model.z7_11_4 - 1.0) + 0.5*(model.x8_0_4 - 1.0)*(model.x8_0_4 - 1.0) \
    + 0.5*(model.z8_0_4 - 1.0)*(model.z8_0_4 - 1.0) + 0.5*(model.x8_11_4 - 1.0)*(model.x8_11_4 - 1.0) \
    + 0.5*(model.z8_11_4 - 1.0)*(model.z8_11_4 - 1.0) + 0.5*(model.x9_0_4 - 1.0)*(model.x9_0_4 - 1.0) \
    + 0.5*(model.z9_0_4 - 1.0)*(model.z9_0_4 - 1.0) + 0.5*(model.x9_11_4 - 1.0)*(model.x9_11_4 - 1.0) \
    + 0.5*(model.z9_11_4 - 1.0)*(model.z9_11_4 - 1.0) + 0.5*(model.x10_0_4 - 1.0)*(model.x10_0_4 - \
    1.0) + 0.5*(model.z10_0_4 - 1.0)*(model.z10_0_4 - 1.0) + 0.5*(model.x10_11_4 - \
    1.0)*(model.x10_11_4 - 1.0) + 0.5*(model.z10_11_4 - 1.0)*(model.z10_11_4 - 1.0) + \
    0.5*(model.x1_0_5 - 1.0)*(model.x1_0_5 - 1.0) + 0.5*(model.z1_0_5 - 1.0)*(model.z1_0_5 - 1.0) + \
    0.5*(model.x1_11_5 - 1.0)*(model.x1_11_5 - 1.0) + 0.5*(model.z1_11_5 - 1.0)*(model.z1_11_5 - 1.0) \
    + 0.5*(model.x2_0_5 - 1.0)*(model.x2_0_5 - 1.0) + 0.5*(model.z2_0_5 - 1.0)*(model.z2_0_5 - 1.0) + \
    0.5*(model.x2_11_5 - 1.0)*(model.x2_11_5 - 1.0) + 0.5*(model.z2_11_5 - 1.0)*(model.z2_11_5 - 1.0) \
    + 0.5*(model.x3_0_5 - 1.0)*(model.x3_0_5 - 1.0) + 0.5*(model.z3_0_5 - 1.0)*(model.z3_0_5 - 1.0) + \
    0.5*(model.x3_11_5 - 1.0)*(model.x3_11_5 - 1.0) + 0.5*(model.z3_11_5 - 1.0)*(model.z3_11_5 - 1.0) \
    + 0.5*(model.x4_0_5 - 1.0)*(model.x4_0_5 - 1.0) + 0.5*(model.z4_0_5 - 1.0)*(model.z4_0_5 - 1.0) + \
    0.5*(model.x4_11_5 - 1.0)*(model.x4_11_5 - 1.0) + 0.5*(model.z4_11_5 - 1.0)*(model.z4_11_5 - 1.0) \
    + 0.5*(model.x5_0_5 - 1.0)*(model.x5_0_5 - 1.0) + 0.5*(model.z5_0_5 - 1.0)*(model.z5_0_5 - 1.0) + \
    0.5*(model.x5_11_5 - 1.0)*(model.x5_11_5 - 1.0) + 0.5*(model.z5_11_5 - 1.0)*(model.z5_11_5 - 1.0) \
    + 0.5*(model.x6_0_5 - 1.0)*(model.x6_0_5 - 1.0) + 0.5*(model.z6_0_5 - 1.0)*(model.z6_0_5 - 1.0) + \
    0.5*(model.x6_11_5 - 1.0)*(model.x6_11_5 - 1.0) + 0.5*(model.z6_11_5 - 1.0)*(model.z6_11_5 - 1.0) \
    + 0.5*(model.x7_0_5 - 1.0)*(model.x7_0_5 - 1.0) + 0.5*(model.z7_0_5 - 1.0)*(model.z7_0_5 - 1.0) + \
    0.5*(model.x7_11_5 - 1.0)*(model.x7_11_5 - 1.0) + 0.5*(model.z7_11_5 - 1.0)*(model.z7_11_5 - 1.0) \
    + 0.5*(model.x8_0_5 - 1.0)*(model.x8_0_5 - 1.0) + 0.5*(model.z8_0_5 - 1.0)*(model.z8_0_5 - 1.0) + \
    0.5*(model.x8_11_5 - 1.0)*(model.x8_11_5 - 1.0) + 0.5*(model.z8_11_5 - 1.0)*(model.z8_11_5 - 1.0) \
    + 0.5*(model.x9_0_5 - 1.0)*(model.x9_0_5 - 1.0) + 0.5*(model.z9_0_5 - 1.0)*(model.z9_0_5 - 1.0) + \
    0.5*(model.x9_11_5 - 1.0)*(model.x9_11_5 - 1.0) + 0.5*(model.z9_11_5 - 1.0)*(model.z9_11_5 - 1.0) \
    + 0.5*(model.x10_0_5 - 1.0)*(model.x10_0_5 - 1.0) + 0.5*(model.z10_0_5 - 1.0)*(model.z10_0_5 - \
    1.0) + 0.5*(model.x10_11_5 - 1.0)*(model.x10_11_5 - 1.0) + 0.5*(model.z10_11_5 - \
    1.0)*(model.z10_11_5 - 1.0) + 0.5*(model.x1_0_6 - 1.0)*(model.x1_0_6 - 1.0) + 0.5*(model.z1_0_6 - \
    1.0)*(model.z1_0_6 - 1.0) + 0.5*(model.x1_11_6 - 1.0)*(model.x1_11_6 - 1.0) + 0.5*(model.z1_11_6 \
    - 1.0)*(model.z1_11_6 - 1.0) + 0.5*(model.x2_0_6 - 1.0)*(model.x2_0_6 - 1.0) + 0.5*(model.z2_0_6 \
    - 1.0)*(model.z2_0_6 - 1.0) + 0.5*(model.x2_11_6 - 1.0)*(model.x2_11_6 - 1.0) + \
    0.5*(model.z2_11_6 - 1.0)*(model.z2_11_6 - 1.0) + 0.5*(model.x3_0_6 - 1.0)*(model.x3_0_6 - 1.0) + \
    0.5*(model.z3_0_6 - 1.0)*(model.z3_0_6 - 1.0) + 0.5*(model.x3_11_6 - 1.0)*(model.x3_11_6 - 1.0) + \
    0.5*(model.z3_11_6 - 1.0)*(model.z3_11_6 - 1.0) + 0.5*(model.x4_0_6 - 1.0)*(model.x4_0_6 - 1.0) + \
    0.5*(model.z4_0_6 - 1.0)*(model.z4_0_6 - 1.0) + 0.5*(model.x4_11_6 - 1.0)*(model.x4_11_6 - 1.0) + \
    0.5*(model.z4_11_6 - 1.0)*(model.z4_11_6 - 1.0) + 0.5*(model.x5_0_6 - 1.0)*(model.x5_0_6 - 1.0) + \
    0.5*(model.z5_0_6 - 1.0)*(model.z5_0_6 - 1.0) + 0.5*(model.x5_11_6 - 1.0)*(model.x5_11_6 - 1.0) + \
    0.5*(model.z5_11_6 - 1.0)*(model.z5_11_6 - 1.0) + 0.5*(model.x6_0_6 - 1.0)*(model.x6_0_6 - 1.0) + \
    0.5*(model.z6_0_6 - 1.0)*(model.z6_0_6 - 1.0) + 0.5*(model.x6_11_6 - 1.0)*(model.x6_11_6 - 1.0) + \
    0.5*(model.z6_11_6 - 1.0)*(model.z6_11_6 - 1.0) + 0.5*(model.x7_0_6 - 1.0)*(model.x7_0_6 - 1.0) + \
    0.5*(model.z7_0_6 - 1.0)*(model.z7_0_6 - 1.0) + 0.5*(model.x7_11_6 - 1.0)*(model.x7_11_6 - 1.0) + \
    0.5*(model.z7_11_6 - 1.0)*(model.z7_11_6 - 1.0) + 0.5*(model.x8_0_6 - 1.0)*(model.x8_0_6 - 1.0) + \
    0.5*(model.z8_0_6 - 1.0)*(model.z8_0_6 - 1.0) + 0.5*(model.x8_11_6 - 1.0)*(model.x8_11_6 - 1.0) + \
    0.5*(model.z8_11_6 - 1.0)*(model.z8_11_6 - 1.0) + 0.5*(model.x9_0_6 - 1.0)*(model.x9_0_6 - 1.0) + \
    0.5*(model.z9_0_6 - 1.0)*(model.z9_0_6 - 1.0) + 0.5*(model.x9_11_6 - 1.0)*(model.x9_11_6 - 1.0) + \
    0.5*(model.z9_11_6 - 1.0)*(model.z9_11_6 - 1.0) + 0.5*(model.x10_0_6 - 1.0)*(model.x10_0_6 - 1.0) \
    + 0.5*(model.z10_0_6 - 1.0)*(model.z10_0_6 - 1.0) + 0.5*(model.x10_11_6 - 1.0)*(model.x10_11_6 - \
    1.0) + 0.5*(model.z10_11_6 - 1.0)*(model.z10_11_6 - 1.0) + 0.5*(model.x1_0_7 - 1.0)*(model.x1_0_7 \
    - 1.0) + 0.5*(model.z1_0_7 - 1.0)*(model.z1_0_7 - 1.0) + 0.5*(model.x1_11_7 - 1.0)*(model.x1_11_7 \
    - 1.0) + 0.5*(model.z1_11_7 - 1.0)*(model.z1_11_7 - 1.0) + 0.5*(model.x2_0_7 - 1.0)*(model.x2_0_7 \
    - 1.0) + 0.5*(model.z2_0_7 - 1.0)*(model.z2_0_7 - 1.0) + 0.5*(model.x2_11_7 - 1.0)*(model.x2_11_7 \
    - 1.0) + 0.5*(model.z2_11_7 - 1.0)*(model.z2_11_7 - 1.0) + 0.5*(model.x3_0_7 - 1.0)*(model.x3_0_7 \
    - 1.0) + 0.5*(model.z3_0_7 - 1.0)*(model.z3_0_7 - 1.0) + 0.5*(model.x3_11_7 - 1.0)*(model.x3_11_7 \
    - 1.0) + 0.5*(model.z3_11_7 - 1.0)*(model.z3_11_7 - 1.0) + 0.5*(model.x4_0_7 - 1.0)*(model.x4_0_7 \
    - 1.0) + 0.5*(model.z4_0_7 - 1.0)*(model.z4_0_7 - 1.0) + 0.5*(model.x4_11_7 - 1.0)*(model.x4_11_7 \
    - 1.0) + 0.5*(model.z4_11_7 - 1.0)*(model.z4_11_7 - 1.0) + 0.5*(model.x5_0_7 - 1.0)*(model.x5_0_7 \
    - 1.0) + 0.5*(model.z5_0_7 - 1.0)*(model.z5_0_7 - 1.0) + 0.5*(model.x5_11_7 - 1.0)*(model.x5_11_7 \
    - 1.0) + 0.5*(model.z5_11_7 - 1.0)*(model.z5_11_7 - 1.0) + 0.5*(model.x6_0_7 - 1.0)*(model.x6_0_7 \
    - 1.0) + 0.5*(model.z6_0_7 - 1.0)*(model.z6_0_7 - 1.0) + 0.5*(model.x6_11_7 - 1.0)*(model.x6_11_7 \
    - 1.0) + 0.5*(model.z6_11_7 - 1.0)*(model.z6_11_7 - 1.0) + 0.5*(model.x7_0_7 - 1.0)*(model.x7_0_7 \
    - 1.0) + 0.5*(model.z7_0_7 - 1.0)*(model.z7_0_7 - 1.0) + 0.5*(model.x7_11_7 - 1.0)*(model.x7_11_7 \
    - 1.0) + 0.5*(model.z7_11_7 - 1.0)*(model.z7_11_7 - 1.0) + 0.5*(model.x8_0_7 - 1.0)*(model.x8_0_7 \
    - 1.0) + 0.5*(model.z8_0_7 - 1.0)*(model.z8_0_7 - 1.0) + 0.5*(model.x8_11_7 - 1.0)*(model.x8_11_7 \
    - 1.0) + 0.5*(model.z8_11_7 - 1.0)*(model.z8_11_7 - 1.0) + 0.5*(model.x9_0_7 - 1.0)*(model.x9_0_7 \
    - 1.0) + 0.5*(model.z9_0_7 - 1.0)*(model.z9_0_7 - 1.0) + 0.5*(model.x9_11_7 - 1.0)*(model.x9_11_7 \
    - 1.0) + 0.5*(model.z9_11_7 - 1.0)*(model.z9_11_7 - 1.0) + 0.5*(model.x10_0_7 - \
    1.0)*(model.x10_0_7 - 1.0) + 0.5*(model.z10_0_7 - 1.0)*(model.z10_0_7 - 1.0) + \
    0.5*(model.x10_11_7 - 1.0)*(model.x10_11_7 - 1.0) + 0.5*(model.z10_11_7 - 1.0)*(model.z10_11_7 - \
    1.0) + 0.5*(model.x1_0_8 - 1.0)*(model.x1_0_8 - 1.0) + 0.5*(model.z1_0_8 - 1.0)*(model.z1_0_8 - \
    1.0) + 0.5*(model.x1_11_8 - 1.0)*(model.x1_11_8 - 1.0) + 0.5*(model.z1_11_8 - 1.0)*(model.z1_11_8 \
    - 1.0) + 0.5*(model.x2_0_8 - 1.0)*(model.x2_0_8 - 1.0) + 0.5*(model.z2_0_8 - 1.0)*(model.z2_0_8 - \
    1.0) + 0.5*(model.x2_11_8 - 1.0)*(model.x2_11_8 - 1.0) + 0.5*(model.z2_11_8 - 1.0)*(model.z2_11_8 \
    - 1.0) + 0.5*(model.x3_0_8 - 1.0)*(model.x3_0_8 - 1.0) + 0.5*(model.z3_0_8 - 1.0)*(model.z3_0_8 - \
    1.0) + 0.5*(model.x3_11_8 - 1.0)*(model.x3_11_8 - 1.0) + 0.5*(model.z3_11_8 - 1.0)*(model.z3_11_8 \
    - 1.0) + 0.5*(model.x4_0_8 - 1.0)*(model.x4_0_8 - 1.0) + 0.5*(model.z4_0_8 - 1.0)*(model.z4_0_8 - \
    1.0) + 0.5*(model.x4_11_8 - 1.0)*(model.x4_11_8 - 1.0) + 0.5*(model.z4_11_8 - 1.0)*(model.z4_11_8 \
    - 1.0) + 0.5*(model.x5_0_8 - 1.0)*(model.x5_0_8 - 1.0) + 0.5*(model.z5_0_8 - 1.0)*(model.z5_0_8 - \
    1.0) + 0.5*(model.x5_11_8 - 1.0)*(model.x5_11_8 - 1.0) + 0.5*(model.z5_11_8 - 1.0)*(model.z5_11_8 \
    - 1.0) + 0.5*(model.x6_0_8 - 1.0)*(model.x6_0_8 - 1.0) + 0.5*(model.z6_0_8 - 1.0)*(model.z6_0_8 - \
    1.0) + 0.5*(model.x6_11_8 - 1.0)*(model.x6_11_8 - 1.0) + 0.5*(model.z6_11_8 - 1.0)*(model.z6_11_8 \
    - 1.0) + 0.5*(model.x7_0_8 - 1.0)*(model.x7_0_8 - 1.0) + 0.5*(model.z7_0_8 - 1.0)*(model.z7_0_8 - \
    1.0) + 0.5*(model.x7_11_8 - 1.0)*(model.x7_11_8 - 1.0) + 0.5*(model.z7_11_8 - 1.0)*(model.z7_11_8 \
    - 1.0) + 0.5*(model.x8_0_8 - 1.0)*(model.x8_0_8 - 1.0) + 0.5*(model.z8_0_8 - 1.0)*(model.z8_0_8 - \
    1.0) + 0.5*(model.x8_11_8 - 1.0)*(model.x8_11_8 - 1.0) + 0.5*(model.z8_11_8 - 1.0)*(model.z8_11_8 \
    - 1.0) + 0.5*(model.x9_0_8 - 1.0)*(model.x9_0_8 - 1.0) + 0.5*(model.z9_0_8 - 1.0)*(model.z9_0_8 - \
    1.0) + 0.5*(model.x9_11_8 - 1.0)*(model.x9_11_8 - 1.0) + 0.5*(model.z9_11_8 - 1.0)*(model.z9_11_8 \
    - 1.0) + 0.5*(model.x10_0_8 - 1.0)*(model.x10_0_8 - 1.0) + 0.5*(model.z10_0_8 - \
    1.0)*(model.z10_0_8 - 1.0) + 0.5*(model.x10_11_8 - 1.0)*(model.x10_11_8 - 1.0) + \
    0.5*(model.z10_11_8 - 1.0)*(model.z10_11_8 - 1.0) + 0.5*(model.x1_0_9 - 1.0)*(model.x1_0_9 - 1.0) \
    + 0.5*(model.z1_0_9 - 1.0)*(model.z1_0_9 - 1.0) + 0.5*(model.x1_11_9 - 1.0)*(model.x1_11_9 - 1.0) \
    + 0.5*(model.z1_11_9 - 1.0)*(model.z1_11_9 - 1.0) + 0.5*(model.x2_0_9 - 1.0)*(model.x2_0_9 - 1.0) \
    + 0.5*(model.z2_0_9 - 1.0)*(model.z2_0_9 - 1.0) + 0.5*(model.x2_11_9 - 1.0)*(model.x2_11_9 - 1.0) \
    + 0.5*(model.z2_11_9 - 1.0)*(model.z2_11_9 - 1.0) + 0.5*(model.x3_0_9 - 1.0)*(model.x3_0_9 - 1.0) \
    + 0.5*(model.z3_0_9 - 1.0)*(model.z3_0_9 - 1.0) + 0.5*(model.x3_11_9 - 1.0)*(model.x3_11_9 - 1.0) \
    + 0.5*(model.z3_11_9 - 1.0)*(model.z3_11_9 - 1.0) + 0.5*(model.x4_0_9 - 1.0)*(model.x4_0_9 - 1.0) \
    + 0.5*(model.z4_0_9 - 1.0)*(model.z4_0_9 - 1.0) + 0.5*(model.x4_11_9 - 1.0)*(model.x4_11_9 - 1.0) \
    + 0.5*(model.z4_11_9 - 1.0)*(model.z4_11_9 - 1.0) + 0.5*(model.x5_0_9 - 1.0)*(model.x5_0_9 - 1.0) \
    + 0.5*(model.z5_0_9 - 1.0)*(model.z5_0_9 - 1.0) + 0.5*(model.x5_11_9 - 1.0)*(model.x5_11_9 - 1.0) \
    + 0.5*(model.z5_11_9 - 1.0)*(model.z5_11_9 - 1.0) + 0.5*(model.x6_0_9 - 1.0)*(model.x6_0_9 - 1.0) \
    + 0.5*(model.z6_0_9 - 1.0)*(model.z6_0_9 - 1.0) + 0.5*(model.x6_11_9 - 1.0)*(model.x6_11_9 - 1.0) \
    + 0.5*(model.z6_11_9 - 1.0)*(model.z6_11_9 - 1.0) + 0.5*(model.x7_0_9 - 1.0)*(model.x7_0_9 - 1.0) \
    + 0.5*(model.z7_0_9 - 1.0)*(model.z7_0_9 - 1.0) + 0.5*(model.x7_11_9 - 1.0)*(model.x7_11_9 - 1.0) \
    + 0.5*(model.z7_11_9 - 1.0)*(model.z7_11_9 - 1.0) + 0.5*(model.x8_0_9 - 1.0)*(model.x8_0_9 - 1.0) \
    + 0.5*(model.z8_0_9 - 1.0)*(model.z8_0_9 - 1.0) + 0.5*(model.x8_11_9 - 1.0)*(model.x8_11_9 - 1.0) \
    + 0.5*(model.z8_11_9 - 1.0)*(model.z8_11_9 - 1.0) + 0.5*(model.x9_0_9 - 1.0)*(model.x9_0_9 - 1.0) \
    + 0.5*(model.z9_0_9 - 1.0)*(model.z9_0_9 - 1.0) + 0.5*(model.x9_11_9 - 1.0)*(model.x9_11_9 - 1.0) \
    + 0.5*(model.z9_11_9 - 1.0)*(model.z9_11_9 - 1.0) + 0.5*(model.x10_0_9 - 1.0)*(model.x10_0_9 - \
    1.0) + 0.5*(model.z10_0_9 - 1.0)*(model.z10_0_9 - 1.0) + 0.5*(model.x10_11_9 - \
    1.0)*(model.x10_11_9 - 1.0) + 0.5*(model.z10_11_9 - 1.0)*(model.z10_11_9 - 1.0) + \
    0.5*(model.x1_0_10 - 1.0)*(model.x1_0_10 - 1.0) + 0.5*(model.z1_0_10 - 1.0)*(model.z1_0_10 - 1.0) \
    + 0.5*(model.x1_11_10 - 1.0)*(model.x1_11_10 - 1.0) + 0.5*(model.z1_11_10 - 1.0)*(model.z1_11_10 \
    - 1.0) + 0.5*(model.x2_0_10 - 1.0)*(model.x2_0_10 - 1.0) + 0.5*(model.z2_0_10 - \
    1.0)*(model.z2_0_10 - 1.0) + 0.5*(model.x2_11_10 - 1.0)*(model.x2_11_10 - 1.0) + \
    0.5*(model.z2_11_10 - 1.0)*(model.z2_11_10 - 1.0) + 0.5*(model.x3_0_10 - 1.0)*(model.x3_0_10 - \
    1.0) + 0.5*(model.z3_0_10 - 1.0)*(model.z3_0_10 - 1.0) + 0.5*(model.x3_11_10 - \
    1.0)*(model.x3_11_10 - 1.0) + 0.5*(model.z3_11_10 - 1.0)*(model.z3_11_10 - 1.0) + \
    0.5*(model.x4_0_10 - 1.0)*(model.x4_0_10 - 1.0) + 0.5*(model.z4_0_10 - 1.0)*(model.z4_0_10 - 1.0) \
    + 0.5*(model.x4_11_10 - 1.0)*(model.x4_11_10 - 1.0) + 0.5*(model.z4_11_10 - 1.0)*(model.z4_11_10 \
    - 1.0) + 0.5*(model.x5_0_10 - 1.0)*(model.x5_0_10 - 1.0) + 0.5*(model.z5_0_10 - \
    1.0)*(model.z5_0_10 - 1.0) + 0.5*(model.x5_11_10 - 1.0)*(model.x5_11_10 - 1.0) + \
    0.5*(model.z5_11_10 - 1.0)*(model.z5_11_10 - 1.0) + 0.5*(model.x6_0_10 - 1.0)*(model.x6_0_10 - \
    1.0) + 0.5*(model.z6_0_10 - 1.0)*(model.z6_0_10 - 1.0) + 0.5*(model.x6_11_10 - \
    1.0)*(model.x6_11_10 - 1.0) + 0.5*(model.z6_11_10 - 1.0)*(model.z6_11_10 - 1.0) + \
    0.5*(model.x7_0_10 - 1.0)*(model.x7_0_10 - 1.0) + 0.5*(model.z7_0_10 - 1.0)*(model.z7_0_10 - 1.0) \
    + 0.5*(model.x7_11_10 - 1.0)*(model.x7_11_10 - 1.0) + 0.5*(model.z7_11_10 - 1.0)*(model.z7_11_10 \
    - 1.0) + 0.5*(model.x8_0_10 - 1.0)*(model.x8_0_10 - 1.0) + 0.5*(model.z8_0_10 - \
    1.0)*(model.z8_0_10 - 1.0) + 0.5*(model.x8_11_10 - 1.0)*(model.x8_11_10 - 1.0) + \
    0.5*(model.z8_11_10 - 1.0)*(model.z8_11_10 - 1.0) + 0.5*(model.x9_0_10 - 1.0)*(model.x9_0_10 - \
    1.0) + 0.5*(model.z9_0_10 - 1.0)*(model.z9_0_10 - 1.0) + 0.5*(model.x9_11_10 - \
    1.0)*(model.x9_11_10 - 1.0) + 0.5*(model.z9_11_10 - 1.0)*(model.z9_11_10 - 1.0) + \
    0.5*(model.x10_0_10 - 1.0)*(model.x10_0_10 - 1.0) + 0.5*(model.z10_0_10 - 1.0)*(model.z10_0_10 - \
    1.0) + 0.5*(model.x10_11_10 - 1.0)*(model.x10_11_10 - 1.0) + 0.5*(model.z10_11_10 - \
    1.0)*(model.z10_11_10 - 1.0) + 0.5*(model.x1_1_0 - 1.0)*(model.x1_1_0 - 1.0) + 0.5*(model.y1_1_0 \
    - 1.0)*(model.y1_1_0 - 1.0) + 0.5*(model.x1_1_11 - 1.0)*(model.x1_1_11 - 1.0) + \
    0.5*(model.y1_1_11 - 1.0)*(model.y1_1_11 - 1.0) + 0.5*(model.x2_1_0 - 1.0)*(model.x2_1_0 - 1.0) + \
    0.5*(model.y2_1_0 - 1.0)*(model.y2_1_0 - 1.0) + 0.5*(model.x2_1_11 - 1.0)*(model.x2_1_11 - 1.0) + \
    0.5*(model.y2_1_11 - 1.0)*(model.y2_1_11 - 1.0) + 0.5*(model.x3_1_0 - 1.0)*(model.x3_1_0 - 1.0) + \
    0.5*(model.y3_1_0 - 1.0)*(model.y3_1_0 - 1.0) + 0.5*(model.x3_1_11 - 1.0)*(model.x3_1_11 - 1.0) + \
    0.5*(model.y3_1_11 - 1.0)*(model.y3_1_11 - 1.0) + 0.5*(model.x4_1_0 - 1.0)*(model.x4_1_0 - 1.0) + \
    0.5*(model.y4_1_0 - 1.0)*(model.y4_1_0 - 1.0) + 0.5*(model.x4_1_11 - 1.0)*(model.x4_1_11 - 1.0) + \
    0.5*(model.y4_1_11 - 1.0)*(model.y4_1_11 - 1.0) + 0.5*(model.x5_1_0 - 1.0)*(model.x5_1_0 - 1.0) + \
    0.5*(model.y5_1_0 - 1.0)*(model.y5_1_0 - 1.0) + 0.5*(model.x5_1_11 - 1.0)*(model.x5_1_11 - 1.0) + \
    0.5*(model.y5_1_11 - 1.0)*(model.y5_1_11 - 1.0) + 0.5*(model.x6_1_0 - 1.0)*(model.x6_1_0 - 1.0) + \
    0.5*(model.y6_1_0 - 1.0)*(model.y6_1_0 - 1.0) + 0.5*(model.x6_1_11 - 1.0)*(model.x6_1_11 - 1.0) + \
    0.5*(model.y6_1_11 - 1.0)*(model.y6_1_11 - 1.0) + 0.5*(model.x7_1_0 - 1.0)*(model.x7_1_0 - 1.0) + \
    0.5*(model.y7_1_0 - 1.0)*(model.y7_1_0 - 1.0) + 0.5*(model.x7_1_11 - 1.0)*(model.x7_1_11 - 1.0) + \
    0.5*(model.y7_1_11 - 1.0)*(model.y7_1_11 - 1.0) + 0.5*(model.x8_1_0 - 1.0)*(model.x8_1_0 - 1.0) + \
    0.5*(model.y8_1_0 - 1.0)*(model.y8_1_0 - 1.0) + 0.5*(model.x8_1_11 - 1.0)*(model.x8_1_11 - 1.0) + \
    0.5*(model.y8_1_11 - 1.0)*(model.y8_1_11 - 1.0) + 0.5*(model.x9_1_0 - 1.0)*(model.x9_1_0 - 1.0) + \
    0.5*(model.y9_1_0 - 1.0)*(model.y9_1_0 - 1.0) + 0.5*(model.x9_1_11 - 1.0)*(model.x9_1_11 - 1.0) + \
    0.5*(model.y9_1_11 - 1.0)*(model.y9_1_11 - 1.0) + 0.5*(model.x10_1_0 - 1.0)*(model.x10_1_0 - 1.0) \
    + 0.5*(model.y10_1_0 - 1.0)*(model.y10_1_0 - 1.0) + 0.5*(model.x10_1_11 - 1.0)*(model.x10_1_11 - \
    1.0) + 0.5*(model.y10_1_11 - 1.0)*(model.y10_1_11 - 1.0) + 0.5*(model.x1_2_0 - 1.0)*(model.x1_2_0 \
    - 1.0) + 0.5*(model.y1_2_0 - 1.0)*(model.y1_2_0 - 1.0) + 0.5*(model.x1_2_11 - 1.0)*(model.x1_2_11 \
    - 1.0) + 0.5*(model.y1_2_11 - 1.0)*(model.y1_2_11 - 1.0) + 0.5*(model.x2_2_0 - 1.0)*(model.x2_2_0 \
    - 1.0) + 0.5*(model.y2_2_0 - 1.0)*(model.y2_2_0 - 1.0) + 0.5*(model.x2_2_11 - 1.0)*(model.x2_2_11 \
    - 1.0) + 0.5*(model.y2_2_11 - 1.0)*(model.y2_2_11 - 1.0) + 0.5*(model.x3_2_0 - 1.0)*(model.x3_2_0 \
    - 1.0) + 0.5*(model.y3_2_0 - 1.0)*(model.y3_2_0 - 1.0) + 0.5*(model.x3_2_11 - 1.0)*(model.x3_2_11 \
    - 1.0) + 0.5*(model.y3_2_11 - 1.0)*(model.y3_2_11 - 1.0) + 0.5*(model.x4_2_0 - 1.0)*(model.x4_2_0 \
    - 1.0) + 0.5*(model.y4_2_0 - 1.0)*(model.y4_2_0 - 1.0) + 0.5*(model.x4_2_11 - 1.0)*(model.x4_2_11 \
    - 1.0) + 0.5*(model.y4_2_11 - 1.0)*(model.y4_2_11 - 1.0) + 0.5*(model.x5_2_0 - 1.0)*(model.x5_2_0 \
    - 1.0) + 0.5*(model.y5_2_0 - 1.0)*(model.y5_2_0 - 1.0) + 0.5*(model.x5_2_11 - 1.0)*(model.x5_2_11 \
    - 1.0) + 0.5*(model.y5_2_11 - 1.0)*(model.y5_2_11 - 1.0) + 0.5*(model.x6_2_0 - 1.0)*(model.x6_2_0 \
    - 1.0) + 0.5*(model.y6_2_0 - 1.0)*(model.y6_2_0 - 1.0) + 0.5*(model.x6_2_11 - 1.0)*(model.x6_2_11 \
    - 1.0) + 0.5*(model.y6_2_11 - 1.0)*(model.y6_2_11 - 1.0) + 0.5*(model.x7_2_0 - 1.0)*(model.x7_2_0 \
    - 1.0) + 0.5*(model.y7_2_0 - 1.0)*(model.y7_2_0 - 1.0) + 0.5*(model.x7_2_11 - 1.0)*(model.x7_2_11 \
    - 1.0) + 0.5*(model.y7_2_11 - 1.0)*(model.y7_2_11 - 1.0) + 0.5*(model.x8_2_0 - 1.0)*(model.x8_2_0 \
    - 1.0) + 0.5*(model.y8_2_0 - 1.0)*(model.y8_2_0 - 1.0) + 0.5*(model.x8_2_11 - 1.0)*(model.x8_2_11 \
    - 1.0) + 0.5*(model.y8_2_11 - 1.0)*(model.y8_2_11 - 1.0) + 0.5*(model.x9_2_0 - 1.0)*(model.x9_2_0 \
    - 1.0) + 0.5*(model.y9_2_0 - 1.0)*(model.y9_2_0 - 1.0) + 0.5*(model.x9_2_11 - 1.0)*(model.x9_2_11 \
    - 1.0) + 0.5*(model.y9_2_11 - 1.0)*(model.y9_2_11 - 1.0) + 0.5*(model.x10_2_0 - \
    1.0)*(model.x10_2_0 - 1.0) + 0.5*(model.y10_2_0 - 1.0)*(model.y10_2_0 - 1.0) + \
    0.5*(model.x10_2_11 - 1.0)*(model.x10_2_11 - 1.0) + 0.5*(model.y10_2_11 - 1.0)*(model.y10_2_11 - \
    1.0) + 0.5*(model.x1_3_0 - 1.0)*(model.x1_3_0 - 1.0) + 0.5*(model.y1_3_0 - 1.0)*(model.y1_3_0 - \
    1.0) + 0.5*(model.x1_3_11 - 1.0)*(model.x1_3_11 - 1.0) + 0.5*(model.y1_3_11 - 1.0)*(model.y1_3_11 \
    - 1.0) + 0.5*(model.x2_3_0 - 1.0)*(model.x2_3_0 - 1.0) + 0.5*(model.y2_3_0 - 1.0)*(model.y2_3_0 - \
    1.0) + 0.5*(model.x2_3_11 - 1.0)*(model.x2_3_11 - 1.0) + 0.5*(model.y2_3_11 - 1.0)*(model.y2_3_11 \
    - 1.0) + 0.5*(model.x3_3_0 - 1.0)*(model.x3_3_0 - 1.0) + 0.5*(model.y3_3_0 - 1.0)*(model.y3_3_0 - \
    1.0) + 0.5*(model.x3_3_11 - 1.0)*(model.x3_3_11 - 1.0) + 0.5*(model.y3_3_11 - 1.0)*(model.y3_3_11 \
    - 1.0) + 0.5*(model.x4_3_0 - 1.0)*(model.x4_3_0 - 1.0) + 0.5*(model.y4_3_0 - 1.0)*(model.y4_3_0 - \
    1.0) + 0.5*(model.x4_3_11 - 1.0)*(model.x4_3_11 - 1.0) + 0.5*(model.y4_3_11 - 1.0)*(model.y4_3_11 \
    - 1.0) + 0.5*(model.x5_3_0 - 1.0)*(model.x5_3_0 - 1.0) + 0.5*(model.y5_3_0 - 1.0)*(model.y5_3_0 - \
    1.0) + 0.5*(model.x5_3_11 - 1.0)*(model.x5_3_11 - 1.0) + 0.5*(model.y5_3_11 - 1.0)*(model.y5_3_11 \
    - 1.0) + 0.5*(model.x6_3_0 - 1.0)*(model.x6_3_0 - 1.0) + 0.5*(model.y6_3_0 - 1.0)*(model.y6_3_0 - \
    1.0) + 0.5*(model.x6_3_11 - 1.0)*(model.x6_3_11 - 1.0) + 0.5*(model.y6_3_11 - 1.0)*(model.y6_3_11 \
    - 1.0) + 0.5*(model.x7_3_0 - 1.0)*(model.x7_3_0 - 1.0) + 0.5*(model.y7_3_0 - 1.0)*(model.y7_3_0 - \
    1.0) + 0.5*(model.x7_3_11 - 1.0)*(model.x7_3_11 - 1.0) + 0.5*(model.y7_3_11 - 1.0)*(model.y7_3_11 \
    - 1.0) + 0.5*(model.x8_3_0 - 1.0)*(model.x8_3_0 - 1.0) + 0.5*(model.y8_3_0 - 1.0)*(model.y8_3_0 - \
    1.0) + 0.5*(model.x8_3_11 - 1.0)*(model.x8_3_11 - 1.0) + 0.5*(model.y8_3_11 - 1.0)*(model.y8_3_11 \
    - 1.0) + 0.5*(model.x9_3_0 - 1.0)*(model.x9_3_0 - 1.0) + 0.5*(model.y9_3_0 - 1.0)*(model.y9_3_0 - \
    1.0) + 0.5*(model.x9_3_11 - 1.0)*(model.x9_3_11 - 1.0) + 0.5*(model.y9_3_11 - 1.0)*(model.y9_3_11 \
    - 1.0) + 0.5*(model.x10_3_0 - 1.0)*(model.x10_3_0 - 1.0) + 0.5*(model.y10_3_0 - \
    1.0)*(model.y10_3_0 - 1.0) + 0.5*(model.x10_3_11 - 1.0)*(model.x10_3_11 - 1.0) + \
    0.5*(model.y10_3_11 - 1.0)*(model.y10_3_11 - 1.0) + 0.5*(model.x1_4_0 - 1.0)*(model.x1_4_0 - 1.0) \
    + 0.5*(model.y1_4_0 - 1.0)*(model.y1_4_0 - 1.0) + 0.5*(model.x1_4_11 - 1.0)*(model.x1_4_11 - 1.0) \
    + 0.5*(model.y1_4_11 - 1.0)*(model.y1_4_11 - 1.0) + 0.5*(model.x2_4_0 - 1.0)*(model.x2_4_0 - 1.0) \
    + 0.5*(model.y2_4_0 - 1.0)*(model.y2_4_0 - 1.0) + 0.5*(model.x2_4_11 - 1.0)*(model.x2_4_11 - 1.0) \
    + 0.5*(model.y2_4_11 - 1.0)*(model.y2_4_11 - 1.0) + 0.5*(model.x3_4_0 - 1.0)*(model.x3_4_0 - 1.0) \
    + 0.5*(model.y3_4_0 - 1.0)*(model.y3_4_0 - 1.0) + 0.5*(model.x3_4_11 - 1.0)*(model.x3_4_11 - 1.0) \
    + 0.5*(model.y3_4_11 - 1.0)*(model.y3_4_11 - 1.0) + 0.5*(model.x4_4_0 - 1.0)*(model.x4_4_0 - 1.0) \
    + 0.5*(model.y4_4_0 - 1.0)*(model.y4_4_0 - 1.0) + 0.5*(model.x4_4_11 - 1.0)*(model.x4_4_11 - 1.0) \
    + 0.5*(model.y4_4_11 - 1.0)*(model.y4_4_11 - 1.0) + 0.5*(model.x5_4_0 - 1.0)*(model.x5_4_0 - 1.0) \
    + 0.5*(model.y5_4_0 - 1.0)*(model.y5_4_0 - 1.0) + 0.5*(model.x5_4_11 - 1.0)*(model.x5_4_11 - 1.0) \
    + 0.5*(model.y5_4_11 - 1.0)*(model.y5_4_11 - 1.0) + 0.5*(model.x6_4_0 - 1.0)*(model.x6_4_0 - 1.0) \
    + 0.5*(model.y6_4_0 - 1.0)*(model.y6_4_0 - 1.0) + 0.5*(model.x6_4_11 - 1.0)*(model.x6_4_11 - 1.0) \
    + 0.5*(model.y6_4_11 - 1.0)*(model.y6_4_11 - 1.0) + 0.5*(model.x7_4_0 - 1.0)*(model.x7_4_0 - 1.0) \
    + 0.5*(model.y7_4_0 - 1.0)*(model.y7_4_0 - 1.0) + 0.5*(model.x7_4_11 - 1.0)*(model.x7_4_11 - 1.0) \
    + 0.5*(model.y7_4_11 - 1.0)*(model.y7_4_11 - 1.0) + 0.5*(model.x8_4_0 - 1.0)*(model.x8_4_0 - 1.0) \
    + 0.5*(model.y8_4_0 - 1.0)*(model.y8_4_0 - 1.0) + 0.5*(model.x8_4_11 - 1.0)*(model.x8_4_11 - 1.0) \
    + 0.5*(model.y8_4_11 - 1.0)*(model.y8_4_11 - 1.0) + 0.5*(model.x9_4_0 - 1.0)*(model.x9_4_0 - 1.0) \
    + 0.5*(model.y9_4_0 - 1.0)*(model.y9_4_0 - 1.0) + 0.5*(model.x9_4_11 - 1.0)*(model.x9_4_11 - 1.0) \
    + 0.5*(model.y9_4_11 - 1.0)*(model.y9_4_11 - 1.0) + 0.5*(model.x10_4_0 - 1.0)*(model.x10_4_0 - \
    1.0) + 0.5*(model.y10_4_0 - 1.0)*(model.y10_4_0 - 1.0) + 0.5*(model.x10_4_11 - \
    1.0)*(model.x10_4_11 - 1.0) + 0.5*(model.y10_4_11 - 1.0)*(model.y10_4_11 - 1.0) + \
    0.5*(model.x1_5_0 - 1.0)*(model.x1_5_0 - 1.0) + 0.5*(model.y1_5_0 - 1.0)*(model.y1_5_0 - 1.0) + \
    0.5*(model.x1_5_11 - 1.0)*(model.x1_5_11 - 1.0) + 0.5*(model.y1_5_11 - 1.0)*(model.y1_5_11 - 1.0) \
    + 0.5*(model.x2_5_0 - 1.0)*(model.x2_5_0 - 1.0) + 0.5*(model.y2_5_0 - 1.0)*(model.y2_5_0 - 1.0) + \
    0.5*(model.x2_5_11 - 1.0)*(model.x2_5_11 - 1.0) + 0.5*(model.y2_5_11 - 1.0)*(model.y2_5_11 - 1.0) \
    + 0.5*(model.x3_5_0 - 1.0)*(model.x3_5_0 - 1.0) + 0.5*(model.y3_5_0 - 1.0)*(model.y3_5_0 - 1.0) + \
    0.5*(model.x3_5_11 - 1.0)*(model.x3_5_11 - 1.0) + 0.5*(model.y3_5_11 - 1.0)*(model.y3_5_11 - 1.0) \
    + 0.5*(model.x4_5_0 - 1.0)*(model.x4_5_0 - 1.0) + 0.5*(model.y4_5_0 - 1.0)*(model.y4_5_0 - 1.0) + \
    0.5*(model.x4_5_11 - 1.0)*(model.x4_5_11 - 1.0) + 0.5*(model.y4_5_11 - 1.0)*(model.y4_5_11 - 1.0) \
    + 0.5*(model.x5_5_0 - 1.0)*(model.x5_5_0 - 1.0) + 0.5*(model.y5_5_0 - 1.0)*(model.y5_5_0 - 1.0) + \
    0.5*(model.x5_5_11 - 1.0)*(model.x5_5_11 - 1.0) + 0.5*(model.y5_5_11 - 1.0)*(model.y5_5_11 - 1.0) \
    + 0.5*(model.x6_5_0 - 1.0)*(model.x6_5_0 - 1.0) + 0.5*(model.y6_5_0 - 1.0)*(model.y6_5_0 - 1.0) + \
    0.5*(model.x6_5_11 - 1.0)*(model.x6_5_11 - 1.0) + 0.5*(model.y6_5_11 - 1.0)*(model.y6_5_11 - 1.0) \
    + 0.5*(model.x7_5_0 - 1.0)*(model.x7_5_0 - 1.0) + 0.5*(model.y7_5_0 - 1.0)*(model.y7_5_0 - 1.0) + \
    0.5*(model.x7_5_11 - 1.0)*(model.x7_5_11 - 1.0) + 0.5*(model.y7_5_11 - 1.0)*(model.y7_5_11 - 1.0) \
    + 0.5*(model.x8_5_0 - 1.0)*(model.x8_5_0 - 1.0) + 0.5*(model.y8_5_0 - 1.0)*(model.y8_5_0 - 1.0) + \
    0.5*(model.x8_5_11 - 1.0)*(model.x8_5_11 - 1.0) + 0.5*(model.y8_5_11 - 1.0)*(model.y8_5_11 - 1.0) \
    + 0.5*(model.x9_5_0 - 1.0)*(model.x9_5_0 - 1.0) + 0.5*(model.y9_5_0 - 1.0)*(model.y9_5_0 - 1.0) + \
    0.5*(model.x9_5_11 - 1.0)*(model.x9_5_11 - 1.0) + 0.5*(model.y9_5_11 - 1.0)*(model.y9_5_11 - 1.0) \
    + 0.5*(model.x10_5_0 - 1.0)*(model.x10_5_0 - 1.0) + 0.5*(model.y10_5_0 - 1.0)*(model.y10_5_0 - \
    1.0) + 0.5*(model.x10_5_11 - 1.0)*(model.x10_5_11 - 1.0) + 0.5*(model.y10_5_11 - \
    1.0)*(model.y10_5_11 - 1.0) + 0.5*(model.x1_6_0 - 1.0)*(model.x1_6_0 - 1.0) + 0.5*(model.y1_6_0 - \
    1.0)*(model.y1_6_0 - 1.0) + 0.5*(model.x1_6_11 - 1.0)*(model.x1_6_11 - 1.0) + 0.5*(model.y1_6_11 \
    - 1.0)*(model.y1_6_11 - 1.0) + 0.5*(model.x2_6_0 - 1.0)*(model.x2_6_0 - 1.0) + 0.5*(model.y2_6_0 \
    - 1.0)*(model.y2_6_0 - 1.0) + 0.5*(model.x2_6_11 - 1.0)*(model.x2_6_11 - 1.0) + \
    0.5*(model.y2_6_11 - 1.0)*(model.y2_6_11 - 1.0) + 0.5*(model.x3_6_0 - 1.0)*(model.x3_6_0 - 1.0) + \
    0.5*(model.y3_6_0 - 1.0)*(model.y3_6_0 - 1.0) + 0.5*(model.x3_6_11 - 1.0)*(model.x3_6_11 - 1.0) + \
    0.5*(model.y3_6_11 - 1.0)*(model.y3_6_11 - 1.0) + 0.5*(model.x4_6_0 - 1.0)*(model.x4_6_0 - 1.0) + \
    0.5*(model.y4_6_0 - 1.0)*(model.y4_6_0 - 1.0) + 0.5*(model.x4_6_11 - 1.0)*(model.x4_6_11 - 1.0) + \
    0.5*(model.y4_6_11 - 1.0)*(model.y4_6_11 - 1.0) + 0.5*(model.x5_6_0 - 1.0)*(model.x5_6_0 - 1.0) + \
    0.5*(model.y5_6_0 - 1.0)*(model.y5_6_0 - 1.0) + 0.5*(model.x5_6_11 - 1.0)*(model.x5_6_11 - 1.0) + \
    0.5*(model.y5_6_11 - 1.0)*(model.y5_6_11 - 1.0) + 0.5*(model.x6_6_0 - 1.0)*(model.x6_6_0 - 1.0) + \
    0.5*(model.y6_6_0 - 1.0)*(model.y6_6_0 - 1.0) + 0.5*(model.x6_6_11 - 1.0)*(model.x6_6_11 - 1.0) + \
    0.5*(model.y6_6_11 - 1.0)*(model.y6_6_11 - 1.0) + 0.5*(model.x7_6_0 - 1.0)*(model.x7_6_0 - 1.0) + \
    0.5*(model.y7_6_0 - 1.0)*(model.y7_6_0 - 1.0) + 0.5*(model.x7_6_11 - 1.0)*(model.x7_6_11 - 1.0) + \
    0.5*(model.y7_6_11 - 1.0)*(model.y7_6_11 - 1.0) + 0.5*(model.x8_6_0 - 1.0)*(model.x8_6_0 - 1.0) + \
    0.5*(model.y8_6_0 - 1.0)*(model.y8_6_0 - 1.0) + 0.5*(model.x8_6_11 - 1.0)*(model.x8_6_11 - 1.0) + \
    0.5*(model.y8_6_11 - 1.0)*(model.y8_6_11 - 1.0) + 0.5*(model.x9_6_0 - 1.0)*(model.x9_6_0 - 1.0) + \
    0.5*(model.y9_6_0 - 1.0)*(model.y9_6_0 - 1.0) + 0.5*(model.x9_6_11 - 1.0)*(model.x9_6_11 - 1.0) + \
    0.5*(model.y9_6_11 - 1.0)*(model.y9_6_11 - 1.0) + 0.5*(model.x10_6_0 - 1.0)*(model.x10_6_0 - 1.0) \
    + 0.5*(model.y10_6_0 - 1.0)*(model.y10_6_0 - 1.0) + 0.5*(model.x10_6_11 - 1.0)*(model.x10_6_11 - \
    1.0) + 0.5*(model.y10_6_11 - 1.0)*(model.y10_6_11 - 1.0) + 0.5*(model.x1_7_0 - 1.0)*(model.x1_7_0 \
    - 1.0) + 0.5*(model.y1_7_0 - 1.0)*(model.y1_7_0 - 1.0) + 0.5*(model.x1_7_11 - 1.0)*(model.x1_7_11 \
    - 1.0) + 0.5*(model.y1_7_11 - 1.0)*(model.y1_7_11 - 1.0) + 0.5*(model.x2_7_0 - 1.0)*(model.x2_7_0 \
    - 1.0) + 0.5*(model.y2_7_0 - 1.0)*(model.y2_7_0 - 1.0) + 0.5*(model.x2_7_11 - 1.0)*(model.x2_7_11 \
    - 1.0) + 0.5*(model.y2_7_11 - 1.0)*(model.y2_7_11 - 1.0) + 0.5*(model.x3_7_0 - 1.0)*(model.x3_7_0 \
    - 1.0) + 0.5*(model.y3_7_0 - 1.0)*(model.y3_7_0 - 1.0) + 0.5*(model.x3_7_11 - 1.0)*(model.x3_7_11 \
    - 1.0) + 0.5*(model.y3_7_11 - 1.0)*(model.y3_7_11 - 1.0) + 0.5*(model.x4_7_0 - 1.0)*(model.x4_7_0 \
    - 1.0) + 0.5*(model.y4_7_0 - 1.0)*(model.y4_7_0 - 1.0) + 0.5*(model.x4_7_11 - 1.0)*(model.x4_7_11 \
    - 1.0) + 0.5*(model.y4_7_11 - 1.0)*(model.y4_7_11 - 1.0) + 0.5*(model.x5_7_0 - 1.0)*(model.x5_7_0 \
    - 1.0) + 0.5*(model.y5_7_0 - 1.0)*(model.y5_7_0 - 1.0) + 0.5*(model.x5_7_11 - 1.0)*(model.x5_7_11 \
    - 1.0) + 0.5*(model.y5_7_11 - 1.0)*(model.y5_7_11 - 1.0) + 0.5*(model.x6_7_0 - 1.0)*(model.x6_7_0 \
    - 1.0) + 0.5*(model.y6_7_0 - 1.0)*(model.y6_7_0 - 1.0) + 0.5*(model.x6_7_11 - 1.0)*(model.x6_7_11 \
    - 1.0) + 0.5*(model.y6_7_11 - 1.0)*(model.y6_7_11 - 1.0) + 0.5*(model.x7_7_0 - 1.0)*(model.x7_7_0 \
    - 1.0) + 0.5*(model.y7_7_0 - 1.0)*(model.y7_7_0 - 1.0) + 0.5*(model.x7_7_11 - 1.0)*(model.x7_7_11 \
    - 1.0) + 0.5*(model.y7_7_11 - 1.0)*(model.y7_7_11 - 1.0) + 0.5*(model.x8_7_0 - 1.0)*(model.x8_7_0 \
    - 1.0) + 0.5*(model.y8_7_0 - 1.0)*(model.y8_7_0 - 1.0) + 0.5*(model.x8_7_11 - 1.0)*(model.x8_7_11 \
    - 1.0) + 0.5*(model.y8_7_11 - 1.0)*(model.y8_7_11 - 1.0) + 0.5*(model.x9_7_0 - 1.0)*(model.x9_7_0 \
    - 1.0) + 0.5*(model.y9_7_0 - 1.0)*(model.y9_7_0 - 1.0) + 0.5*(model.x9_7_11 - 1.0)*(model.x9_7_11 \
    - 1.0) + 0.5*(model.y9_7_11 - 1.0)*(model.y9_7_11 - 1.0) + 0.5*(model.x10_7_0 - \
    1.0)*(model.x10_7_0 - 1.0) + 0.5*(model.y10_7_0 - 1.0)*(model.y10_7_0 - 1.0) + \
    0.5*(model.x10_7_11 - 1.0)*(model.x10_7_11 - 1.0) + 0.5*(model.y10_7_11 - 1.0)*(model.y10_7_11 - \
    1.0) + 0.5*(model.x1_8_0 - 1.0)*(model.x1_8_0 - 1.0) + 0.5*(model.y1_8_0 - 1.0)*(model.y1_8_0 - \
    1.0) + 0.5*(model.x1_8_11 - 1.0)*(model.x1_8_11 - 1.0) + 0.5*(model.y1_8_11 - 1.0)*(model.y1_8_11 \
    - 1.0) + 0.5*(model.x2_8_0 - 1.0)*(model.x2_8_0 - 1.0) + 0.5*(model.y2_8_0 - 1.0)*(model.y2_8_0 - \
    1.0) + 0.5*(model.x2_8_11 - 1.0)*(model.x2_8_11 - 1.0) + 0.5*(model.y2_8_11 - 1.0)*(model.y2_8_11 \
    - 1.0) + 0.5*(model.x3_8_0 - 1.0)*(model.x3_8_0 - 1.0) + 0.5*(model.y3_8_0 - 1.0)*(model.y3_8_0 - \
    1.0) + 0.5*(model.x3_8_11 - 1.0)*(model.x3_8_11 - 1.0) + 0.5*(model.y3_8_11 - 1.0)*(model.y3_8_11 \
    - 1.0) + 0.5*(model.x4_8_0 - 1.0)*(model.x4_8_0 - 1.0) + 0.5*(model.y4_8_0 - 1.0)*(model.y4_8_0 - \
    1.0) + 0.5*(model.x4_8_11 - 1.0)*(model.x4_8_11 - 1.0) + 0.5*(model.y4_8_11 - 1.0)*(model.y4_8_11 \
    - 1.0) + 0.5*(model.x5_8_0 - 1.0)*(model.x5_8_0 - 1.0) + 0.5*(model.y5_8_0 - 1.0)*(model.y5_8_0 - \
    1.0) + 0.5*(model.x5_8_11 - 1.0)*(model.x5_8_11 - 1.0) + 0.5*(model.y5_8_11 - 1.0)*(model.y5_8_11 \
    - 1.0) + 0.5*(model.x6_8_0 - 1.0)*(model.x6_8_0 - 1.0) + 0.5*(model.y6_8_0 - 1.0)*(model.y6_8_0 - \
    1.0) + 0.5*(model.x6_8_11 - 1.0)*(model.x6_8_11 - 1.0) + 0.5*(model.y6_8_11 - 1.0)*(model.y6_8_11 \
    - 1.0) + 0.5*(model.x7_8_0 - 1.0)*(model.x7_8_0 - 1.0) + 0.5*(model.y7_8_0 - 1.0)*(model.y7_8_0 - \
    1.0) + 0.5*(model.x7_8_11 - 1.0)*(model.x7_8_11 - 1.0) + 0.5*(model.y7_8_11 - 1.0)*(model.y7_8_11 \
    - 1.0) + 0.5*(model.x8_8_0 - 1.0)*(model.x8_8_0 - 1.0) + 0.5*(model.y8_8_0 - 1.0)*(model.y8_8_0 - \
    1.0) + 0.5*(model.x8_8_11 - 1.0)*(model.x8_8_11 - 1.0) + 0.5*(model.y8_8_11 - 1.0)*(model.y8_8_11 \
    - 1.0) + 0.5*(model.x9_8_0 - 1.0)*(model.x9_8_0 - 1.0) + 0.5*(model.y9_8_0 - 1.0)*(model.y9_8_0 - \
    1.0) + 0.5*(model.x9_8_11 - 1.0)*(model.x9_8_11 - 1.0) + 0.5*(model.y9_8_11 - 1.0)*(model.y9_8_11 \
    - 1.0) + 0.5*(model.x10_8_0 - 1.0)*(model.x10_8_0 - 1.0) + 0.5*(model.y10_8_0 - \
    1.0)*(model.y10_8_0 - 1.0) + 0.5*(model.x10_8_11 - 1.0)*(model.x10_8_11 - 1.0) + \
    0.5*(model.y10_8_11 - 1.0)*(model.y10_8_11 - 1.0) + 0.5*(model.x1_9_0 - 1.0)*(model.x1_9_0 - 1.0) \
    + 0.5*(model.y1_9_0 - 1.0)*(model.y1_9_0 - 1.0) + 0.5*(model.x1_9_11 - 1.0)*(model.x1_9_11 - 1.0) \
    + 0.5*(model.y1_9_11 - 1.0)*(model.y1_9_11 - 1.0) + 0.5*(model.x2_9_0 - 1.0)*(model.x2_9_0 - 1.0) \
    + 0.5*(model.y2_9_0 - 1.0)*(model.y2_9_0 - 1.0) + 0.5*(model.x2_9_11 - 1.0)*(model.x2_9_11 - 1.0) \
    + 0.5*(model.y2_9_11 - 1.0)*(model.y2_9_11 - 1.0) + 0.5*(model.x3_9_0 - 1.0)*(model.x3_9_0 - 1.0) \
    + 0.5*(model.y3_9_0 - 1.0)*(model.y3_9_0 - 1.0) + 0.5*(model.x3_9_11 - 1.0)*(model.x3_9_11 - 1.0) \
    + 0.5*(model.y3_9_11 - 1.0)*(model.y3_9_11 - 1.0) + 0.5*(model.x4_9_0 - 1.0)*(model.x4_9_0 - 1.0) \
    + 0.5*(model.y4_9_0 - 1.0)*(model.y4_9_0 - 1.0) + 0.5*(model.x4_9_11 - 1.0)*(model.x4_9_11 - 1.0) \
    + 0.5*(model.y4_9_11 - 1.0)*(model.y4_9_11 - 1.0) + 0.5*(model.x5_9_0 - 1.0)*(model.x5_9_0 - 1.0) \
    + 0.5*(model.y5_9_0 - 1.0)*(model.y5_9_0 - 1.0) + 0.5*(model.x5_9_11 - 1.0)*(model.x5_9_11 - 1.0) \
    + 0.5*(model.y5_9_11 - 1.0)*(model.y5_9_11 - 1.0) + 0.5*(model.x6_9_0 - 1.0)*(model.x6_9_0 - 1.0) \
    + 0.5*(model.y6_9_0 - 1.0)*(model.y6_9_0 - 1.0) + 0.5*(model.x6_9_11 - 1.0)*(model.x6_9_11 - 1.0) \
    + 0.5*(model.y6_9_11 - 1.0)*(model.y6_9_11 - 1.0) + 0.5*(model.x7_9_0 - 1.0)*(model.x7_9_0 - 1.0) \
    + 0.5*(model.y7_9_0 - 1.0)*(model.y7_9_0 - 1.0) + 0.5*(model.x7_9_11 - 1.0)*(model.x7_9_11 - 1.0) \
    + 0.5*(model.y7_9_11 - 1.0)*(model.y7_9_11 - 1.0) + 0.5*(model.x8_9_0 - 1.0)*(model.x8_9_0 - 1.0) \
    + 0.5*(model.y8_9_0 - 1.0)*(model.y8_9_0 - 1.0) + 0.5*(model.x8_9_11 - 1.0)*(model.x8_9_11 - 1.0) \
    + 0.5*(model.y8_9_11 - 1.0)*(model.y8_9_11 - 1.0) + 0.5*(model.x9_9_0 - 1.0)*(model.x9_9_0 - 1.0) \
    + 0.5*(model.y9_9_0 - 1.0)*(model.y9_9_0 - 1.0) + 0.5*(model.x9_9_11 - 1.0)*(model.x9_9_11 - 1.0) \
    + 0.5*(model.y9_9_11 - 1.0)*(model.y9_9_11 - 1.0) + 0.5*(model.x10_9_0 - 1.0)*(model.x10_9_0 - \
    1.0) + 0.5*(model.y10_9_0 - 1.0)*(model.y10_9_0 - 1.0) + 0.5*(model.x10_9_11 - \
    1.0)*(model.x10_9_11 - 1.0) + 0.5*(model.y10_9_11 - 1.0)*(model.y10_9_11 - 1.0) + \
    0.5*(model.x1_10_0 - 1.0)*(model.x1_10_0 - 1.0) + 0.5*(model.y1_10_0 - 1.0)*(model.y1_10_0 - 1.0) \
    + 0.5*(model.x1_10_11 - 1.0)*(model.x1_10_11 - 1.0) + 0.5*(model.y1_10_11 - 1.0)*(model.y1_10_11 \
    - 1.0) + 0.5*(model.x2_10_0 - 1.0)*(model.x2_10_0 - 1.0) + 0.5*(model.y2_10_0 - \
    1.0)*(model.y2_10_0 - 1.0) + 0.5*(model.x2_10_11 - 1.0)*(model.x2_10_11 - 1.0) + \
    0.5*(model.y2_10_11 - 1.0)*(model.y2_10_11 - 1.0) + 0.5*(model.x3_10_0 - 1.0)*(model.x3_10_0 - \
    1.0) + 0.5*(model.y3_10_0 - 1.0)*(model.y3_10_0 - 1.0) + 0.5*(model.x3_10_11 - \
    1.0)*(model.x3_10_11 - 1.0) + 0.5*(model.y3_10_11 - 1.0)*(model.y3_10_11 - 1.0) + \
    0.5*(model.x4_10_0 - 1.0)*(model.x4_10_0 - 1.0) + 0.5*(model.y4_10_0 - 1.0)*(model.y4_10_0 - 1.0) \
    + 0.5*(model.x4_10_11 - 1.0)*(model.x4_10_11 - 1.0) + 0.5*(model.y4_10_11 - 1.0)*(model.y4_10_11 \
    - 1.0) + 0.5*(model.x5_10_0 - 1.0)*(model.x5_10_0 - 1.0) + 0.5*(model.y5_10_0 - \
    1.0)*(model.y5_10_0 - 1.0) + 0.5*(model.x5_10_11 - 1.0)*(model.x5_10_11 - 1.0) + \
    0.5*(model.y5_10_11 - 1.0)*(model.y5_10_11 - 1.0) + 0.5*(model.x6_10_0 - 1.0)*(model.x6_10_0 - \
    1.0) + 0.5*(model.y6_10_0 - 1.0)*(model.y6_10_0 - 1.0) + 0.5*(model.x6_10_11 - \
    1.0)*(model.x6_10_11 - 1.0) + 0.5*(model.y6_10_11 - 1.0)*(model.y6_10_11 - 1.0) + \
    0.5*(model.x7_10_0 - 1.0)*(model.x7_10_0 - 1.0) + 0.5*(model.y7_10_0 - 1.0)*(model.y7_10_0 - 1.0) \
    + 0.5*(model.x7_10_11 - 1.0)*(model.x7_10_11 - 1.0) + 0.5*(model.y7_10_11 - 1.0)*(model.y7_10_11 \
    - 1.0) + 0.5*(model.x8_10_0 - 1.0)*(model.x8_10_0 - 1.0) + 0.5*(model.y8_10_0 - \
    1.0)*(model.y8_10_0 - 1.0) + 0.5*(model.x8_10_11 - 1.0)*(model.x8_10_11 - 1.0) + \
    0.5*(model.y8_10_11 - 1.0)*(model.y8_10_11 - 1.0) + 0.5*(model.x9_10_0 - 1.0)*(model.x9_10_0 - \
    1.0) + 0.5*(model.y9_10_0 - 1.0)*(model.y9_10_0 - 1.0) + 0.5*(model.x9_10_11 - \
    1.0)*(model.x9_10_11 - 1.0) + 0.5*(model.y9_10_11 - 1.0)*(model.y9_10_11 - 1.0) + \
    0.5*(model.x10_10_0 - 1.0)*(model.x10_10_0 - 1.0) + 0.5*(model.y10_10_0 - 1.0)*(model.y10_10_0 - \
    1.0) + 0.5*(model.x10_10_11 - 1.0)*(model.x10_10_11 - 1.0) + 0.5*(model.y10_10_11 - \
    1.0)*(model.y10_10_11 - 1.0))

model.v1_1_1 = Constraint(expr=model.x1_1_1 + model.y1_1_1 + model.z1_1_1 + model.y0_1_1 + model.z0_1_1 + model.x1_0_1 + model.z1_0_1 + model.x1_1_0 + model.y1_1_0 - 1.0 == 0)
model.v2_1_1 = Constraint(expr=-model.x1_1_1 + model.x2_1_1 + model.y2_1_1 + model.z2_1_1 + model.x2_0_1 + model.z2_0_1 + model.x2_1_0 + model.y2_1_0 - 1.0 == 0)
model.v3_1_1 = Constraint(expr=-model.x2_1_1 + model.x3_1_1 + model.y3_1_1 + model.z3_1_1 + model.x3_0_1 + model.z3_0_1 + model.x3_1_0 + model.y3_1_0 - 1.0 == 0)
model.v4_1_1 = Constraint(expr=-model.x3_1_1 + model.x4_1_1 + model.y4_1_1 + model.z4_1_1 + model.x4_0_1 + model.z4_0_1 + model.x4_1_0 + model.y4_1_0 - 1.0 == 0)
model.v5_1_1 = Constraint(expr=-model.x4_1_1 + model.x5_1_1 + model.y5_1_1 + model.z5_1_1 + model.x5_0_1 + model.z5_0_1 + model.x5_1_0 + model.y5_1_0 - 1.0 == 0)
model.v6_1_1 = Constraint(expr=-model.x5_1_1 + model.x6_1_1 + model.y6_1_1 + model.z6_1_1 + model.x6_0_1 + model.z6_0_1 + model.x6_1_0 + model.y6_1_0 - 1.0 == 0)
model.v7_1_1 = Constraint(expr=-model.x6_1_1 + model.x7_1_1 + model.y7_1_1 + model.z7_1_1 + model.x7_0_1 + model.z7_0_1 + model.x7_1_0 + model.y7_1_0 - 1.0 == 0)
model.v8_1_1 = Constraint(expr=-model.x7_1_1 + model.x8_1_1 + model.y8_1_1 + model.z8_1_1 + model.x8_0_1 + model.z8_0_1 + model.x8_1_0 + model.y8_1_0 - 1.0 == 0)
model.v9_1_1 = Constraint(expr=-model.x8_1_1 + model.x9_1_1 + model.y9_1_1 + model.z9_1_1 + model.x9_0_1 + model.z9_0_1 + model.x9_1_0 + model.y9_1_0 - 1.0 == 0)
model.v10_1_1 = Constraint(expr=-model.x9_1_1 + model.y10_1_1 + model.z10_1_1 + model.y11_1_1 + model.z11_1_1 + model.x10_0_1 + model.z10_0_1 + model.x10_1_0 + model.y10_1_0 - 1.0 == 0)
model.v1_2_1 = Constraint(expr=-model.y1_1_1 + model.x1_2_1 + model.y1_2_1 + model.z1_2_1 + model.y0_2_1 + model.z0_2_1 + model.x1_2_0 + model.y1_2_0 - 1.0 == 0)
model.v2_2_1 = Constraint(expr=-model.y2_1_1 - model.x1_2_1 + model.x2_2_1 + model.y2_2_1 + model.z2_2_1 + model.x2_2_0 + model.y2_2_0 - 1.0 == 0)
model.v3_2_1 = Constraint(expr=-model.y3_1_1 - model.x2_2_1 + model.x3_2_1 + model.y3_2_1 + model.z3_2_1 + model.x3_2_0 + model.y3_2_0 - 1.0 == 0)
model.v4_2_1 = Constraint(expr=-model.y4_1_1 - model.x3_2_1 + model.x4_2_1 + model.y4_2_1 + model.z4_2_1 + model.x4_2_0 + model.y4_2_0 - 1.0 == 0)
model.v5_2_1 = Constraint(expr=-model.y5_1_1 - model.x4_2_1 + model.x5_2_1 + model.y5_2_1 + model.z5_2_1 + model.x5_2_0 + model.y5_2_0 - 1.0 == 0)
model.v6_2_1 = Constraint(expr=-model.y6_1_1 - model.x5_2_1 + model.x6_2_1 + model.y6_2_1 + model.z6_2_1 + model.x6_2_0 + model.y6_2_0 - 1.0 == 0)
model.v7_2_1 = Constraint(expr=-model.y7_1_1 - model.x6_2_1 + model.x7_2_1 + model.y7_2_1 + model.z7_2_1 + model.x7_2_0 + model.y7_2_0 - 1.0 == 0)
model.v8_2_1 = Constraint(expr=-model.y8_1_1 - model.x7_2_1 + model.x8_2_1 + model.y8_2_1 + model.z8_2_1 + model.x8_2_0 + model.y8_2_0 - 1.0 == 0)
model.v9_2_1 = Constraint(expr=-model.y9_1_1 - model.x8_2_1 + model.x9_2_1 + model.y9_2_1 + model.z9_2_1 + model.x9_2_0 + model.y9_2_0 - 1.0 == 0)
model.v10_2_1 = Constraint(expr=-model.x9_2_1 - model.y10_1_1 + model.y10_2_1 + model.z10_2_1 + model.y11_2_1 + model.z11_2_1 + model.x10_2_0 + model.y10_2_0 - 1.0 == 0)
model.v1_3_1 = Constraint(expr=-model.y1_2_1 + model.x1_3_1 + model.y1_3_1 + model.z1_3_1 + model.y0_3_1 + model.z0_3_1 + model.x1_3_0 + model.y1_3_0 - 1.0 == 0)
model.v2_3_1 = Constraint(expr=-model.y2_2_1 - model.x1_3_1 + model.x2_3_1 + model.y2_3_1 + model.z2_3_1 + model.x2_3_0 + model.y2_3_0 - 1.0 == 0)
model.v3_3_1 = Constraint(expr=-model.y3_2_1 - model.x2_3_1 + model.x3_3_1 + model.y3_3_1 + model.z3_3_1 + model.x3_3_0 + model.y3_3_0 - 1.0 == 0)
model.v4_3_1 = Constraint(expr=-model.y4_2_1 - model.x3_3_1 + model.x4_3_1 + model.y4_3_1 + model.z4_3_1 + model.x4_3_0 + model.y4_3_0 - 1.0 == 0)
model.v5_3_1 = Constraint(expr=-model.y5_2_1 - model.x4_3_1 + model.x5_3_1 + model.y5_3_1 + model.z5_3_1 + model.x5_3_0 + model.y5_3_0 - 1.0 == 0)
model.v6_3_1 = Constraint(expr=-model.y6_2_1 - model.x5_3_1 + model.x6_3_1 + model.y6_3_1 + model.z6_3_1 + model.x6_3_0 + model.y6_3_0 - 1.0 == 0)
model.v7_3_1 = Constraint(expr=-model.y7_2_1 - model.x6_3_1 + model.x7_3_1 + model.y7_3_1 + model.z7_3_1 + model.x7_3_0 + model.y7_3_0 - 1.0 == 0)
model.v8_3_1 = Constraint(expr=-model.y8_2_1 - model.x7_3_1 + model.x8_3_1 + model.y8_3_1 + model.z8_3_1 + model.x8_3_0 + model.y8_3_0 - 1.0 == 0)
model.v9_3_1 = Constraint(expr=-model.y9_2_1 - model.x8_3_1 + model.x9_3_1 + model.y9_3_1 + model.z9_3_1 + model.x9_3_0 + model.y9_3_0 - 1.0 == 0)
model.v10_3_1 = Constraint(expr=-model.x9_3_1 - model.y10_2_1 + model.y10_3_1 + model.z10_3_1 + model.y11_3_1 + model.z11_3_1 + model.x10_3_0 + model.y10_3_0 - 1.0 == 0)
model.v1_4_1 = Constraint(expr=-model.y1_3_1 + model.x1_4_1 + model.y1_4_1 + model.z1_4_1 + model.y0_4_1 + model.z0_4_1 + model.x1_4_0 + model.y1_4_0 - 1.0 == 0)
model.v2_4_1 = Constraint(expr=-model.y2_3_1 - model.x1_4_1 + model.x2_4_1 + model.y2_4_1 + model.z2_4_1 + model.x2_4_0 + model.y2_4_0 - 1.0 == 0)
model.v3_4_1 = Constraint(expr=-model.y3_3_1 - model.x2_4_1 + model.x3_4_1 + model.y3_4_1 + model.z3_4_1 + model.x3_4_0 + model.y3_4_0 - 1.0 == 0)
model.v4_4_1 = Constraint(expr=-model.y4_3_1 - model.x3_4_1 + model.x4_4_1 + model.y4_4_1 + model.z4_4_1 + model.x4_4_0 + model.y4_4_0 - 1.0 == 0)
model.v5_4_1 = Constraint(expr=-model.y5_3_1 - model.x4_4_1 + model.x5_4_1 + model.y5_4_1 + model.z5_4_1 + model.x5_4_0 + model.y5_4_0 - 1.0 == 0)
model.v6_4_1 = Constraint(expr=-model.y6_3_1 - model.x5_4_1 + model.x6_4_1 + model.y6_4_1 + model.z6_4_1 + model.x6_4_0 + model.y6_4_0 - 1.0 == 0)
model.v7_4_1 = Constraint(expr=-model.y7_3_1 - model.x6_4_1 + model.x7_4_1 + model.y7_4_1 + model.z7_4_1 + model.x7_4_0 + model.y7_4_0 - 1.0 == 0)
model.v8_4_1 = Constraint(expr=-model.y8_3_1 - model.x7_4_1 + model.x8_4_1 + model.y8_4_1 + model.z8_4_1 + model.x8_4_0 + model.y8_4_0 - 1.0 == 0)
model.v9_4_1 = Constraint(expr=-model.y9_3_1 - model.x8_4_1 + model.x9_4_1 + model.y9_4_1 + model.z9_4_1 + model.x9_4_0 + model.y9_4_0 - 1.0 == 0)
model.v10_4_1 = Constraint(expr=-model.x9_4_1 - model.y10_3_1 + model.y10_4_1 + model.z10_4_1 + model.y11_4_1 + model.z11_4_1 + model.x10_4_0 + model.y10_4_0 - 1.0 == 0)
model.v1_5_1 = Constraint(expr=-model.y1_4_1 + model.x1_5_1 + model.y1_5_1 + model.z1_5_1 + model.y0_5_1 + model.z0_5_1 + model.x1_5_0 + model.y1_5_0 - 1.0 == 0)
model.v2_5_1 = Constraint(expr=-model.y2_4_1 - model.x1_5_1 + model.x2_5_1 + model.y2_5_1 + model.z2_5_1 + model.x2_5_0 + model.y2_5_0 - 1.0 == 0)
model.v3_5_1 = Constraint(expr=-model.y3_4_1 - model.x2_5_1 + model.x3_5_1 + model.y3_5_1 + model.z3_5_1 + model.x3_5_0 + model.y3_5_0 - 1.0 == 0)
model.v4_5_1 = Constraint(expr=-model.y4_4_1 - model.x3_5_1 + model.x4_5_1 + model.y4_5_1 + model.z4_5_1 + model.x4_5_0 + model.y4_5_0 - 1.0 == 0)
model.v5_5_1 = Constraint(expr=-model.y5_4_1 - model.x4_5_1 + model.x5_5_1 + model.y5_5_1 + model.z5_5_1 + model.x5_5_0 + model.y5_5_0 - 1.0 == 0)
model.v6_5_1 = Constraint(expr=-model.y6_4_1 - model.x5_5_1 + model.x6_5_1 + model.y6_5_1 + model.z6_5_1 + model.x6_5_0 + model.y6_5_0 - 1.0 == 0)
model.v7_5_1 = Constraint(expr=-model.y7_4_1 - model.x6_5_1 + model.x7_5_1 + model.y7_5_1 + model.z7_5_1 + model.x7_5_0 + model.y7_5_0 - 1.0 == 0)
model.v8_5_1 = Constraint(expr=-model.y8_4_1 - model.x7_5_1 + model.x8_5_1 + model.y8_5_1 + model.z8_5_1 + model.x8_5_0 + model.y8_5_0 - 1.0 == 0)
model.v9_5_1 = Constraint(expr=-model.y9_4_1 - model.x8_5_1 + model.x9_5_1 + model.y9_5_1 + model.z9_5_1 + model.x9_5_0 + model.y9_5_0 - 1.0 == 0)
model.v10_5_1 = Constraint(expr=-model.x9_5_1 - model.y10_4_1 + model.y10_5_1 + model.z10_5_1 + model.y11_5_1 + model.z11_5_1 + model.x10_5_0 + model.y10_5_0 - 1.0 == 0)
model.v1_6_1 = Constraint(expr=-model.y1_5_1 + model.x1_6_1 + model.y1_6_1 + model.z1_6_1 + model.y0_6_1 + model.z0_6_1 + model.x1_6_0 + model.y1_6_0 - 1.0 == 0)
model.v2_6_1 = Constraint(expr=-model.y2_5_1 - model.x1_6_1 + model.x2_6_1 + model.y2_6_1 + model.z2_6_1 + model.x2_6_0 + model.y2_6_0 - 1.0 == 0)
model.v3_6_1 = Constraint(expr=-model.y3_5_1 - model.x2_6_1 + model.x3_6_1 + model.y3_6_1 + model.z3_6_1 + model.x3_6_0 + model.y3_6_0 - 1.0 == 0)
model.v4_6_1 = Constraint(expr=-model.y4_5_1 - model.x3_6_1 + model.x4_6_1 + model.y4_6_1 + model.z4_6_1 + model.x4_6_0 + model.y4_6_0 - 1.0 == 0)
model.v5_6_1 = Constraint(expr=-model.y5_5_1 - model.x4_6_1 + model.x5_6_1 + model.y5_6_1 + model.z5_6_1 + model.x5_6_0 + model.y5_6_0 - 1.0 == 0)
model.v6_6_1 = Constraint(expr=-model.y6_5_1 - model.x5_6_1 + model.x6_6_1 + model.y6_6_1 + model.z6_6_1 + model.x6_6_0 + model.y6_6_0 - 1.0 == 0)
model.v7_6_1 = Constraint(expr=-model.y7_5_1 - model.x6_6_1 + model.x7_6_1 + model.y7_6_1 + model.z7_6_1 + model.x7_6_0 + model.y7_6_0 - 1.0 == 0)
model.v8_6_1 = Constraint(expr=-model.y8_5_1 - model.x7_6_1 + model.x8_6_1 + model.y8_6_1 + model.z8_6_1 + model.x8_6_0 + model.y8_6_0 - 1.0 == 0)
model.v9_6_1 = Constraint(expr=-model.y9_5_1 - model.x8_6_1 + model.x9_6_1 + model.y9_6_1 + model.z9_6_1 + model.x9_6_0 + model.y9_6_0 - 1.0 == 0)
model.v10_6_1 = Constraint(expr=-model.x9_6_1 - model.y10_5_1 + model.y10_6_1 + model.z10_6_1 + model.y11_6_1 + model.z11_6_1 + model.x10_6_0 + model.y10_6_0 - 1.0 == 0)
model.v1_7_1 = Constraint(expr=-model.y1_6_1 + model.x1_7_1 + model.y1_7_1 + model.z1_7_1 + model.y0_7_1 + model.z0_7_1 + model.x1_7_0 + model.y1_7_0 - 1.0 == 0)
model.v2_7_1 = Constraint(expr=-model.y2_6_1 - model.x1_7_1 + model.x2_7_1 + model.y2_7_1 + model.z2_7_1 + model.x2_7_0 + model.y2_7_0 - 1.0 == 0)
model.v3_7_1 = Constraint(expr=-model.y3_6_1 - model.x2_7_1 + model.x3_7_1 + model.y3_7_1 + model.z3_7_1 + model.x3_7_0 + model.y3_7_0 - 1.0 == 0)
model.v4_7_1 = Constraint(expr=-model.y4_6_1 - model.x3_7_1 + model.x4_7_1 + model.y4_7_1 + model.z4_7_1 + model.x4_7_0 + model.y4_7_0 - 1.0 == 0)
model.v5_7_1 = Constraint(expr=-model.y5_6_1 - model.x4_7_1 + model.x5_7_1 + model.y5_7_1 + model.z5_7_1 + model.x5_7_0 + model.y5_7_0 - 1.0 == 0)
model.v6_7_1 = Constraint(expr=-model.y6_6_1 - model.x5_7_1 + model.x6_7_1 + model.y6_7_1 + model.z6_7_1 + model.x6_7_0 + model.y6_7_0 - 1.0 == 0)
model.v7_7_1 = Constraint(expr=-model.y7_6_1 - model.x6_7_1 + model.x7_7_1 + model.y7_7_1 + model.z7_7_1 + model.x7_7_0 + model.y7_7_0 - 1.0 == 0)
model.v8_7_1 = Constraint(expr=-model.y8_6_1 - model.x7_7_1 + model.x8_7_1 + model.y8_7_1 + model.z8_7_1 + model.x8_7_0 + model.y8_7_0 - 1.0 == 0)
model.v9_7_1 = Constraint(expr=-model.y9_6_1 - model.x8_7_1 + model.x9_7_1 + model.y9_7_1 + model.z9_7_1 + model.x9_7_0 + model.y9_7_0 - 1.0 == 0)
model.v10_7_1 = Constraint(expr=-model.x9_7_1 - model.y10_6_1 + model.y10_7_1 + model.z10_7_1 + model.y11_7_1 + model.z11_7_1 + model.x10_7_0 + model.y10_7_0 - 1.0 == 0)
model.v1_8_1 = Constraint(expr=-model.y1_7_1 + model.x1_8_1 + model.y1_8_1 + model.z1_8_1 + model.y0_8_1 + model.z0_8_1 + model.x1_8_0 + model.y1_8_0 - 1.0 == 0)
model.v2_8_1 = Constraint(expr=-model.y2_7_1 - model.x1_8_1 + model.x2_8_1 + model.y2_8_1 + model.z2_8_1 + model.x2_8_0 + model.y2_8_0 - 1.0 == 0)
model.v3_8_1 = Constraint(expr=-model.y3_7_1 - model.x2_8_1 + model.x3_8_1 + model.y3_8_1 + model.z3_8_1 + model.x3_8_0 + model.y3_8_0 - 1.0 == 0)
model.v4_8_1 = Constraint(expr=-model.y4_7_1 - model.x3_8_1 + model.x4_8_1 + model.y4_8_1 + model.z4_8_1 + model.x4_8_0 + model.y4_8_0 - 1.0 == 0)
model.v5_8_1 = Constraint(expr=-model.y5_7_1 - model.x4_8_1 + model.x5_8_1 + model.y5_8_1 + model.z5_8_1 + model.x5_8_0 + model.y5_8_0 - 1.0 == 0)
model.v6_8_1 = Constraint(expr=-model.y6_7_1 - model.x5_8_1 + model.x6_8_1 + model.y6_8_1 + model.z6_8_1 + model.x6_8_0 + model.y6_8_0 - 1.0 == 0)
model.v7_8_1 = Constraint(expr=-model.y7_7_1 - model.x6_8_1 + model.x7_8_1 + model.y7_8_1 + model.z7_8_1 + model.x7_8_0 + model.y7_8_0 - 1.0 == 0)
model.v8_8_1 = Constraint(expr=-model.y8_7_1 - model.x7_8_1 + model.x8_8_1 + model.y8_8_1 + model.z8_8_1 + model.x8_8_0 + model.y8_8_0 - 1.0 == 0)
model.v9_8_1 = Constraint(expr=-model.y9_7_1 - model.x8_8_1 + model.x9_8_1 + model.y9_8_1 + model.z9_8_1 + model.x9_8_0 + model.y9_8_0 - 1.0 == 0)
model.v10_8_1 = Constraint(expr=-model.x9_8_1 - model.y10_7_1 + model.y10_8_1 + model.z10_8_1 + model.y11_8_1 + model.z11_8_1 + model.x10_8_0 + model.y10_8_0 - 1.0 == 0)
model.v1_9_1 = Constraint(expr=-model.y1_8_1 + model.x1_9_1 + model.y1_9_1 + model.z1_9_1 + model.y0_9_1 + model.z0_9_1 + model.x1_9_0 + model.y1_9_0 - 1.0 == 0)
model.v2_9_1 = Constraint(expr=-model.y2_8_1 - model.x1_9_1 + model.x2_9_1 + model.y2_9_1 + model.z2_9_1 + model.x2_9_0 + model.y2_9_0 - 1.0 == 0)
model.v3_9_1 = Constraint(expr=-model.y3_8_1 - model.x2_9_1 + model.x3_9_1 + model.y3_9_1 + model.z3_9_1 + model.x3_9_0 + model.y3_9_0 - 1.0 == 0)
model.v4_9_1 = Constraint(expr=-model.y4_8_1 - model.x3_9_1 + model.x4_9_1 + model.y4_9_1 + model.z4_9_1 + model.x4_9_0 + model.y4_9_0 - 1.0 == 0)
model.v5_9_1 = Constraint(expr=-model.y5_8_1 - model.x4_9_1 + model.x5_9_1 + model.y5_9_1 + model.z5_9_1 + model.x5_9_0 + model.y5_9_0 - 1.0 == 0)
model.v6_9_1 = Constraint(expr=-model.y6_8_1 - model.x5_9_1 + model.x6_9_1 + model.y6_9_1 + model.z6_9_1 + model.x6_9_0 + model.y6_9_0 - 1.0 == 0)
model.v7_9_1 = Constraint(expr=-model.y7_8_1 - model.x6_9_1 + model.x7_9_1 + model.y7_9_1 + model.z7_9_1 + model.x7_9_0 + model.y7_9_0 - 1.0 == 0)
model.v8_9_1 = Constraint(expr=-model.y8_8_1 - model.x7_9_1 + model.x8_9_1 + model.y8_9_1 + model.z8_9_1 + model.x8_9_0 + model.y8_9_0 - 1.0 == 0)
model.v9_9_1 = Constraint(expr=-model.y9_8_1 - model.x8_9_1 + model.x9_9_1 + model.y9_9_1 + model.z9_9_1 + model.x9_9_0 + model.y9_9_0 - 1.0 == 0)
model.v10_9_1 = Constraint(expr=-model.x9_9_1 - model.y10_8_1 + model.y10_9_1 + model.z10_9_1 + model.y11_9_1 + model.z11_9_1 + model.x10_9_0 + model.y10_9_0 - 1.0 == 0)
model.v1_10_1 = Constraint(expr=-model.y1_9_1 + model.x1_10_1 + model.z1_10_1 + model.y0_10_1 + model.z0_10_1 + model.x1_11_1 + model.z1_11_1 + model.x1_10_0 + model.y1_10_0 - 1.0 == 0)
model.v2_10_1 = Constraint(expr=-model.y2_9_1 - model.x1_10_1 + model.x2_10_1 + model.z2_10_1 + model.x2_11_1 + model.z2_11_1 + model.x2_10_0 + model.y2_10_0 - 1.0 == 0)
model.v3_10_1 = Constraint(expr=-model.y3_9_1 - model.x2_10_1 + model.x3_10_1 + model.z3_10_1 + model.x3_11_1 + model.z3_11_1 + model.x3_10_0 + model.y3_10_0 - 1.0 == 0)
model.v4_10_1 = Constraint(expr=-model.y4_9_1 - model.x3_10_1 + model.x4_10_1 + model.z4_10_1 + model.x4_11_1 + model.z4_11_1 + model.x4_10_0 + model.y4_10_0 - 1.0 == 0)
model.v5_10_1 = Constraint(expr=-model.y5_9_1 - model.x4_10_1 + model.x5_10_1 + model.z5_10_1 + model.x5_11_1 + model.z5_11_1 + model.x5_10_0 + model.y5_10_0 - 1.0 == 0)
model.v6_10_1 = Constraint(expr=-model.y6_9_1 - model.x5_10_1 + model.x6_10_1 + model.z6_10_1 + model.x6_11_1 + model.z6_11_1 + model.x6_10_0 + model.y6_10_0 - 1.0 == 0)
model.v7_10_1 = Constraint(expr=-model.y7_9_1 - model.x6_10_1 + model.x7_10_1 + model.z7_10_1 + model.x7_11_1 + model.z7_11_1 + model.x7_10_0 + model.y7_10_0 - 1.0 == 0)
model.v8_10_1 = Constraint(expr=-model.y8_9_1 - model.x7_10_1 + model.x8_10_1 + model.z8_10_1 + model.x8_11_1 + model.z8_11_1 + model.x8_10_0 + model.y8_10_0 - 1.0 == 0)
model.v9_10_1 = Constraint(expr=-model.y9_9_1 - model.x8_10_1 + model.x9_10_1 + model.z9_10_1 + model.x9_11_1 + model.z9_11_1 + model.x9_10_0 + model.y9_10_0 - 1.0 == 0)
model.v10_10_1 = Constraint(expr=-model.y10_9_1 - model.x9_10_1 + model.y11_10_1 + model.z11_10_1 + model.x10_11_1 + model.z10_11_1 + model.x10_10_0 + model.y10_10_0 - 1.0 == 0)
model.v1_1_2 = Constraint(expr=-model.z1_1_1 + model.x1_1_2 + model.y1_1_2 + model.z1_1_2 + model.y0_1_2 + model.z0_1_2 + model.x1_0_2 + model.z1_0_2 - 1.0 == 0)
model.v2_1_2 = Constraint(expr=-model.z2_1_1 - model.x1_1_2 + model.x2_1_2 + model.y2_1_2 + model.z2_1_2 + model.x2_0_2 + model.z2_0_2 - 1.0 == 0)
model.v3_1_2 = Constraint(expr=-model.z3_1_1 - model.x2_1_2 + model.x3_1_2 + model.y3_1_2 + model.z3_1_2 + model.x3_0_2 + model.z3_0_2 - 1.0 == 0)
model.v4_1_2 = Constraint(expr=-model.z4_1_1 - model.x3_1_2 + model.x4_1_2 + model.y4_1_2 + model.z4_1_2 + model.x4_0_2 + model.z4_0_2 - 1.0 == 0)
model.v5_1_2 = Constraint(expr=-model.z5_1_1 - model.x4_1_2 + model.x5_1_2 + model.y5_1_2 + model.z5_1_2 + model.x5_0_2 + model.z5_0_2 - 1.0 == 0)
model.v6_1_2 = Constraint(expr=-model.z6_1_1 - model.x5_1_2 + model.x6_1_2 + model.y6_1_2 + model.z6_1_2 + model.x6_0_2 + model.z6_0_2 - 1.0 == 0)
model.v7_1_2 = Constraint(expr=-model.z7_1_1 - model.x6_1_2 + model.x7_1_2 + model.y7_1_2 + model.z7_1_2 + model.x7_0_2 + model.z7_0_2 - 1.0 == 0)
model.v8_1_2 = Constraint(expr=-model.z8_1_1 - model.x7_1_2 + model.x8_1_2 + model.y8_1_2 + model.z8_1_2 + model.x8_0_2 + model.z8_0_2 - 1.0 == 0)
model.v9_1_2 = Constraint(expr=-model.z9_1_1 - model.x8_1_2 + model.x9_1_2 + model.y9_1_2 + model.z9_1_2 + model.x9_0_2 + model.z9_0_2 - 1.0 == 0)
model.v10_1_2 = Constraint(expr=-model.x9_1_2 - model.z10_1_1 + model.y10_1_2 + model.z10_1_2 + model.y11_1_2 + model.z11_1_2 + model.x10_0_2 + model.z10_0_2 - 1.0 == 0)
model.v1_2_2 = Constraint(expr=-model.z1_2_1 - model.y1_1_2 + model.x1_2_2 + model.y1_2_2 + model.z1_2_2 + model.y0_2_2 + model.z0_2_2 - 1.0 == 0)
model.v2_2_2 = Constraint(expr=-model.z2_2_1 - model.y2_1_2 - model.x1_2_2 + model.x2_2_2 + model.y2_2_2 + model.z2_2_2 - 1.0 == 0)
model.v3_2_2 = Constraint(expr=-model.z3_2_1 - model.y3_1_2 - model.x2_2_2 + model.x3_2_2 + model.y3_2_2 + model.z3_2_2 - 1.0 == 0)
model.v4_2_2 = Constraint(expr=-model.z4_2_1 - model.y4_1_2 - model.x3_2_2 + model.x4_2_2 + model.y4_2_2 + model.z4_2_2 - 1.0 == 0)
model.v5_2_2 = Constraint(expr=-model.z5_2_1 - model.y5_1_2 - model.x4_2_2 + model.x5_2_2 + model.y5_2_2 + model.z5_2_2 - 1.0 == 0)
model.v6_2_2 = Constraint(expr=-model.z6_2_1 - model.y6_1_2 - model.x5_2_2 + model.x6_2_2 + model.y6_2_2 + model.z6_2_2 - 1.0 == 0)
model.v7_2_2 = Constraint(expr=-model.z7_2_1 - model.y7_1_2 - model.x6_2_2 + model.x7_2_2 + model.y7_2_2 + model.z7_2_2 - 1.0 == 0)
model.v8_2_2 = Constraint(expr=-model.z8_2_1 - model.y8_1_2 - model.x7_2_2 + model.x8_2_2 + model.y8_2_2 + model.z8_2_2 - 1.0 == 0)
model.v9_2_2 = Constraint(expr=-model.z9_2_1 - model.y9_1_2 - model.x8_2_2 + model.x9_2_2 + model.y9_2_2 + model.z9_2_2 - 1.0 == 0)
model.v10_2_2 = Constraint(expr=-model.x9_2_2 - model.z10_2_1 - model.y10_1_2 + model.y10_2_2 + model.z10_2_2 + model.y11_2_2 + model.z11_2_2 - 1.0 == 0)
model.v1_3_2 = Constraint(expr=-model.z1_3_1 - model.y1_2_2 + model.x1_3_2 + model.y1_3_2 + model.z1_3_2 + model.y0_3_2 + model.z0_3_2 - 1.0 == 0)
model.v2_3_2 = Constraint(expr=-model.z2_3_1 - model.y2_2_2 - model.x1_3_2 + model.x2_3_2 + model.y2_3_2 + model.z2_3_2 - 1.0 == 0)
model.v3_3_2 = Constraint(expr=-model.z3_3_1 - model.y3_2_2 - model.x2_3_2 + model.x3_3_2 + model.y3_3_2 + model.z3_3_2 - 1.0 == 0)
model.v4_3_2 = Constraint(expr=-model.z4_3_1 - model.y4_2_2 - model.x3_3_2 + model.x4_3_2 + model.y4_3_2 + model.z4_3_2 - 1.0 == 0)
model.v5_3_2 = Constraint(expr=-model.z5_3_1 - model.y5_2_2 - model.x4_3_2 + model.x5_3_2 + model.y5_3_2 + model.z5_3_2 - 1.0 == 0)
model.v6_3_2 = Constraint(expr=-model.z6_3_1 - model.y6_2_2 - model.x5_3_2 + model.x6_3_2 + model.y6_3_2 + model.z6_3_2 - 1.0 == 0)
model.v7_3_2 = Constraint(expr=-model.z7_3_1 - model.y7_2_2 - model.x6_3_2 + model.x7_3_2 + model.y7_3_2 + model.z7_3_2 - 1.0 == 0)
model.v8_3_2 = Constraint(expr=-model.z8_3_1 - model.y8_2_2 - model.x7_3_2 + model.x8_3_2 + model.y8_3_2 + model.z8_3_2 - 1.0 == 0)
model.v9_3_2 = Constraint(expr=-model.z9_3_1 - model.y9_2_2 - model.x8_3_2 + model.x9_3_2 + model.y9_3_2 + model.z9_3_2 - 1.0 == 0)
model.v10_3_2 = Constraint(expr=-model.x9_3_2 - model.z10_3_1 - model.y10_2_2 + model.y10_3_2 + model.z10_3_2 + model.y11_3_2 + model.z11_3_2 - 1.0 == 0)
model.v1_4_2 = Constraint(expr=-model.z1_4_1 - model.y1_3_2 + model.x1_4_2 + model.y1_4_2 + model.z1_4_2 + model.y0_4_2 + model.z0_4_2 - 1.0 == 0)
model.v2_4_2 = Constraint(expr=-model.z2_4_1 - model.y2_3_2 - model.x1_4_2 + model.x2_4_2 + model.y2_4_2 + model.z2_4_2 - 1.0 == 0)
model.v3_4_2 = Constraint(expr=-model.z3_4_1 - model.y3_3_2 - model.x2_4_2 + model.x3_4_2 + model.y3_4_2 + model.z3_4_2 - 1.0 == 0)
model.v4_4_2 = Constraint(expr=-model.z4_4_1 - model.y4_3_2 - model.x3_4_2 + model.x4_4_2 + model.y4_4_2 + model.z4_4_2 - 1.0 == 0)
model.v5_4_2 = Constraint(expr=-model.z5_4_1 - model.y5_3_2 - model.x4_4_2 + model.x5_4_2 + model.y5_4_2 + model.z5_4_2 - 1.0 == 0)
model.v6_4_2 = Constraint(expr=-model.z6_4_1 - model.y6_3_2 - model.x5_4_2 + model.x6_4_2 + model.y6_4_2 + model.z6_4_2 - 1.0 == 0)
model.v7_4_2 = Constraint(expr=-model.z7_4_1 - model.y7_3_2 - model.x6_4_2 + model.x7_4_2 + model.y7_4_2 + model.z7_4_2 - 1.0 == 0)
model.v8_4_2 = Constraint(expr=-model.z8_4_1 - model.y8_3_2 - model.x7_4_2 + model.x8_4_2 + model.y8_4_2 + model.z8_4_2 - 1.0 == 0)
model.v9_4_2 = Constraint(expr=-model.z9_4_1 - model.y9_3_2 - model.x8_4_2 + model.x9_4_2 + model.y9_4_2 + model.z9_4_2 - 1.0 == 0)
model.v10_4_2 = Constraint(expr=-model.x9_4_2 - model.z10_4_1 - model.y10_3_2 + model.y10_4_2 + model.z10_4_2 + model.y11_4_2 + model.z11_4_2 - 1.0 == 0)
model.v1_5_2 = Constraint(expr=-model.z1_5_1 - model.y1_4_2 + model.x1_5_2 + model.y1_5_2 + model.z1_5_2 + model.y0_5_2 + model.z0_5_2 - 1.0 == 0)
model.v2_5_2 = Constraint(expr=-model.z2_5_1 - model.y2_4_2 - model.x1_5_2 + model.x2_5_2 + model.y2_5_2 + model.z2_5_2 - 1.0 == 0)
model.v3_5_2 = Constraint(expr=-model.z3_5_1 - model.y3_4_2 - model.x2_5_2 + model.x3_5_2 + model.y3_5_2 + model.z3_5_2 - 1.0 == 0)
model.v4_5_2 = Constraint(expr=-model.z4_5_1 - model.y4_4_2 - model.x3_5_2 + model.x4_5_2 + model.y4_5_2 + model.z4_5_2 - 1.0 == 0)
model.v5_5_2 = Constraint(expr=-model.z5_5_1 - model.y5_4_2 - model.x4_5_2 + model.x5_5_2 + model.y5_5_2 + model.z5_5_2 - 1.0 == 0)
model.v6_5_2 = Constraint(expr=-model.z6_5_1 - model.y6_4_2 - model.x5_5_2 + model.x6_5_2 + model.y6_5_2 + model.z6_5_2 - 1.0 == 0)
model.v7_5_2 = Constraint(expr=-model.z7_5_1 - model.y7_4_2 - model.x6_5_2 + model.x7_5_2 + model.y7_5_2 + model.z7_5_2 - 1.0 == 0)
model.v8_5_2 = Constraint(expr=-model.z8_5_1 - model.y8_4_2 - model.x7_5_2 + model.x8_5_2 + model.y8_5_2 + model.z8_5_2 - 1.0 == 0)
model.v9_5_2 = Constraint(expr=-model.z9_5_1 - model.y9_4_2 - model.x8_5_2 + model.x9_5_2 + model.y9_5_2 + model.z9_5_2 - 1.0 == 0)
model.v10_5_2 = Constraint(expr=-model.x9_5_2 - model.z10_5_1 - model.y10_4_2 + model.y10_5_2 + model.z10_5_2 + model.y11_5_2 + model.z11_5_2 - 1.0 == 0)
model.v1_6_2 = Constraint(expr=-model.z1_6_1 - model.y1_5_2 + model.x1_6_2 + model.y1_6_2 + model.z1_6_2 + model.y0_6_2 + model.z0_6_2 - 1.0 == 0)
model.v2_6_2 = Constraint(expr=-model.z2_6_1 - model.y2_5_2 - model.x1_6_2 + model.x2_6_2 + model.y2_6_2 + model.z2_6_2 - 1.0 == 0)
model.v3_6_2 = Constraint(expr=-model.z3_6_1 - model.y3_5_2 - model.x2_6_2 + model.x3_6_2 + model.y3_6_2 + model.z3_6_2 - 1.0 == 0)
model.v4_6_2 = Constraint(expr=-model.z4_6_1 - model.y4_5_2 - model.x3_6_2 + model.x4_6_2 + model.y4_6_2 + model.z4_6_2 - 1.0 == 0)
model.v5_6_2 = Constraint(expr=-model.z5_6_1 - model.y5_5_2 - model.x4_6_2 + model.x5_6_2 + model.y5_6_2 + model.z5_6_2 - 1.0 == 0)
model.v6_6_2 = Constraint(expr=-model.z6_6_1 - model.y6_5_2 - model.x5_6_2 + model.x6_6_2 + model.y6_6_2 + model.z6_6_2 - 1.0 == 0)
model.v7_6_2 = Constraint(expr=-model.z7_6_1 - model.y7_5_2 - model.x6_6_2 + model.x7_6_2 + model.y7_6_2 + model.z7_6_2 - 1.0 == 0)
model.v8_6_2 = Constraint(expr=-model.z8_6_1 - model.y8_5_2 - model.x7_6_2 + model.x8_6_2 + model.y8_6_2 + model.z8_6_2 - 1.0 == 0)
model.v9_6_2 = Constraint(expr=-model.z9_6_1 - model.y9_5_2 - model.x8_6_2 + model.x9_6_2 + model.y9_6_2 + model.z9_6_2 - 1.0 == 0)
model.v10_6_2 = Constraint(expr=-model.x9_6_2 - model.z10_6_1 - model.y10_5_2 + model.y10_6_2 + model.z10_6_2 + model.y11_6_2 + model.z11_6_2 - 1.0 == 0)
model.v1_7_2 = Constraint(expr=-model.z1_7_1 - model.y1_6_2 + model.x1_7_2 + model.y1_7_2 + model.z1_7_2 + model.y0_7_2 + model.z0_7_2 - 1.0 == 0)
model.v2_7_2 = Constraint(expr=-model.z2_7_1 - model.y2_6_2 - model.x1_7_2 + model.x2_7_2 + model.y2_7_2 + model.z2_7_2 - 1.0 == 0)
model.v3_7_2 = Constraint(expr=-model.z3_7_1 - model.y3_6_2 - model.x2_7_2 + model.x3_7_2 + model.y3_7_2 + model.z3_7_2 - 1.0 == 0)
model.v4_7_2 = Constraint(expr=-model.z4_7_1 - model.y4_6_2 - model.x3_7_2 + model.x4_7_2 + model.y4_7_2 + model.z4_7_2 - 1.0 == 0)
model.v5_7_2 = Constraint(expr=-model.z5_7_1 - model.y5_6_2 - model.x4_7_2 + model.x5_7_2 + model.y5_7_2 + model.z5_7_2 - 1.0 == 0)
model.v6_7_2 = Constraint(expr=-model.z6_7_1 - model.y6_6_2 - model.x5_7_2 + model.x6_7_2 + model.y6_7_2 + model.z6_7_2 - 1.0 == 0)
model.v7_7_2 = Constraint(expr=-model.z7_7_1 - model.y7_6_2 - model.x6_7_2 + model.x7_7_2 + model.y7_7_2 + model.z7_7_2 - 1.0 == 0)
model.v8_7_2 = Constraint(expr=-model.z8_7_1 - model.y8_6_2 - model.x7_7_2 + model.x8_7_2 + model.y8_7_2 + model.z8_7_2 - 1.0 == 0)
model.v9_7_2 = Constraint(expr=-model.z9_7_1 - model.y9_6_2 - model.x8_7_2 + model.x9_7_2 + model.y9_7_2 + model.z9_7_2 - 1.0 == 0)
model.v10_7_2 = Constraint(expr=-model.x9_7_2 - model.z10_7_1 - model.y10_6_2 + model.y10_7_2 + model.z10_7_2 + model.y11_7_2 + model.z11_7_2 - 1.0 == 0)
model.v1_8_2 = Constraint(expr=-model.z1_8_1 - model.y1_7_2 + model.x1_8_2 + model.y1_8_2 + model.z1_8_2 + model.y0_8_2 + model.z0_8_2 - 1.0 == 0)
model.v2_8_2 = Constraint(expr=-model.z2_8_1 - model.y2_7_2 - model.x1_8_2 + model.x2_8_2 + model.y2_8_2 + model.z2_8_2 - 1.0 == 0)
model.v3_8_2 = Constraint(expr=-model.z3_8_1 - model.y3_7_2 - model.x2_8_2 + model.x3_8_2 + model.y3_8_2 + model.z3_8_2 - 1.0 == 0)
model.v4_8_2 = Constraint(expr=-model.z4_8_1 - model.y4_7_2 - model.x3_8_2 + model.x4_8_2 + model.y4_8_2 + model.z4_8_2 - 1.0 == 0)
model.v5_8_2 = Constraint(expr=-model.z5_8_1 - model.y5_7_2 - model.x4_8_2 + model.x5_8_2 + model.y5_8_2 + model.z5_8_2 - 1.0 == 0)
model.v6_8_2 = Constraint(expr=-model.z6_8_1 - model.y6_7_2 - model.x5_8_2 + model.x6_8_2 + model.y6_8_2 + model.z6_8_2 - 1.0 == 0)
model.v7_8_2 = Constraint(expr=-model.z7_8_1 - model.y7_7_2 - model.x6_8_2 + model.x7_8_2 + model.y7_8_2 + model.z7_8_2 - 1.0 == 0)
model.v8_8_2 = Constraint(expr=-model.z8_8_1 - model.y8_7_2 - model.x7_8_2 + model.x8_8_2 + model.y8_8_2 + model.z8_8_2 - 1.0 == 0)
model.v9_8_2 = Constraint(expr=-model.z9_8_1 - model.y9_7_2 - model.x8_8_2 + model.x9_8_2 + model.y9_8_2 + model.z9_8_2 - 1.0 == 0)
model.v10_8_2 = Constraint(expr=-model.x9_8_2 - model.z10_8_1 - model.y10_7_2 + model.y10_8_2 + model.z10_8_2 + model.y11_8_2 + model.z11_8_2 - 1.0 == 0)
model.v1_9_2 = Constraint(expr=-model.z1_9_1 - model.y1_8_2 + model.x1_9_2 + model.y1_9_2 + model.z1_9_2 + model.y0_9_2 + model.z0_9_2 - 1.0 == 0)
model.v2_9_2 = Constraint(expr=-model.z2_9_1 - model.y2_8_2 - model.x1_9_2 + model.x2_9_2 + model.y2_9_2 + model.z2_9_2 - 1.0 == 0)
model.v3_9_2 = Constraint(expr=-model.z3_9_1 - model.y3_8_2 - model.x2_9_2 + model.x3_9_2 + model.y3_9_2 + model.z3_9_2 - 1.0 == 0)
model.v4_9_2 = Constraint(expr=-model.z4_9_1 - model.y4_8_2 - model.x3_9_2 + model.x4_9_2 + model.y4_9_2 + model.z4_9_2 - 1.0 == 0)
model.v5_9_2 = Constraint(expr=-model.z5_9_1 - model.y5_8_2 - model.x4_9_2 + model.x5_9_2 + model.y5_9_2 + model.z5_9_2 - 1.0 == 0)
model.v6_9_2 = Constraint(expr=-model.z6_9_1 - model.y6_8_2 - model.x5_9_2 + model.x6_9_2 + model.y6_9_2 + model.z6_9_2 - 1.0 == 0)
model.v7_9_2 = Constraint(expr=-model.z7_9_1 - model.y7_8_2 - model.x6_9_2 + model.x7_9_2 + model.y7_9_2 + model.z7_9_2 - 1.0 == 0)
model.v8_9_2 = Constraint(expr=-model.z8_9_1 - model.y8_8_2 - model.x7_9_2 + model.x8_9_2 + model.y8_9_2 + model.z8_9_2 - 1.0 == 0)
model.v9_9_2 = Constraint(expr=-model.z9_9_1 - model.y9_8_2 - model.x8_9_2 + model.x9_9_2 + model.y9_9_2 + model.z9_9_2 - 1.0 == 0)
model.v10_9_2 = Constraint(expr=-model.x9_9_2 - model.z10_9_1 - model.y10_8_2 + model.y10_9_2 + model.z10_9_2 + model.y11_9_2 + model.z11_9_2 - 1.0 == 0)
model.v1_10_2 = Constraint(expr=-model.y1_9_2 - model.z1_10_1 + model.x1_10_2 + model.z1_10_2 + model.y0_10_2 + model.z0_10_2 + model.x1_11_2 + model.z1_11_2 - 1.0 == 0)
model.v2_10_2 = Constraint(expr=-model.y2_9_2 - model.z2_10_1 - model.x1_10_2 + model.x2_10_2 + model.z2_10_2 + model.x2_11_2 + model.z2_11_2 - 1.0 == 0)
model.v3_10_2 = Constraint(expr=-model.y3_9_2 - model.z3_10_1 - model.x2_10_2 + model.x3_10_2 + model.z3_10_2 + model.x3_11_2 + model.z3_11_2 - 1.0 == 0)
model.v4_10_2 = Constraint(expr=-model.y4_9_2 - model.z4_10_1 - model.x3_10_2 + model.x4_10_2 + model.z4_10_2 + model.x4_11_2 + model.z4_11_2 - 1.0 == 0)
model.v5_10_2 = Constraint(expr=-model.y5_9_2 - model.z5_10_1 - model.x4_10_2 + model.x5_10_2 + model.z5_10_2 + model.x5_11_2 + model.z5_11_2 - 1.0 == 0)
model.v6_10_2 = Constraint(expr=-model.y6_9_2 - model.z6_10_1 - model.x5_10_2 + model.x6_10_2 + model.z6_10_2 + model.x6_11_2 + model.z6_11_2 - 1.0 == 0)
model.v7_10_2 = Constraint(expr=-model.y7_9_2 - model.z7_10_1 - model.x6_10_2 + model.x7_10_2 + model.z7_10_2 + model.x7_11_2 + model.z7_11_2 - 1.0 == 0)
model.v8_10_2 = Constraint(expr=-model.y8_9_2 - model.z8_10_1 - model.x7_10_2 + model.x8_10_2 + model.z8_10_2 + model.x8_11_2 + model.z8_11_2 - 1.0 == 0)
model.v9_10_2 = Constraint(expr=-model.y9_9_2 - model.z9_10_1 - model.x8_10_2 + model.x9_10_2 + model.z9_10_2 + model.x9_11_2 + model.z9_11_2 - 1.0 == 0)
model.v10_10_2 = Constraint(expr=-model.y10_9_2 - model.x9_10_2 + model.y11_10_2 + model.z11_10_2 + model.x10_11_2 + model.z10_11_2 - 1.0 == 0)
model.v1_1_3 = Constraint(expr=-model.z1_1_2 + model.x1_1_3 + model.y1_1_3 + model.z1_1_3 + model.y0_1_3 + model.z0_1_3 + model.x1_0_3 + model.z1_0_3 - 1.0 == 0)
model.v2_1_3 = Constraint(expr=-model.z2_1_2 - model.x1_1_3 + model.x2_1_3 + model.y2_1_3 + model.z2_1_3 + model.x2_0_3 + model.z2_0_3 - 1.0 == 0)
model.v3_1_3 = Constraint(expr=-model.z3_1_2 - model.x2_1_3 + model.x3_1_3 + model.y3_1_3 + model.z3_1_3 + model.x3_0_3 + model.z3_0_3 - 1.0 == 0)
model.v4_1_3 = Constraint(expr=-model.z4_1_2 - model.x3_1_3 + model.x4_1_3 + model.y4_1_3 + model.z4_1_3 + model.x4_0_3 + model.z4_0_3 - 1.0 == 0)
model.v5_1_3 = Constraint(expr=-model.z5_1_2 - model.x4_1_3 + model.x5_1_3 + model.y5_1_3 + model.z5_1_3 + model.x5_0_3 + model.z5_0_3 - 1.0 == 0)
model.v6_1_3 = Constraint(expr=-model.z6_1_2 - model.x5_1_3 + model.x6_1_3 + model.y6_1_3 + model.z6_1_3 + model.x6_0_3 + model.z6_0_3 - 1.0 == 0)
model.v7_1_3 = Constraint(expr=-model.z7_1_2 - model.x6_1_3 + model.x7_1_3 + model.y7_1_3 + model.z7_1_3 + model.x7_0_3 + model.z7_0_3 - 1.0 == 0)
model.v8_1_3 = Constraint(expr=-model.z8_1_2 - model.x7_1_3 + model.x8_1_3 + model.y8_1_3 + model.z8_1_3 + model.x8_0_3 + model.z8_0_3 - 1.0 == 0)
model.v9_1_3 = Constraint(expr=-model.z9_1_2 - model.x8_1_3 + model.x9_1_3 + model.y9_1_3 + model.z9_1_3 + model.x9_0_3 + model.z9_0_3 - 1.0 == 0)
model.v10_1_3 = Constraint(expr=-model.x9_1_3 - model.z10_1_2 + model.y10_1_3 + model.z10_1_3 + model.y11_1_3 + model.z11_1_3 + model.x10_0_3 + model.z10_0_3 - 1.0 == 0)
model.v1_2_3 = Constraint(expr=-model.z1_2_2 - model.y1_1_3 + model.x1_2_3 + model.y1_2_3 + model.z1_2_3 + model.y0_2_3 + model.z0_2_3 - 1.0 == 0)
model.v2_2_3 = Constraint(expr=-model.z2_2_2 - model.y2_1_3 - model.x1_2_3 + model.x2_2_3 + model.y2_2_3 + model.z2_2_3 - 1.0 == 0)
model.v3_2_3 = Constraint(expr=-model.z3_2_2 - model.y3_1_3 - model.x2_2_3 + model.x3_2_3 + model.y3_2_3 + model.z3_2_3 - 1.0 == 0)
model.v4_2_3 = Constraint(expr=-model.z4_2_2 - model.y4_1_3 - model.x3_2_3 + model.x4_2_3 + model.y4_2_3 + model.z4_2_3 - 1.0 == 0)
model.v5_2_3 = Constraint(expr=-model.z5_2_2 - model.y5_1_3 - model.x4_2_3 + model.x5_2_3 + model.y5_2_3 + model.z5_2_3 - 1.0 == 0)
model.v6_2_3 = Constraint(expr=-model.z6_2_2 - model.y6_1_3 - model.x5_2_3 + model.x6_2_3 + model.y6_2_3 + model.z6_2_3 - 1.0 == 0)
model.v7_2_3 = Constraint(expr=-model.z7_2_2 - model.y7_1_3 - model.x6_2_3 + model.x7_2_3 + model.y7_2_3 + model.z7_2_3 - 1.0 == 0)
model.v8_2_3 = Constraint(expr=-model.z8_2_2 - model.y8_1_3 - model.x7_2_3 + model.x8_2_3 + model.y8_2_3 + model.z8_2_3 - 1.0 == 0)
model.v9_2_3 = Constraint(expr=-model.z9_2_2 - model.y9_1_3 - model.x8_2_3 + model.x9_2_3 + model.y9_2_3 + model.z9_2_3 - 1.0 == 0)
model.v10_2_3 = Constraint(expr=-model.x9_2_3 - model.z10_2_2 - model.y10_1_3 + model.y10_2_3 + model.z10_2_3 + model.y11_2_3 + model.z11_2_3 - 1.0 == 0)
model.v1_3_3 = Constraint(expr=-model.z1_3_2 - model.y1_2_3 + model.x1_3_3 + model.y1_3_3 + model.z1_3_3 + model.y0_3_3 + model.z0_3_3 - 1.0 == 0)
model.v2_3_3 = Constraint(expr=-model.z2_3_2 - model.y2_2_3 - model.x1_3_3 + model.x2_3_3 + model.y2_3_3 + model.z2_3_3 - 1.0 == 0)
model.v3_3_3 = Constraint(expr=-model.z3_3_2 - model.y3_2_3 - model.x2_3_3 + model.x3_3_3 + model.y3_3_3 + model.z3_3_3 - 1.0 == 0)
model.v4_3_3 = Constraint(expr=-model.z4_3_2 - model.y4_2_3 - model.x3_3_3 + model.x4_3_3 + model.y4_3_3 + model.z4_3_3 - 1.0 == 0)
model.v5_3_3 = Constraint(expr=-model.z5_3_2 - model.y5_2_3 - model.x4_3_3 + model.x5_3_3 + model.y5_3_3 + model.z5_3_3 - 1.0 == 0)
model.v6_3_3 = Constraint(expr=-model.z6_3_2 - model.y6_2_3 - model.x5_3_3 + model.x6_3_3 + model.y6_3_3 + model.z6_3_3 - 1.0 == 0)
model.v7_3_3 = Constraint(expr=-model.z7_3_2 - model.y7_2_3 - model.x6_3_3 + model.x7_3_3 + model.y7_3_3 + model.z7_3_3 - 1.0 == 0)
model.v8_3_3 = Constraint(expr=-model.z8_3_2 - model.y8_2_3 - model.x7_3_3 + model.x8_3_3 + model.y8_3_3 + model.z8_3_3 - 1.0 == 0)
model.v9_3_3 = Constraint(expr=-model.z9_3_2 - model.y9_2_3 - model.x8_3_3 + model.x9_3_3 + model.y9_3_3 + model.z9_3_3 - 1.0 == 0)
model.v10_3_3 = Constraint(expr=-model.x9_3_3 - model.z10_3_2 - model.y10_2_3 + model.y10_3_3 + model.z10_3_3 + model.y11_3_3 + model.z11_3_3 - 1.0 == 0)
model.v1_4_3 = Constraint(expr=-model.z1_4_2 - model.y1_3_3 + model.x1_4_3 + model.y1_4_3 + model.z1_4_3 + model.y0_4_3 + model.z0_4_3 - 1.0 == 0)
model.v2_4_3 = Constraint(expr=-model.z2_4_2 - model.y2_3_3 - model.x1_4_3 + model.x2_4_3 + model.y2_4_3 + model.z2_4_3 - 1.0 == 0)
model.v3_4_3 = Constraint(expr=-model.z3_4_2 - model.y3_3_3 - model.x2_4_3 + model.x3_4_3 + model.y3_4_3 + model.z3_4_3 - 1.0 == 0)
model.v4_4_3 = Constraint(expr=-model.z4_4_2 - model.y4_3_3 - model.x3_4_3 + model.x4_4_3 + model.y4_4_3 + model.z4_4_3 - 1.0 == 0)
model.v5_4_3 = Constraint(expr=-model.z5_4_2 - model.y5_3_3 - model.x4_4_3 + model.x5_4_3 + model.y5_4_3 + model.z5_4_3 - 1.0 == 0)
model.v6_4_3 = Constraint(expr=-model.z6_4_2 - model.y6_3_3 - model.x5_4_3 + model.x6_4_3 + model.y6_4_3 + model.z6_4_3 - 1.0 == 0)
model.v7_4_3 = Constraint(expr=-model.z7_4_2 - model.y7_3_3 - model.x6_4_3 + model.x7_4_3 + model.y7_4_3 + model.z7_4_3 - 1.0 == 0)
model.v8_4_3 = Constraint(expr=-model.z8_4_2 - model.y8_3_3 - model.x7_4_3 + model.x8_4_3 + model.y8_4_3 + model.z8_4_3 - 1.0 == 0)
model.v9_4_3 = Constraint(expr=-model.z9_4_2 - model.y9_3_3 - model.x8_4_3 + model.x9_4_3 + model.y9_4_3 + model.z9_4_3 - 1.0 == 0)
model.v10_4_3 = Constraint(expr=-model.x9_4_3 - model.z10_4_2 - model.y10_3_3 + model.y10_4_3 + model.z10_4_3 + model.y11_4_3 + model.z11_4_3 - 1.0 == 0)
model.v1_5_3 = Constraint(expr=-model.z1_5_2 - model.y1_4_3 + model.x1_5_3 + model.y1_5_3 + model.z1_5_3 + model.y0_5_3 + model.z0_5_3 - 1.0 == 0)
model.v2_5_3 = Constraint(expr=-model.z2_5_2 - model.y2_4_3 - model.x1_5_3 + model.x2_5_3 + model.y2_5_3 + model.z2_5_3 - 1.0 == 0)
model.v3_5_3 = Constraint(expr=-model.z3_5_2 - model.y3_4_3 - model.x2_5_3 + model.x3_5_3 + model.y3_5_3 + model.z3_5_3 - 1.0 == 0)
model.v4_5_3 = Constraint(expr=-model.z4_5_2 - model.y4_4_3 - model.x3_5_3 + model.x4_5_3 + model.y4_5_3 + model.z4_5_3 - 1.0 == 0)
model.v5_5_3 = Constraint(expr=-model.z5_5_2 - model.y5_4_3 - model.x4_5_3 + model.x5_5_3 + model.y5_5_3 + model.z5_5_3 - 1.0 == 0)
model.v6_5_3 = Constraint(expr=-model.z6_5_2 - model.y6_4_3 - model.x5_5_3 + model.x6_5_3 + model.y6_5_3 + model.z6_5_3 - 1.0 == 0)
model.v7_5_3 = Constraint(expr=-model.z7_5_2 - model.y7_4_3 - model.x6_5_3 + model.x7_5_3 + model.y7_5_3 + model.z7_5_3 - 1.0 == 0)
model.v8_5_3 = Constraint(expr=-model.z8_5_2 - model.y8_4_3 - model.x7_5_3 + model.x8_5_3 + model.y8_5_3 + model.z8_5_3 - 1.0 == 0)
model.v9_5_3 = Constraint(expr=-model.z9_5_2 - model.y9_4_3 - model.x8_5_3 + model.x9_5_3 + model.y9_5_3 + model.z9_5_3 - 1.0 == 0)
model.v10_5_3 = Constraint(expr=-model.x9_5_3 - model.z10_5_2 - model.y10_4_3 + model.y10_5_3 + model.z10_5_3 + model.y11_5_3 + model.z11_5_3 - 1.0 == 0)
model.v1_6_3 = Constraint(expr=-model.z1_6_2 - model.y1_5_3 + model.x1_6_3 + model.y1_6_3 + model.z1_6_3 + model.y0_6_3 + model.z0_6_3 - 1.0 == 0)
model.v2_6_3 = Constraint(expr=-model.z2_6_2 - model.y2_5_3 - model.x1_6_3 + model.x2_6_3 + model.y2_6_3 + model.z2_6_3 - 1.0 == 0)
model.v3_6_3 = Constraint(expr=-model.z3_6_2 - model.y3_5_3 - model.x2_6_3 + model.x3_6_3 + model.y3_6_3 + model.z3_6_3 - 1.0 == 0)
model.v4_6_3 = Constraint(expr=-model.z4_6_2 - model.y4_5_3 - model.x3_6_3 + model.x4_6_3 + model.y4_6_3 + model.z4_6_3 - 1.0 == 0)
model.v5_6_3 = Constraint(expr=-model.z5_6_2 - model.y5_5_3 - model.x4_6_3 + model.x5_6_3 + model.y5_6_3 + model.z5_6_3 - 1.0 == 0)
model.v6_6_3 = Constraint(expr=-model.z6_6_2 - model.y6_5_3 - model.x5_6_3 + model.x6_6_3 + model.y6_6_3 + model.z6_6_3 - 1.0 == 0)
model.v7_6_3 = Constraint(expr=-model.z7_6_2 - model.y7_5_3 - model.x6_6_3 + model.x7_6_3 + model.y7_6_3 + model.z7_6_3 - 1.0 == 0)
model.v8_6_3 = Constraint(expr=-model.z8_6_2 - model.y8_5_3 - model.x7_6_3 + model.x8_6_3 + model.y8_6_3 + model.z8_6_3 - 1.0 == 0)
model.v9_6_3 = Constraint(expr=-model.z9_6_2 - model.y9_5_3 - model.x8_6_3 + model.x9_6_3 + model.y9_6_3 + model.z9_6_3 - 1.0 == 0)
model.v10_6_3 = Constraint(expr=-model.x9_6_3 - model.z10_6_2 - model.y10_5_3 + model.y10_6_3 + model.z10_6_3 + model.y11_6_3 + model.z11_6_3 - 1.0 == 0)
model.v1_7_3 = Constraint(expr=-model.z1_7_2 - model.y1_6_3 + model.x1_7_3 + model.y1_7_3 + model.z1_7_3 + model.y0_7_3 + model.z0_7_3 - 1.0 == 0)
model.v2_7_3 = Constraint(expr=-model.z2_7_2 - model.y2_6_3 - model.x1_7_3 + model.x2_7_3 + model.y2_7_3 + model.z2_7_3 - 1.0 == 0)
model.v3_7_3 = Constraint(expr=-model.z3_7_2 - model.y3_6_3 - model.x2_7_3 + model.x3_7_3 + model.y3_7_3 + model.z3_7_3 - 1.0 == 0)
model.v4_7_3 = Constraint(expr=-model.z4_7_2 - model.y4_6_3 - model.x3_7_3 + model.x4_7_3 + model.y4_7_3 + model.z4_7_3 - 1.0 == 0)
model.v5_7_3 = Constraint(expr=-model.z5_7_2 - model.y5_6_3 - model.x4_7_3 + model.x5_7_3 + model.y5_7_3 + model.z5_7_3 - 1.0 == 0)
model.v6_7_3 = Constraint(expr=-model.z6_7_2 - model.y6_6_3 - model.x5_7_3 + model.x6_7_3 + model.y6_7_3 + model.z6_7_3 - 1.0 == 0)
model.v7_7_3 = Constraint(expr=-model.z7_7_2 - model.y7_6_3 - model.x6_7_3 + model.x7_7_3 + model.y7_7_3 + model.z7_7_3 - 1.0 == 0)
model.v8_7_3 = Constraint(expr=-model.z8_7_2 - model.y8_6_3 - model.x7_7_3 + model.x8_7_3 + model.y8_7_3 + model.z8_7_3 - 1.0 == 0)
model.v9_7_3 = Constraint(expr=-model.z9_7_2 - model.y9_6_3 - model.x8_7_3 + model.x9_7_3 + model.y9_7_3 + model.z9_7_3 - 1.0 == 0)
model.v10_7_3 = Constraint(expr=-model.x9_7_3 - model.z10_7_2 - model.y10_6_3 + model.y10_7_3 + model.z10_7_3 + model.y11_7_3 + model.z11_7_3 - 1.0 == 0)
model.v1_8_3 = Constraint(expr=-model.z1_8_2 - model.y1_7_3 + model.x1_8_3 + model.y1_8_3 + model.z1_8_3 + model.y0_8_3 + model.z0_8_3 - 1.0 == 0)
model.v2_8_3 = Constraint(expr=-model.z2_8_2 - model.y2_7_3 - model.x1_8_3 + model.x2_8_3 + model.y2_8_3 + model.z2_8_3 - 1.0 == 0)
model.v3_8_3 = Constraint(expr=-model.z3_8_2 - model.y3_7_3 - model.x2_8_3 + model.x3_8_3 + model.y3_8_3 + model.z3_8_3 - 1.0 == 0)
model.v4_8_3 = Constraint(expr=-model.z4_8_2 - model.y4_7_3 - model.x3_8_3 + model.x4_8_3 + model.y4_8_3 + model.z4_8_3 - 1.0 == 0)
model.v5_8_3 = Constraint(expr=-model.z5_8_2 - model.y5_7_3 - model.x4_8_3 + model.x5_8_3 + model.y5_8_3 + model.z5_8_3 - 1.0 == 0)
model.v6_8_3 = Constraint(expr=-model.z6_8_2 - model.y6_7_3 - model.x5_8_3 + model.x6_8_3 + model.y6_8_3 + model.z6_8_3 - 1.0 == 0)
model.v7_8_3 = Constraint(expr=-model.z7_8_2 - model.y7_7_3 - model.x6_8_3 + model.x7_8_3 + model.y7_8_3 + model.z7_8_3 - 1.0 == 0)
model.v8_8_3 = Constraint(expr=-model.z8_8_2 - model.y8_7_3 - model.x7_8_3 + model.x8_8_3 + model.y8_8_3 + model.z8_8_3 - 1.0 == 0)
model.v9_8_3 = Constraint(expr=-model.z9_8_2 - model.y9_7_3 - model.x8_8_3 + model.x9_8_3 + model.y9_8_3 + model.z9_8_3 - 1.0 == 0)
model.v10_8_3 = Constraint(expr=-model.x9_8_3 - model.z10_8_2 - model.y10_7_3 + model.y10_8_3 + model.z10_8_3 + model.y11_8_3 + model.z11_8_3 - 1.0 == 0)
model.v1_9_3 = Constraint(expr=-model.z1_9_2 - model.y1_8_3 + model.x1_9_3 + model.y1_9_3 + model.z1_9_3 + model.y0_9_3 + model.z0_9_3 - 1.0 == 0)
model.v2_9_3 = Constraint(expr=-model.z2_9_2 - model.y2_8_3 - model.x1_9_3 + model.x2_9_3 + model.y2_9_3 + model.z2_9_3 - 1.0 == 0)
model.v3_9_3 = Constraint(expr=-model.z3_9_2 - model.y3_8_3 - model.x2_9_3 + model.x3_9_3 + model.y3_9_3 + model.z3_9_3 - 1.0 == 0)
model.v4_9_3 = Constraint(expr=-model.z4_9_2 - model.y4_8_3 - model.x3_9_3 + model.x4_9_3 + model.y4_9_3 + model.z4_9_3 - 1.0 == 0)
model.v5_9_3 = Constraint(expr=-model.z5_9_2 - model.y5_8_3 - model.x4_9_3 + model.x5_9_3 + model.y5_9_3 + model.z5_9_3 - 1.0 == 0)
model.v6_9_3 = Constraint(expr=-model.z6_9_2 - model.y6_8_3 - model.x5_9_3 + model.x6_9_3 + model.y6_9_3 + model.z6_9_3 - 1.0 == 0)
model.v7_9_3 = Constraint(expr=-model.z7_9_2 - model.y7_8_3 - model.x6_9_3 + model.x7_9_3 + model.y7_9_3 + model.z7_9_3 - 1.0 == 0)
model.v8_9_3 = Constraint(expr=-model.z8_9_2 - model.y8_8_3 - model.x7_9_3 + model.x8_9_3 + model.y8_9_3 + model.z8_9_3 - 1.0 == 0)
model.v9_9_3 = Constraint(expr=-model.z9_9_2 - model.y9_8_3 - model.x8_9_3 + model.x9_9_3 + model.y9_9_3 + model.z9_9_3 - 1.0 == 0)
model.v10_9_3 = Constraint(expr=-model.x9_9_3 - model.z10_9_2 - model.y10_8_3 + model.y10_9_3 + model.z10_9_3 + model.y11_9_3 + model.z11_9_3 - 1.0 == 0)
model.v1_10_3 = Constraint(expr=-model.y1_9_3 - model.z1_10_2 + model.x1_10_3 + model.z1_10_3 + model.y0_10_3 + model.z0_10_3 + model.x1_11_3 + model.z1_11_3 - 1.0 == 0)
model.v2_10_3 = Constraint(expr=-model.y2_9_3 - model.z2_10_2 - model.x1_10_3 + model.x2_10_3 + model.z2_10_3 + model.x2_11_3 + model.z2_11_3 - 1.0 == 0)
model.v3_10_3 = Constraint(expr=-model.y3_9_3 - model.z3_10_2 - model.x2_10_3 + model.x3_10_3 + model.z3_10_3 + model.x3_11_3 + model.z3_11_3 - 1.0 == 0)
model.v4_10_3 = Constraint(expr=-model.y4_9_3 - model.z4_10_2 - model.x3_10_3 + model.x4_10_3 + model.z4_10_3 + model.x4_11_3 + model.z4_11_3 - 1.0 == 0)
model.v5_10_3 = Constraint(expr=-model.y5_9_3 - model.z5_10_2 - model.x4_10_3 + model.x5_10_3 + model.z5_10_3 + model.x5_11_3 + model.z5_11_3 - 1.0 == 0)
model.v6_10_3 = Constraint(expr=-model.y6_9_3 - model.z6_10_2 - model.x5_10_3 + model.x6_10_3 + model.z6_10_3 + model.x6_11_3 + model.z6_11_3 - 1.0 == 0)
model.v7_10_3 = Constraint(expr=-model.y7_9_3 - model.z7_10_2 - model.x6_10_3 + model.x7_10_3 + model.z7_10_3 + model.x7_11_3 + model.z7_11_3 - 1.0 == 0)
model.v8_10_3 = Constraint(expr=-model.y8_9_3 - model.z8_10_2 - model.x7_10_3 + model.x8_10_3 + model.z8_10_3 + model.x8_11_3 + model.z8_11_3 - 1.0 == 0)
model.v9_10_3 = Constraint(expr=-model.y9_9_3 - model.z9_10_2 - model.x8_10_3 + model.x9_10_3 + model.z9_10_3 + model.x9_11_3 + model.z9_11_3 - 1.0 == 0)
model.v10_10_3 = Constraint(expr=-model.y10_9_3 - model.x9_10_3 + model.y11_10_3 + model.z11_10_3 + model.x10_11_3 + model.z10_11_3 - 1.0 == 0)
model.v1_1_4 = Constraint(expr=-model.z1_1_3 + model.x1_1_4 + model.y1_1_4 + model.z1_1_4 + model.y0_1_4 + model.z0_1_4 + model.x1_0_4 + model.z1_0_4 - 1.0 == 0)
model.v2_1_4 = Constraint(expr=-model.z2_1_3 - model.x1_1_4 + model.x2_1_4 + model.y2_1_4 + model.z2_1_4 + model.x2_0_4 + model.z2_0_4 - 1.0 == 0)
model.v3_1_4 = Constraint(expr=-model.z3_1_3 - model.x2_1_4 + model.x3_1_4 + model.y3_1_4 + model.z3_1_4 + model.x3_0_4 + model.z3_0_4 - 1.0 == 0)
model.v4_1_4 = Constraint(expr=-model.z4_1_3 - model.x3_1_4 + model.x4_1_4 + model.y4_1_4 + model.z4_1_4 + model.x4_0_4 + model.z4_0_4 - 1.0 == 0)
model.v5_1_4 = Constraint(expr=-model.z5_1_3 - model.x4_1_4 + model.x5_1_4 + model.y5_1_4 + model.z5_1_4 + model.x5_0_4 + model.z5_0_4 - 1.0 == 0)
model.v6_1_4 = Constraint(expr=-model.z6_1_3 - model.x5_1_4 + model.x6_1_4 + model.y6_1_4 + model.z6_1_4 + model.x6_0_4 + model.z6_0_4 - 1.0 == 0)
model.v7_1_4 = Constraint(expr=-model.z7_1_3 - model.x6_1_4 + model.x7_1_4 + model.y7_1_4 + model.z7_1_4 + model.x7_0_4 + model.z7_0_4 - 1.0 == 0)
model.v8_1_4 = Constraint(expr=-model.z8_1_3 - model.x7_1_4 + model.x8_1_4 + model.y8_1_4 + model.z8_1_4 + model.x8_0_4 + model.z8_0_4 - 1.0 == 0)
model.v9_1_4 = Constraint(expr=-model.z9_1_3 - model.x8_1_4 + model.x9_1_4 + model.y9_1_4 + model.z9_1_4 + model.x9_0_4 + model.z9_0_4 - 1.0 == 0)
model.v10_1_4 = Constraint(expr=-model.x9_1_4 - model.z10_1_3 + model.y10_1_4 + model.z10_1_4 + model.y11_1_4 + model.z11_1_4 + model.x10_0_4 + model.z10_0_4 - 1.0 == 0)
model.v1_2_4 = Constraint(expr=-model.z1_2_3 - model.y1_1_4 + model.x1_2_4 + model.y1_2_4 + model.z1_2_4 + model.y0_2_4 + model.z0_2_4 - 1.0 == 0)
model.v2_2_4 = Constraint(expr=-model.z2_2_3 - model.y2_1_4 - model.x1_2_4 + model.x2_2_4 + model.y2_2_4 + model.z2_2_4 - 1.0 == 0)
model.v3_2_4 = Constraint(expr=-model.z3_2_3 - model.y3_1_4 - model.x2_2_4 + model.x3_2_4 + model.y3_2_4 + model.z3_2_4 - 1.0 == 0)
model.v4_2_4 = Constraint(expr=-model.z4_2_3 - model.y4_1_4 - model.x3_2_4 + model.x4_2_4 + model.y4_2_4 + model.z4_2_4 - 1.0 == 0)
model.v5_2_4 = Constraint(expr=-model.z5_2_3 - model.y5_1_4 - model.x4_2_4 + model.x5_2_4 + model.y5_2_4 + model.z5_2_4 - 1.0 == 0)
model.v6_2_4 = Constraint(expr=-model.z6_2_3 - model.y6_1_4 - model.x5_2_4 + model.x6_2_4 + model.y6_2_4 + model.z6_2_4 - 1.0 == 0)
model.v7_2_4 = Constraint(expr=-model.z7_2_3 - model.y7_1_4 - model.x6_2_4 + model.x7_2_4 + model.y7_2_4 + model.z7_2_4 - 1.0 == 0)
model.v8_2_4 = Constraint(expr=-model.z8_2_3 - model.y8_1_4 - model.x7_2_4 + model.x8_2_4 + model.y8_2_4 + model.z8_2_4 - 1.0 == 0)
model.v9_2_4 = Constraint(expr=-model.z9_2_3 - model.y9_1_4 - model.x8_2_4 + model.x9_2_4 + model.y9_2_4 + model.z9_2_4 - 1.0 == 0)
model.v10_2_4 = Constraint(expr=-model.x9_2_4 - model.z10_2_3 - model.y10_1_4 + model.y10_2_4 + model.z10_2_4 + model.y11_2_4 + model.z11_2_4 - 1.0 == 0)
model.v1_3_4 = Constraint(expr=-model.z1_3_3 - model.y1_2_4 + model.x1_3_4 + model.y1_3_4 + model.z1_3_4 + model.y0_3_4 + model.z0_3_4 - 1.0 == 0)
model.v2_3_4 = Constraint(expr=-model.z2_3_3 - model.y2_2_4 - model.x1_3_4 + model.x2_3_4 + model.y2_3_4 + model.z2_3_4 - 1.0 == 0)
model.v3_3_4 = Constraint(expr=-model.z3_3_3 - model.y3_2_4 - model.x2_3_4 + model.x3_3_4 + model.y3_3_4 + model.z3_3_4 - 1.0 == 0)
model.v4_3_4 = Constraint(expr=-model.z4_3_3 - model.y4_2_4 - model.x3_3_4 + model.x4_3_4 + model.y4_3_4 + model.z4_3_4 - 1.0 == 0)
model.v5_3_4 = Constraint(expr=-model.z5_3_3 - model.y5_2_4 - model.x4_3_4 + model.x5_3_4 + model.y5_3_4 + model.z5_3_4 - 1.0 == 0)
model.v6_3_4 = Constraint(expr=-model.z6_3_3 - model.y6_2_4 - model.x5_3_4 + model.x6_3_4 + model.y6_3_4 + model.z6_3_4 - 1.0 == 0)
model.v7_3_4 = Constraint(expr=-model.z7_3_3 - model.y7_2_4 - model.x6_3_4 + model.x7_3_4 + model.y7_3_4 + model.z7_3_4 - 1.0 == 0)
model.v8_3_4 = Constraint(expr=-model.z8_3_3 - model.y8_2_4 - model.x7_3_4 + model.x8_3_4 + model.y8_3_4 + model.z8_3_4 - 1.0 == 0)
model.v9_3_4 = Constraint(expr=-model.z9_3_3 - model.y9_2_4 - model.x8_3_4 + model.x9_3_4 + model.y9_3_4 + model.z9_3_4 - 1.0 == 0)
model.v10_3_4 = Constraint(expr=-model.x9_3_4 - model.z10_3_3 - model.y10_2_4 + model.y10_3_4 + model.z10_3_4 + model.y11_3_4 + model.z11_3_4 - 1.0 == 0)
model.v1_4_4 = Constraint(expr=-model.z1_4_3 - model.y1_3_4 + model.x1_4_4 + model.y1_4_4 + model.z1_4_4 + model.y0_4_4 + model.z0_4_4 - 1.0 == 0)
model.v2_4_4 = Constraint(expr=-model.z2_4_3 - model.y2_3_4 - model.x1_4_4 + model.x2_4_4 + model.y2_4_4 + model.z2_4_4 - 1.0 == 0)
model.v3_4_4 = Constraint(expr=-model.z3_4_3 - model.y3_3_4 - model.x2_4_4 + model.x3_4_4 + model.y3_4_4 + model.z3_4_4 - 1.0 == 0)
model.v4_4_4 = Constraint(expr=-model.z4_4_3 - model.y4_3_4 - model.x3_4_4 + model.x4_4_4 + model.y4_4_4 + model.z4_4_4 - 1.0 == 0)
model.v5_4_4 = Constraint(expr=-model.z5_4_3 - model.y5_3_4 - model.x4_4_4 + model.x5_4_4 + model.y5_4_4 + model.z5_4_4 - 1.0 == 0)
model.v6_4_4 = Constraint(expr=-model.z6_4_3 - model.y6_3_4 - model.x5_4_4 + model.x6_4_4 + model.y6_4_4 + model.z6_4_4 - 1.0 == 0)
model.v7_4_4 = Constraint(expr=-model.z7_4_3 - model.y7_3_4 - model.x6_4_4 + model.x7_4_4 + model.y7_4_4 + model.z7_4_4 - 1.0 == 0)
model.v8_4_4 = Constraint(expr=-model.z8_4_3 - model.y8_3_4 - model.x7_4_4 + model.x8_4_4 + model.y8_4_4 + model.z8_4_4 - 1.0 == 0)
model.v9_4_4 = Constraint(expr=-model.z9_4_3 - model.y9_3_4 - model.x8_4_4 + model.x9_4_4 + model.y9_4_4 + model.z9_4_4 - 1.0 == 0)
model.v10_4_4 = Constraint(expr=-model.x9_4_4 - model.z10_4_3 - model.y10_3_4 + model.y10_4_4 + model.z10_4_4 + model.y11_4_4 + model.z11_4_4 - 1.0 == 0)
model.v1_5_4 = Constraint(expr=-model.z1_5_3 - model.y1_4_4 + model.x1_5_4 + model.y1_5_4 + model.z1_5_4 + model.y0_5_4 + model.z0_5_4 - 1.0 == 0)
model.v2_5_4 = Constraint(expr=-model.z2_5_3 - model.y2_4_4 - model.x1_5_4 + model.x2_5_4 + model.y2_5_4 + model.z2_5_4 - 1.0 == 0)
model.v3_5_4 = Constraint(expr=-model.z3_5_3 - model.y3_4_4 - model.x2_5_4 + model.x3_5_4 + model.y3_5_4 + model.z3_5_4 - 1.0 == 0)
model.v4_5_4 = Constraint(expr=-model.z4_5_3 - model.y4_4_4 - model.x3_5_4 + model.x4_5_4 + model.y4_5_4 + model.z4_5_4 - 1.0 == 0)
model.v5_5_4 = Constraint(expr=-model.z5_5_3 - model.y5_4_4 - model.x4_5_4 + model.x5_5_4 + model.y5_5_4 + model.z5_5_4 - 1.0 == 0)
model.v6_5_4 = Constraint(expr=-model.z6_5_3 - model.y6_4_4 - model.x5_5_4 + model.x6_5_4 + model.y6_5_4 + model.z6_5_4 - 1.0 == 0)
model.v7_5_4 = Constraint(expr=-model.z7_5_3 - model.y7_4_4 - model.x6_5_4 + model.x7_5_4 + model.y7_5_4 + model.z7_5_4 - 1.0 == 0)
model.v8_5_4 = Constraint(expr=-model.z8_5_3 - model.y8_4_4 - model.x7_5_4 + model.x8_5_4 + model.y8_5_4 + model.z8_5_4 - 1.0 == 0)
model.v9_5_4 = Constraint(expr=-model.z9_5_3 - model.y9_4_4 - model.x8_5_4 + model.x9_5_4 + model.y9_5_4 + model.z9_5_4 - 1.0 == 0)
model.v10_5_4 = Constraint(expr=-model.x9_5_4 - model.z10_5_3 - model.y10_4_4 + model.y10_5_4 + model.z10_5_4 + model.y11_5_4 + model.z11_5_4 - 1.0 == 0)
model.v1_6_4 = Constraint(expr=-model.z1_6_3 - model.y1_5_4 + model.x1_6_4 + model.y1_6_4 + model.z1_6_4 + model.y0_6_4 + model.z0_6_4 - 1.0 == 0)
model.v2_6_4 = Constraint(expr=-model.z2_6_3 - model.y2_5_4 - model.x1_6_4 + model.x2_6_4 + model.y2_6_4 + model.z2_6_4 - 1.0 == 0)
model.v3_6_4 = Constraint(expr=-model.z3_6_3 - model.y3_5_4 - model.x2_6_4 + model.x3_6_4 + model.y3_6_4 + model.z3_6_4 - 1.0 == 0)
model.v4_6_4 = Constraint(expr=-model.z4_6_3 - model.y4_5_4 - model.x3_6_4 + model.x4_6_4 + model.y4_6_4 + model.z4_6_4 - 1.0 == 0)
model.v5_6_4 = Constraint(expr=-model.z5_6_3 - model.y5_5_4 - model.x4_6_4 + model.x5_6_4 + model.y5_6_4 + model.z5_6_4 - 1.0 == 0)
model.v6_6_4 = Constraint(expr=-model.z6_6_3 - model.y6_5_4 - model.x5_6_4 + model.x6_6_4 + model.y6_6_4 + model.z6_6_4 - 1.0 == 0)
model.v7_6_4 = Constraint(expr=-model.z7_6_3 - model.y7_5_4 - model.x6_6_4 + model.x7_6_4 + model.y7_6_4 + model.z7_6_4 - 1.0 == 0)
model.v8_6_4 = Constraint(expr=-model.z8_6_3 - model.y8_5_4 - model.x7_6_4 + model.x8_6_4 + model.y8_6_4 + model.z8_6_4 - 1.0 == 0)
model.v9_6_4 = Constraint(expr=-model.z9_6_3 - model.y9_5_4 - model.x8_6_4 + model.x9_6_4 + model.y9_6_4 + model.z9_6_4 - 1.0 == 0)
model.v10_6_4 = Constraint(expr=-model.x9_6_4 - model.z10_6_3 - model.y10_5_4 + model.y10_6_4 + model.z10_6_4 + model.y11_6_4 + model.z11_6_4 - 1.0 == 0)
model.v1_7_4 = Constraint(expr=-model.z1_7_3 - model.y1_6_4 + model.x1_7_4 + model.y1_7_4 + model.z1_7_4 + model.y0_7_4 + model.z0_7_4 - 1.0 == 0)
model.v2_7_4 = Constraint(expr=-model.z2_7_3 - model.y2_6_4 - model.x1_7_4 + model.x2_7_4 + model.y2_7_4 + model.z2_7_4 - 1.0 == 0)
model.v3_7_4 = Constraint(expr=-model.z3_7_3 - model.y3_6_4 - model.x2_7_4 + model.x3_7_4 + model.y3_7_4 + model.z3_7_4 - 1.0 == 0)
model.v4_7_4 = Constraint(expr=-model.z4_7_3 - model.y4_6_4 - model.x3_7_4 + model.x4_7_4 + model.y4_7_4 + model.z4_7_4 - 1.0 == 0)
model.v5_7_4 = Constraint(expr=-model.z5_7_3 - model.y5_6_4 - model.x4_7_4 + model.x5_7_4 + model.y5_7_4 + model.z5_7_4 - 1.0 == 0)
model.v6_7_4 = Constraint(expr=-model.z6_7_3 - model.y6_6_4 - model.x5_7_4 + model.x6_7_4 + model.y6_7_4 + model.z6_7_4 - 1.0 == 0)
model.v7_7_4 = Constraint(expr=-model.z7_7_3 - model.y7_6_4 - model.x6_7_4 + model.x7_7_4 + model.y7_7_4 + model.z7_7_4 - 1.0 == 0)
model.v8_7_4 = Constraint(expr=-model.z8_7_3 - model.y8_6_4 - model.x7_7_4 + model.x8_7_4 + model.y8_7_4 + model.z8_7_4 - 1.0 == 0)
model.v9_7_4 = Constraint(expr=-model.z9_7_3 - model.y9_6_4 - model.x8_7_4 + model.x9_7_4 + model.y9_7_4 + model.z9_7_4 - 1.0 == 0)
model.v10_7_4 = Constraint(expr=-model.x9_7_4 - model.z10_7_3 - model.y10_6_4 + model.y10_7_4 + model.z10_7_4 + model.y11_7_4 + model.z11_7_4 - 1.0 == 0)
model.v1_8_4 = Constraint(expr=-model.z1_8_3 - model.y1_7_4 + model.x1_8_4 + model.y1_8_4 + model.z1_8_4 + model.y0_8_4 + model.z0_8_4 - 1.0 == 0)
model.v2_8_4 = Constraint(expr=-model.z2_8_3 - model.y2_7_4 - model.x1_8_4 + model.x2_8_4 + model.y2_8_4 + model.z2_8_4 - 1.0 == 0)
model.v3_8_4 = Constraint(expr=-model.z3_8_3 - model.y3_7_4 - model.x2_8_4 + model.x3_8_4 + model.y3_8_4 + model.z3_8_4 - 1.0 == 0)
model.v4_8_4 = Constraint(expr=-model.z4_8_3 - model.y4_7_4 - model.x3_8_4 + model.x4_8_4 + model.y4_8_4 + model.z4_8_4 - 1.0 == 0)
model.v5_8_4 = Constraint(expr=-model.z5_8_3 - model.y5_7_4 - model.x4_8_4 + model.x5_8_4 + model.y5_8_4 + model.z5_8_4 - 1.0 == 0)
model.v6_8_4 = Constraint(expr=-model.z6_8_3 - model.y6_7_4 - model.x5_8_4 + model.x6_8_4 + model.y6_8_4 + model.z6_8_4 - 1.0 == 0)
model.v7_8_4 = Constraint(expr=-model.z7_8_3 - model.y7_7_4 - model.x6_8_4 + model.x7_8_4 + model.y7_8_4 + model.z7_8_4 - 1.0 == 0)
model.v8_8_4 = Constraint(expr=-model.z8_8_3 - model.y8_7_4 - model.x7_8_4 + model.x8_8_4 + model.y8_8_4 + model.z8_8_4 - 1.0 == 0)
model.v9_8_4 = Constraint(expr=-model.z9_8_3 - model.y9_7_4 - model.x8_8_4 + model.x9_8_4 + model.y9_8_4 + model.z9_8_4 - 1.0 == 0)
model.v10_8_4 = Constraint(expr=-model.x9_8_4 - model.z10_8_3 - model.y10_7_4 + model.y10_8_4 + model.z10_8_4 + model.y11_8_4 + model.z11_8_4 - 1.0 == 0)
model.v1_9_4 = Constraint(expr=-model.z1_9_3 - model.y1_8_4 + model.x1_9_4 + model.y1_9_4 + model.z1_9_4 + model.y0_9_4 + model.z0_9_4 - 1.0 == 0)
model.v2_9_4 = Constraint(expr=-model.z2_9_3 - model.y2_8_4 - model.x1_9_4 + model.x2_9_4 + model.y2_9_4 + model.z2_9_4 - 1.0 == 0)
model.v3_9_4 = Constraint(expr=-model.z3_9_3 - model.y3_8_4 - model.x2_9_4 + model.x3_9_4 + model.y3_9_4 + model.z3_9_4 - 1.0 == 0)
model.v4_9_4 = Constraint(expr=-model.z4_9_3 - model.y4_8_4 - model.x3_9_4 + model.x4_9_4 + model.y4_9_4 + model.z4_9_4 - 1.0 == 0)
model.v5_9_4 = Constraint(expr=-model.z5_9_3 - model.y5_8_4 - model.x4_9_4 + model.x5_9_4 + model.y5_9_4 + model.z5_9_4 - 1.0 == 0)
model.v6_9_4 = Constraint(expr=-model.z6_9_3 - model.y6_8_4 - model.x5_9_4 + model.x6_9_4 + model.y6_9_4 + model.z6_9_4 - 1.0 == 0)
model.v7_9_4 = Constraint(expr=-model.z7_9_3 - model.y7_8_4 - model.x6_9_4 + model.x7_9_4 + model.y7_9_4 + model.z7_9_4 - 1.0 == 0)
model.v8_9_4 = Constraint(expr=-model.z8_9_3 - model.y8_8_4 - model.x7_9_4 + model.x8_9_4 + model.y8_9_4 + model.z8_9_4 - 1.0 == 0)
model.v9_9_4 = Constraint(expr=-model.z9_9_3 - model.y9_8_4 - model.x8_9_4 + model.x9_9_4 + model.y9_9_4 + model.z9_9_4 - 1.0 == 0)
model.v10_9_4 = Constraint(expr=-model.x9_9_4 - model.z10_9_3 - model.y10_8_4 + model.y10_9_4 + model.z10_9_4 + model.y11_9_4 + model.z11_9_4 - 1.0 == 0)
model.v1_10_4 = Constraint(expr=-model.y1_9_4 - model.z1_10_3 + model.x1_10_4 + model.z1_10_4 + model.y0_10_4 + model.z0_10_4 + model.x1_11_4 + model.z1_11_4 - 1.0 == 0)
model.v2_10_4 = Constraint(expr=-model.y2_9_4 - model.z2_10_3 - model.x1_10_4 + model.x2_10_4 + model.z2_10_4 + model.x2_11_4 + model.z2_11_4 - 1.0 == 0)
model.v3_10_4 = Constraint(expr=-model.y3_9_4 - model.z3_10_3 - model.x2_10_4 + model.x3_10_4 + model.z3_10_4 + model.x3_11_4 + model.z3_11_4 - 1.0 == 0)
model.v4_10_4 = Constraint(expr=-model.y4_9_4 - model.z4_10_3 - model.x3_10_4 + model.x4_10_4 + model.z4_10_4 + model.x4_11_4 + model.z4_11_4 - 1.0 == 0)
model.v5_10_4 = Constraint(expr=-model.y5_9_4 - model.z5_10_3 - model.x4_10_4 + model.x5_10_4 + model.z5_10_4 + model.x5_11_4 + model.z5_11_4 - 1.0 == 0)
model.v6_10_4 = Constraint(expr=-model.y6_9_4 - model.z6_10_3 - model.x5_10_4 + model.x6_10_4 + model.z6_10_4 + model.x6_11_4 + model.z6_11_4 - 1.0 == 0)
model.v7_10_4 = Constraint(expr=-model.y7_9_4 - model.z7_10_3 - model.x6_10_4 + model.x7_10_4 + model.z7_10_4 + model.x7_11_4 + model.z7_11_4 - 1.0 == 0)
model.v8_10_4 = Constraint(expr=-model.y8_9_4 - model.z8_10_3 - model.x7_10_4 + model.x8_10_4 + model.z8_10_4 + model.x8_11_4 + model.z8_11_4 - 1.0 == 0)
model.v9_10_4 = Constraint(expr=-model.y9_9_4 - model.z9_10_3 - model.x8_10_4 + model.x9_10_4 + model.z9_10_4 + model.x9_11_4 + model.z9_11_4 - 1.0 == 0)
model.v10_10_4 = Constraint(expr=-model.y10_9_4 - model.x9_10_4 + model.y11_10_4 + model.z11_10_4 + model.x10_11_4 + model.z10_11_4 - 1.0 == 0)
model.v1_1_5 = Constraint(expr=-model.z1_1_4 + model.x1_1_5 + model.y1_1_5 + model.z1_1_5 + model.y0_1_5 + model.z0_1_5 + model.x1_0_5 + model.z1_0_5 - 1.0 == 0)
model.v2_1_5 = Constraint(expr=-model.z2_1_4 - model.x1_1_5 + model.x2_1_5 + model.y2_1_5 + model.z2_1_5 + model.x2_0_5 + model.z2_0_5 - 1.0 == 0)
model.v3_1_5 = Constraint(expr=-model.z3_1_4 - model.x2_1_5 + model.x3_1_5 + model.y3_1_5 + model.z3_1_5 + model.x3_0_5 + model.z3_0_5 - 1.0 == 0)
model.v4_1_5 = Constraint(expr=-model.z4_1_4 - model.x3_1_5 + model.x4_1_5 + model.y4_1_5 + model.z4_1_5 + model.x4_0_5 + model.z4_0_5 - 1.0 == 0)
model.v5_1_5 = Constraint(expr=-model.z5_1_4 - model.x4_1_5 + model.x5_1_5 + model.y5_1_5 + model.z5_1_5 + model.x5_0_5 + model.z5_0_5 - 1.0 == 0)
model.v6_1_5 = Constraint(expr=-model.z6_1_4 - model.x5_1_5 + model.x6_1_5 + model.y6_1_5 + model.z6_1_5 + model.x6_0_5 + model.z6_0_5 - 1.0 == 0)
model.v7_1_5 = Constraint(expr=-model.z7_1_4 - model.x6_1_5 + model.x7_1_5 + model.y7_1_5 + model.z7_1_5 + model.x7_0_5 + model.z7_0_5 - 1.0 == 0)
model.v8_1_5 = Constraint(expr=-model.z8_1_4 - model.x7_1_5 + model.x8_1_5 + model.y8_1_5 + model.z8_1_5 + model.x8_0_5 + model.z8_0_5 - 1.0 == 0)
model.v9_1_5 = Constraint(expr=-model.z9_1_4 - model.x8_1_5 + model.x9_1_5 + model.y9_1_5 + model.z9_1_5 + model.x9_0_5 + model.z9_0_5 - 1.0 == 0)
model.v10_1_5 = Constraint(expr=-model.x9_1_5 - model.z10_1_4 + model.y10_1_5 + model.z10_1_5 + model.y11_1_5 + model.z11_1_5 + model.x10_0_5 + model.z10_0_5 - 1.0 == 0)
model.v1_2_5 = Constraint(expr=-model.z1_2_4 - model.y1_1_5 + model.x1_2_5 + model.y1_2_5 + model.z1_2_5 + model.y0_2_5 + model.z0_2_5 - 1.0 == 0)
model.v2_2_5 = Constraint(expr=-model.z2_2_4 - model.y2_1_5 - model.x1_2_5 + model.x2_2_5 + model.y2_2_5 + model.z2_2_5 - 1.0 == 0)
model.v3_2_5 = Constraint(expr=-model.z3_2_4 - model.y3_1_5 - model.x2_2_5 + model.x3_2_5 + model.y3_2_5 + model.z3_2_5 - 1.0 == 0)
model.v4_2_5 = Constraint(expr=-model.z4_2_4 - model.y4_1_5 - model.x3_2_5 + model.x4_2_5 + model.y4_2_5 + model.z4_2_5 - 1.0 == 0)
model.v5_2_5 = Constraint(expr=-model.z5_2_4 - model.y5_1_5 - model.x4_2_5 + model.x5_2_5 + model.y5_2_5 + model.z5_2_5 - 1.0 == 0)
model.v6_2_5 = Constraint(expr=-model.z6_2_4 - model.y6_1_5 - model.x5_2_5 + model.x6_2_5 + model.y6_2_5 + model.z6_2_5 - 1.0 == 0)
model.v7_2_5 = Constraint(expr=-model.z7_2_4 - model.y7_1_5 - model.x6_2_5 + model.x7_2_5 + model.y7_2_5 + model.z7_2_5 - 1.0 == 0)
model.v8_2_5 = Constraint(expr=-model.z8_2_4 - model.y8_1_5 - model.x7_2_5 + model.x8_2_5 + model.y8_2_5 + model.z8_2_5 - 1.0 == 0)
model.v9_2_5 = Constraint(expr=-model.z9_2_4 - model.y9_1_5 - model.x8_2_5 + model.x9_2_5 + model.y9_2_5 + model.z9_2_5 - 1.0 == 0)
model.v10_2_5 = Constraint(expr=-model.x9_2_5 - model.z10_2_4 - model.y10_1_5 + model.y10_2_5 + model.z10_2_5 + model.y11_2_5 + model.z11_2_5 - 1.0 == 0)
model.v1_3_5 = Constraint(expr=-model.z1_3_4 - model.y1_2_5 + model.x1_3_5 + model.y1_3_5 + model.z1_3_5 + model.y0_3_5 + model.z0_3_5 - 1.0 == 0)
model.v2_3_5 = Constraint(expr=-model.z2_3_4 - model.y2_2_5 - model.x1_3_5 + model.x2_3_5 + model.y2_3_5 + model.z2_3_5 - 1.0 == 0)
model.v3_3_5 = Constraint(expr=-model.z3_3_4 - model.y3_2_5 - model.x2_3_5 + model.x3_3_5 + model.y3_3_5 + model.z3_3_5 - 1.0 == 0)
model.v4_3_5 = Constraint(expr=-model.z4_3_4 - model.y4_2_5 - model.x3_3_5 + model.x4_3_5 + model.y4_3_5 + model.z4_3_5 - 1.0 == 0)
model.v5_3_5 = Constraint(expr=-model.z5_3_4 - model.y5_2_5 - model.x4_3_5 + model.x5_3_5 + model.y5_3_5 + model.z5_3_5 - 1.0 == 0)
model.v6_3_5 = Constraint(expr=-model.z6_3_4 - model.y6_2_5 - model.x5_3_5 + model.x6_3_5 + model.y6_3_5 + model.z6_3_5 - 1.0 == 0)
model.v7_3_5 = Constraint(expr=-model.z7_3_4 - model.y7_2_5 - model.x6_3_5 + model.x7_3_5 + model.y7_3_5 + model.z7_3_5 - 1.0 == 0)
model.v8_3_5 = Constraint(expr=-model.z8_3_4 - model.y8_2_5 - model.x7_3_5 + model.x8_3_5 + model.y8_3_5 + model.z8_3_5 - 1.0 == 0)
model.v9_3_5 = Constraint(expr=-model.z9_3_4 - model.y9_2_5 - model.x8_3_5 + model.x9_3_5 + model.y9_3_5 + model.z9_3_5 - 1.0 == 0)
model.v10_3_5 = Constraint(expr=-model.x9_3_5 - model.z10_3_4 - model.y10_2_5 + model.y10_3_5 + model.z10_3_5 + model.y11_3_5 + model.z11_3_5 - 1.0 == 0)
model.v1_4_5 = Constraint(expr=-model.z1_4_4 - model.y1_3_5 + model.x1_4_5 + model.y1_4_5 + model.z1_4_5 + model.y0_4_5 + model.z0_4_5 - 1.0 == 0)
model.v2_4_5 = Constraint(expr=-model.z2_4_4 - model.y2_3_5 - model.x1_4_5 + model.x2_4_5 + model.y2_4_5 + model.z2_4_5 - 1.0 == 0)
model.v3_4_5 = Constraint(expr=-model.z3_4_4 - model.y3_3_5 - model.x2_4_5 + model.x3_4_5 + model.y3_4_5 + model.z3_4_5 - 1.0 == 0)
model.v4_4_5 = Constraint(expr=-model.z4_4_4 - model.y4_3_5 - model.x3_4_5 + model.x4_4_5 + model.y4_4_5 + model.z4_4_5 - 1.0 == 0)
model.v5_4_5 = Constraint(expr=-model.z5_4_4 - model.y5_3_5 - model.x4_4_5 + model.x5_4_5 + model.y5_4_5 + model.z5_4_5 - 1.0 == 0)
model.v6_4_5 = Constraint(expr=-model.z6_4_4 - model.y6_3_5 - model.x5_4_5 + model.x6_4_5 + model.y6_4_5 + model.z6_4_5 - 1.0 == 0)
model.v7_4_5 = Constraint(expr=-model.z7_4_4 - model.y7_3_5 - model.x6_4_5 + model.x7_4_5 + model.y7_4_5 + model.z7_4_5 - 1.0 == 0)
model.v8_4_5 = Constraint(expr=-model.z8_4_4 - model.y8_3_5 - model.x7_4_5 + model.x8_4_5 + model.y8_4_5 + model.z8_4_5 - 1.0 == 0)
model.v9_4_5 = Constraint(expr=-model.z9_4_4 - model.y9_3_5 - model.x8_4_5 + model.x9_4_5 + model.y9_4_5 + model.z9_4_5 - 1.0 == 0)
model.v10_4_5 = Constraint(expr=-model.x9_4_5 - model.z10_4_4 - model.y10_3_5 + model.y10_4_5 + model.z10_4_5 + model.y11_4_5 + model.z11_4_5 - 1.0 == 0)
model.v1_5_5 = Constraint(expr=-model.z1_5_4 - model.y1_4_5 + model.x1_5_5 + model.y1_5_5 + model.z1_5_5 + model.y0_5_5 + model.z0_5_5 - 1.0 == 0)
model.v2_5_5 = Constraint(expr=-model.z2_5_4 - model.y2_4_5 - model.x1_5_5 + model.x2_5_5 + model.y2_5_5 + model.z2_5_5 - 1.0 == 0)
model.v3_5_5 = Constraint(expr=-model.z3_5_4 - model.y3_4_5 - model.x2_5_5 + model.x3_5_5 + model.y3_5_5 + model.z3_5_5 - 1.0 == 0)
model.v4_5_5 = Constraint(expr=-model.z4_5_4 - model.y4_4_5 - model.x3_5_5 + model.x4_5_5 + model.y4_5_5 + model.z4_5_5 - 1.0 == 0)
model.v5_5_5 = Constraint(expr=-model.z5_5_4 - model.y5_4_5 - model.x4_5_5 + model.x5_5_5 + model.y5_5_5 + model.z5_5_5 - 1.0 == 0)
model.v6_5_5 = Constraint(expr=-model.z6_5_4 - model.y6_4_5 - model.x5_5_5 + model.x6_5_5 + model.y6_5_5 + model.z6_5_5 - 1.0 == 0)
model.v7_5_5 = Constraint(expr=-model.z7_5_4 - model.y7_4_5 - model.x6_5_5 + model.x7_5_5 + model.y7_5_5 + model.z7_5_5 - 1.0 == 0)
model.v8_5_5 = Constraint(expr=-model.z8_5_4 - model.y8_4_5 - model.x7_5_5 + model.x8_5_5 + model.y8_5_5 + model.z8_5_5 - 1.0 == 0)
model.v9_5_5 = Constraint(expr=-model.z9_5_4 - model.y9_4_5 - model.x8_5_5 + model.x9_5_5 + model.y9_5_5 + model.z9_5_5 - 1.0 == 0)
model.v10_5_5 = Constraint(expr=-model.x9_5_5 - model.z10_5_4 - model.y10_4_5 + model.y10_5_5 + model.z10_5_5 + model.y11_5_5 + model.z11_5_5 - 1.0 == 0)
model.v1_6_5 = Constraint(expr=-model.z1_6_4 - model.y1_5_5 + model.x1_6_5 + model.y1_6_5 + model.z1_6_5 + model.y0_6_5 + model.z0_6_5 - 1.0 == 0)
model.v2_6_5 = Constraint(expr=-model.z2_6_4 - model.y2_5_5 - model.x1_6_5 + model.x2_6_5 + model.y2_6_5 + model.z2_6_5 - 1.0 == 0)
model.v3_6_5 = Constraint(expr=-model.z3_6_4 - model.y3_5_5 - model.x2_6_5 + model.x3_6_5 + model.y3_6_5 + model.z3_6_5 - 1.0 == 0)
model.v4_6_5 = Constraint(expr=-model.z4_6_4 - model.y4_5_5 - model.x3_6_5 + model.x4_6_5 + model.y4_6_5 + model.z4_6_5 - 1.0 == 0)
model.v5_6_5 = Constraint(expr=-model.z5_6_4 - model.y5_5_5 - model.x4_6_5 + model.x5_6_5 + model.y5_6_5 + model.z5_6_5 - 1.0 == 0)
model.v6_6_5 = Constraint(expr=-model.z6_6_4 - model.y6_5_5 - model.x5_6_5 + model.x6_6_5 + model.y6_6_5 + model.z6_6_5 - 1.0 == 0)
model.v7_6_5 = Constraint(expr=-model.z7_6_4 - model.y7_5_5 - model.x6_6_5 + model.x7_6_5 + model.y7_6_5 + model.z7_6_5 - 1.0 == 0)
model.v8_6_5 = Constraint(expr=-model.z8_6_4 - model.y8_5_5 - model.x7_6_5 + model.x8_6_5 + model.y8_6_5 + model.z8_6_5 - 1.0 == 0)
model.v9_6_5 = Constraint(expr=-model.z9_6_4 - model.y9_5_5 - model.x8_6_5 + model.x9_6_5 + model.y9_6_5 + model.z9_6_5 - 1.0 == 0)
model.v10_6_5 = Constraint(expr=-model.x9_6_5 - model.z10_6_4 - model.y10_5_5 + model.y10_6_5 + model.z10_6_5 + model.y11_6_5 + model.z11_6_5 - 1.0 == 0)
model.v1_7_5 = Constraint(expr=-model.z1_7_4 - model.y1_6_5 + model.x1_7_5 + model.y1_7_5 + model.z1_7_5 + model.y0_7_5 + model.z0_7_5 - 1.0 == 0)
model.v2_7_5 = Constraint(expr=-model.z2_7_4 - model.y2_6_5 - model.x1_7_5 + model.x2_7_5 + model.y2_7_5 + model.z2_7_5 - 1.0 == 0)
model.v3_7_5 = Constraint(expr=-model.z3_7_4 - model.y3_6_5 - model.x2_7_5 + model.x3_7_5 + model.y3_7_5 + model.z3_7_5 - 1.0 == 0)
model.v4_7_5 = Constraint(expr=-model.z4_7_4 - model.y4_6_5 - model.x3_7_5 + model.x4_7_5 + model.y4_7_5 + model.z4_7_5 - 1.0 == 0)
model.v5_7_5 = Constraint(expr=-model.z5_7_4 - model.y5_6_5 - model.x4_7_5 + model.x5_7_5 + model.y5_7_5 + model.z5_7_5 - 1.0 == 0)
model.v6_7_5 = Constraint(expr=-model.z6_7_4 - model.y6_6_5 - model.x5_7_5 + model.x6_7_5 + model.y6_7_5 + model.z6_7_5 - 1.0 == 0)
model.v7_7_5 = Constraint(expr=-model.z7_7_4 - model.y7_6_5 - model.x6_7_5 + model.x7_7_5 + model.y7_7_5 + model.z7_7_5 - 1.0 == 0)
model.v8_7_5 = Constraint(expr=-model.z8_7_4 - model.y8_6_5 - model.x7_7_5 + model.x8_7_5 + model.y8_7_5 + model.z8_7_5 - 1.0 == 0)
model.v9_7_5 = Constraint(expr=-model.z9_7_4 - model.y9_6_5 - model.x8_7_5 + model.x9_7_5 + model.y9_7_5 + model.z9_7_5 - 1.0 == 0)
model.v10_7_5 = Constraint(expr=-model.x9_7_5 - model.z10_7_4 - model.y10_6_5 + model.y10_7_5 + model.z10_7_5 + model.y11_7_5 + model.z11_7_5 - 1.0 == 0)
model.v1_8_5 = Constraint(expr=-model.z1_8_4 - model.y1_7_5 + model.x1_8_5 + model.y1_8_5 + model.z1_8_5 + model.y0_8_5 + model.z0_8_5 - 1.0 == 0)
model.v2_8_5 = Constraint(expr=-model.z2_8_4 - model.y2_7_5 - model.x1_8_5 + model.x2_8_5 + model.y2_8_5 + model.z2_8_5 - 1.0 == 0)
model.v3_8_5 = Constraint(expr=-model.z3_8_4 - model.y3_7_5 - model.x2_8_5 + model.x3_8_5 + model.y3_8_5 + model.z3_8_5 - 1.0 == 0)
model.v4_8_5 = Constraint(expr=-model.z4_8_4 - model.y4_7_5 - model.x3_8_5 + model.x4_8_5 + model.y4_8_5 + model.z4_8_5 - 1.0 == 0)
model.v5_8_5 = Constraint(expr=-model.z5_8_4 - model.y5_7_5 - model.x4_8_5 + model.x5_8_5 + model.y5_8_5 + model.z5_8_5 - 1.0 == 0)
model.v6_8_5 = Constraint(expr=-model.z6_8_4 - model.y6_7_5 - model.x5_8_5 + model.x6_8_5 + model.y6_8_5 + model.z6_8_5 - 1.0 == 0)
model.v7_8_5 = Constraint(expr=-model.z7_8_4 - model.y7_7_5 - model.x6_8_5 + model.x7_8_5 + model.y7_8_5 + model.z7_8_5 - 1.0 == 0)
model.v8_8_5 = Constraint(expr=-model.z8_8_4 - model.y8_7_5 - model.x7_8_5 + model.x8_8_5 + model.y8_8_5 + model.z8_8_5 - 1.0 == 0)
model.v9_8_5 = Constraint(expr=-model.z9_8_4 - model.y9_7_5 - model.x8_8_5 + model.x9_8_5 + model.y9_8_5 + model.z9_8_5 - 1.0 == 0)
model.v10_8_5 = Constraint(expr=-model.x9_8_5 - model.z10_8_4 - model.y10_7_5 + model.y10_8_5 + model.z10_8_5 + model.y11_8_5 + model.z11_8_5 - 1.0 == 0)
model.v1_9_5 = Constraint(expr=-model.z1_9_4 - model.y1_8_5 + model.x1_9_5 + model.y1_9_5 + model.z1_9_5 + model.y0_9_5 + model.z0_9_5 - 1.0 == 0)
model.v2_9_5 = Constraint(expr=-model.z2_9_4 - model.y2_8_5 - model.x1_9_5 + model.x2_9_5 + model.y2_9_5 + model.z2_9_5 - 1.0 == 0)
model.v3_9_5 = Constraint(expr=-model.z3_9_4 - model.y3_8_5 - model.x2_9_5 + model.x3_9_5 + model.y3_9_5 + model.z3_9_5 - 1.0 == 0)
model.v4_9_5 = Constraint(expr=-model.z4_9_4 - model.y4_8_5 - model.x3_9_5 + model.x4_9_5 + model.y4_9_5 + model.z4_9_5 - 1.0 == 0)
model.v5_9_5 = Constraint(expr=-model.z5_9_4 - model.y5_8_5 - model.x4_9_5 + model.x5_9_5 + model.y5_9_5 + model.z5_9_5 - 1.0 == 0)
model.v6_9_5 = Constraint(expr=-model.z6_9_4 - model.y6_8_5 - model.x5_9_5 + model.x6_9_5 + model.y6_9_5 + model.z6_9_5 - 1.0 == 0)
model.v7_9_5 = Constraint(expr=-model.z7_9_4 - model.y7_8_5 - model.x6_9_5 + model.x7_9_5 + model.y7_9_5 + model.z7_9_5 - 1.0 == 0)
model.v8_9_5 = Constraint(expr=-model.z8_9_4 - model.y8_8_5 - model.x7_9_5 + model.x8_9_5 + model.y8_9_5 + model.z8_9_5 - 1.0 == 0)
model.v9_9_5 = Constraint(expr=-model.z9_9_4 - model.y9_8_5 - model.x8_9_5 + model.x9_9_5 + model.y9_9_5 + model.z9_9_5 - 1.0 == 0)
model.v10_9_5 = Constraint(expr=-model.x9_9_5 - model.z10_9_4 - model.y10_8_5 + model.y10_9_5 + model.z10_9_5 + model.y11_9_5 + model.z11_9_5 - 1.0 == 0)
model.v1_10_5 = Constraint(expr=-model.y1_9_5 - model.z1_10_4 + model.x1_10_5 + model.z1_10_5 + model.y0_10_5 + model.z0_10_5 + model.x1_11_5 + model.z1_11_5 - 1.0 == 0)
model.v2_10_5 = Constraint(expr=-model.y2_9_5 - model.z2_10_4 - model.x1_10_5 + model.x2_10_5 + model.z2_10_5 + model.x2_11_5 + model.z2_11_5 - 1.0 == 0)
model.v3_10_5 = Constraint(expr=-model.y3_9_5 - model.z3_10_4 - model.x2_10_5 + model.x3_10_5 + model.z3_10_5 + model.x3_11_5 + model.z3_11_5 - 1.0 == 0)
model.v4_10_5 = Constraint(expr=-model.y4_9_5 - model.z4_10_4 - model.x3_10_5 + model.x4_10_5 + model.z4_10_5 + model.x4_11_5 + model.z4_11_5 - 1.0 == 0)
model.v5_10_5 = Constraint(expr=-model.y5_9_5 - model.z5_10_4 - model.x4_10_5 + model.x5_10_5 + model.z5_10_5 + model.x5_11_5 + model.z5_11_5 - 1.0 == 0)
model.v6_10_5 = Constraint(expr=-model.y6_9_5 - model.z6_10_4 - model.x5_10_5 + model.x6_10_5 + model.z6_10_5 + model.x6_11_5 + model.z6_11_5 - 1.0 == 0)
model.v7_10_5 = Constraint(expr=-model.y7_9_5 - model.z7_10_4 - model.x6_10_5 + model.x7_10_5 + model.z7_10_5 + model.x7_11_5 + model.z7_11_5 - 1.0 == 0)
model.v8_10_5 = Constraint(expr=-model.y8_9_5 - model.z8_10_4 - model.x7_10_5 + model.x8_10_5 + model.z8_10_5 + model.x8_11_5 + model.z8_11_5 - 1.0 == 0)
model.v9_10_5 = Constraint(expr=-model.y9_9_5 - model.z9_10_4 - model.x8_10_5 + model.x9_10_5 + model.z9_10_5 + model.x9_11_5 + model.z9_11_5 - 1.0 == 0)
model.v10_10_5 = Constraint(expr=-model.y10_9_5 - model.x9_10_5 + model.y11_10_5 + model.z11_10_5 + model.x10_11_5 + model.z10_11_5 - 1.0 == 0)
model.v1_1_6 = Constraint(expr=-model.z1_1_5 + model.x1_1_6 + model.y1_1_6 + model.z1_1_6 + model.y0_1_6 + model.z0_1_6 + model.x1_0_6 + model.z1_0_6 - 1.0 == 0)
model.v2_1_6 = Constraint(expr=-model.z2_1_5 - model.x1_1_6 + model.x2_1_6 + model.y2_1_6 + model.z2_1_6 + model.x2_0_6 + model.z2_0_6 - 1.0 == 0)
model.v3_1_6 = Constraint(expr=-model.z3_1_5 - model.x2_1_6 + model.x3_1_6 + model.y3_1_6 + model.z3_1_6 + model.x3_0_6 + model.z3_0_6 - 1.0 == 0)
model.v4_1_6 = Constraint(expr=-model.z4_1_5 - model.x3_1_6 + model.x4_1_6 + model.y4_1_6 + model.z4_1_6 + model.x4_0_6 + model.z4_0_6 - 1.0 == 0)
model.v5_1_6 = Constraint(expr=-model.z5_1_5 - model.x4_1_6 + model.x5_1_6 + model.y5_1_6 + model.z5_1_6 + model.x5_0_6 + model.z5_0_6 - 1.0 == 0)
model.v6_1_6 = Constraint(expr=-model.z6_1_5 - model.x5_1_6 + model.x6_1_6 + model.y6_1_6 + model.z6_1_6 + model.x6_0_6 + model.z6_0_6 - 1.0 == 0)
model.v7_1_6 = Constraint(expr=-model.z7_1_5 - model.x6_1_6 + model.x7_1_6 + model.y7_1_6 + model.z7_1_6 + model.x7_0_6 + model.z7_0_6 - 1.0 == 0)
model.v8_1_6 = Constraint(expr=-model.z8_1_5 - model.x7_1_6 + model.x8_1_6 + model.y8_1_6 + model.z8_1_6 + model.x8_0_6 + model.z8_0_6 - 1.0 == 0)
model.v9_1_6 = Constraint(expr=-model.z9_1_5 - model.x8_1_6 + model.x9_1_6 + model.y9_1_6 + model.z9_1_6 + model.x9_0_6 + model.z9_0_6 - 1.0 == 0)
model.v10_1_6 = Constraint(expr=-model.x9_1_6 - model.z10_1_5 + model.y10_1_6 + model.z10_1_6 + model.y11_1_6 + model.z11_1_6 + model.x10_0_6 + model.z10_0_6 - 1.0 == 0)
model.v1_2_6 = Constraint(expr=-model.z1_2_5 - model.y1_1_6 + model.x1_2_6 + model.y1_2_6 + model.z1_2_6 + model.y0_2_6 + model.z0_2_6 - 1.0 == 0)
model.v2_2_6 = Constraint(expr=-model.z2_2_5 - model.y2_1_6 - model.x1_2_6 + model.x2_2_6 + model.y2_2_6 + model.z2_2_6 - 1.0 == 0)
model.v3_2_6 = Constraint(expr=-model.z3_2_5 - model.y3_1_6 - model.x2_2_6 + model.x3_2_6 + model.y3_2_6 + model.z3_2_6 - 1.0 == 0)
model.v4_2_6 = Constraint(expr=-model.z4_2_5 - model.y4_1_6 - model.x3_2_6 + model.x4_2_6 + model.y4_2_6 + model.z4_2_6 - 1.0 == 0)
model.v5_2_6 = Constraint(expr=-model.z5_2_5 - model.y5_1_6 - model.x4_2_6 + model.x5_2_6 + model.y5_2_6 + model.z5_2_6 - 1.0 == 0)
model.v6_2_6 = Constraint(expr=-model.z6_2_5 - model.y6_1_6 - model.x5_2_6 + model.x6_2_6 + model.y6_2_6 + model.z6_2_6 - 1.0 == 0)
model.v7_2_6 = Constraint(expr=-model.z7_2_5 - model.y7_1_6 - model.x6_2_6 + model.x7_2_6 + model.y7_2_6 + model.z7_2_6 - 1.0 == 0)
model.v8_2_6 = Constraint(expr=-model.z8_2_5 - model.y8_1_6 - model.x7_2_6 + model.x8_2_6 + model.y8_2_6 + model.z8_2_6 - 1.0 == 0)
model.v9_2_6 = Constraint(expr=-model.z9_2_5 - model.y9_1_6 - model.x8_2_6 + model.x9_2_6 + model.y9_2_6 + model.z9_2_6 - 1.0 == 0)
model.v10_2_6 = Constraint(expr=-model.x9_2_6 - model.z10_2_5 - model.y10_1_6 + model.y10_2_6 + model.z10_2_6 + model.y11_2_6 + model.z11_2_6 - 1.0 == 0)
model.v1_3_6 = Constraint(expr=-model.z1_3_5 - model.y1_2_6 + model.x1_3_6 + model.y1_3_6 + model.z1_3_6 + model.y0_3_6 + model.z0_3_6 - 1.0 == 0)
model.v2_3_6 = Constraint(expr=-model.z2_3_5 - model.y2_2_6 - model.x1_3_6 + model.x2_3_6 + model.y2_3_6 + model.z2_3_6 - 1.0 == 0)
model.v3_3_6 = Constraint(expr=-model.z3_3_5 - model.y3_2_6 - model.x2_3_6 + model.x3_3_6 + model.y3_3_6 + model.z3_3_6 - 1.0 == 0)
model.v4_3_6 = Constraint(expr=-model.z4_3_5 - model.y4_2_6 - model.x3_3_6 + model.x4_3_6 + model.y4_3_6 + model.z4_3_6 - 1.0 == 0)
model.v5_3_6 = Constraint(expr=-model.z5_3_5 - model.y5_2_6 - model.x4_3_6 + model.x5_3_6 + model.y5_3_6 + model.z5_3_6 - 1.0 == 0)
model.v6_3_6 = Constraint(expr=-model.z6_3_5 - model.y6_2_6 - model.x5_3_6 + model.x6_3_6 + model.y6_3_6 + model.z6_3_6 - 1.0 == 0)
model.v7_3_6 = Constraint(expr=-model.z7_3_5 - model.y7_2_6 - model.x6_3_6 + model.x7_3_6 + model.y7_3_6 + model.z7_3_6 - 1.0 == 0)
model.v8_3_6 = Constraint(expr=-model.z8_3_5 - model.y8_2_6 - model.x7_3_6 + model.x8_3_6 + model.y8_3_6 + model.z8_3_6 - 1.0 == 0)
model.v9_3_6 = Constraint(expr=-model.z9_3_5 - model.y9_2_6 - model.x8_3_6 + model.x9_3_6 + model.y9_3_6 + model.z9_3_6 - 1.0 == 0)
model.v10_3_6 = Constraint(expr=-model.x9_3_6 - model.z10_3_5 - model.y10_2_6 + model.y10_3_6 + model.z10_3_6 + model.y11_3_6 + model.z11_3_6 - 1.0 == 0)
model.v1_4_6 = Constraint(expr=-model.z1_4_5 - model.y1_3_6 + model.x1_4_6 + model.y1_4_6 + model.z1_4_6 + model.y0_4_6 + model.z0_4_6 - 1.0 == 0)
model.v2_4_6 = Constraint(expr=-model.z2_4_5 - model.y2_3_6 - model.x1_4_6 + model.x2_4_6 + model.y2_4_6 + model.z2_4_6 - 1.0 == 0)
model.v3_4_6 = Constraint(expr=-model.z3_4_5 - model.y3_3_6 - model.x2_4_6 + model.x3_4_6 + model.y3_4_6 + model.z3_4_6 - 1.0 == 0)
model.v4_4_6 = Constraint(expr=-model.z4_4_5 - model.y4_3_6 - model.x3_4_6 + model.x4_4_6 + model.y4_4_6 + model.z4_4_6 - 1.0 == 0)
model.v5_4_6 = Constraint(expr=-model.z5_4_5 - model.y5_3_6 - model.x4_4_6 + model.x5_4_6 + model.y5_4_6 + model.z5_4_6 - 1.0 == 0)
model.v6_4_6 = Constraint(expr=-model.z6_4_5 - model.y6_3_6 - model.x5_4_6 + model.x6_4_6 + model.y6_4_6 + model.z6_4_6 - 1.0 == 0)
model.v7_4_6 = Constraint(expr=-model.z7_4_5 - model.y7_3_6 - model.x6_4_6 + model.x7_4_6 + model.y7_4_6 + model.z7_4_6 - 1.0 == 0)
model.v8_4_6 = Constraint(expr=-model.z8_4_5 - model.y8_3_6 - model.x7_4_6 + model.x8_4_6 + model.y8_4_6 + model.z8_4_6 - 1.0 == 0)
model.v9_4_6 = Constraint(expr=-model.z9_4_5 - model.y9_3_6 - model.x8_4_6 + model.x9_4_6 + model.y9_4_6 + model.z9_4_6 - 1.0 == 0)
model.v10_4_6 = Constraint(expr=-model.x9_4_6 - model.z10_4_5 - model.y10_3_6 + model.y10_4_6 + model.z10_4_6 + model.y11_4_6 + model.z11_4_6 - 1.0 == 0)
model.v1_5_6 = Constraint(expr=-model.z1_5_5 - model.y1_4_6 + model.x1_5_6 + model.y1_5_6 + model.z1_5_6 + model.y0_5_6 + model.z0_5_6 - 1.0 == 0)
model.v2_5_6 = Constraint(expr=-model.z2_5_5 - model.y2_4_6 - model.x1_5_6 + model.x2_5_6 + model.y2_5_6 + model.z2_5_6 - 1.0 == 0)
model.v3_5_6 = Constraint(expr=-model.z3_5_5 - model.y3_4_6 - model.x2_5_6 + model.x3_5_6 + model.y3_5_6 + model.z3_5_6 - 1.0 == 0)
model.v4_5_6 = Constraint(expr=-model.z4_5_5 - model.y4_4_6 - model.x3_5_6 + model.x4_5_6 + model.y4_5_6 + model.z4_5_6 - 1.0 == 0)
model.v5_5_6 = Constraint(expr=-model.z5_5_5 - model.y5_4_6 - model.x4_5_6 + model.x5_5_6 + model.y5_5_6 + model.z5_5_6 - 1.0 == 0)
model.v6_5_6 = Constraint(expr=-model.z6_5_5 - model.y6_4_6 - model.x5_5_6 + model.x6_5_6 + model.y6_5_6 + model.z6_5_6 - 1.0 == 0)
model.v7_5_6 = Constraint(expr=-model.z7_5_5 - model.y7_4_6 - model.x6_5_6 + model.x7_5_6 + model.y7_5_6 + model.z7_5_6 - 1.0 == 0)
model.v8_5_6 = Constraint(expr=-model.z8_5_5 - model.y8_4_6 - model.x7_5_6 + model.x8_5_6 + model.y8_5_6 + model.z8_5_6 - 1.0 == 0)
model.v9_5_6 = Constraint(expr=-model.z9_5_5 - model.y9_4_6 - model.x8_5_6 + model.x9_5_6 + model.y9_5_6 + model.z9_5_6 - 1.0 == 0)
model.v10_5_6 = Constraint(expr=-model.x9_5_6 - model.z10_5_5 - model.y10_4_6 + model.y10_5_6 + model.z10_5_6 + model.y11_5_6 + model.z11_5_6 - 1.0 == 0)
model.v1_6_6 = Constraint(expr=-model.z1_6_5 - model.y1_5_6 + model.x1_6_6 + model.y1_6_6 + model.z1_6_6 + model.y0_6_6 + model.z0_6_6 - 1.0 == 0)
model.v2_6_6 = Constraint(expr=-model.z2_6_5 - model.y2_5_6 - model.x1_6_6 + model.x2_6_6 + model.y2_6_6 + model.z2_6_6 - 1.0 == 0)
model.v3_6_6 = Constraint(expr=-model.z3_6_5 - model.y3_5_6 - model.x2_6_6 + model.x3_6_6 + model.y3_6_6 + model.z3_6_6 - 1.0 == 0)
model.v4_6_6 = Constraint(expr=-model.z4_6_5 - model.y4_5_6 - model.x3_6_6 + model.x4_6_6 + model.y4_6_6 + model.z4_6_6 - 1.0 == 0)
model.v5_6_6 = Constraint(expr=-model.z5_6_5 - model.y5_5_6 - model.x4_6_6 + model.x5_6_6 + model.y5_6_6 + model.z5_6_6 - 1.0 == 0)
model.v6_6_6 = Constraint(expr=-model.z6_6_5 - model.y6_5_6 - model.x5_6_6 + model.x6_6_6 + model.y6_6_6 + model.z6_6_6 - 1.0 == 0)
model.v7_6_6 = Constraint(expr=-model.z7_6_5 - model.y7_5_6 - model.x6_6_6 + model.x7_6_6 + model.y7_6_6 + model.z7_6_6 - 1.0 == 0)
model.v8_6_6 = Constraint(expr=-model.z8_6_5 - model.y8_5_6 - model.x7_6_6 + model.x8_6_6 + model.y8_6_6 + model.z8_6_6 - 1.0 == 0)
model.v9_6_6 = Constraint(expr=-model.z9_6_5 - model.y9_5_6 - model.x8_6_6 + model.x9_6_6 + model.y9_6_6 + model.z9_6_6 - 1.0 == 0)
model.v10_6_6 = Constraint(expr=-model.x9_6_6 - model.z10_6_5 - model.y10_5_6 + model.y10_6_6 + model.z10_6_6 + model.y11_6_6 + model.z11_6_6 - 1.0 == 0)
model.v1_7_6 = Constraint(expr=-model.z1_7_5 - model.y1_6_6 + model.x1_7_6 + model.y1_7_6 + model.z1_7_6 + model.y0_7_6 + model.z0_7_6 - 1.0 == 0)
model.v2_7_6 = Constraint(expr=-model.z2_7_5 - model.y2_6_6 - model.x1_7_6 + model.x2_7_6 + model.y2_7_6 + model.z2_7_6 - 1.0 == 0)
model.v3_7_6 = Constraint(expr=-model.z3_7_5 - model.y3_6_6 - model.x2_7_6 + model.x3_7_6 + model.y3_7_6 + model.z3_7_6 - 1.0 == 0)
model.v4_7_6 = Constraint(expr=-model.z4_7_5 - model.y4_6_6 - model.x3_7_6 + model.x4_7_6 + model.y4_7_6 + model.z4_7_6 - 1.0 == 0)
model.v5_7_6 = Constraint(expr=-model.z5_7_5 - model.y5_6_6 - model.x4_7_6 + model.x5_7_6 + model.y5_7_6 + model.z5_7_6 - 1.0 == 0)
model.v6_7_6 = Constraint(expr=-model.z6_7_5 - model.y6_6_6 - model.x5_7_6 + model.x6_7_6 + model.y6_7_6 + model.z6_7_6 - 1.0 == 0)
model.v7_7_6 = Constraint(expr=-model.z7_7_5 - model.y7_6_6 - model.x6_7_6 + model.x7_7_6 + model.y7_7_6 + model.z7_7_6 - 1.0 == 0)
model.v8_7_6 = Constraint(expr=-model.z8_7_5 - model.y8_6_6 - model.x7_7_6 + model.x8_7_6 + model.y8_7_6 + model.z8_7_6 - 1.0 == 0)
model.v9_7_6 = Constraint(expr=-model.z9_7_5 - model.y9_6_6 - model.x8_7_6 + model.x9_7_6 + model.y9_7_6 + model.z9_7_6 - 1.0 == 0)
model.v10_7_6 = Constraint(expr=-model.x9_7_6 - model.z10_7_5 - model.y10_6_6 + model.y10_7_6 + model.z10_7_6 + model.y11_7_6 + model.z11_7_6 - 1.0 == 0)
model.v1_8_6 = Constraint(expr=-model.z1_8_5 - model.y1_7_6 + model.x1_8_6 + model.y1_8_6 + model.z1_8_6 + model.y0_8_6 + model.z0_8_6 - 1.0 == 0)
model.v2_8_6 = Constraint(expr=-model.z2_8_5 - model.y2_7_6 - model.x1_8_6 + model.x2_8_6 + model.y2_8_6 + model.z2_8_6 - 1.0 == 0)
model.v3_8_6 = Constraint(expr=-model.z3_8_5 - model.y3_7_6 - model.x2_8_6 + model.x3_8_6 + model.y3_8_6 + model.z3_8_6 - 1.0 == 0)
model.v4_8_6 = Constraint(expr=-model.z4_8_5 - model.y4_7_6 - model.x3_8_6 + model.x4_8_6 + model.y4_8_6 + model.z4_8_6 - 1.0 == 0)
model.v5_8_6 = Constraint(expr=-model.z5_8_5 - model.y5_7_6 - model.x4_8_6 + model.x5_8_6 + model.y5_8_6 + model.z5_8_6 - 1.0 == 0)
model.v6_8_6 = Constraint(expr=-model.z6_8_5 - model.y6_7_6 - model.x5_8_6 + model.x6_8_6 + model.y6_8_6 + model.z6_8_6 - 1.0 == 0)
model.v7_8_6 = Constraint(expr=-model.z7_8_5 - model.y7_7_6 - model.x6_8_6 + model.x7_8_6 + model.y7_8_6 + model.z7_8_6 - 1.0 == 0)
model.v8_8_6 = Constraint(expr=-model.z8_8_5 - model.y8_7_6 - model.x7_8_6 + model.x8_8_6 + model.y8_8_6 + model.z8_8_6 - 1.0 == 0)
model.v9_8_6 = Constraint(expr=-model.z9_8_5 - model.y9_7_6 - model.x8_8_6 + model.x9_8_6 + model.y9_8_6 + model.z9_8_6 - 1.0 == 0)
model.v10_8_6 = Constraint(expr=-model.x9_8_6 - model.z10_8_5 - model.y10_7_6 + model.y10_8_6 + model.z10_8_6 + model.y11_8_6 + model.z11_8_6 - 1.0 == 0)
model.v1_9_6 = Constraint(expr=-model.z1_9_5 - model.y1_8_6 + model.x1_9_6 + model.y1_9_6 + model.z1_9_6 + model.y0_9_6 + model.z0_9_6 - 1.0 == 0)
model.v2_9_6 = Constraint(expr=-model.z2_9_5 - model.y2_8_6 - model.x1_9_6 + model.x2_9_6 + model.y2_9_6 + model.z2_9_6 - 1.0 == 0)
model.v3_9_6 = Constraint(expr=-model.z3_9_5 - model.y3_8_6 - model.x2_9_6 + model.x3_9_6 + model.y3_9_6 + model.z3_9_6 - 1.0 == 0)
model.v4_9_6 = Constraint(expr=-model.z4_9_5 - model.y4_8_6 - model.x3_9_6 + model.x4_9_6 + model.y4_9_6 + model.z4_9_6 - 1.0 == 0)
model.v5_9_6 = Constraint(expr=-model.z5_9_5 - model.y5_8_6 - model.x4_9_6 + model.x5_9_6 + model.y5_9_6 + model.z5_9_6 - 1.0 == 0)
model.v6_9_6 = Constraint(expr=-model.z6_9_5 - model.y6_8_6 - model.x5_9_6 + model.x6_9_6 + model.y6_9_6 + model.z6_9_6 - 1.0 == 0)
model.v7_9_6 = Constraint(expr=-model.z7_9_5 - model.y7_8_6 - model.x6_9_6 + model.x7_9_6 + model.y7_9_6 + model.z7_9_6 - 1.0 == 0)
model.v8_9_6 = Constraint(expr=-model.z8_9_5 - model.y8_8_6 - model.x7_9_6 + model.x8_9_6 + model.y8_9_6 + model.z8_9_6 - 1.0 == 0)
model.v9_9_6 = Constraint(expr=-model.z9_9_5 - model.y9_8_6 - model.x8_9_6 + model.x9_9_6 + model.y9_9_6 + model.z9_9_6 - 1.0 == 0)
model.v10_9_6 = Constraint(expr=-model.x9_9_6 - model.z10_9_5 - model.y10_8_6 + model.y10_9_6 + model.z10_9_6 + model.y11_9_6 + model.z11_9_6 - 1.0 == 0)
model.v1_10_6 = Constraint(expr=-model.y1_9_6 - model.z1_10_5 + model.x1_10_6 + model.z1_10_6 + model.y0_10_6 + model.z0_10_6 + model.x1_11_6 + model.z1_11_6 - 1.0 == 0)
model.v2_10_6 = Constraint(expr=-model.y2_9_6 - model.z2_10_5 - model.x1_10_6 + model.x2_10_6 + model.z2_10_6 + model.x2_11_6 + model.z2_11_6 - 1.0 == 0)
model.v3_10_6 = Constraint(expr=-model.y3_9_6 - model.z3_10_5 - model.x2_10_6 + model.x3_10_6 + model.z3_10_6 + model.x3_11_6 + model.z3_11_6 - 1.0 == 0)
model.v4_10_6 = Constraint(expr=-model.y4_9_6 - model.z4_10_5 - model.x3_10_6 + model.x4_10_6 + model.z4_10_6 + model.x4_11_6 + model.z4_11_6 - 1.0 == 0)
model.v5_10_6 = Constraint(expr=-model.y5_9_6 - model.z5_10_5 - model.x4_10_6 + model.x5_10_6 + model.z5_10_6 + model.x5_11_6 + model.z5_11_6 - 1.0 == 0)
model.v6_10_6 = Constraint(expr=-model.y6_9_6 - model.z6_10_5 - model.x5_10_6 + model.x6_10_6 + model.z6_10_6 + model.x6_11_6 + model.z6_11_6 - 1.0 == 0)
model.v7_10_6 = Constraint(expr=-model.y7_9_6 - model.z7_10_5 - model.x6_10_6 + model.x7_10_6 + model.z7_10_6 + model.x7_11_6 + model.z7_11_6 - 1.0 == 0)
model.v8_10_6 = Constraint(expr=-model.y8_9_6 - model.z8_10_5 - model.x7_10_6 + model.x8_10_6 + model.z8_10_6 + model.x8_11_6 + model.z8_11_6 - 1.0 == 0)
model.v9_10_6 = Constraint(expr=-model.y9_9_6 - model.z9_10_5 - model.x8_10_6 + model.x9_10_6 + model.z9_10_6 + model.x9_11_6 + model.z9_11_6 - 1.0 == 0)
model.v10_10_6 = Constraint(expr=-model.y10_9_6 - model.x9_10_6 + model.y11_10_6 + model.z11_10_6 + model.x10_11_6 + model.z10_11_6 - 1.0 == 0)
model.v1_1_7 = Constraint(expr=-model.z1_1_6 + model.x1_1_7 + model.y1_1_7 + model.z1_1_7 + model.y0_1_7 + model.z0_1_7 + model.x1_0_7 + model.z1_0_7 - 1.0 == 0)
model.v2_1_7 = Constraint(expr=-model.z2_1_6 - model.x1_1_7 + model.x2_1_7 + model.y2_1_7 + model.z2_1_7 + model.x2_0_7 + model.z2_0_7 - 1.0 == 0)
model.v3_1_7 = Constraint(expr=-model.z3_1_6 - model.x2_1_7 + model.x3_1_7 + model.y3_1_7 + model.z3_1_7 + model.x3_0_7 + model.z3_0_7 - 1.0 == 0)
model.v4_1_7 = Constraint(expr=-model.z4_1_6 - model.x3_1_7 + model.x4_1_7 + model.y4_1_7 + model.z4_1_7 + model.x4_0_7 + model.z4_0_7 - 1.0 == 0)
model.v5_1_7 = Constraint(expr=-model.z5_1_6 - model.x4_1_7 + model.x5_1_7 + model.y5_1_7 + model.z5_1_7 + model.x5_0_7 + model.z5_0_7 - 1.0 == 0)
model.v6_1_7 = Constraint(expr=-model.z6_1_6 - model.x5_1_7 + model.x6_1_7 + model.y6_1_7 + model.z6_1_7 + model.x6_0_7 + model.z6_0_7 - 1.0 == 0)
model.v7_1_7 = Constraint(expr=-model.z7_1_6 - model.x6_1_7 + model.x7_1_7 + model.y7_1_7 + model.z7_1_7 + model.x7_0_7 + model.z7_0_7 - 1.0 == 0)
model.v8_1_7 = Constraint(expr=-model.z8_1_6 - model.x7_1_7 + model.x8_1_7 + model.y8_1_7 + model.z8_1_7 + model.x8_0_7 + model.z8_0_7 - 1.0 == 0)
model.v9_1_7 = Constraint(expr=-model.z9_1_6 - model.x8_1_7 + model.x9_1_7 + model.y9_1_7 + model.z9_1_7 + model.x9_0_7 + model.z9_0_7 - 1.0 == 0)
model.v10_1_7 = Constraint(expr=-model.x9_1_7 - model.z10_1_6 + model.y10_1_7 + model.z10_1_7 + model.y11_1_7 + model.z11_1_7 + model.x10_0_7 + model.z10_0_7 - 1.0 == 0)
model.v1_2_7 = Constraint(expr=-model.z1_2_6 - model.y1_1_7 + model.x1_2_7 + model.y1_2_7 + model.z1_2_7 + model.y0_2_7 + model.z0_2_7 - 1.0 == 0)
model.v2_2_7 = Constraint(expr=-model.z2_2_6 - model.y2_1_7 - model.x1_2_7 + model.x2_2_7 + model.y2_2_7 + model.z2_2_7 - 1.0 == 0)
model.v3_2_7 = Constraint(expr=-model.z3_2_6 - model.y3_1_7 - model.x2_2_7 + model.x3_2_7 + model.y3_2_7 + model.z3_2_7 - 1.0 == 0)
model.v4_2_7 = Constraint(expr=-model.z4_2_6 - model.y4_1_7 - model.x3_2_7 + model.x4_2_7 + model.y4_2_7 + model.z4_2_7 - 1.0 == 0)
model.v5_2_7 = Constraint(expr=-model.z5_2_6 - model.y5_1_7 - model.x4_2_7 + model.x5_2_7 + model.y5_2_7 + model.z5_2_7 - 1.0 == 0)
model.v6_2_7 = Constraint(expr=-model.z6_2_6 - model.y6_1_7 - model.x5_2_7 + model.x6_2_7 + model.y6_2_7 + model.z6_2_7 - 1.0 == 0)
model.v7_2_7 = Constraint(expr=-model.z7_2_6 - model.y7_1_7 - model.x6_2_7 + model.x7_2_7 + model.y7_2_7 + model.z7_2_7 - 1.0 == 0)
model.v8_2_7 = Constraint(expr=-model.z8_2_6 - model.y8_1_7 - model.x7_2_7 + model.x8_2_7 + model.y8_2_7 + model.z8_2_7 - 1.0 == 0)
model.v9_2_7 = Constraint(expr=-model.z9_2_6 - model.y9_1_7 - model.x8_2_7 + model.x9_2_7 + model.y9_2_7 + model.z9_2_7 - 1.0 == 0)
model.v10_2_7 = Constraint(expr=-model.x9_2_7 - model.z10_2_6 - model.y10_1_7 + model.y10_2_7 + model.z10_2_7 + model.y11_2_7 + model.z11_2_7 - 1.0 == 0)
model.v1_3_7 = Constraint(expr=-model.z1_3_6 - model.y1_2_7 + model.x1_3_7 + model.y1_3_7 + model.z1_3_7 + model.y0_3_7 + model.z0_3_7 - 1.0 == 0)
model.v2_3_7 = Constraint(expr=-model.z2_3_6 - model.y2_2_7 - model.x1_3_7 + model.x2_3_7 + model.y2_3_7 + model.z2_3_7 - 1.0 == 0)
model.v3_3_7 = Constraint(expr=-model.z3_3_6 - model.y3_2_7 - model.x2_3_7 + model.x3_3_7 + model.y3_3_7 + model.z3_3_7 - 1.0 == 0)
model.v4_3_7 = Constraint(expr=-model.z4_3_6 - model.y4_2_7 - model.x3_3_7 + model.x4_3_7 + model.y4_3_7 + model.z4_3_7 - 1.0 == 0)
model.v5_3_7 = Constraint(expr=-model.z5_3_6 - model.y5_2_7 - model.x4_3_7 + model.x5_3_7 + model.y5_3_7 + model.z5_3_7 - 1.0 == 0)
model.v6_3_7 = Constraint(expr=-model.z6_3_6 - model.y6_2_7 - model.x5_3_7 + model.x6_3_7 + model.y6_3_7 + model.z6_3_7 - 1.0 == 0)
model.v7_3_7 = Constraint(expr=-model.z7_3_6 - model.y7_2_7 - model.x6_3_7 + model.x7_3_7 + model.y7_3_7 + model.z7_3_7 - 1.0 == 0)
model.v8_3_7 = Constraint(expr=-model.z8_3_6 - model.y8_2_7 - model.x7_3_7 + model.x8_3_7 + model.y8_3_7 + model.z8_3_7 - 1.0 == 0)
model.v9_3_7 = Constraint(expr=-model.z9_3_6 - model.y9_2_7 - model.x8_3_7 + model.x9_3_7 + model.y9_3_7 + model.z9_3_7 - 1.0 == 0)
model.v10_3_7 = Constraint(expr=-model.x9_3_7 - model.z10_3_6 - model.y10_2_7 + model.y10_3_7 + model.z10_3_7 + model.y11_3_7 + model.z11_3_7 - 1.0 == 0)
model.v1_4_7 = Constraint(expr=-model.z1_4_6 - model.y1_3_7 + model.x1_4_7 + model.y1_4_7 + model.z1_4_7 + model.y0_4_7 + model.z0_4_7 - 1.0 == 0)
model.v2_4_7 = Constraint(expr=-model.z2_4_6 - model.y2_3_7 - model.x1_4_7 + model.x2_4_7 + model.y2_4_7 + model.z2_4_7 - 1.0 == 0)
model.v3_4_7 = Constraint(expr=-model.z3_4_6 - model.y3_3_7 - model.x2_4_7 + model.x3_4_7 + model.y3_4_7 + model.z3_4_7 - 1.0 == 0)
model.v4_4_7 = Constraint(expr=-model.z4_4_6 - model.y4_3_7 - model.x3_4_7 + model.x4_4_7 + model.y4_4_7 + model.z4_4_7 - 1.0 == 0)
model.v5_4_7 = Constraint(expr=-model.z5_4_6 - model.y5_3_7 - model.x4_4_7 + model.x5_4_7 + model.y5_4_7 + model.z5_4_7 - 1.0 == 0)
model.v6_4_7 = Constraint(expr=-model.z6_4_6 - model.y6_3_7 - model.x5_4_7 + model.x6_4_7 + model.y6_4_7 + model.z6_4_7 - 1.0 == 0)
model.v7_4_7 = Constraint(expr=-model.z7_4_6 - model.y7_3_7 - model.x6_4_7 + model.x7_4_7 + model.y7_4_7 + model.z7_4_7 - 1.0 == 0)
model.v8_4_7 = Constraint(expr=-model.z8_4_6 - model.y8_3_7 - model.x7_4_7 + model.x8_4_7 + model.y8_4_7 + model.z8_4_7 - 1.0 == 0)
model.v9_4_7 = Constraint(expr=-model.z9_4_6 - model.y9_3_7 - model.x8_4_7 + model.x9_4_7 + model.y9_4_7 + model.z9_4_7 - 1.0 == 0)
model.v10_4_7 = Constraint(expr=-model.x9_4_7 - model.z10_4_6 - model.y10_3_7 + model.y10_4_7 + model.z10_4_7 + model.y11_4_7 + model.z11_4_7 - 1.0 == 0)
model.v1_5_7 = Constraint(expr=-model.z1_5_6 - model.y1_4_7 + model.x1_5_7 + model.y1_5_7 + model.z1_5_7 + model.y0_5_7 + model.z0_5_7 - 1.0 == 0)
model.v2_5_7 = Constraint(expr=-model.z2_5_6 - model.y2_4_7 - model.x1_5_7 + model.x2_5_7 + model.y2_5_7 + model.z2_5_7 - 1.0 == 0)
model.v3_5_7 = Constraint(expr=-model.z3_5_6 - model.y3_4_7 - model.x2_5_7 + model.x3_5_7 + model.y3_5_7 + model.z3_5_7 - 1.0 == 0)
model.v4_5_7 = Constraint(expr=-model.z4_5_6 - model.y4_4_7 - model.x3_5_7 + model.x4_5_7 + model.y4_5_7 + model.z4_5_7 - 1.0 == 0)
model.v5_5_7 = Constraint(expr=-model.z5_5_6 - model.y5_4_7 - model.x4_5_7 + model.x5_5_7 + model.y5_5_7 + model.z5_5_7 - 1.0 == 0)
model.v6_5_7 = Constraint(expr=-model.z6_5_6 - model.y6_4_7 - model.x5_5_7 + model.x6_5_7 + model.y6_5_7 + model.z6_5_7 - 1.0 == 0)
model.v7_5_7 = Constraint(expr=-model.z7_5_6 - model.y7_4_7 - model.x6_5_7 + model.x7_5_7 + model.y7_5_7 + model.z7_5_7 - 1.0 == 0)
model.v8_5_7 = Constraint(expr=-model.z8_5_6 - model.y8_4_7 - model.x7_5_7 + model.x8_5_7 + model.y8_5_7 + model.z8_5_7 - 1.0 == 0)
model.v9_5_7 = Constraint(expr=-model.z9_5_6 - model.y9_4_7 - model.x8_5_7 + model.x9_5_7 + model.y9_5_7 + model.z9_5_7 - 1.0 == 0)
model.v10_5_7 = Constraint(expr=-model.x9_5_7 - model.z10_5_6 - model.y10_4_7 + model.y10_5_7 + model.z10_5_7 + model.y11_5_7 + model.z11_5_7 - 1.0 == 0)
model.v1_6_7 = Constraint(expr=-model.z1_6_6 - model.y1_5_7 + model.x1_6_7 + model.y1_6_7 + model.z1_6_7 + model.y0_6_7 + model.z0_6_7 - 1.0 == 0)
model.v2_6_7 = Constraint(expr=-model.z2_6_6 - model.y2_5_7 - model.x1_6_7 + model.x2_6_7 + model.y2_6_7 + model.z2_6_7 - 1.0 == 0)
model.v3_6_7 = Constraint(expr=-model.z3_6_6 - model.y3_5_7 - model.x2_6_7 + model.x3_6_7 + model.y3_6_7 + model.z3_6_7 - 1.0 == 0)
model.v4_6_7 = Constraint(expr=-model.z4_6_6 - model.y4_5_7 - model.x3_6_7 + model.x4_6_7 + model.y4_6_7 + model.z4_6_7 - 1.0 == 0)
model.v5_6_7 = Constraint(expr=-model.z5_6_6 - model.y5_5_7 - model.x4_6_7 + model.x5_6_7 + model.y5_6_7 + model.z5_6_7 - 1.0 == 0)
model.v6_6_7 = Constraint(expr=-model.z6_6_6 - model.y6_5_7 - model.x5_6_7 + model.x6_6_7 + model.y6_6_7 + model.z6_6_7 - 1.0 == 0)
model.v7_6_7 = Constraint(expr=-model.z7_6_6 - model.y7_5_7 - model.x6_6_7 + model.x7_6_7 + model.y7_6_7 + model.z7_6_7 - 1.0 == 0)
model.v8_6_7 = Constraint(expr=-model.z8_6_6 - model.y8_5_7 - model.x7_6_7 + model.x8_6_7 + model.y8_6_7 + model.z8_6_7 - 1.0 == 0)
model.v9_6_7 = Constraint(expr=-model.z9_6_6 - model.y9_5_7 - model.x8_6_7 + model.x9_6_7 + model.y9_6_7 + model.z9_6_7 - 1.0 == 0)
model.v10_6_7 = Constraint(expr=-model.x9_6_7 - model.z10_6_6 - model.y10_5_7 + model.y10_6_7 + model.z10_6_7 + model.y11_6_7 + model.z11_6_7 - 1.0 == 0)
model.v1_7_7 = Constraint(expr=-model.z1_7_6 - model.y1_6_7 + model.x1_7_7 + model.y1_7_7 + model.z1_7_7 + model.y0_7_7 + model.z0_7_7 - 1.0 == 0)
model.v2_7_7 = Constraint(expr=-model.z2_7_6 - model.y2_6_7 - model.x1_7_7 + model.x2_7_7 + model.y2_7_7 + model.z2_7_7 - 1.0 == 0)
model.v3_7_7 = Constraint(expr=-model.z3_7_6 - model.y3_6_7 - model.x2_7_7 + model.x3_7_7 + model.y3_7_7 + model.z3_7_7 - 1.0 == 0)
model.v4_7_7 = Constraint(expr=-model.z4_7_6 - model.y4_6_7 - model.x3_7_7 + model.x4_7_7 + model.y4_7_7 + model.z4_7_7 - 1.0 == 0)
model.v5_7_7 = Constraint(expr=-model.z5_7_6 - model.y5_6_7 - model.x4_7_7 + model.x5_7_7 + model.y5_7_7 + model.z5_7_7 - 1.0 == 0)
model.v6_7_7 = Constraint(expr=-model.z6_7_6 - model.y6_6_7 - model.x5_7_7 + model.x6_7_7 + model.y6_7_7 + model.z6_7_7 - 1.0 == 0)
model.v7_7_7 = Constraint(expr=-model.z7_7_6 - model.y7_6_7 - model.x6_7_7 + model.x7_7_7 + model.y7_7_7 + model.z7_7_7 - 1.0 == 0)
model.v8_7_7 = Constraint(expr=-model.z8_7_6 - model.y8_6_7 - model.x7_7_7 + model.x8_7_7 + model.y8_7_7 + model.z8_7_7 - 1.0 == 0)
model.v9_7_7 = Constraint(expr=-model.z9_7_6 - model.y9_6_7 - model.x8_7_7 + model.x9_7_7 + model.y9_7_7 + model.z9_7_7 - 1.0 == 0)
model.v10_7_7 = Constraint(expr=-model.x9_7_7 - model.z10_7_6 - model.y10_6_7 + model.y10_7_7 + model.z10_7_7 + model.y11_7_7 + model.z11_7_7 - 1.0 == 0)
model.v1_8_7 = Constraint(expr=-model.z1_8_6 - model.y1_7_7 + model.x1_8_7 + model.y1_8_7 + model.z1_8_7 + model.y0_8_7 + model.z0_8_7 - 1.0 == 0)
model.v2_8_7 = Constraint(expr=-model.z2_8_6 - model.y2_7_7 - model.x1_8_7 + model.x2_8_7 + model.y2_8_7 + model.z2_8_7 - 1.0 == 0)
model.v3_8_7 = Constraint(expr=-model.z3_8_6 - model.y3_7_7 - model.x2_8_7 + model.x3_8_7 + model.y3_8_7 + model.z3_8_7 - 1.0 == 0)
model.v4_8_7 = Constraint(expr=-model.z4_8_6 - model.y4_7_7 - model.x3_8_7 + model.x4_8_7 + model.y4_8_7 + model.z4_8_7 - 1.0 == 0)
model.v5_8_7 = Constraint(expr=-model.z5_8_6 - model.y5_7_7 - model.x4_8_7 + model.x5_8_7 + model.y5_8_7 + model.z5_8_7 - 1.0 == 0)
model.v6_8_7 = Constraint(expr=-model.z6_8_6 - model.y6_7_7 - model.x5_8_7 + model.x6_8_7 + model.y6_8_7 + model.z6_8_7 - 1.0 == 0)
model.v7_8_7 = Constraint(expr=-model.z7_8_6 - model.y7_7_7 - model.x6_8_7 + model.x7_8_7 + model.y7_8_7 + model.z7_8_7 - 1.0 == 0)
model.v8_8_7 = Constraint(expr=-model.z8_8_6 - model.y8_7_7 - model.x7_8_7 + model.x8_8_7 + model.y8_8_7 + model.z8_8_7 - 1.0 == 0)
model.v9_8_7 = Constraint(expr=-model.z9_8_6 - model.y9_7_7 - model.x8_8_7 + model.x9_8_7 + model.y9_8_7 + model.z9_8_7 - 1.0 == 0)
model.v10_8_7 = Constraint(expr=-model.x9_8_7 - model.z10_8_6 - model.y10_7_7 + model.y10_8_7 + model.z10_8_7 + model.y11_8_7 + model.z11_8_7 - 1.0 == 0)
model.v1_9_7 = Constraint(expr=-model.z1_9_6 - model.y1_8_7 + model.x1_9_7 + model.y1_9_7 + model.z1_9_7 + model.y0_9_7 + model.z0_9_7 - 1.0 == 0)
model.v2_9_7 = Constraint(expr=-model.z2_9_6 - model.y2_8_7 - model.x1_9_7 + model.x2_9_7 + model.y2_9_7 + model.z2_9_7 - 1.0 == 0)
model.v3_9_7 = Constraint(expr=-model.z3_9_6 - model.y3_8_7 - model.x2_9_7 + model.x3_9_7 + model.y3_9_7 + model.z3_9_7 - 1.0 == 0)
model.v4_9_7 = Constraint(expr=-model.z4_9_6 - model.y4_8_7 - model.x3_9_7 + model.x4_9_7 + model.y4_9_7 + model.z4_9_7 - 1.0 == 0)
model.v5_9_7 = Constraint(expr=-model.z5_9_6 - model.y5_8_7 - model.x4_9_7 + model.x5_9_7 + model.y5_9_7 + model.z5_9_7 - 1.0 == 0)
model.v6_9_7 = Constraint(expr=-model.z6_9_6 - model.y6_8_7 - model.x5_9_7 + model.x6_9_7 + model.y6_9_7 + model.z6_9_7 - 1.0 == 0)
model.v7_9_7 = Constraint(expr=-model.z7_9_6 - model.y7_8_7 - model.x6_9_7 + model.x7_9_7 + model.y7_9_7 + model.z7_9_7 - 1.0 == 0)
model.v8_9_7 = Constraint(expr=-model.z8_9_6 - model.y8_8_7 - model.x7_9_7 + model.x8_9_7 + model.y8_9_7 + model.z8_9_7 - 1.0 == 0)
model.v9_9_7 = Constraint(expr=-model.z9_9_6 - model.y9_8_7 - model.x8_9_7 + model.x9_9_7 + model.y9_9_7 + model.z9_9_7 - 1.0 == 0)
model.v10_9_7 = Constraint(expr=-model.x9_9_7 - model.z10_9_6 - model.y10_8_7 + model.y10_9_7 + model.z10_9_7 + model.y11_9_7 + model.z11_9_7 - 1.0 == 0)
model.v1_10_7 = Constraint(expr=-model.y1_9_7 - model.z1_10_6 + model.x1_10_7 + model.z1_10_7 + model.y0_10_7 + model.z0_10_7 + model.x1_11_7 + model.z1_11_7 - 1.0 == 0)
model.v2_10_7 = Constraint(expr=-model.y2_9_7 - model.z2_10_6 - model.x1_10_7 + model.x2_10_7 + model.z2_10_7 + model.x2_11_7 + model.z2_11_7 - 1.0 == 0)
model.v3_10_7 = Constraint(expr=-model.y3_9_7 - model.z3_10_6 - model.x2_10_7 + model.x3_10_7 + model.z3_10_7 + model.x3_11_7 + model.z3_11_7 - 1.0 == 0)
model.v4_10_7 = Constraint(expr=-model.y4_9_7 - model.z4_10_6 - model.x3_10_7 + model.x4_10_7 + model.z4_10_7 + model.x4_11_7 + model.z4_11_7 - 1.0 == 0)
model.v5_10_7 = Constraint(expr=-model.y5_9_7 - model.z5_10_6 - model.x4_10_7 + model.x5_10_7 + model.z5_10_7 + model.x5_11_7 + model.z5_11_7 - 1.0 == 0)
model.v6_10_7 = Constraint(expr=-model.y6_9_7 - model.z6_10_6 - model.x5_10_7 + model.x6_10_7 + model.z6_10_7 + model.x6_11_7 + model.z6_11_7 - 1.0 == 0)
model.v7_10_7 = Constraint(expr=-model.y7_9_7 - model.z7_10_6 - model.x6_10_7 + model.x7_10_7 + model.z7_10_7 + model.x7_11_7 + model.z7_11_7 - 1.0 == 0)
model.v8_10_7 = Constraint(expr=-model.y8_9_7 - model.z8_10_6 - model.x7_10_7 + model.x8_10_7 + model.z8_10_7 + model.x8_11_7 + model.z8_11_7 - 1.0 == 0)
model.v9_10_7 = Constraint(expr=-model.y9_9_7 - model.z9_10_6 - model.x8_10_7 + model.x9_10_7 + model.z9_10_7 + model.x9_11_7 + model.z9_11_7 - 1.0 == 0)
model.v10_10_7 = Constraint(expr=-model.y10_9_7 - model.x9_10_7 + model.y11_10_7 + model.z11_10_7 + model.x10_11_7 + model.z10_11_7 - 1.0 == 0)
model.v1_1_8 = Constraint(expr=-model.z1_1_7 + model.x1_1_8 + model.y1_1_8 + model.z1_1_8 + model.y0_1_8 + model.z0_1_8 + model.x1_0_8 + model.z1_0_8 - 1.0 == 0)
model.v2_1_8 = Constraint(expr=-model.z2_1_7 - model.x1_1_8 + model.x2_1_8 + model.y2_1_8 + model.z2_1_8 + model.x2_0_8 + model.z2_0_8 - 1.0 == 0)
model.v3_1_8 = Constraint(expr=-model.z3_1_7 - model.x2_1_8 + model.x3_1_8 + model.y3_1_8 + model.z3_1_8 + model.x3_0_8 + model.z3_0_8 - 1.0 == 0)
model.v4_1_8 = Constraint(expr=-model.z4_1_7 - model.x3_1_8 + model.x4_1_8 + model.y4_1_8 + model.z4_1_8 + model.x4_0_8 + model.z4_0_8 - 1.0 == 0)
model.v5_1_8 = Constraint(expr=-model.z5_1_7 - model.x4_1_8 + model.x5_1_8 + model.y5_1_8 + model.z5_1_8 + model.x5_0_8 + model.z5_0_8 - 1.0 == 0)
model.v6_1_8 = Constraint(expr=-model.z6_1_7 - model.x5_1_8 + model.x6_1_8 + model.y6_1_8 + model.z6_1_8 + model.x6_0_8 + model.z6_0_8 - 1.0 == 0)
model.v7_1_8 = Constraint(expr=-model.z7_1_7 - model.x6_1_8 + model.x7_1_8 + model.y7_1_8 + model.z7_1_8 + model.x7_0_8 + model.z7_0_8 - 1.0 == 0)
model.v8_1_8 = Constraint(expr=-model.z8_1_7 - model.x7_1_8 + model.x8_1_8 + model.y8_1_8 + model.z8_1_8 + model.x8_0_8 + model.z8_0_8 - 1.0 == 0)
model.v9_1_8 = Constraint(expr=-model.z9_1_7 - model.x8_1_8 + model.x9_1_8 + model.y9_1_8 + model.z9_1_8 + model.x9_0_8 + model.z9_0_8 - 1.0 == 0)
model.v10_1_8 = Constraint(expr=-model.x9_1_8 - model.z10_1_7 + model.y10_1_8 + model.z10_1_8 + model.y11_1_8 + model.z11_1_8 + model.x10_0_8 + model.z10_0_8 - 1.0 == 0)
model.v1_2_8 = Constraint(expr=-model.z1_2_7 - model.y1_1_8 + model.x1_2_8 + model.y1_2_8 + model.z1_2_8 + model.y0_2_8 + model.z0_2_8 - 1.0 == 0)
model.v2_2_8 = Constraint(expr=-model.z2_2_7 - model.y2_1_8 - model.x1_2_8 + model.x2_2_8 + model.y2_2_8 + model.z2_2_8 - 1.0 == 0)
model.v3_2_8 = Constraint(expr=-model.z3_2_7 - model.y3_1_8 - model.x2_2_8 + model.x3_2_8 + model.y3_2_8 + model.z3_2_8 - 1.0 == 0)
model.v4_2_8 = Constraint(expr=-model.z4_2_7 - model.y4_1_8 - model.x3_2_8 + model.x4_2_8 + model.y4_2_8 + model.z4_2_8 - 1.0 == 0)
model.v5_2_8 = Constraint(expr=-model.z5_2_7 - model.y5_1_8 - model.x4_2_8 + model.x5_2_8 + model.y5_2_8 + model.z5_2_8 - 1.0 == 0)
model.v6_2_8 = Constraint(expr=-model.z6_2_7 - model.y6_1_8 - model.x5_2_8 + model.x6_2_8 + model.y6_2_8 + model.z6_2_8 - 1.0 == 0)
model.v7_2_8 = Constraint(expr=-model.z7_2_7 - model.y7_1_8 - model.x6_2_8 + model.x7_2_8 + model.y7_2_8 + model.z7_2_8 - 1.0 == 0)
model.v8_2_8 = Constraint(expr=-model.z8_2_7 - model.y8_1_8 - model.x7_2_8 + model.x8_2_8 + model.y8_2_8 + model.z8_2_8 - 1.0 == 0)
model.v9_2_8 = Constraint(expr=-model.z9_2_7 - model.y9_1_8 - model.x8_2_8 + model.x9_2_8 + model.y9_2_8 + model.z9_2_8 - 1.0 == 0)
model.v10_2_8 = Constraint(expr=-model.x9_2_8 - model.z10_2_7 - model.y10_1_8 + model.y10_2_8 + model.z10_2_8 + model.y11_2_8 + model.z11_2_8 - 1.0 == 0)
model.v1_3_8 = Constraint(expr=-model.z1_3_7 - model.y1_2_8 + model.x1_3_8 + model.y1_3_8 + model.z1_3_8 + model.y0_3_8 + model.z0_3_8 - 1.0 == 0)
model.v2_3_8 = Constraint(expr=-model.z2_3_7 - model.y2_2_8 - model.x1_3_8 + model.x2_3_8 + model.y2_3_8 + model.z2_3_8 - 1.0 == 0)
model.v3_3_8 = Constraint(expr=-model.z3_3_7 - model.y3_2_8 - model.x2_3_8 + model.x3_3_8 + model.y3_3_8 + model.z3_3_8 - 1.0 == 0)
model.v4_3_8 = Constraint(expr=-model.z4_3_7 - model.y4_2_8 - model.x3_3_8 + model.x4_3_8 + model.y4_3_8 + model.z4_3_8 - 1.0 == 0)
model.v5_3_8 = Constraint(expr=-model.z5_3_7 - model.y5_2_8 - model.x4_3_8 + model.x5_3_8 + model.y5_3_8 + model.z5_3_8 - 1.0 == 0)
model.v6_3_8 = Constraint(expr=-model.z6_3_7 - model.y6_2_8 - model.x5_3_8 + model.x6_3_8 + model.y6_3_8 + model.z6_3_8 - 1.0 == 0)
model.v7_3_8 = Constraint(expr=-model.z7_3_7 - model.y7_2_8 - model.x6_3_8 + model.x7_3_8 + model.y7_3_8 + model.z7_3_8 - 1.0 == 0)
model.v8_3_8 = Constraint(expr=-model.z8_3_7 - model.y8_2_8 - model.x7_3_8 + model.x8_3_8 + model.y8_3_8 + model.z8_3_8 - 1.0 == 0)
model.v9_3_8 = Constraint(expr=-model.z9_3_7 - model.y9_2_8 - model.x8_3_8 + model.x9_3_8 + model.y9_3_8 + model.z9_3_8 - 1.0 == 0)
model.v10_3_8 = Constraint(expr=-model.x9_3_8 - model.z10_3_7 - model.y10_2_8 + model.y10_3_8 + model.z10_3_8 + model.y11_3_8 + model.z11_3_8 - 1.0 == 0)
model.v1_4_8 = Constraint(expr=-model.z1_4_7 - model.y1_3_8 + model.x1_4_8 + model.y1_4_8 + model.z1_4_8 + model.y0_4_8 + model.z0_4_8 - 1.0 == 0)
model.v2_4_8 = Constraint(expr=-model.z2_4_7 - model.y2_3_8 - model.x1_4_8 + model.x2_4_8 + model.y2_4_8 + model.z2_4_8 - 1.0 == 0)
model.v3_4_8 = Constraint(expr=-model.z3_4_7 - model.y3_3_8 - model.x2_4_8 + model.x3_4_8 + model.y3_4_8 + model.z3_4_8 - 1.0 == 0)
model.v4_4_8 = Constraint(expr=-model.z4_4_7 - model.y4_3_8 - model.x3_4_8 + model.x4_4_8 + model.y4_4_8 + model.z4_4_8 - 1.0 == 0)
model.v5_4_8 = Constraint(expr=-model.z5_4_7 - model.y5_3_8 - model.x4_4_8 + model.x5_4_8 + model.y5_4_8 + model.z5_4_8 - 1.0 == 0)
model.v6_4_8 = Constraint(expr=-model.z6_4_7 - model.y6_3_8 - model.x5_4_8 + model.x6_4_8 + model.y6_4_8 + model.z6_4_8 - 1.0 == 0)
model.v7_4_8 = Constraint(expr=-model.z7_4_7 - model.y7_3_8 - model.x6_4_8 + model.x7_4_8 + model.y7_4_8 + model.z7_4_8 - 1.0 == 0)
model.v8_4_8 = Constraint(expr=-model.z8_4_7 - model.y8_3_8 - model.x7_4_8 + model.x8_4_8 + model.y8_4_8 + model.z8_4_8 - 1.0 == 0)
model.v9_4_8 = Constraint(expr=-model.z9_4_7 - model.y9_3_8 - model.x8_4_8 + model.x9_4_8 + model.y9_4_8 + model.z9_4_8 - 1.0 == 0)
model.v10_4_8 = Constraint(expr=-model.x9_4_8 - model.z10_4_7 - model.y10_3_8 + model.y10_4_8 + model.z10_4_8 + model.y11_4_8 + model.z11_4_8 - 1.0 == 0)
model.v1_5_8 = Constraint(expr=-model.z1_5_7 - model.y1_4_8 + model.x1_5_8 + model.y1_5_8 + model.z1_5_8 + model.y0_5_8 + model.z0_5_8 - 1.0 == 0)
model.v2_5_8 = Constraint(expr=-model.z2_5_7 - model.y2_4_8 - model.x1_5_8 + model.x2_5_8 + model.y2_5_8 + model.z2_5_8 - 1.0 == 0)
model.v3_5_8 = Constraint(expr=-model.z3_5_7 - model.y3_4_8 - model.x2_5_8 + model.x3_5_8 + model.y3_5_8 + model.z3_5_8 - 1.0 == 0)
model.v4_5_8 = Constraint(expr=-model.z4_5_7 - model.y4_4_8 - model.x3_5_8 + model.x4_5_8 + model.y4_5_8 + model.z4_5_8 - 1.0 == 0)
model.v5_5_8 = Constraint(expr=-model.z5_5_7 - model.y5_4_8 - model.x4_5_8 + model.x5_5_8 + model.y5_5_8 + model.z5_5_8 - 1.0 == 0)
model.v6_5_8 = Constraint(expr=-model.z6_5_7 - model.y6_4_8 - model.x5_5_8 + model.x6_5_8 + model.y6_5_8 + model.z6_5_8 - 1.0 == 0)
model.v7_5_8 = Constraint(expr=-model.z7_5_7 - model.y7_4_8 - model.x6_5_8 + model.x7_5_8 + model.y7_5_8 + model.z7_5_8 - 1.0 == 0)
model.v8_5_8 = Constraint(expr=-model.z8_5_7 - model.y8_4_8 - model.x7_5_8 + model.x8_5_8 + model.y8_5_8 + model.z8_5_8 - 1.0 == 0)
model.v9_5_8 = Constraint(expr=-model.z9_5_7 - model.y9_4_8 - model.x8_5_8 + model.x9_5_8 + model.y9_5_8 + model.z9_5_8 - 1.0 == 0)
model.v10_5_8 = Constraint(expr=-model.x9_5_8 - model.z10_5_7 - model.y10_4_8 + model.y10_5_8 + model.z10_5_8 + model.y11_5_8 + model.z11_5_8 - 1.0 == 0)
model.v1_6_8 = Constraint(expr=-model.z1_6_7 - model.y1_5_8 + model.x1_6_8 + model.y1_6_8 + model.z1_6_8 + model.y0_6_8 + model.z0_6_8 - 1.0 == 0)
model.v2_6_8 = Constraint(expr=-model.z2_6_7 - model.y2_5_8 - model.x1_6_8 + model.x2_6_8 + model.y2_6_8 + model.z2_6_8 - 1.0 == 0)
model.v3_6_8 = Constraint(expr=-model.z3_6_7 - model.y3_5_8 - model.x2_6_8 + model.x3_6_8 + model.y3_6_8 + model.z3_6_8 - 1.0 == 0)
model.v4_6_8 = Constraint(expr=-model.z4_6_7 - model.y4_5_8 - model.x3_6_8 + model.x4_6_8 + model.y4_6_8 + model.z4_6_8 - 1.0 == 0)
model.v5_6_8 = Constraint(expr=-model.z5_6_7 - model.y5_5_8 - model.x4_6_8 + model.x5_6_8 + model.y5_6_8 + model.z5_6_8 - 1.0 == 0)
model.v6_6_8 = Constraint(expr=-model.z6_6_7 - model.y6_5_8 - model.x5_6_8 + model.x6_6_8 + model.y6_6_8 + model.z6_6_8 - 1.0 == 0)
model.v7_6_8 = Constraint(expr=-model.z7_6_7 - model.y7_5_8 - model.x6_6_8 + model.x7_6_8 + model.y7_6_8 + model.z7_6_8 - 1.0 == 0)
model.v8_6_8 = Constraint(expr=-model.z8_6_7 - model.y8_5_8 - model.x7_6_8 + model.x8_6_8 + model.y8_6_8 + model.z8_6_8 - 1.0 == 0)
model.v9_6_8 = Constraint(expr=-model.z9_6_7 - model.y9_5_8 - model.x8_6_8 + model.x9_6_8 + model.y9_6_8 + model.z9_6_8 - 1.0 == 0)
model.v10_6_8 = Constraint(expr=-model.x9_6_8 - model.z10_6_7 - model.y10_5_8 + model.y10_6_8 + model.z10_6_8 + model.y11_6_8 + model.z11_6_8 - 1.0 == 0)
model.v1_7_8 = Constraint(expr=-model.z1_7_7 - model.y1_6_8 + model.x1_7_8 + model.y1_7_8 + model.z1_7_8 + model.y0_7_8 + model.z0_7_8 - 1.0 == 0)
model.v2_7_8 = Constraint(expr=-model.z2_7_7 - model.y2_6_8 - model.x1_7_8 + model.x2_7_8 + model.y2_7_8 + model.z2_7_8 - 1.0 == 0)
model.v3_7_8 = Constraint(expr=-model.z3_7_7 - model.y3_6_8 - model.x2_7_8 + model.x3_7_8 + model.y3_7_8 + model.z3_7_8 - 1.0 == 0)
model.v4_7_8 = Constraint(expr=-model.z4_7_7 - model.y4_6_8 - model.x3_7_8 + model.x4_7_8 + model.y4_7_8 + model.z4_7_8 - 1.0 == 0)
model.v5_7_8 = Constraint(expr=-model.z5_7_7 - model.y5_6_8 - model.x4_7_8 + model.x5_7_8 + model.y5_7_8 + model.z5_7_8 - 1.0 == 0)
model.v6_7_8 = Constraint(expr=-model.z6_7_7 - model.y6_6_8 - model.x5_7_8 + model.x6_7_8 + model.y6_7_8 + model.z6_7_8 - 1.0 == 0)
model.v7_7_8 = Constraint(expr=-model.z7_7_7 - model.y7_6_8 - model.x6_7_8 + model.x7_7_8 + model.y7_7_8 + model.z7_7_8 - 1.0 == 0)
model.v8_7_8 = Constraint(expr=-model.z8_7_7 - model.y8_6_8 - model.x7_7_8 + model.x8_7_8 + model.y8_7_8 + model.z8_7_8 - 1.0 == 0)
model.v9_7_8 = Constraint(expr=-model.z9_7_7 - model.y9_6_8 - model.x8_7_8 + model.x9_7_8 + model.y9_7_8 + model.z9_7_8 - 1.0 == 0)
model.v10_7_8 = Constraint(expr=-model.x9_7_8 - model.z10_7_7 - model.y10_6_8 + model.y10_7_8 + model.z10_7_8 + model.y11_7_8 + model.z11_7_8 - 1.0 == 0)
model.v1_8_8 = Constraint(expr=-model.z1_8_7 - model.y1_7_8 + model.x1_8_8 + model.y1_8_8 + model.z1_8_8 + model.y0_8_8 + model.z0_8_8 - 1.0 == 0)
model.v2_8_8 = Constraint(expr=-model.z2_8_7 - model.y2_7_8 - model.x1_8_8 + model.x2_8_8 + model.y2_8_8 + model.z2_8_8 - 1.0 == 0)
model.v3_8_8 = Constraint(expr=-model.z3_8_7 - model.y3_7_8 - model.x2_8_8 + model.x3_8_8 + model.y3_8_8 + model.z3_8_8 - 1.0 == 0)
model.v4_8_8 = Constraint(expr=-model.z4_8_7 - model.y4_7_8 - model.x3_8_8 + model.x4_8_8 + model.y4_8_8 + model.z4_8_8 - 1.0 == 0)
model.v5_8_8 = Constraint(expr=-model.z5_8_7 - model.y5_7_8 - model.x4_8_8 + model.x5_8_8 + model.y5_8_8 + model.z5_8_8 - 1.0 == 0)
model.v6_8_8 = Constraint(expr=-model.z6_8_7 - model.y6_7_8 - model.x5_8_8 + model.x6_8_8 + model.y6_8_8 + model.z6_8_8 - 1.0 == 0)
model.v7_8_8 = Constraint(expr=-model.z7_8_7 - model.y7_7_8 - model.x6_8_8 + model.x7_8_8 + model.y7_8_8 + model.z7_8_8 - 1.0 == 0)
model.v8_8_8 = Constraint(expr=-model.z8_8_7 - model.y8_7_8 - model.x7_8_8 + model.x8_8_8 + model.y8_8_8 + model.z8_8_8 - 1.0 == 0)
model.v9_8_8 = Constraint(expr=-model.z9_8_7 - model.y9_7_8 - model.x8_8_8 + model.x9_8_8 + model.y9_8_8 + model.z9_8_8 - 1.0 == 0)
model.v10_8_8 = Constraint(expr=-model.x9_8_8 - model.z10_8_7 - model.y10_7_8 + model.y10_8_8 + model.z10_8_8 + model.y11_8_8 + model.z11_8_8 - 1.0 == 0)
model.v1_9_8 = Constraint(expr=-model.z1_9_7 - model.y1_8_8 + model.x1_9_8 + model.y1_9_8 + model.z1_9_8 + model.y0_9_8 + model.z0_9_8 - 1.0 == 0)
model.v2_9_8 = Constraint(expr=-model.z2_9_7 - model.y2_8_8 - model.x1_9_8 + model.x2_9_8 + model.y2_9_8 + model.z2_9_8 - 1.0 == 0)
model.v3_9_8 = Constraint(expr=-model.z3_9_7 - model.y3_8_8 - model.x2_9_8 + model.x3_9_8 + model.y3_9_8 + model.z3_9_8 - 1.0 == 0)
model.v4_9_8 = Constraint(expr=-model.z4_9_7 - model.y4_8_8 - model.x3_9_8 + model.x4_9_8 + model.y4_9_8 + model.z4_9_8 - 1.0 == 0)
model.v5_9_8 = Constraint(expr=-model.z5_9_7 - model.y5_8_8 - model.x4_9_8 + model.x5_9_8 + model.y5_9_8 + model.z5_9_8 - 1.0 == 0)
model.v6_9_8 = Constraint(expr=-model.z6_9_7 - model.y6_8_8 - model.x5_9_8 + model.x6_9_8 + model.y6_9_8 + model.z6_9_8 - 1.0 == 0)
model.v7_9_8 = Constraint(expr=-model.z7_9_7 - model.y7_8_8 - model.x6_9_8 + model.x7_9_8 + model.y7_9_8 + model.z7_9_8 - 1.0 == 0)
model.v8_9_8 = Constraint(expr=-model.z8_9_7 - model.y8_8_8 - model.x7_9_8 + model.x8_9_8 + model.y8_9_8 + model.z8_9_8 - 1.0 == 0)
model.v9_9_8 = Constraint(expr=-model.z9_9_7 - model.y9_8_8 - model.x8_9_8 + model.x9_9_8 + model.y9_9_8 + model.z9_9_8 - 1.0 == 0)
model.v10_9_8 = Constraint(expr=-model.x9_9_8 - model.z10_9_7 - model.y10_8_8 + model.y10_9_8 + model.z10_9_8 + model.y11_9_8 + model.z11_9_8 - 1.0 == 0)
model.v1_10_8 = Constraint(expr=-model.y1_9_8 - model.z1_10_7 + model.x1_10_8 + model.z1_10_8 + model.y0_10_8 + model.z0_10_8 + model.x1_11_8 + model.z1_11_8 - 1.0 == 0)
model.v2_10_8 = Constraint(expr=-model.y2_9_8 - model.z2_10_7 - model.x1_10_8 + model.x2_10_8 + model.z2_10_8 + model.x2_11_8 + model.z2_11_8 - 1.0 == 0)
model.v3_10_8 = Constraint(expr=-model.y3_9_8 - model.z3_10_7 - model.x2_10_8 + model.x3_10_8 + model.z3_10_8 + model.x3_11_8 + model.z3_11_8 - 1.0 == 0)
model.v4_10_8 = Constraint(expr=-model.y4_9_8 - model.z4_10_7 - model.x3_10_8 + model.x4_10_8 + model.z4_10_8 + model.x4_11_8 + model.z4_11_8 - 1.0 == 0)
model.v5_10_8 = Constraint(expr=-model.y5_9_8 - model.z5_10_7 - model.x4_10_8 + model.x5_10_8 + model.z5_10_8 + model.x5_11_8 + model.z5_11_8 - 1.0 == 0)
model.v6_10_8 = Constraint(expr=-model.y6_9_8 - model.z6_10_7 - model.x5_10_8 + model.x6_10_8 + model.z6_10_8 + model.x6_11_8 + model.z6_11_8 - 1.0 == 0)
model.v7_10_8 = Constraint(expr=-model.y7_9_8 - model.z7_10_7 - model.x6_10_8 + model.x7_10_8 + model.z7_10_8 + model.x7_11_8 + model.z7_11_8 - 1.0 == 0)
model.v8_10_8 = Constraint(expr=-model.y8_9_8 - model.z8_10_7 - model.x7_10_8 + model.x8_10_8 + model.z8_10_8 + model.x8_11_8 + model.z8_11_8 - 1.0 == 0)
model.v9_10_8 = Constraint(expr=-model.y9_9_8 - model.z9_10_7 - model.x8_10_8 + model.x9_10_8 + model.z9_10_8 + model.x9_11_8 + model.z9_11_8 - 1.0 == 0)
model.v10_10_8 = Constraint(expr=-model.y10_9_8 - model.x9_10_8 + model.y11_10_8 + model.z11_10_8 + model.x10_11_8 + model.z10_11_8 - 1.0 == 0)
model.v1_1_9 = Constraint(expr=-model.z1_1_8 + model.x1_1_9 + model.y1_1_9 + model.z1_1_9 + model.y0_1_9 + model.z0_1_9 + model.x1_0_9 + model.z1_0_9 - 1.0 == 0)
model.v2_1_9 = Constraint(expr=-model.z2_1_8 - model.x1_1_9 + model.x2_1_9 + model.y2_1_9 + model.z2_1_9 + model.x2_0_9 + model.z2_0_9 - 1.0 == 0)
model.v3_1_9 = Constraint(expr=-model.z3_1_8 - model.x2_1_9 + model.x3_1_9 + model.y3_1_9 + model.z3_1_9 + model.x3_0_9 + model.z3_0_9 - 1.0 == 0)
model.v4_1_9 = Constraint(expr=-model.z4_1_8 - model.x3_1_9 + model.x4_1_9 + model.y4_1_9 + model.z4_1_9 + model.x4_0_9 + model.z4_0_9 - 1.0 == 0)
model.v5_1_9 = Constraint(expr=-model.z5_1_8 - model.x4_1_9 + model.x5_1_9 + model.y5_1_9 + model.z5_1_9 + model.x5_0_9 + model.z5_0_9 - 1.0 == 0)
model.v6_1_9 = Constraint(expr=-model.z6_1_8 - model.x5_1_9 + model.x6_1_9 + model.y6_1_9 + model.z6_1_9 + model.x6_0_9 + model.z6_0_9 - 1.0 == 0)
model.v7_1_9 = Constraint(expr=-model.z7_1_8 - model.x6_1_9 + model.x7_1_9 + model.y7_1_9 + model.z7_1_9 + model.x7_0_9 + model.z7_0_9 - 1.0 == 0)
model.v8_1_9 = Constraint(expr=-model.z8_1_8 - model.x7_1_9 + model.x8_1_9 + model.y8_1_9 + model.z8_1_9 + model.x8_0_9 + model.z8_0_9 - 1.0 == 0)
model.v9_1_9 = Constraint(expr=-model.z9_1_8 - model.x8_1_9 + model.x9_1_9 + model.y9_1_9 + model.z9_1_9 + model.x9_0_9 + model.z9_0_9 - 1.0 == 0)
model.v10_1_9 = Constraint(expr=-model.x9_1_9 - model.z10_1_8 + model.y10_1_9 + model.z10_1_9 + model.y11_1_9 + model.z11_1_9 + model.x10_0_9 + model.z10_0_9 - 1.0 == 0)
model.v1_2_9 = Constraint(expr=-model.z1_2_8 - model.y1_1_9 + model.x1_2_9 + model.y1_2_9 + model.z1_2_9 + model.y0_2_9 + model.z0_2_9 - 1.0 == 0)
model.v2_2_9 = Constraint(expr=-model.z2_2_8 - model.y2_1_9 - model.x1_2_9 + model.x2_2_9 + model.y2_2_9 + model.z2_2_9 - 1.0 == 0)
model.v3_2_9 = Constraint(expr=-model.z3_2_8 - model.y3_1_9 - model.x2_2_9 + model.x3_2_9 + model.y3_2_9 + model.z3_2_9 - 1.0 == 0)
model.v4_2_9 = Constraint(expr=-model.z4_2_8 - model.y4_1_9 - model.x3_2_9 + model.x4_2_9 + model.y4_2_9 + model.z4_2_9 - 1.0 == 0)
model.v5_2_9 = Constraint(expr=-model.z5_2_8 - model.y5_1_9 - model.x4_2_9 + model.x5_2_9 + model.y5_2_9 + model.z5_2_9 - 1.0 == 0)
model.v6_2_9 = Constraint(expr=-model.z6_2_8 - model.y6_1_9 - model.x5_2_9 + model.x6_2_9 + model.y6_2_9 + model.z6_2_9 - 1.0 == 0)
model.v7_2_9 = Constraint(expr=-model.z7_2_8 - model.y7_1_9 - model.x6_2_9 + model.x7_2_9 + model.y7_2_9 + model.z7_2_9 - 1.0 == 0)
model.v8_2_9 = Constraint(expr=-model.z8_2_8 - model.y8_1_9 - model.x7_2_9 + model.x8_2_9 + model.y8_2_9 + model.z8_2_9 - 1.0 == 0)
model.v9_2_9 = Constraint(expr=-model.z9_2_8 - model.y9_1_9 - model.x8_2_9 + model.x9_2_9 + model.y9_2_9 + model.z9_2_9 - 1.0 == 0)
model.v10_2_9 = Constraint(expr=-model.x9_2_9 - model.z10_2_8 - model.y10_1_9 + model.y10_2_9 + model.z10_2_9 + model.y11_2_9 + model.z11_2_9 - 1.0 == 0)
model.v1_3_9 = Constraint(expr=-model.z1_3_8 - model.y1_2_9 + model.x1_3_9 + model.y1_3_9 + model.z1_3_9 + model.y0_3_9 + model.z0_3_9 - 1.0 == 0)
model.v2_3_9 = Constraint(expr=-model.z2_3_8 - model.y2_2_9 - model.x1_3_9 + model.x2_3_9 + model.y2_3_9 + model.z2_3_9 - 1.0 == 0)
model.v3_3_9 = Constraint(expr=-model.z3_3_8 - model.y3_2_9 - model.x2_3_9 + model.x3_3_9 + model.y3_3_9 + model.z3_3_9 - 1.0 == 0)
model.v4_3_9 = Constraint(expr=-model.z4_3_8 - model.y4_2_9 - model.x3_3_9 + model.x4_3_9 + model.y4_3_9 + model.z4_3_9 - 1.0 == 0)
model.v5_3_9 = Constraint(expr=-model.z5_3_8 - model.y5_2_9 - model.x4_3_9 + model.x5_3_9 + model.y5_3_9 + model.z5_3_9 - 1.0 == 0)
model.v6_3_9 = Constraint(expr=-model.z6_3_8 - model.y6_2_9 - model.x5_3_9 + model.x6_3_9 + model.y6_3_9 + model.z6_3_9 - 1.0 == 0)
model.v7_3_9 = Constraint(expr=-model.z7_3_8 - model.y7_2_9 - model.x6_3_9 + model.x7_3_9 + model.y7_3_9 + model.z7_3_9 - 1.0 == 0)
model.v8_3_9 = Constraint(expr=-model.z8_3_8 - model.y8_2_9 - model.x7_3_9 + model.x8_3_9 + model.y8_3_9 + model.z8_3_9 - 1.0 == 0)
model.v9_3_9 = Constraint(expr=-model.z9_3_8 - model.y9_2_9 - model.x8_3_9 + model.x9_3_9 + model.y9_3_9 + model.z9_3_9 - 1.0 == 0)
model.v10_3_9 = Constraint(expr=-model.x9_3_9 - model.z10_3_8 - model.y10_2_9 + model.y10_3_9 + model.z10_3_9 + model.y11_3_9 + model.z11_3_9 - 1.0 == 0)
model.v1_4_9 = Constraint(expr=-model.z1_4_8 - model.y1_3_9 + model.x1_4_9 + model.y1_4_9 + model.z1_4_9 + model.y0_4_9 + model.z0_4_9 - 1.0 == 0)
model.v2_4_9 = Constraint(expr=-model.z2_4_8 - model.y2_3_9 - model.x1_4_9 + model.x2_4_9 + model.y2_4_9 + model.z2_4_9 - 1.0 == 0)
model.v3_4_9 = Constraint(expr=-model.z3_4_8 - model.y3_3_9 - model.x2_4_9 + model.x3_4_9 + model.y3_4_9 + model.z3_4_9 - 1.0 == 0)
model.v4_4_9 = Constraint(expr=-model.z4_4_8 - model.y4_3_9 - model.x3_4_9 + model.x4_4_9 + model.y4_4_9 + model.z4_4_9 - 1.0 == 0)
model.v5_4_9 = Constraint(expr=-model.z5_4_8 - model.y5_3_9 - model.x4_4_9 + model.x5_4_9 + model.y5_4_9 + model.z5_4_9 - 1.0 == 0)
model.v6_4_9 = Constraint(expr=-model.z6_4_8 - model.y6_3_9 - model.x5_4_9 + model.x6_4_9 + model.y6_4_9 + model.z6_4_9 - 1.0 == 0)
model.v7_4_9 = Constraint(expr=-model.z7_4_8 - model.y7_3_9 - model.x6_4_9 + model.x7_4_9 + model.y7_4_9 + model.z7_4_9 - 1.0 == 0)
model.v8_4_9 = Constraint(expr=-model.z8_4_8 - model.y8_3_9 - model.x7_4_9 + model.x8_4_9 + model.y8_4_9 + model.z8_4_9 - 1.0 == 0)
model.v9_4_9 = Constraint(expr=-model.z9_4_8 - model.y9_3_9 - model.x8_4_9 + model.x9_4_9 + model.y9_4_9 + model.z9_4_9 - 1.0 == 0)
model.v10_4_9 = Constraint(expr=-model.x9_4_9 - model.z10_4_8 - model.y10_3_9 + model.y10_4_9 + model.z10_4_9 + model.y11_4_9 + model.z11_4_9 - 1.0 == 0)
model.v1_5_9 = Constraint(expr=-model.z1_5_8 - model.y1_4_9 + model.x1_5_9 + model.y1_5_9 + model.z1_5_9 + model.y0_5_9 + model.z0_5_9 - 1.0 == 0)
model.v2_5_9 = Constraint(expr=-model.z2_5_8 - model.y2_4_9 - model.x1_5_9 + model.x2_5_9 + model.y2_5_9 + model.z2_5_9 - 1.0 == 0)
model.v3_5_9 = Constraint(expr=-model.z3_5_8 - model.y3_4_9 - model.x2_5_9 + model.x3_5_9 + model.y3_5_9 + model.z3_5_9 - 1.0 == 0)
model.v4_5_9 = Constraint(expr=-model.z4_5_8 - model.y4_4_9 - model.x3_5_9 + model.x4_5_9 + model.y4_5_9 + model.z4_5_9 - 1.0 == 0)
model.v5_5_9 = Constraint(expr=-model.z5_5_8 - model.y5_4_9 - model.x4_5_9 + model.x5_5_9 + model.y5_5_9 + model.z5_5_9 - 1.0 == 0)
model.v6_5_9 = Constraint(expr=-model.z6_5_8 - model.y6_4_9 - model.x5_5_9 + model.x6_5_9 + model.y6_5_9 + model.z6_5_9 - 1.0 == 0)
model.v7_5_9 = Constraint(expr=-model.z7_5_8 - model.y7_4_9 - model.x6_5_9 + model.x7_5_9 + model.y7_5_9 + model.z7_5_9 - 1.0 == 0)
model.v8_5_9 = Constraint(expr=-model.z8_5_8 - model.y8_4_9 - model.x7_5_9 + model.x8_5_9 + model.y8_5_9 + model.z8_5_9 - 1.0 == 0)
model.v9_5_9 = Constraint(expr=-model.z9_5_8 - model.y9_4_9 - model.x8_5_9 + model.x9_5_9 + model.y9_5_9 + model.z9_5_9 - 1.0 == 0)
model.v10_5_9 = Constraint(expr=-model.x9_5_9 - model.z10_5_8 - model.y10_4_9 + model.y10_5_9 + model.z10_5_9 + model.y11_5_9 + model.z11_5_9 - 1.0 == 0)
model.v1_6_9 = Constraint(expr=-model.z1_6_8 - model.y1_5_9 + model.x1_6_9 + model.y1_6_9 + model.z1_6_9 + model.y0_6_9 + model.z0_6_9 - 1.0 == 0)
model.v2_6_9 = Constraint(expr=-model.z2_6_8 - model.y2_5_9 - model.x1_6_9 + model.x2_6_9 + model.y2_6_9 + model.z2_6_9 - 1.0 == 0)
model.v3_6_9 = Constraint(expr=-model.z3_6_8 - model.y3_5_9 - model.x2_6_9 + model.x3_6_9 + model.y3_6_9 + model.z3_6_9 - 1.0 == 0)
model.v4_6_9 = Constraint(expr=-model.z4_6_8 - model.y4_5_9 - model.x3_6_9 + model.x4_6_9 + model.y4_6_9 + model.z4_6_9 - 1.0 == 0)
model.v5_6_9 = Constraint(expr=-model.z5_6_8 - model.y5_5_9 - model.x4_6_9 + model.x5_6_9 + model.y5_6_9 + model.z5_6_9 - 1.0 == 0)
model.v6_6_9 = Constraint(expr=-model.z6_6_8 - model.y6_5_9 - model.x5_6_9 + model.x6_6_9 + model.y6_6_9 + model.z6_6_9 - 1.0 == 0)
model.v7_6_9 = Constraint(expr=-model.z7_6_8 - model.y7_5_9 - model.x6_6_9 + model.x7_6_9 + model.y7_6_9 + model.z7_6_9 - 1.0 == 0)
model.v8_6_9 = Constraint(expr=-model.z8_6_8 - model.y8_5_9 - model.x7_6_9 + model.x8_6_9 + model.y8_6_9 + model.z8_6_9 - 1.0 == 0)
model.v9_6_9 = Constraint(expr=-model.z9_6_8 - model.y9_5_9 - model.x8_6_9 + model.x9_6_9 + model.y9_6_9 + model.z9_6_9 - 1.0 == 0)
model.v10_6_9 = Constraint(expr=-model.x9_6_9 - model.z10_6_8 - model.y10_5_9 + model.y10_6_9 + model.z10_6_9 + model.y11_6_9 + model.z11_6_9 - 1.0 == 0)
model.v1_7_9 = Constraint(expr=-model.z1_7_8 - model.y1_6_9 + model.x1_7_9 + model.y1_7_9 + model.z1_7_9 + model.y0_7_9 + model.z0_7_9 - 1.0 == 0)
model.v2_7_9 = Constraint(expr=-model.z2_7_8 - model.y2_6_9 - model.x1_7_9 + model.x2_7_9 + model.y2_7_9 + model.z2_7_9 - 1.0 == 0)
model.v3_7_9 = Constraint(expr=-model.z3_7_8 - model.y3_6_9 - model.x2_7_9 + model.x3_7_9 + model.y3_7_9 + model.z3_7_9 - 1.0 == 0)
model.v4_7_9 = Constraint(expr=-model.z4_7_8 - model.y4_6_9 - model.x3_7_9 + model.x4_7_9 + model.y4_7_9 + model.z4_7_9 - 1.0 == 0)
model.v5_7_9 = Constraint(expr=-model.z5_7_8 - model.y5_6_9 - model.x4_7_9 + model.x5_7_9 + model.y5_7_9 + model.z5_7_9 - 1.0 == 0)
model.v6_7_9 = Constraint(expr=-model.z6_7_8 - model.y6_6_9 - model.x5_7_9 + model.x6_7_9 + model.y6_7_9 + model.z6_7_9 - 1.0 == 0)
model.v7_7_9 = Constraint(expr=-model.z7_7_8 - model.y7_6_9 - model.x6_7_9 + model.x7_7_9 + model.y7_7_9 + model.z7_7_9 - 1.0 == 0)
model.v8_7_9 = Constraint(expr=-model.z8_7_8 - model.y8_6_9 - model.x7_7_9 + model.x8_7_9 + model.y8_7_9 + model.z8_7_9 - 1.0 == 0)
model.v9_7_9 = Constraint(expr=-model.z9_7_8 - model.y9_6_9 - model.x8_7_9 + model.x9_7_9 + model.y9_7_9 + model.z9_7_9 - 1.0 == 0)
model.v10_7_9 = Constraint(expr=-model.x9_7_9 - model.z10_7_8 - model.y10_6_9 + model.y10_7_9 + model.z10_7_9 + model.y11_7_9 + model.z11_7_9 - 1.0 == 0)
model.v1_8_9 = Constraint(expr=-model.z1_8_8 - model.y1_7_9 + model.x1_8_9 + model.y1_8_9 + model.z1_8_9 + model.y0_8_9 + model.z0_8_9 - 1.0 == 0)
model.v2_8_9 = Constraint(expr=-model.z2_8_8 - model.y2_7_9 - model.x1_8_9 + model.x2_8_9 + model.y2_8_9 + model.z2_8_9 - 1.0 == 0)
model.v3_8_9 = Constraint(expr=-model.z3_8_8 - model.y3_7_9 - model.x2_8_9 + model.x3_8_9 + model.y3_8_9 + model.z3_8_9 - 1.0 == 0)
model.v4_8_9 = Constraint(expr=-model.z4_8_8 - model.y4_7_9 - model.x3_8_9 + model.x4_8_9 + model.y4_8_9 + model.z4_8_9 - 1.0 == 0)
model.v5_8_9 = Constraint(expr=-model.z5_8_8 - model.y5_7_9 - model.x4_8_9 + model.x5_8_9 + model.y5_8_9 + model.z5_8_9 - 1.0 == 0)
model.v6_8_9 = Constraint(expr=-model.z6_8_8 - model.y6_7_9 - model.x5_8_9 + model.x6_8_9 + model.y6_8_9 + model.z6_8_9 - 1.0 == 0)
model.v7_8_9 = Constraint(expr=-model.z7_8_8 - model.y7_7_9 - model.x6_8_9 + model.x7_8_9 + model.y7_8_9 + model.z7_8_9 - 1.0 == 0)
model.v8_8_9 = Constraint(expr=-model.z8_8_8 - model.y8_7_9 - model.x7_8_9 + model.x8_8_9 + model.y8_8_9 + model.z8_8_9 - 1.0 == 0)
model.v9_8_9 = Constraint(expr=-model.z9_8_8 - model.y9_7_9 - model.x8_8_9 + model.x9_8_9 + model.y9_8_9 + model.z9_8_9 - 1.0 == 0)
model.v10_8_9 = Constraint(expr=-model.x9_8_9 - model.z10_8_8 - model.y10_7_9 + model.y10_8_9 + model.z10_8_9 + model.y11_8_9 + model.z11_8_9 - 1.0 == 0)
model.v1_9_9 = Constraint(expr=-model.z1_9_8 - model.y1_8_9 + model.x1_9_9 + model.y1_9_9 + model.z1_9_9 + model.y0_9_9 + model.z0_9_9 - 1.0 == 0)
model.v2_9_9 = Constraint(expr=-model.z2_9_8 - model.y2_8_9 - model.x1_9_9 + model.x2_9_9 + model.y2_9_9 + model.z2_9_9 - 1.0 == 0)
model.v3_9_9 = Constraint(expr=-model.z3_9_8 - model.y3_8_9 - model.x2_9_9 + model.x3_9_9 + model.y3_9_9 + model.z3_9_9 - 1.0 == 0)
model.v4_9_9 = Constraint(expr=-model.z4_9_8 - model.y4_8_9 - model.x3_9_9 + model.x4_9_9 + model.y4_9_9 + model.z4_9_9 - 1.0 == 0)
model.v5_9_9 = Constraint(expr=-model.z5_9_8 - model.y5_8_9 - model.x4_9_9 + model.x5_9_9 + model.y5_9_9 + model.z5_9_9 - 1.0 == 0)
model.v6_9_9 = Constraint(expr=-model.z6_9_8 - model.y6_8_9 - model.x5_9_9 + model.x6_9_9 + model.y6_9_9 + model.z6_9_9 - 1.0 == 0)
model.v7_9_9 = Constraint(expr=-model.z7_9_8 - model.y7_8_9 - model.x6_9_9 + model.x7_9_9 + model.y7_9_9 + model.z7_9_9 - 1.0 == 0)
model.v8_9_9 = Constraint(expr=-model.z8_9_8 - model.y8_8_9 - model.x7_9_9 + model.x8_9_9 + model.y8_9_9 + model.z8_9_9 - 1.0 == 0)
model.v9_9_9 = Constraint(expr=-model.z9_9_8 - model.y9_8_9 - model.x8_9_9 + model.x9_9_9 + model.y9_9_9 + model.z9_9_9 - 1.0 == 0)
model.v10_9_9 = Constraint(expr=-model.x9_9_9 - model.z10_9_8 - model.y10_8_9 + model.y10_9_9 + model.z10_9_9 + model.y11_9_9 + model.z11_9_9 - 1.0 == 0)
model.v1_10_9 = Constraint(expr=-model.y1_9_9 - model.z1_10_8 + model.x1_10_9 + model.z1_10_9 + model.y0_10_9 + model.z0_10_9 + model.x1_11_9 + model.z1_11_9 - 1.0 == 0)
model.v2_10_9 = Constraint(expr=-model.y2_9_9 - model.z2_10_8 - model.x1_10_9 + model.x2_10_9 + model.z2_10_9 + model.x2_11_9 + model.z2_11_9 - 1.0 == 0)
model.v3_10_9 = Constraint(expr=-model.y3_9_9 - model.z3_10_8 - model.x2_10_9 + model.x3_10_9 + model.z3_10_9 + model.x3_11_9 + model.z3_11_9 - 1.0 == 0)
model.v4_10_9 = Constraint(expr=-model.y4_9_9 - model.z4_10_8 - model.x3_10_9 + model.x4_10_9 + model.z4_10_9 + model.x4_11_9 + model.z4_11_9 - 1.0 == 0)
model.v5_10_9 = Constraint(expr=-model.y5_9_9 - model.z5_10_8 - model.x4_10_9 + model.x5_10_9 + model.z5_10_9 + model.x5_11_9 + model.z5_11_9 - 1.0 == 0)
model.v6_10_9 = Constraint(expr=-model.y6_9_9 - model.z6_10_8 - model.x5_10_9 + model.x6_10_9 + model.z6_10_9 + model.x6_11_9 + model.z6_11_9 - 1.0 == 0)
model.v7_10_9 = Constraint(expr=-model.y7_9_9 - model.z7_10_8 - model.x6_10_9 + model.x7_10_9 + model.z7_10_9 + model.x7_11_9 + model.z7_11_9 - 1.0 == 0)
model.v8_10_9 = Constraint(expr=-model.y8_9_9 - model.z8_10_8 - model.x7_10_9 + model.x8_10_9 + model.z8_10_9 + model.x8_11_9 + model.z8_11_9 - 1.0 == 0)
model.v9_10_9 = Constraint(expr=-model.y9_9_9 - model.z9_10_8 - model.x8_10_9 + model.x9_10_9 + model.z9_10_9 + model.x9_11_9 + model.z9_11_9 - 1.0 == 0)
model.v10_10_9 = Constraint(expr=-model.y10_9_9 - model.x9_10_9 + model.y11_10_9 + model.z11_10_9 + model.x10_11_9 + model.z10_11_9 - 1.0 == 0)
model.v1_1_10 = Constraint(expr=-model.z1_1_9 + model.x1_1_10 + model.y1_1_10 + model.y0_1_10 + model.z0_1_10 + model.x1_0_10 + model.z1_0_10 + model.x1_1_11 + model.y1_1_11 - 1.0 == 0)
model.v2_1_10 = Constraint(expr=-model.z2_1_9 - model.x1_1_10 + model.x2_1_10 + model.y2_1_10 + model.x2_0_10 + model.z2_0_10 + model.x2_1_11 + model.y2_1_11 - 1.0 == 0)
model.v3_1_10 = Constraint(expr=-model.z3_1_9 - model.x2_1_10 + model.x3_1_10 + model.y3_1_10 + model.x3_0_10 + model.z3_0_10 + model.x3_1_11 + model.y3_1_11 - 1.0 == 0)
model.v4_1_10 = Constraint(expr=-model.z4_1_9 - model.x3_1_10 + model.x4_1_10 + model.y4_1_10 + model.x4_0_10 + model.z4_0_10 + model.x4_1_11 + model.y4_1_11 - 1.0 == 0)
model.v5_1_10 = Constraint(expr=-model.z5_1_9 - model.x4_1_10 + model.x5_1_10 + model.y5_1_10 + model.x5_0_10 + model.z5_0_10 + model.x5_1_11 + model.y5_1_11 - 1.0 == 0)
model.v6_1_10 = Constraint(expr=-model.z6_1_9 - model.x5_1_10 + model.x6_1_10 + model.y6_1_10 + model.x6_0_10 + model.z6_0_10 + model.x6_1_11 + model.y6_1_11 - 1.0 == 0)
model.v7_1_10 = Constraint(expr=-model.z7_1_9 - model.x6_1_10 + model.x7_1_10 + model.y7_1_10 + model.x7_0_10 + model.z7_0_10 + model.x7_1_11 + model.y7_1_11 - 1.0 == 0)
model.v8_1_10 = Constraint(expr=-model.z8_1_9 - model.x7_1_10 + model.x8_1_10 + model.y8_1_10 + model.x8_0_10 + model.z8_0_10 + model.x8_1_11 + model.y8_1_11 - 1.0 == 0)
model.v9_1_10 = Constraint(expr=-model.z9_1_9 - model.x8_1_10 + model.x9_1_10 + model.y9_1_10 + model.x9_0_10 + model.z9_0_10 + model.x9_1_11 + model.y9_1_11 - 1.0 == 0)
model.v10_1_10 = Constraint(expr=-model.z10_1_9 - model.x9_1_10 + model.y11_1_10 + model.z11_1_10 + model.x10_0_10 + model.z10_0_10 + model.x10_1_11 + model.y10_1_11 - 1.0 == 0)
model.v1_2_10 = Constraint(expr=-model.z1_2_9 - model.y1_1_10 + model.x1_2_10 + model.y1_2_10 + model.y0_2_10 + model.z0_2_10 + model.x1_2_11 + model.y1_2_11 - 1.0 == 0)
model.v2_2_10 = Constraint(expr=-model.z2_2_9 - model.y2_1_10 - model.x1_2_10 + model.x2_2_10 + model.y2_2_10 + model.x2_2_11 + model.y2_2_11 - 1.0 == 0)
model.v3_2_10 = Constraint(expr=-model.z3_2_9 - model.y3_1_10 - model.x2_2_10 + model.x3_2_10 + model.y3_2_10 + model.x3_2_11 + model.y3_2_11 - 1.0 == 0)
model.v4_2_10 = Constraint(expr=-model.z4_2_9 - model.y4_1_10 - model.x3_2_10 + model.x4_2_10 + model.y4_2_10 + model.x4_2_11 + model.y4_2_11 - 1.0 == 0)
model.v5_2_10 = Constraint(expr=-model.z5_2_9 - model.y5_1_10 - model.x4_2_10 + model.x5_2_10 + model.y5_2_10 + model.x5_2_11 + model.y5_2_11 - 1.0 == 0)
model.v6_2_10 = Constraint(expr=-model.z6_2_9 - model.y6_1_10 - model.x5_2_10 + model.x6_2_10 + model.y6_2_10 + model.x6_2_11 + model.y6_2_11 - 1.0 == 0)
model.v7_2_10 = Constraint(expr=-model.z7_2_9 - model.y7_1_10 - model.x6_2_10 + model.x7_2_10 + model.y7_2_10 + model.x7_2_11 + model.y7_2_11 - 1.0 == 0)
model.v8_2_10 = Constraint(expr=-model.z8_2_9 - model.y8_1_10 - model.x7_2_10 + model.x8_2_10 + model.y8_2_10 + model.x8_2_11 + model.y8_2_11 - 1.0 == 0)
model.v9_2_10 = Constraint(expr=-model.z9_2_9 - model.y9_1_10 - model.x8_2_10 + model.x9_2_10 + model.y9_2_10 + model.x9_2_11 + model.y9_2_11 - 1.0 == 0)
model.v10_2_10 = Constraint(expr=-model.z10_2_9 - model.x9_2_10 + model.y11_2_10 + model.z11_2_10 + model.x10_2_11 + model.y10_2_11 - 1.0 == 0)
model.v1_3_10 = Constraint(expr=-model.z1_3_9 - model.y1_2_10 + model.x1_3_10 + model.y1_3_10 + model.y0_3_10 + model.z0_3_10 + model.x1_3_11 + model.y1_3_11 - 1.0 == 0)
model.v2_3_10 = Constraint(expr=-model.z2_3_9 - model.y2_2_10 - model.x1_3_10 + model.x2_3_10 + model.y2_3_10 + model.x2_3_11 + model.y2_3_11 - 1.0 == 0)
model.v3_3_10 = Constraint(expr=-model.z3_3_9 - model.y3_2_10 - model.x2_3_10 + model.x3_3_10 + model.y3_3_10 + model.x3_3_11 + model.y3_3_11 - 1.0 == 0)
model.v4_3_10 = Constraint(expr=-model.z4_3_9 - model.y4_2_10 - model.x3_3_10 + model.x4_3_10 + model.y4_3_10 + model.x4_3_11 + model.y4_3_11 - 1.0 == 0)
model.v5_3_10 = Constraint(expr=-model.z5_3_9 - model.y5_2_10 - model.x4_3_10 + model.x5_3_10 + model.y5_3_10 + model.x5_3_11 + model.y5_3_11 - 1.0 == 0)
model.v6_3_10 = Constraint(expr=-model.z6_3_9 - model.y6_2_10 - model.x5_3_10 + model.x6_3_10 + model.y6_3_10 + model.x6_3_11 + model.y6_3_11 - 1.0 == 0)
model.v7_3_10 = Constraint(expr=-model.z7_3_9 - model.y7_2_10 - model.x6_3_10 + model.x7_3_10 + model.y7_3_10 + model.x7_3_11 + model.y7_3_11 - 1.0 == 0)
model.v8_3_10 = Constraint(expr=-model.z8_3_9 - model.y8_2_10 - model.x7_3_10 + model.x8_3_10 + model.y8_3_10 + model.x8_3_11 + model.y8_3_11 - 1.0 == 0)
model.v9_3_10 = Constraint(expr=-model.z9_3_9 - model.y9_2_10 - model.x8_3_10 + model.x9_3_10 + model.y9_3_10 + model.x9_3_11 + model.y9_3_11 - 1.0 == 0)
model.v10_3_10 = Constraint(expr=-model.z10_3_9 - model.x9_3_10 + model.y11_3_10 + model.z11_3_10 + model.x10_3_11 + model.y10_3_11 - 1.0 == 0)
model.v1_4_10 = Constraint(expr=-model.z1_4_9 - model.y1_3_10 + model.x1_4_10 + model.y1_4_10 + model.y0_4_10 + model.z0_4_10 + model.x1_4_11 + model.y1_4_11 - 1.0 == 0)
model.v2_4_10 = Constraint(expr=-model.z2_4_9 - model.y2_3_10 - model.x1_4_10 + model.x2_4_10 + model.y2_4_10 + model.x2_4_11 + model.y2_4_11 - 1.0 == 0)
model.v3_4_10 = Constraint(expr=-model.z3_4_9 - model.y3_3_10 - model.x2_4_10 + model.x3_4_10 + model.y3_4_10 + model.x3_4_11 + model.y3_4_11 - 1.0 == 0)
model.v4_4_10 = Constraint(expr=-model.z4_4_9 - model.y4_3_10 - model.x3_4_10 + model.x4_4_10 + model.y4_4_10 + model.x4_4_11 + model.y4_4_11 - 1.0 == 0)
model.v5_4_10 = Constraint(expr=-model.z5_4_9 - model.y5_3_10 - model.x4_4_10 + model.x5_4_10 + model.y5_4_10 + model.x5_4_11 + model.y5_4_11 - 1.0 == 0)
model.v6_4_10 = Constraint(expr=-model.z6_4_9 - model.y6_3_10 - model.x5_4_10 + model.x6_4_10 + model.y6_4_10 + model.x6_4_11 + model.y6_4_11 - 1.0 == 0)
model.v7_4_10 = Constraint(expr=-model.z7_4_9 - model.y7_3_10 - model.x6_4_10 + model.x7_4_10 + model.y7_4_10 + model.x7_4_11 + model.y7_4_11 - 1.0 == 0)
model.v8_4_10 = Constraint(expr=-model.z8_4_9 - model.y8_3_10 - model.x7_4_10 + model.x8_4_10 + model.y8_4_10 + model.x8_4_11 + model.y8_4_11 - 1.0 == 0)
model.v9_4_10 = Constraint(expr=-model.z9_4_9 - model.y9_3_10 - model.x8_4_10 + model.x9_4_10 + model.y9_4_10 + model.x9_4_11 + model.y9_4_11 - 1.0 == 0)
model.v10_4_10 = Constraint(expr=-model.z10_4_9 - model.x9_4_10 + model.y11_4_10 + model.z11_4_10 + model.x10_4_11 + model.y10_4_11 - 1.0 == 0)
model.v1_5_10 = Constraint(expr=-model.z1_5_9 - model.y1_4_10 + model.x1_5_10 + model.y1_5_10 + model.y0_5_10 + model.z0_5_10 + model.x1_5_11 + model.y1_5_11 - 1.0 == 0)
model.v2_5_10 = Constraint(expr=-model.z2_5_9 - model.y2_4_10 - model.x1_5_10 + model.x2_5_10 + model.y2_5_10 + model.x2_5_11 + model.y2_5_11 - 1.0 == 0)
model.v3_5_10 = Constraint(expr=-model.z3_5_9 - model.y3_4_10 - model.x2_5_10 + model.x3_5_10 + model.y3_5_10 + model.x3_5_11 + model.y3_5_11 - 1.0 == 0)
model.v4_5_10 = Constraint(expr=-model.z4_5_9 - model.y4_4_10 - model.x3_5_10 + model.x4_5_10 + model.y4_5_10 + model.x4_5_11 + model.y4_5_11 - 1.0 == 0)
model.v5_5_10 = Constraint(expr=-model.z5_5_9 - model.y5_4_10 - model.x4_5_10 + model.x5_5_10 + model.y5_5_10 + model.x5_5_11 + model.y5_5_11 - 1.0 == 0)
model.v6_5_10 = Constraint(expr=-model.z6_5_9 - model.y6_4_10 - model.x5_5_10 + model.x6_5_10 + model.y6_5_10 + model.x6_5_11 + model.y6_5_11 - 1.0 == 0)
model.v7_5_10 = Constraint(expr=-model.z7_5_9 - model.y7_4_10 - model.x6_5_10 + model.x7_5_10 + model.y7_5_10 + model.x7_5_11 + model.y7_5_11 - 1.0 == 0)
model.v8_5_10 = Constraint(expr=-model.z8_5_9 - model.y8_4_10 - model.x7_5_10 + model.x8_5_10 + model.y8_5_10 + model.x8_5_11 + model.y8_5_11 - 1.0 == 0)
model.v9_5_10 = Constraint(expr=-model.z9_5_9 - model.y9_4_10 - model.x8_5_10 + model.x9_5_10 + model.y9_5_10 + model.x9_5_11 + model.y9_5_11 - 1.0 == 0)
model.v10_5_10 = Constraint(expr=-model.z10_5_9 - model.x9_5_10 + model.y11_5_10 + model.z11_5_10 + model.x10_5_11 + model.y10_5_11 - 1.0 == 0)
model.v1_6_10 = Constraint(expr=-model.z1_6_9 - model.y1_5_10 + model.x1_6_10 + model.y1_6_10 + model.y0_6_10 + model.z0_6_10 + model.x1_6_11 + model.y1_6_11 - 1.0 == 0)
model.v2_6_10 = Constraint(expr=-model.z2_6_9 - model.y2_5_10 - model.x1_6_10 + model.x2_6_10 + model.y2_6_10 + model.x2_6_11 + model.y2_6_11 - 1.0 == 0)
model.v3_6_10 = Constraint(expr=-model.z3_6_9 - model.y3_5_10 - model.x2_6_10 + model.x3_6_10 + model.y3_6_10 + model.x3_6_11 + model.y3_6_11 - 1.0 == 0)
model.v4_6_10 = Constraint(expr=-model.z4_6_9 - model.y4_5_10 - model.x3_6_10 + model.x4_6_10 + model.y4_6_10 + model.x4_6_11 + model.y4_6_11 - 1.0 == 0)
model.v5_6_10 = Constraint(expr=-model.z5_6_9 - model.y5_5_10 - model.x4_6_10 + model.x5_6_10 + model.y5_6_10 + model.x5_6_11 + model.y5_6_11 - 1.0 == 0)
model.v6_6_10 = Constraint(expr=-model.z6_6_9 - model.y6_5_10 - model.x5_6_10 + model.x6_6_10 + model.y6_6_10 + model.x6_6_11 + model.y6_6_11 - 1.0 == 0)
model.v7_6_10 = Constraint(expr=-model.z7_6_9 - model.y7_5_10 - model.x6_6_10 + model.x7_6_10 + model.y7_6_10 + model.x7_6_11 + model.y7_6_11 - 1.0 == 0)
model.v8_6_10 = Constraint(expr=-model.z8_6_9 - model.y8_5_10 - model.x7_6_10 + model.x8_6_10 + model.y8_6_10 + model.x8_6_11 + model.y8_6_11 - 1.0 == 0)
model.v9_6_10 = Constraint(expr=-model.z9_6_9 - model.y9_5_10 - model.x8_6_10 + model.x9_6_10 + model.y9_6_10 + model.x9_6_11 + model.y9_6_11 - 1.0 == 0)
model.v10_6_10 = Constraint(expr=-model.z10_6_9 - model.x9_6_10 + model.y11_6_10 + model.z11_6_10 + model.x10_6_11 + model.y10_6_11 - 1.0 == 0)
model.v1_7_10 = Constraint(expr=-model.z1_7_9 - model.y1_6_10 + model.x1_7_10 + model.y1_7_10 + model.y0_7_10 + model.z0_7_10 + model.x1_7_11 + model.y1_7_11 - 1.0 == 0)
model.v2_7_10 = Constraint(expr=-model.z2_7_9 - model.y2_6_10 - model.x1_7_10 + model.x2_7_10 + model.y2_7_10 + model.x2_7_11 + model.y2_7_11 - 1.0 == 0)
model.v3_7_10 = Constraint(expr=-model.z3_7_9 - model.y3_6_10 - model.x2_7_10 + model.x3_7_10 + model.y3_7_10 + model.x3_7_11 + model.y3_7_11 - 1.0 == 0)
model.v4_7_10 = Constraint(expr=-model.z4_7_9 - model.y4_6_10 - model.x3_7_10 + model.x4_7_10 + model.y4_7_10 + model.x4_7_11 + model.y4_7_11 - 1.0 == 0)
model.v5_7_10 = Constraint(expr=-model.z5_7_9 - model.y5_6_10 - model.x4_7_10 + model.x5_7_10 + model.y5_7_10 + model.x5_7_11 + model.y5_7_11 - 1.0 == 0)
model.v6_7_10 = Constraint(expr=-model.z6_7_9 - model.y6_6_10 - model.x5_7_10 + model.x6_7_10 + model.y6_7_10 + model.x6_7_11 + model.y6_7_11 - 1.0 == 0)
model.v7_7_10 = Constraint(expr=-model.z7_7_9 - model.y7_6_10 - model.x6_7_10 + model.x7_7_10 + model.y7_7_10 + model.x7_7_11 + model.y7_7_11 - 1.0 == 0)
model.v8_7_10 = Constraint(expr=-model.z8_7_9 - model.y8_6_10 - model.x7_7_10 + model.x8_7_10 + model.y8_7_10 + model.x8_7_11 + model.y8_7_11 - 1.0 == 0)
model.v9_7_10 = Constraint(expr=-model.z9_7_9 - model.y9_6_10 - model.x8_7_10 + model.x9_7_10 + model.y9_7_10 + model.x9_7_11 + model.y9_7_11 - 1.0 == 0)
model.v10_7_10 = Constraint(expr=-model.z10_7_9 - model.x9_7_10 + model.y11_7_10 + model.z11_7_10 + model.x10_7_11 + model.y10_7_11 - 1.0 == 0)
model.v1_8_10 = Constraint(expr=-model.z1_8_9 - model.y1_7_10 + model.x1_8_10 + model.y1_8_10 + model.y0_8_10 + model.z0_8_10 + model.x1_8_11 + model.y1_8_11 - 1.0 == 0)
model.v2_8_10 = Constraint(expr=-model.z2_8_9 - model.y2_7_10 - model.x1_8_10 + model.x2_8_10 + model.y2_8_10 + model.x2_8_11 + model.y2_8_11 - 1.0 == 0)
model.v3_8_10 = Constraint(expr=-model.z3_8_9 - model.y3_7_10 - model.x2_8_10 + model.x3_8_10 + model.y3_8_10 + model.x3_8_11 + model.y3_8_11 - 1.0 == 0)
model.v4_8_10 = Constraint(expr=-model.z4_8_9 - model.y4_7_10 - model.x3_8_10 + model.x4_8_10 + model.y4_8_10 + model.x4_8_11 + model.y4_8_11 - 1.0 == 0)
model.v5_8_10 = Constraint(expr=-model.z5_8_9 - model.y5_7_10 - model.x4_8_10 + model.x5_8_10 + model.y5_8_10 + model.x5_8_11 + model.y5_8_11 - 1.0 == 0)
model.v6_8_10 = Constraint(expr=-model.z6_8_9 - model.y6_7_10 - model.x5_8_10 + model.x6_8_10 + model.y6_8_10 + model.x6_8_11 + model.y6_8_11 - 1.0 == 0)
model.v7_8_10 = Constraint(expr=-model.z7_8_9 - model.y7_7_10 - model.x6_8_10 + model.x7_8_10 + model.y7_8_10 + model.x7_8_11 + model.y7_8_11 - 1.0 == 0)
model.v8_8_10 = Constraint(expr=-model.z8_8_9 - model.y8_7_10 - model.x7_8_10 + model.x8_8_10 + model.y8_8_10 + model.x8_8_11 + model.y8_8_11 - 1.0 == 0)
model.v9_8_10 = Constraint(expr=-model.z9_8_9 - model.y9_7_10 - model.x8_8_10 + model.x9_8_10 + model.y9_8_10 + model.x9_8_11 + model.y9_8_11 - 1.0 == 0)
model.v10_8_10 = Constraint(expr=-model.z10_8_9 - model.x9_8_10 + model.y11_8_10 + model.z11_8_10 + model.x10_8_11 + model.y10_8_11 - 1.0 == 0)
model.v1_9_10 = Constraint(expr=-model.z1_9_9 - model.y1_8_10 + model.x1_9_10 + model.y1_9_10 + model.y0_9_10 + model.z0_9_10 + model.x1_9_11 + model.y1_9_11 - 1.0 == 0)
model.v2_9_10 = Constraint(expr=-model.z2_9_9 - model.y2_8_10 - model.x1_9_10 + model.x2_9_10 + model.y2_9_10 + model.x2_9_11 + model.y2_9_11 - 1.0 == 0)
model.v3_9_10 = Constraint(expr=-model.z3_9_9 - model.y3_8_10 - model.x2_9_10 + model.x3_9_10 + model.y3_9_10 + model.x3_9_11 + model.y3_9_11 - 1.0 == 0)
model.v4_9_10 = Constraint(expr=-model.z4_9_9 - model.y4_8_10 - model.x3_9_10 + model.x4_9_10 + model.y4_9_10 + model.x4_9_11 + model.y4_9_11 - 1.0 == 0)
model.v5_9_10 = Constraint(expr=-model.z5_9_9 - model.y5_8_10 - model.x4_9_10 + model.x5_9_10 + model.y5_9_10 + model.x5_9_11 + model.y5_9_11 - 1.0 == 0)
model.v6_9_10 = Constraint(expr=-model.z6_9_9 - model.y6_8_10 - model.x5_9_10 + model.x6_9_10 + model.y6_9_10 + model.x6_9_11 + model.y6_9_11 - 1.0 == 0)
model.v7_9_10 = Constraint(expr=-model.z7_9_9 - model.y7_8_10 - model.x6_9_10 + model.x7_9_10 + model.y7_9_10 + model.x7_9_11 + model.y7_9_11 - 1.0 == 0)
model.v8_9_10 = Constraint(expr=-model.z8_9_9 - model.y8_8_10 - model.x7_9_10 + model.x8_9_10 + model.y8_9_10 + model.x8_9_11 + model.y8_9_11 - 1.0 == 0)
model.v9_9_10 = Constraint(expr=-model.z9_9_9 - model.y9_8_10 - model.x8_9_10 + model.x9_9_10 + model.y9_9_10 + model.x9_9_11 + model.y9_9_11 - 1.0 == 0)
model.v10_9_10 = Constraint(expr=-model.z10_9_9 - model.x9_9_10 + model.y11_9_10 + model.z11_9_10 + model.x10_9_11 + model.y10_9_11 - 1.0 == 0)
model.v1_10_10 = Constraint(expr=-model.z1_10_9 - model.y1_9_10 + model.y0_10_10 + model.z0_10_10 + model.x1_11_10 + model.z1_11_10 + model.x1_10_11 + model.y1_10_11 - 1.0 == 0)
model.v2_10_10 = Constraint(expr=-model.z2_10_9 - model.y2_9_10 + model.x2_11_10 + model.z2_11_10 + model.x2_10_11 + model.y2_10_11 - 1.0 == 0)
model.v3_10_10 = Constraint(expr=-model.z3_10_9 - model.y3_9_10 + model.x3_11_10 + model.z3_11_10 + model.x3_10_11 + model.y3_10_11 - 1.0 == 0)
model.v4_10_10 = Constraint(expr=-model.z4_10_9 - model.y4_9_10 + model.x4_11_10 + model.z4_11_10 + model.x4_10_11 + model.y4_10_11 - 1.0 == 0)
model.v5_10_10 = Constraint(expr=-model.z5_10_9 - model.y5_9_10 + model.x5_11_10 + model.z5_11_10 + model.x5_10_11 + model.y5_10_11 - 1.0 == 0)
model.v6_10_10 = Constraint(expr=-model.z6_10_9 - model.y6_9_10 + model.x6_11_10 + model.z6_11_10 + model.x6_10_11 + model.y6_10_11 - 1.0 == 0)
model.v7_10_10 = Constraint(expr=-model.z7_10_9 - model.y7_9_10 + model.x7_11_10 + model.z7_11_10 + model.x7_10_11 + model.y7_10_11 - 1.0 == 0)
model.v8_10_10 = Constraint(expr=-model.z8_10_9 - model.y8_9_10 + model.x8_11_10 + model.z8_11_10 + model.x8_10_11 + model.y8_10_11 - 1.0 == 0)
model.v9_10_10 = Constraint(expr=-model.z9_10_9 - model.y9_9_10 + model.x9_11_10 + model.z9_11_10 + model.x9_10_11 + model.y9_10_11 - 1.0 == 0)
model.v10_10_10 = Constraint(expr=model.y11_10_10 + model.z11_10_10 + model.x10_11_10 + model.z10_11_10 + model.x10_10_11 + model.y10_10_11 - 1.0 == 0)
