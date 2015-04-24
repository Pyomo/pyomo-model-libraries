# kth2.py
# 
# simple MPEC # 2

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()

model.z1 = Var(within=NonNegativeReals, initialize=0)
model.z2 = Var(within=NonNegativeReals, initialize=1)

model.objf = Objective(expr=model.z1 + (model.z2 - 1)**2)

model.compl = Complementarity(expr=complements(0 <= model.z1, model.z2 >= 0))


