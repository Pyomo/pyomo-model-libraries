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

# josephy.py
#
#   Complementarity problem from Kojima, via Josephy.
#

from pyomo.environ import *
from pyomo.mpec import *


model = AbstractModel()

model.Rn = RangeSet(1,4)
model.initpoint = RangeSet(1,8)

model.A = Param(model.Rn, model.Rn, model.Rn)
model.B = Param(model.Rn, model.Rn)
model.c = Param(model.Rn)
model.xinit = Param(model.Rn, model.initpoint, within=NonNegativeReals)

model.x = Var(model.Rn, within=NonNegativeReals)

def f_rule(model, i):
    return complements(
            0 <= model.x[i],
            model.c[i] + 
                sum(model.B[i,j]*model.x[j] + 
                    sum(model.A[i,j,k]*model.x[j]*model.x[k] for k in model.Rn) for j in model.Rn) >= 0
            )
model.f = Complementarity(model.R, rule=f_rule)

