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

#
#  obstacle.py
#
# Calculate the position of a membrane pushed up through a (rectangular)
# hole in a rigid plate; in addition, there are rigid obstacle(s) inside
# the hole (perhaps not at the same level as the plate).  These
# obstacles can constrain the membrane from above or from below.  The
# correct position of the membrane (the position of minimum energy) is
# determined by the minimization of a quadratic function of the membrane
# position, subject to the constraints imposed by the hole and the
# obstacle.  The MCP below arises from the optimality conditions for
# this QP. Reference:
#
# 	Ciarlet, Philippe G.  The finite element method for 
# 	elliptic problems.  North-Holland, 1978.
#

from pyomo.environ import *
from pyomo.mpec import *

model = ConcreteModel()

def valid_gridpt(model, x):
    return x >= 1
# Number of interior grid pts in Y direction
model.M = Param(default=50, within=Integers, validate=valid_gridpt)
# Number of interior grid pts in X direction
model.N = Param(default=50, within=Integers, validate=valid_gridpt)

model.Y = RangeSet(0, model.M+1)
model.X = RangeSet(0, model.N+1)

model.xlo = Param(initialize=0)
def xhi_(model, val):
    return val > model.xlo
model.xhi = Param(initialize=1, validate=xhi_)

model.ylo = Param(initialize=0)
def yhi_(model, val):
    return val > model.ylo
model.yhi = Param(initialize=1, validate=yhi_)

def dy_(model):
    return (model.yhi - model.ylo) / (model.M + 1)
model.dy = Param(initialize=dy_)

model.dx = Param(initialize=(model.xhi - model.xlo) / (model.N + 1))

model.c = Param(initialize=1)

def ub_init(model, i, j):
    if 1 <= i <= model.M and 1 <= j <= model.N:
	    return (sin(9.2*(model.xlo+model.dx*i))*sin(9.3*(model.ylo+j*model.dy)))**2 + 0.2
model.ub = Param(model.Y, model.X, initialize=ub_init, within=Any)

def lb_init(model, i, j):
    if 1 <= i <= model.M and 1 <= j <= model.N:
        return (sin(9.2*(model.xlo+model.dx*i))*sin(9.3*(model.ylo+j*model.dy)))**3
    return 0
model.lb = Param(model.Y, model.X, initialize=lb_init, within=Any)

# height of membrane
def v_bounds(model, i, j):
    return (model.lb[i,j], model.ub[i,j])
def v_init(model, i, j):
    return max(0, model.lb[i,j])
model.v = Var(model.Y, model.X, bounds=v_bounds, initialize=v_init)

model.Y_dv = RangeSet(1, model.M)
model.X_dv = RangeSet(1, model.N)

def dv_rule(model, i, j):
    return complements(
            model.lb[i,j] <= model.v[i,j] <= model.ub[i,j],
		    (model.dy/model.dx) * (2*model.v[i,j] - model.v[i+1,j] - model.v[i-1,j]) +
		        (model.dx/model.dy) * (2*model.v[i,j] - model.v[i,j+1] - model.v[i,j-1]) -
		        model.c * model.dx * model.dy
            )
model.dv = Complementarity(model.Y_dv, model.X_dv, rule=dv_rule)

