#  _________________________________________________________________________
#                                                                           
#  Pyomo: Python Optimization Modeling Objects                          
#  Copyright (c) 2010 Sandia Corporation.                                  
#  This software is distributed under the BSD License.                     
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,  
#  the U.S. Government retains certain rights in this software.            
#  For more information, see the Pyomo README.txt file.                    
#  _________________________________________________________________________

# Formulated in Pyomo by Carl D. Laird, Daniel P. Word, and Brandon C. Barrera
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

#   Source: Problem 55 in
#   A.R. Conn, N.I.M. Gould, M. Lescrenier and Ph.L. Toint,
#   "Performance of a multifrontal scheme for partially separable
#   optimization",
#   Report 88/4, Dept of Mathematics, FUNDP (Namur, B), 1988.

#   SIF input: Ph. Toint, Dec 1989.

#   classification OUR2-AN-V-0

from pyomo.core import *
model = AbstractModel()

model.N = Param(initialize=5000)
model.S = RangeSet(1,model.N)
model.x = Var(model.S, initialize=1.0)
model.SS = RangeSet(1,model.N-1)
def f(model):
    expsum1 = sum ((-4*model.x[i]+3.0) for i in model.SS)
    expsum2 = sum ((model.x[i]**2+model.x[value(model.N)]**2)**2 for i in model.SS)
    return expsum1 + expsum2
model.f = Objective(rule=f,sense=minimize)
