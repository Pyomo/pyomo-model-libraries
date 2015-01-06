from pyomo.environ import *

# --------------------------------------------------
# @set1:
model = AbstractModel()
model.A = Set()

data = DataPortal()
data.load(filename='A.tab', set=model.A)
instance = model.create(data)
# @:set1
# --------------------------------------------------
model = AbstractModel()
data = DataPortal()
# @set2:
model.A = Set(dimen=2)

data.load(filename='C.tab', set=model.A)
# @:set2
instance = model.create(data)
# --------------------------------------------------
model = AbstractModel()
data = DataPortal()
# @param1:
model.z = Param()

data.load(filename='Z.tab', param=model.z)
# @:param1
instance = model.create(data)
# --------------------------------------------------
model = AbstractModel()
data = DataPortal()
# @param2:
model.A = Set(initialize=['A1','A2','A3','A4'])
model.y = Param(model.A)

data.load(filename='Y.tab', param=model.y)
# @:param2
instance = model.create(data)
# --------------------------------------------------
model = AbstractModel()
data = DataPortal()
# @param3:
model.A = Set(initialize=['A1','A2','A3','A4'])
model.x = Param(model.A)
model.w = Param(model.A)

data.load(filename='XW.tab', param=(model.x,model.w))
# @:param3
instance = model.create(data)
# --------------------------------------------------
model = AbstractModel()
data = DataPortal()
# @param4:
model.A = Set()
model.x = Param(model.A)
model.w = Param(model.A)

data.load(filename='XW.tab', param=(model.x,model.w), index=model.A)
# @:param4
instance = model.create(data)
# --------------------------------------------------
model = AbstractModel()
data = DataPortal()
# @param5:
model.A = Set()
model.w = Param(model.A)

data.load(filename='XW.tab', select=('A','W'), param=model.w, index=model.A)
# @:param5
instance = model.create(data)
# --------------------------------------------------

