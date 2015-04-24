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


