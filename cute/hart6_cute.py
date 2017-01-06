#  This software is distributed under the BSD License.
#  under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
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

#   Source: Hartman problem 6 in
#   L. C. W. Dixon and G. P. Szego (Eds.)
#   Towards Global Optimization
#   North Holland, 1975.
#   Paper 9, page 163.

#   SIF input: A.R. Conn May 1995

#   classification OBR2-AN-6-0

from pyomo.environ import *
model = AbstractModel()

model.c = Param(RangeSet(1,4))
model.a = Param(RangeSet(1,4),RangeSet(1,6))
model.p = Param(RangeSet(1,4),RangeSet(1,6))

model.x = Var(RangeSet(1,6),bounds=(0.0,1.0),initialize=0.2)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create_instance(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'))

def obj_rule(model):
    return - sum(model.c[i]*\
    exp(-sum(model.a[i,j]*(model.x[j]-model.p[i,j])**2 for j in range(1,7))) for i in range(1,5))
model.obj = Objective(rule=obj_rule)
