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

#   Source:  problem 208 (p. 56) in
#   A.R. Buckley,
#   "Test functions for unconstrained minimization",
#   TR 1989CS-3, Mathematics, statistics and computing centre,
#   Dalhousie University, Halifax (CDN), 1989.

#   SIF input: Ph. Toint, Dec 1989.

#   classification NQR2-AN-2-2

from pyomo.core import *
model = ConcreteModel()

model.x = Var(RangeSet(1,2),initialize=0.5)

def f_rule(model):
    return 0
model.f = Objective(rule=f_rule)
    
def cons_rule(model):
    return (model.x[1]-0.1136*(model.x[1]+3.0*model.x[2])*(1-model.x[1])) == 0
model.cons = Constraint(rule=cons_rule)

def cons2_rule(model):
    return (model.x[2]+7.5*(2.0*model.x[1]-model.x[2])*(1-model.x[2])) == 0
model.cons2 = Constraint(rule=cons2_rule)
