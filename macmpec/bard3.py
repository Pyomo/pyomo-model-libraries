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

# bard3.py QQR2-MN-8-6
# Original Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer

# An MPEC from J.F. Bard, Convex two-level optimization,
# Mathematical Programming 40(1), 15-27, 1988.

# Number of variables:   4 + 2 multipliers
# Number of constraints: 5

import pyomo.environ
from pyomo.core import *
from pyomo.mpec import *

model = ConcreteModel()

N = [1,2]

model.x = Var(N, within=NonNegativeReals)
model.y = Var(N, within=NonNegativeReals)

# ... slack variables & multipliers
model.l = Var(N, within=NonNegativeReals)

model.f = Objective(expr=- model.x[1]**2 - 3*model.x[2] - 4*model.y[1] + model.y[2]**2)

model.nlncs = Constraint(expr=model.x[1]**2 + 2*model.x[2] <= 4)

model.KKT1 = Constraint(expr= 2*model.y[1] + model.l[1]*2 - model.l[2]*3 == 0)
model.KKT2 = Constraint(expr=-5            - model.l[1]   + model.l[2]*4 == 0)

model.lin_1 = Complementarity(expr=complements(0 <= model.x[1]**2 - 2*model.x[1] + model.x[2]**2 - 2*model.y[1] + model.y[2] + 3, model.l[1] >= 0))

model.lin_2 = Complementarity(expr=complements(0 <= model.x[2] + 3*model.y[1] - 4*model.y[2] - 4, model.l[2] >= 0))

