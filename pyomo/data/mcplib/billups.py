#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________
#
# billups.py
#
# Problem adapted from billups.gms
# http://ftp.cs.wisc.edu/pub/mcplib/gams/
#
# Initial values of 3.0 helped PATH and mpec_nlp
#

from pyomo.environ import *
from pyomo.mpec import *


def pyomo_create_model(**kwargs):
    M = ConcreteModel()
    M.x = Var(initialize=3.0)
    M.c = Complementarity(expr=complements((M.x - 1.0)*(M.x - 1.0) - 1.01 >= 0, M.x >= 0))
    return M

