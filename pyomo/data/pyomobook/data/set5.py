import pyomo.environ
from pyomo.core import *

model = AbstractModel()

# @decl:
model.A = Set(dimen=4)
# @:decl

instance = model.create('set5.dat')


for tpl in sorted(list(instance.A.data())):
    print(tpl)
