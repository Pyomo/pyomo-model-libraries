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

# design-cent-2.py    QOR-MY-NLP-13-13-3
#
# Design centering problem cast as an MPEC, from an idea by
# O. Stein and G. Still, "Solving semi-infinite optimization 
# problems with Interior Point techniques", Lehrstuhl C fuer 
# Mathematik, Rheinisch Westfaelische Technische Hochschule,
# Preprint No. 96, November 2001.
#
# Maximize the volume of the parameterized body B(x) contained 
# in a second body G, described by a set of convex inequalities.
#
# Original Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer, University of Dundee, Jan. 2002

import pyomo.environ
from pyomo.core import *
from pyomo.mpec import *


model = ConcreteModel()

# ... sets
model.I = RangeSet(1,4)     # ... design variables
model.J = RangeSet(1,2)     # ... lower level variables
model.K = RangeSet(1,3)     # ... lower level constraints

# ... parameters
model.pi = Param(initialize=3.141592654)

# ... initial points from solving design-init-1.mod
model.x0 = Param(model.I, default=0.5)
model.y0 = Param(model.J, model.K, default=0)
model.l0 = Param(model.K, default=1)

# ... variables
model.x = Var(model.I, initialize=model.x0)                             # ... description of B(x)
model.y = Var(model.J, model.K, initialize=model.y0)                    # ... contact points of B(x), G
model.l = Var(model.K, within=NonNegativeReals, initialize=model.l0)    # ... multipliers gamma

# ... maximize the volume of the inscribed body
model.volume = Objective(expr=model.pi*model.x[3]*model.x[4], sense=maximize)

# ... lower level solutions lie in body G
model.g1 = Constraint(expr=- model.y[1,1] - model.y[2,1]**2     <= 0)
model.g2 = Constraint(expr=model.y[1,2]/4 + model.y[2,2] - 3/4 <= 0)
model.g3 = Constraint(expr=- model.y[2,3] - 1   <= 0)

# ... constraints deduced from KKT conditions
model.KKT_11n = Constraint(expr=model.y[1,1] - model.x[1] <= 0)
model.KKT_12n = Constraint(expr=model.y[1,2] - model.x[1] >= 0)
model.KKT_22n = Constraint(expr=model.y[2,2] - model.x[2] >= 0)
model.KKT_23n = Constraint(expr=model.y[2,3] - model.x[2] <= 0)

# ... first order conditions for 3 lower level problem
model.KKT_11 = Constraint(expr=1                 + 2*(model.y[1,1] - model.x[1])/(model.x[3]**2) * model.l[1] == 0)
model.KKT_21 = Constraint(expr=2*model.y[2,1]    + 2*(model.y[2,1] - model.x[2])/(model.x[4]**2) * model.l[1] == 0)

model.KKT_12 = Constraint(expr=-1/4              + 2*(model.y[1,2] - model.x[1])/(model.x[3]**2) * model.l[2] == 0)
model.KKT_22 = Constraint(expr=-1                + 2*(model.y[2,2] - model.x[2])/(model.x[4]**2) * model.l[2] == 0)

model.KKT_13 = Constraint(expr=0                 + 2*(model.y[1,3] - model.x[1])/(model.x[3]**2) * model.l[3] == 0)
model.KKT_23 = Constraint(expr=1                 + 2*(model.y[2,3] - model.x[2])/(model.x[4]**2) * model.l[3] == 0)

# ... complementarity & dual feasibility for lower level problem
def compl_(model, k):
    return complements(0 <= model.l[k],
                       ((model.y[1,k] - model.x[1])**2)/(model.x[3]**2) + ((model.y[2,k] - model.x[2])**2)/(model.x[4]**2) <= 1)
model.compl = Complementarity(model.K, rule=compl_)

