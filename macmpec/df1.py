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

# df1.py   QQR2-MN-4-2
# Original Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer, University of Dundee

# An MPEC from S.P. Dirkse and M.C. Ferris, Modeling & Solution 
# Environment for MPEC: GAMS & MATLAB, University of Wisconsin
# CS report, 1997.

# Number of variables:   3
# Number of constraints: 2

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()

model.x = Var(bounds=(-1,2))
model.y = Var(within=NonNegativeReals)

model.theta = Objective(expr=(model.x - 1 - model.y)**2)

model.h = Constraint(expr=model.x**2 <= 2)
model.g = Constraint(expr=(model.x - 1)**2 + (model.y - 1)**2 <= 3)
model.MCP = Complementarity(expr=complements(0 <= model.y - model.x**2 + 1, model.y >= 0))

