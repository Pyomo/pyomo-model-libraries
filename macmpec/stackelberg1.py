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

# stackelberg1.py  QQR2-MN-4-2
# Original Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer, University of Dundee

# An MPEC from F. Facchinei, H. Jiang and L. Qi, A smoothing method for
# mathematical programs with equilibrium constraints, Universita di Roma
# Technical report, 03.96. Problem number 6

# Number of variables:   3
# Number of constraints: 2

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()
model.x = Var(bounds=(0,200))
model.y = Var(bounds=(0,None))
model.l = Var(bounds=(0,None))      # Multipliers

model.f = Objective(expr=0.5*model.x**2 + 0.5*model.x*model.y - 95*model.x)

model.F = Constraint(expr=2*model.y + 0.5*model.x - 100 - model.l == 0)

model.g = Complementarity(expr=complements(0 <= model.y, model.l >= 0))

