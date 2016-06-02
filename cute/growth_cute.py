#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil, Juan Lopez
# Taken from:

#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   GROWTH problem in 3 variables
#   Fit the observed growth g(n) from Gaussian Elimination
#   with complete pivoting to a function of the form
#
#        U1 * n ** ( U2 + LOG(n) * U3 )
#   SIF input: Nick Gould, Nov, 1991.
#   classification NOR2-AN-3-12
#T  'DEFAULT' L2
#   Solution

from pyomo.core import *
model = ConcreteModel()

n = 3

model.u1 = Var(initialize=100.0)
model.u2 = Var()
model.u3 = Var()

def obj_rule(model):
    return (model.u1 * (8.0**(model.u2+(log(8.0))*model.u3)) - 8.0)**2 +\
    (model.u1 * (9.0**(model.u2+(log(9.0))*model.u3)) - \
    8.4305)**2 + (model.u1 * (10.0**(model.u2+(log(10.0))*model.u3)) - 9.5294)**2 + (model.u1 * \
    (11.0**(model.u2+(log(11.0))*model.u3)) - 10.4627)**2 + \
    (model.u1 * (12.0**(model.u2+(log(12.0))*model.u3)) -\
    12.0)**2 + (model.u1 * (13.0**(model.u2+(log(13.0))*model.u3)) - 13.0205)**2 + (model.u1 * \
    (14.0**(model.u2+(log(14.0))*model.u3)) - 14.5949)**2 + \
    (model.u1 * (15.0**(model.u2+(log(15.0))*model.u3)) -\
    16.1078)**2 + (model.u1 * (16.0**(model.u2+(log(16.0))*model.u3)) - 18.0596)**2 + (model.u1 * \
    (18.0**(model.u2+(log(18.0))*model.u3)) - 20.4569)**2 + \
    (model.u1 * (20.0**(model.u2+(log(20.0))*model.u3)) -\
    24.25)**2 + (model.u1 * (25.0**(model.u2+(log(25.0))*model.u3)) - 32.9863)**2
model.obj = Objective(rule=obj_rule)
