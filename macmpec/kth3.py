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

# kth3.py
# 
# simple MPEC # 3

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()

model.z1 = Var(within=NonNegativeReals, initialize=0)
model.z2 = Var(within=NonNegativeReals, initialize=1)

model.objf = Objective(expr=0.5*(model.z1 - 1)**2 + (model.z2 - 1)**2)

model.compl = Complementarity(expr=complements(0 <= model.z1, model.z2 >= 0))


