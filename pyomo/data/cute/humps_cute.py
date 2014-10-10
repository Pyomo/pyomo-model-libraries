#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Formulated in pyomo by Logan Barnes. Taken from:

# AMPL Model by Hande Y. Benson
#
# Copyright (C) 2001 Princeton University
# All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that the copyright notice and this
# permission notice appear in all supporting documentation.                     

#   Source: 
#   Ph. Toint, private communication, 1997.

#   SDIF input: Ph. Toint, May 1997.

#   classification SUR2-AN-2-0

from pyomo.core import *
model = ConcreteModel()
zeta = 20.0
model.x = Var(initialize=-506.0)
model.y = Var(initialize=-506.2)

model.f = Objective(expr=0.05*(model.x**2+model.y**2)+(sin(zeta*model.x)*sin(zeta*model.y))**2)
