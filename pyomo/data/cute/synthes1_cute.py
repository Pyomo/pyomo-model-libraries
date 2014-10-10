#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, Brandon C. Barrera and Saumyajyoti Chaudhuri
#Taken from:
#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   Source: Test problem 1 (Synthesis of processing system) in
#   M. Duran & I.E. Grossmann,
#   "An outer approximation algorithm for a class of mixed integer nonlinear
#    programs", Mathematical Programming 36, pp. 307-339, 1986.
#   SIF input: S. Leyffer, October 1997
#   classification OOR2-AN-6-6

from pyomo.core import *
model = AbstractModel()

model.x1 = Var(bounds=(0.0,2.0))
model.x2 = Var(bounds=(0.0,2.0))
model.x3 = Var(bounds=(0.0,1.0))
model.y1 = Var(bounds=(0.0,1.0))
model.y2 = Var(bounds=(0.0,1.0))
model.y3 = Var(bounds=(0.0,1.0))

def obj(model):
    return - 18.0*log ( model.x2 + 1.0 )  - 19.2*log ( model.x1 - model.x2 + 1.0 ) \
     + 5.0*model.y1 + 6.0*model.y2 + 8.0*model.y3 + 10.0*model.x1 - 7.0*model.x3 + 10.0
model.obj = Objective(rule=obj,sense =minimize)

def n1(model):
    return (0,0.8*log (model.x2 + 1.0 )  + 0.96*log (model.x1 - model.x2 + 1.0 )  - 0.8*model.x3,None)
model.n1 = Constraint(rule=n1)
def n2(model):
    return (0,log (model.x2 + 1.0 )  + 1.2*log (model.x1 -model.x2 + 1.0 )  -model.x3 - 2.0*model.y3 + 2.0,None)
model.n2 = Constraint(rule=n2)
def l3(model):
    return 0>= model.x2 - model.x1
model.l3 = Constraint(rule=l3)
def l4(model):
    return 0 >= model.x2 - 2.0*model.y1
model.l4 = Constraint(rule=l4)
def l5(model):
    return 0 >= -model.x2 + model.x1 - 2.0*model.y2
model.l5 = Constraint(rule=l5)
def l6(model):
    return 0 >= model.y1 + model.y2 - 1.0
model.l6 = Constraint(rule=l6)
