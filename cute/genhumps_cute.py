#
#  Pyomo Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Gabe Hackebeil, Juan Lopez
# Taken from:

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

#   Source 
#   Ph. Toint, private communication, 1997.

#   SDIF input N. Gould and Ph. Toint, November 1997.

#   classification SUR2-AN-V-0

from pyomo.core import *
model = ConcreteModel()

zeta = 2
N = 5

def x_init_rule(model,i):
    if i==1:
        return -506.0
    else:
        return 506.2
model.x = Var(RangeSet(1,N),initialize=x_init_rule)

def f_rule(model):
    return sum(sin (zeta*model.x[i])**2*sin(zeta*model.x[i+1])**2+0.05*(model.x[i]**2+model.x[i+1]**2) for i in range(1,N))
model.f = Objective(rule=f_rule)
