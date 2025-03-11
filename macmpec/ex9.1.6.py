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

# ex9.1.6.py LLR-AY-NLP-14-13-6 
# Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer, Apr. 2001,

# From Nonconvex Optimization and its Applications, Volume 33
# Kluwer Academic Publishers, Dordrecht, Hardbound, ISBN 0-7923-5801-5
# (see also titan.princeton.edu/TestProblems/)
#
# Test problem 9.2.7 in the Test Collection Book
# Test problem 9.1.6 in the web page
# Test Problem from Anandalingam and White 1990
# They took from Bialas and Karwan 1982

import pyomo.environ
from pyomo.core import *
from pyomo.mpec import *


model = ConcreteModel()

I = range(1,7)

model.x = Var(within=NonNegativeReals)
model.y = Var(within=NonNegativeReals)
model.s = Var(I, within=NonNegativeReals)
model.l = Var(I, within=NonNegativeReals)

# ... Outer Objective function
model.ob = Objective(expr=-model.x -3*model.y)

# ... Inner Problem Constraints
model.c1 = Constraint(expr=- model.x - 2*model.y + model.s[1] == -10)
model.c2 = Constraint(expr=  model.x - 2*model.y + model.s[2] == 6)
model.c3 = Constraint(expr=2*model.x -   model.y + model.s[3] == 21)
model.c4 = Constraint(expr=  model.x + 2*model.y + model.s[4] == 38)
model.c5 = Constraint(expr= -model.x + 2*model.y + model.s[5] == 18)
model.c6 = Constraint(expr=            - model.y + model.s[6] == 0)

# ... KKT conditions for the inner problem optimum
model.kt1 = Constraint(expr=3 - 2*model.l[1] - 2*model.l[2] - model.l[3] + 2*model.l[4] + 2*model.l[5] - model.l[6] == 0)

def compl_(model, i):
    return complements(0 <= model.l[i], model.s[i] >= 0)
model.compl = Complementarity(I, rule=compl_)
