#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird and Daniel P. Word                                                                                                   # Taken from:
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

#   Source:
#   A.R. Conn, N. Gould and Ph.L. Toint,
#   "LANCELOT, A Fortran Package for Large-Scale Nonlinear Optimization
#   (Release A)"
#   Springer Verlag, 1992.

#   SIF input: N. Gould and Ph. Toint, June 1994.

#   classification OBR2-AY-3-0

from pyomo.core import *
model = AbstractModel()
model.x1 = Var()
model.x2 = Var(bounds=(-1.0,1.0))
model.x3 = Var(bounds=(1.0,2.0))

def obj(m):
    return (m.x1**2 + (m.x2*m.x3)**4 + m.x1*m.x3 + m.x2*sin(m.x1+m.x3) + m.x2)
model.obj = Objective(rule=obj, sense=minimize)
