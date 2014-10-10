from __future__ import division
from pyomo.core import *

# @body:
model = AbstractModel()
model.I = Set()
model.p = Param(model.I)
# @:body
