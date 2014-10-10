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
#  Formulated in pyomo by Logan Barnes and Gabe Hackebeil.
#
#  Taken from:
#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   Source: an expanded form of problem 99 in
#   W. Hock and K. Schittkowski,
#   "Test examples for nonlinear programming codes",
#   Lectures Notes in Economics and Mathematical Systems 187, Springer
#   Verlag, Heidelberg, 1981.
#   SIF input: Ph. Toint, April 1991.
#   classification OOR2-AN-31-21
#   Problem data
#   Constants
#   Increments
#   Solution

from pyomo.core import *
model = ConcreteModel()
t1 = 0.0
t2 = 25.0
t3 = 50.0
t4 = 100.0
t5 = 150.0
t6 = 200.0
t7 = 290.0
t8 = 380.0
a1 = 0.0
a2 = 50.0
a3 = 50.0
a4 = 75.0
a5 = 75.0
a6 = 75.0
a7 = 100.0
a8 = 100.0
b = 32.0
im1 = -1 + (8)
dtisq = ((380.0) - (290.0)) * ((380.0) - (290.0))
dt2 = (25.0) - (0.0)
dtsqd22 = 0.5 * (((25.0) - (0.0)) * ((25.0) - (0.0)))
dt3 = (50.0) - (25.0)
dtsqd23 = 0.5 * (((50.0) - (25.0)) * ((50.0) - (25.0)))
dt4 = (100.0) - (50.0)
dtsqd24 = 0.5 * (((100.0) - (50.0)) * ((100.0) - (50.0)))
dt5 = (150.0) - (100.0)
dtsqd25 = 0.5 * (((150.0) - (100.0)) * ((150.0) - (100.0)))
dt6 = (200.0) - (150.0)
dtsqd26 = 0.5 * (((200.0) - (150.0)) * ((200.0) - (150.0)))
dt7 = (290.0) - (200.0)
dtsqd27 = 0.5 * (((290.0) - (200.0)) * ((290.0) - (200.0)))
dt8 = (380.0) - (290.0)
dtsqd28 = 0.5 * (((380.0) - (290.0)) * ((380.0) - (290.0)))
rhs = ((290.0) - (200.0)) * (32.0)
w = (100.0) * (0.5 * (((380.0) - (290.0)) * ((380.0) - (290.0))))

model.x1 = Var(bounds=(0.0,1.58),initialize=0.5)
model.r1 = Var(bounds=(0.0,0.0))
model.q1 = Var(bounds=(0.0,0.0))
model.s1 = Var(bounds=(0.0,0.0))
model.x2 = Var(bounds=(0.0,1.58),initialize=0.5)
model.r2 = Var()
model.q2 = Var()
model.s2 = Var()
model.x3 = Var(bounds=(0.0,1.58),initialize=0.5)
model.r3 = Var()
model.q3 = Var()
model.s3 = Var()
model.x4 = Var(bounds=(0.0,1.58),initialize=0.5)
model.r4 = Var()
model.q4 = Var()
model.s4 = Var()
model.x5 = Var(bounds=(0.0,1.58),initialize=0.5)
model.r5 = Var()
model.q5 = Var()
model.s5 = Var()
model.x6 = Var(bounds=(0.0,1.58),initialize=0.5)
model.r6 = Var()
model.q6 = Var()
model.s6 = Var()
model.x7 = Var(bounds=(0.0,1.58),initialize=0.5)
model.r7 = Var()
model.q7 = Var()
model.s7 = Var()
model.r8 = Var()
model.q8 = Var()
model.s8 = Var()

model.obj = Objective(expr=-model.r8*model.r8)

model.rdef2 = Constraint(expr= 1250.0*(cos(model.x1)) - model.r2 + model.r1 == 0)
model.qdef2 = Constraint(expr= 15625.0*(sin(model.x1)) - model.q2 + model.q1 + 25.0*model.s1 - 10000.0 == 0)
model.sdef2 = Constraint(expr= 1250.0*(sin(model.x1)) - model.s2 + model.s1 - 800.0 == 0)
model.rdef3 = Constraint(expr= 1250.0*(cos(model.x2)) - model.r3 + model.r2 == 0)
model.qdef3 = Constraint(expr= 15625.0*(sin(model.x2)) - model.q3 + model.q2 + 25.0*model.s2 - 10000.0 == 0)
model.sdef3 = Constraint(expr= 1250.0*(sin(model.x2)) - model.s3 + model.s2 - 800.0 == 0)
model.rdef4 = Constraint(expr= 3750.0*(cos(model.x3)) - model.r4 + model.r3 == 0)
model.qdef4 = Constraint(expr= 93750.0*(sin(model.x3)) - model.q4 + model.q3 + 50.0*model.s3 - 40000.0 == 0)
model.sdef4 = Constraint(expr= 3750.0*(sin(model.x3)) - model.s4 + model.s3 - 1600.0 == 0)
model.rdef5 = Constraint(expr= 3750.0*(cos(model.x4)) - model.r5 + model.r4 == 0)
model.qdef5 = Constraint(expr= 93750.0*(sin(model.x4)) - model.q5 + model.q4 + 50.0*model.s4 - 40000.0 == 0)
model.sdef5 = Constraint(expr= 3750.0*(sin(model.x4)) - model.s5 + model.s4 - 1600.0 == 0)
model.rdef6 = Constraint(expr= 3750.0*(cos(model.x5)) - model.r6 + model.r5 == 0)
model.qdef6 = Constraint(expr= 93750.0*(sin(model.x5)) - model.q6 + model.q5 + 50.0*model.s5 - 40000.0 == 0)
model.sdef6 = Constraint(expr= 3750.0*(sin(model.x5)) - model.s6 + model.s5 - 1600.0 == 0)
model.rdef7 = Constraint(expr= 9000.0*(cos(model.x6)) - model.r7 + model.r6 == 0)
model.qdef7 = Constraint(expr= 405000.0*(sin(model.x6)) - model.q7 + model.q6 + 90.0*model.s6 - 129600.0 == 0)
model.sdef7 = Constraint(expr= 9000.0*(sin(model.x6)) - model.s7 + model.s6 - 2880.0 == 0)
model.rdef8 = Constraint(expr= 9000.0*(cos(model.x7)) - model.r8 + model.r7 == 0)
model.qdef8 = Constraint(expr= 405000.0*(sin(model.x7)) - model.q8 + model.q7 + 90.0*model.s7 - 100000.0 == 0)
model.sdef8 = Constraint(expr= 9000.0*(sin(model.x7)) - model.s8 + model.s7 - 1000.0 == 0)
