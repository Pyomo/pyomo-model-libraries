from pyomo.environ import *

# --------------------------------------------------
# @load:
model = AbstractModel()
model.A = Set()
data = DataPortal()
data.load(filename='A.tab', set=model.A)
instance = model.create(data)
# @:load
instance.pprint()
# --------------------------------------------------
# @set1:
model = AbstractModel()
model.A = Set()
data = DataPortal()
data.load(filename='A.tab', set=model.A)
instance = model.create(data)
# @:set1
instance.pprint()
# --------------------------------------------------
# @set2:
model = AbstractModel()
model.C = Set(dimen=2)
data = DataPortal()
data.load(filename='C.tab', set=model.C)
instance = model.create(data)
# @:set2
instance.pprint()
# --------------------------------------------------
# @set3:
model = AbstractModel()
model.D = Set(dimen=2)
data = DataPortal()
data.load(filename='D.tab', set=model.D, format='set_array')
instance = model.create(data)
# @:set3
instance.pprint()

# --------------------------------------------------
# @param1:
model = AbstractModel()
data = DataPortal()
model.z = Param()
data.load(filename='Z.tab', param=model.z)
instance = model.create(data)
# @:param1
instance.pprint()
# --------------------------------------------------
# @param2:
model = AbstractModel()
data = DataPortal()
model.A = Set(initialize=['A1','A2','A3'])
model.y = Param(model.A)
data.load(filename='Y.tab', param=model.y)
instance = model.create(data)
# @:param2
instance.pprint()
# --------------------------------------------------
# @param4:
model = AbstractModel()
data = DataPortal()
model.A = Set(initialize=['A1','A2','A3'])
model.x = Param(model.A)
model.w = Param(model.A)
data.load(filename='XW.tab', param=(model.x,model.w))
instance = model.create(data)
# @:param4
instance.pprint()
# --------------------------------------------------
# @param3:
model = AbstractModel()
data = DataPortal()
model.A = Set()
model.y = Param(model.A)
data.load(filename='Y.tab', param=model.y, index=model.A)
instance = model.create(data)
# @:param3
instance.pprint()
# --------------------------------------------------
# @param5:
model = AbstractModel()
data = DataPortal()
model.A = Set()
model.w = Param(model.A)
data.load(filename='XW.tab', select=('A','W'), 
                param=model.w, index=model.A)
instance = model.create(data)
# @:param5
instance.pprint()
# --------------------------------------------------
# @param6:
model = AbstractModel()
data = DataPortal()
model.A = Set(initialize=['A1','A2','A3'])
model.I = Set(initialize=['I1','I2','I3','I4'])
model.u = Param(model.I, model.A)
data.load(filename='U.tab', param=model.u, 
                                    format='array')
instance = model.create(data)
# @:param6
instance.pprint()
# --------------------------------------------------
# @param7:
model = AbstractModel()
data = DataPortal()
model.A = Set(initialize=['A1','A2','A3'])
model.I = Set(initialize=['I1','I2','I3','I4'])
model.t = Param(model.A, model.I)
data.load(filename='U.tab', param=model.t, 
                                    format='transposed_array')
instance = model.create(data)
# @:param7
instance.pprint()
# --------------------------------------------------
# @param8:
model = AbstractModel()
data = DataPortal()
model.A = Set()
model.s = Param(model.A)
data.load(filename='S.tab', param=model.s, index=model.A)
instance = model.create(data)
# @:param8
instance.pprint()
# --------------------------------------------------
# @param9:
model = AbstractModel()
data = DataPortal()
model.A = Set(initialize=['A1','A2','A3','A4'])
model.y = Param(model.A)
data.load(filename='Y.tab', param=model.y)
instance = model.create(data)
# @:param9
instance.pprint()
# --------------------------------------------------
# @param10:
model = AbstractModel()
data = DataPortal()
model.A = Set(dimen=2)
model.p = Param(model.A)
data.load(filename='PP.tab', param=model.p, index=model.A)
instance = model.create(data)
# @:param10
instance.pprint()
# --------------------------------------------------
# @param11:
model = AbstractModel()
data = DataPortal()
model.A = Set()
model.B = Set()
model.q = Param(model.A, model.B)
data.load(filename='PP.tab', param=model.q, index=(model.A,model.B))
#instance = model.create(data)
# @:param11
# --------------------------------------------------
# @concrete1:
data = DataPortal()
data.load(filename='A.tab', set="A", format="set")

model = ConcreteModel()
model.A = Set(initialize=data['A'])
instance = model.create(data)
# @:concrete1
instance.pprint()
# --------------------------------------------------
# @concrete2:
data = DataPortal()
data.load(filename='Z.tab', param="z", format="param")
data.load(filename='Y.tab', param="y", format="table")

model = ConcreteModel()
model.z = Param(initialize=data['z'])
model.y = Param(['A1','A2','A3'], initialize=data['y'])
instance = model.create(data)
# @:concrete2
instance.pprint()
# --------------------------------------------------
# @getitem::
data = DataPortal()
data.load(filename='A.tab', set="A", format="set")
print(data['A'])    #['A1', 'A2', 'A3']

data.load(filename='Z.tab', param="z", format="param")
print(data['z'])    #1.1

data.load(filename='Y.tab', param="y", format="table")
for key in sorted(data['y']):
    print("%s %s" % (key, data['y'][key]))
# @:getitem
# --------------------------------------------------
# @excel1:
model = AbstractModel()
data = DataPortal()
model.A = Set(dimen=2)
model.p = Param(model.A)
data.load(filename='excel.xls', range='PPtable', 
                    param=model.p, index=model.A)
instance = model.create(data)
# @:excel1
instance.pprint()
# --------------------------------------------------
# @excel2:
model = AbstractModel()
data = DataPortal()
model.A = Set(dimen=2)
model.p = Param(model.A)
#data.load(filename='excel.xls', range='AX2:AZ5', 
#                    param=model.p, index=model.A)
instance = model.create(data)
# @:excel2
instance.pprint()
# --------------------------------------------------
# @db1:
model = AbstractModel()
data = DataPortal()
model.A = Set(dimen=2)
model.p = Param(model.A)
#data.load(filename='db.sqlite', using='pymysql',
#                   query="SELECT A,B,PP from Data",
#                   param=model.p, index=model.A)
instance = model.create(data)
# @:db1
instance.pprint()
# --------------------------------------------------
# @json1:
model = AbstractModel()
data = DataPortal()
model.A = Set()
model.B = Set(dimen=2)
model.p = Param()
model.q = Param(model.A)
model.r = Param(model.B)
data.load(filename='T.json')
instance = model.create(data)
instance.pprint()
# @:json1
# --------------------------------------------------

