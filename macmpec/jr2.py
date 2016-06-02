# jr2.py   QLR2-AN-LCP-2-1-1
#
# QPEC from ideas by Jiang & Ralph
#

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()

model.z1 = Var()
model.z2 = Var(within=NonNegativeReals)

model.objf = Objective(expr=(model.z2 - 1)**2 + model.z1**2)

model.compl = Complementarity(expr=complements(0 <= model.z2, model.z2 - model.z1 >= 0))

