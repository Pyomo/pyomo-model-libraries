# ralph2.py    QUR-AN-LCP-2-0-1 
# Original AMPL coding by Sven Leyffer
# Original Pyomo coding by Sven Leyffer

# An LPEC from D. Ralph, Judge Inst., University of Cambridge.

from pyomo.environ import *
from pyomo.mpec import *


model = ConcreteModel()
model.x = Var(within=NonNegativeReals, initialize=1)
model.y = Var(initialize=1)

model.f = Objective(expr=model.x**2 + model.y**2 - 4*model.x*model.y)

model.compl = Complementarity(expr=complements(0 <= model.x, model.y >= 0))

