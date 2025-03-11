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

# ralph1.py	LUR-AN-LCP-2-0-1 
# Original Pyomo coding by William Hart
# Adapted from original AMPL coding by Sven Leyffer

# An LPEC from D. Ralph, Judge Inst., University of Cambridge.
# This problem violates strong stationarity, but is B-stationary.

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()

model.x = Var(within=NonNegativeReals)
model.y = Var(within=NonNegativeReals)

model.f1 = Objective(expr=2*model.x - model.y)
#minimize f2:   x - y;

model.compl = Complementarity(expr=complements(0 <= model.y, model.y-model.x >= 0))

