#  This software is distributed under the BSD License.
#  under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
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
#        u1 * n ** ( u2 + LOG(n) * u3 )
#   SIF input: Nick Gould, Nov, 1991, modified by Ph. Toint, March 1994.
#   classification SUR2-AN-3-0
#   Solution

from pyomo.core import *
model = ConcreteModel()

n = 3

model.u1 = Var(initialize=100.0)
model.u2 = Var()
model.u3 = Var()

def obj_rule(model):
    return (model.u1 * (8.0**(model.u2+(log(8.0))*model.u3)) - 8.0)*(model.u1 * (8.0**(model.u2+(log(8.0))*model.u3)) - 8.0) + \
    (model.u1 * (9.0**(model.u2+(log(9.0))*model.u3)) - 8.4305)*(model.u1 * (9.0**(model.u2+(log(9.0))*model.u3)) - \
    8.4305) + (model.u1 * (10.0**(model.u2+(log(10.0))*model.u3)) - 9.5294)*(model.u1 * \
    (10.0**(model.u2+(log(10.0))*model.u3)) - 9.5294) + (model.u1 * (11.0**(model.u2+(log(11.0))*model.u3)) -\
    10.4627)*(model.u1 * (11.0**(model.u2+(log(11.0))*model.u3)) - 10.4627) + (model.u1 * \
    (12.0**(model.u2+(log(12.0))*model.u3)) - 12.0)*(model.u1 * (12.0**(model.u2+(log(12.0))*model.u3)) - 12.0) +\
    (model.u1 * (13.0**(model.u2+(log(13.0))*model.u3)) - 13.0205)*(model.u1 * (13.0**(model.u2+(log(13.0))*model.u3)) -\
    13.0205) + (model.u1 * (14.0**(model.u2+(log(14.0))*model.u3)) - 14.5949)*(model.u1 * \
    (14.0**(model.u2+(log(14.0))*model.u3)) - 14.5949) + (model.u1 * (15.0**(model.u2+(log(15.0))*model.u3)) -\
    16.1078)*(model.u1 * (15.0**(model.u2+(log(15.0))*model.u3)) - 16.1078) + (model.u1 * \
    (16.0**(model.u2+(log(16.0))*model.u3)) - 18.0596)*(model.u1 * (16.0**(model.u2+(log(16.0))*model.u3)) -\
    18.0596) + (model.u1 * (18.0**(model.u2+(log(18.0))*model.u3)) - 20.4569)*(model.u1 * \
    (18.0**(model.u2+(log(18.0))*model.u3)) - 20.4569) + (model.u1 * (20.0**(model.u2+(log(20.0))*model.u3)) -\
    24.25)*(model.u1 * (20.0**(model.u2+(log(20.0))*model.u3)) - 24.25) + (model.u1 * \
    (25.0**(model.u2+(log(25.0))*model.u3)) - 32.9863)*(model.u1 * (25.0**(model.u2+(log(25.0))*model.u3)) -\
    32.9863)
model.obj = Objective(rule=obj_rule)
