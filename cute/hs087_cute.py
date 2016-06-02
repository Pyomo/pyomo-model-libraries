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
# Formulated in pyomo by Logan Barnes and Gabe Hackebeil.
#
# Taken from:
# hs87.mod  LOR2-RN-11-24
# Original AMPL coding by Elena Bobrovnikova (summer 1996 at Bell Labs).

# The problem given here is stated in the notation of Hock & Schittkowski,
# but is corrected to conform to the problem as stated in
#   D. M. Himmelblau, Applied Nonlinear Programming,
#   McGraw-Hill, 1972, pp. 413-414
# except that jump-discontinuities in the objective function are
# omitted by stating it as the sum of two piecewise-linear terms.
# Errors in the problem statement by Hock & Schittkowski are noted in
# comments below.  (dmg, 19970820)

# Nonlinear electrical network

# Ref.: A.R.Colville. A Comparative Study on Nonlinear Programming
# Codes. IBM Scientific Center Report 320-2949, no.6, 1968.

# Ref.: W. Hock and K. Schittkowski, Test Examples for Nonlinear Programming
# Codes.  Lecture Notes in Economics and Mathematical Systems, v. 187,
# Springer-Verlag, New York, 1981, p. 106.

# Number of variables:  11 (6 before presolve and linearization of pl terms)
# Number of constraints:  24 (16 before presolve and linearization of pl terms)
# Objective convex piece-wise linear
# Nonlinear constraints

from pyomo.core import *
model = ConcreteModel()

model.a = 131.078
model.b = 1.48477
model.c = 0.90798
model.d = cos(1.47588)
model.e = sin(1.47588)
model.lim1 = 300
model.lim2 = 100
model.lim3 = 200
model.rate1 = 30
model.rate2 = 31
model.rate3 = 28
model.rate4 = 29
model.rate5 = 30

model.N = RangeSet(1,6)

model.z1 = Var()
model.z2 = Var()
model.x1 = Var()
model.x2 = Var()
model.x3 = Var()
model.x4 = Var()
model.x5 = Var()
model.x6 = Var()
model.x1.setlb(0.0)
model.x1.setub(400.0)
model.x2.setlb(0.0)
model.x2.setub(1000.0)
model.x3.setlb(340.0)
model.x3.setub(420.0)
model.x4.setlb(340.0)
model.x4.setub(420.0)
model.x5.setlb(-1000.0)
model.x5.setub(1000.0)
model.x6.setlb(0.0)
model.x6.setub(0.5236)

model.x1 = 390.0
model.x2 = 1000.0
model.x3 = 419.5
model.x4 = 340.5
model.x5 = 198.175
model.x6 = 0.5

model.obj = Objective(expr=model.z1 + model.z2)

def f1(model,x):
    if x == 0:
        return 0.0
    elif x == 300:
        return 300*30.0
    elif x == 400:
        return 30.0*300.0+31.0*100.0

def f2(model,x):
    if x == 0:
        return 0.0
    elif x == 100:
        return 28.0*100.0
    elif x == 200:
        return 28.0*100.0+29*100.0
    elif x == 1000:
        return 28.0*100.0+29*100.0+30.0*800

model.piecew1 = Piecewise(model.z1,model.x1,pw_constr_type='LB',pw_pts=[0.0,model.lim1,400.0],f_rule=f1)
model.piecew2 = Piecewise(model.z2,model.x2,pw_constr_type='LB',pw_pts=[0.0,model.lim2,model.lim3,1000.0],f_rule=f2)

model.e1 = Constraint(expr = model.x1 == 300 - model.x3*model.x4*cos(model.b - model.x6)/model.a\
     + model.c*model.x3**2*model.d/model.a)
model.e2 = Constraint(expr = model.x2 == -model.x3*model.x4*cos(model.b + model.x6)/model.a\
     + model.c*model.x4**2*model.d/model.a)
model.e3 = Constraint(expr = model.x5 == -model.x3*model.x4*sin(model.b + model.x6)/model.a\
     + model.c*model.x4**2*model.e/model.a)
model.e4 = Constraint(expr = 200 - model.x3*model.x4*sin(model.b - model.x6)/model.a\
     + model.c*model.x3**2*model.e/model.a == 0)
