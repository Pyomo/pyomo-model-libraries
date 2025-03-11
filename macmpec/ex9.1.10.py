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

# ex9.1.10.py LLR-AY-NLP-14-12-5
# Pyomo coding by William Hart
# Adapted from AMPL coding by Sven Leyffer, Apr. 2001,

# From Nonconvex Optimization and its Applications, Volume 33
# Kluwer Academic Publishers, Dordrecht, Hardbound, ISBN 0-7923-5801-5
# (see also titan.princeton.edu/TestProblems/)
#
# Test problem 9.2.10 in the Test Collection Book
# Test problem 9.1.10 in the web page
# Test problem from Tuy et al  93

import pyomo.environ
from pyomo.core import *
from pyomo.mpec import *


model = ConcreteModel()

I = range(1,6)

model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)
model.y1 = Var(within=NonNegativeReals)
model.y2 = Var(within=NonNegativeReals)
model.y3 = Var(within=NonNegativeReals)
model.s  = Var(I, within=NonNegativeReals)
model.l  = Var(I, within=NonNegativeReals)

# ... Outer Objective function
model.ob = Objective(expr=- 2*model.x1 + model.x2 + 0.5*model.y1)

# ... Outer constraint
model.c0 = Constraint(expr=model.x1 + model.x2 <= 2)

# ... Inner Problem Constraints
model.c1 = Constraint(expr= -2*model.x1 +   model.y1 - model.y2 + model.s[1]  == -2.5)
model.c2 = Constraint(expr=    model.x1 - 3*model.x2 + model.y2 + model.s[2]  == 2)
model.c3 = Constraint(expr=  - model.y1 + model.s[3] == 0)
model.c4 = Constraint(expr=  - model.y2 + model.s[4] == 0)

# ... KKT conditions for the inner problem optimum
model.kt1 = Constraint(expr= model.l[1] - model.l[3] == 4)
model.kt2 = Constraint(expr= model.l[1] + model.l[2] - model.l[4] == -1)

def compl_(model, i):
    return complements(0 <= model.l[i], model.s[i] >= 0)
model.compl = Complementarity(I, rule=compl_)
