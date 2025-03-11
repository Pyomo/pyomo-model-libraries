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

# dempe.py QQR2-MN-4-3
# Original Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer

# An MPEC from S. Dempe, "A necessary and sufficient optimality
# condition for bilevel programming problems", Optimization 25,
# pp. 341-354, 1992. From book Math. Progr. with Equil. Constr,
# by Luo, Pang & Ralph, CUP, 1997, p. 354.

# Number of variables:   2 + 1 multipliers
# Number of constraints: 2
# Nonlinear complementarity constraints

import pyomo.environ
from pyomo.core import *
from pyomo.mpec import *


model = ConcreteModel()

model.x = Var(initialize=1)
model.z = Var(initialize=1)
model.w = Var(initialize=1, within=NonNegativeReals)

model.f = Objective(expr=(model.x - 3.5)**2 + (model.z + 4)**2)

model.con1 = Constraint(expr=model.z - 3 + 2*model.z*model.w == 0)
model.con2 = Complementarity(expr=complements(0 >= model.z**2 - model.x, model.w >= 0))

