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
#   M.M. Makela,
#   "Nonsmooth optimization",
#   Ph.D. thesis, Jyvaskyla University, 1990

#   SIF input: Ph. Toint, Nov 1993.

#   classification  LLR2-AN-51-50

#
# Sept 11, 2012
# This model was modified by Gabe Hackebeil for the purposes
# of testing Pyomo.
#
# Constraints of the form:
#     U >= expr;
#     L <= expr;
# Were changed to:
#     expr <= U;
#     expr >= L;
#
# This change was made so that AMPL would not "flip"
# the constraint representation in the corresponding nl file
#

param ri := 50;
param t := -25.5 + (50);

var x {j in 1..50} := -25.5+j;
var u;

minimize obj: u;

subject to f {i in 1..50}: 50*x[i] - sum {j in 1..50} x[j] <= u;
#subject to f {i in 1..50}: u >= 50*x[i] - sum {j in 1..50} x[j];

solve;
display x;
display u;
display obj;
