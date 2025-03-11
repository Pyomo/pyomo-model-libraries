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

# scholtes3.py	QOR2-MN-2-0
# Original Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer

# An QPEC from S. Scholtes

# Number of variables:   2 slack
# Number of constraints: 0

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()

# start point close to (0,0)
model.x = Var([1,2], within=NonNegativeReals, initialize=0.0001)

model.objf = Objective(expr=0.5*( (model.x[1] - 1)**2 + (model.x[2] - 1)**2 ))

model.LCP = Complementarity(expr=complements(0 <= model.x[1], model.x[2] >= 0))
