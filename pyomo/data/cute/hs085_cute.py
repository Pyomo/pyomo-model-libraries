#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#  Formulated in pyomo by Gabe Hackebeil and Logan Barnes.
#
#  Taken CUTE models
from pyomo.core import *
model = ConcreteModel()

a = {}
a[ 2] =      17.505
a[ 3] =      11.275
a[ 4] =     214.228
a[ 5] =       7.458
a[ 6] =        .961
a[ 7] =       1.612
a[ 8] =        .146
a[ 9] =     107.99
a[10] =     922.693
a[11] =     926.832
a[12] =      18.766
a[13] =    1072.163
a[14] =    8961.448
a[15] =        .063
a[16] =   71084.33
a[17] = 2802713.0


b = {}
b[2] = 1053.6667
b[ 3] =      35.03
b[ 4] =     665.585
b[ 5] =     584.463
b[ 6] =     265.916
b[ 7] =       7.046
b[ 8] =        .222
b[ 9] =     273.366
b[10] =    1286.105
b[11] =    1444.046
b[12] =     537.141
b[13] =    3247.039
b[14] =   26844.086
b[15] =        .386
b[16] =  140000.0
b[17] = 12146108

c10 = 12.3/752.3

model.x = Var(range(1,6))
model.x[1] = 900.0
model.x[2] = 80.0
model.x[3] = 115.0
model.x[4] = 267.0
model.x[5] = 27.0

model.y1  = Expression(initialize= model.x[2]+model.x[3]+41.6 )
model.c1  = Expression(initialize= .024*model.x[4]-4.62 )
model.y2  = Expression(initialize= 12.5/model.c1+12 )
model.c2  = Expression(initialize= .0003535*model.x[1]**2+.5311*model.x[1]+.08705*model.y2*model.x[1] )
model.c3  = Expression(initialize= .052*model.x[1]+78+.002377*model.y2*model.x[1] )
model.y3  = Expression(initialize= model.c2/model.c3 )
model.y4  = Expression(initialize= 19.*model.y3 )
model.c4  = Expression(initialize= .04782*(model.x[1]-model.y3)+.1956*(model.x[1]-model.y3)**2./model.x[2]+.6376*model.y4+1.594*model.y3 )
model.c5  = Expression(initialize= 100.*model.x[2] )
model.c6  = Expression(initialize= model.x[1]-model.y3-model.y4 )
model.c7  = Expression(initialize= .95-model.c4/model.c5 )
model.y5  = Expression(initialize= model.c6*model.c7 )
model.y6  = Expression(initialize= model.x[1]-model.y5-model.y4-model.y3 )
model.c8  = Expression(initialize= (model.y5+model.y4)*.995 )
model.y7  = Expression(initialize= model.c8/model.y1 )
model.y8  = Expression(initialize= model.c8/3798. )
model.c9  = Expression(initialize= model.y7-.0663*model.y7/model.y8-.3153 )
model.y9  = Expression(initialize= 96.82/model.c9+.321*model.y1 )
model.y10 = Expression(initialize= 1.29*model.y5+1.258*model.y4+2.29*model.y3+1.71*model.y6 )
model.y11 = Expression(initialize= 1.71*model.x[1]-.452*model.y4+.58*model.y3 )
model.c11 = Expression(initialize= 1.75*model.y2*.995*model.x[1] )
model.c12 = Expression(initialize= .995*model.y10+1998. )
model.y12 = Expression(initialize= c10*model.x[1]+model.c11/model.c12 )
model.y13 = Expression(initialize= model.c12-1.75*model.y2 )
model.y14 = Expression(initialize= 3623.+64.4*model.x[2]+58.4*model.x[3]+146312./(model.y9+model.x[5]) )
model.c13 = Expression(initialize= .995*model.y10+60.8*model.x[2]+48.*model.x[4]-.1121*model.y14-5095. )
model.y15 = Expression(initialize= model.y13/model.c13 )
model.y16 = Expression(initialize= 148000.-331000.*model.y15+40.*model.y13-61.*model.y15*model.y13 )
model.c14 = Expression(initialize= 2324.*model.y10-28740000.*model.y2 )
model.y17 = Expression(initialize= 14130000.-1328.*model.y10-531.*model.y11+model.c14/model.c12 )
model.c15 = Expression(initialize= model.y13/model.y15-model.y13/.52 )
model.c16 = Expression(initialize= 1.104-.72*model.y15 )
model.c17 = Expression(initialize= model.y9+model.x[5] )

model.obj = Objective(expr=-5.843e-7*model.y17+1.17e-4*model.y14+2.358e-5*model.y13+1.502e-6*model.y16\
                           +.0321*model.y12+.004324*model.y5+1e-4*model.c15/model.c16+37.48*model.y2/model.c12+.1365)

model.con1 = Constraint(expr=1.5*model.x[2]-model.x[3]>=0)
model.con2 = Constraint(expr=model.y1-213.1>=0)
model.con3 = Constraint(expr=405.23-model.y1>=0)
model.con4 = Constraint(expr=model.x[1]>=704.4148)
model.con5 = Constraint(expr=model.x[1]<=906.3855)
model.con6 = Constraint(expr=model.x[2]>=68.6)
model.con7 = Constraint(expr=model.x[2]<=288.88)
model.con8 = Constraint(expr=model.x[3]>=0)
model.con9 = Constraint(expr=model.x[3]<=134.75)
model.con10 = Constraint(expr=model.x[4]>=193)
model.con11 = Constraint(expr=model.x[4]<=287.0966)
model.con12 = Constraint(expr=model.x[5]>=25)
model.con13 = Constraint(expr=model.x[5]<=84.1988)
model.con14 = Constraint(expr=model.y2-a[2]>=0)
model.con15 = Constraint(expr=model.y3-a[3]>=0)
model.con16 = Constraint(expr=model.y4-a[4]>=0)
model.con17 = Constraint(expr=model.y5-a[5]>=0)
model.con18 = Constraint(expr=model.y6-a[6]>=0)
model.con19 = Constraint(expr=model.y7-a[7]>=0)
model.con20 = Constraint(expr=model.y8-a[8]>=0)
model.con21 = Constraint(expr=model.y9-a[9]>=0)
model.con22 = Constraint(expr=model.y10-a[10]>=0)
model.con23 = Constraint(expr=model.y11-a[11]>=0)
model.con24 = Constraint(expr=model.y12-a[12]>=0)
model.con25 = Constraint(expr=model.y13-a[13]>=0)
model.con26 = Constraint(expr=model.y14-a[14]>=0)
model.con27 = Constraint(expr=model.y15-a[15]>=0)
model.con28 = Constraint(expr=model.y16-a[16]>=0)
model.con29 = Constraint(expr=model.y17-a[17]>=0)
model.con30 = Constraint(expr=b[2]-model.y2>=0)
model.con31 = Constraint(expr=b[3]-model.y3>=0)
model.con32 = Constraint(expr=b[4]-model.y4>=0)
model.con33 = Constraint(expr=b[5]-model.y5>=0)
model.con34 = Constraint(expr=b[6]-model.y6>=0)
model.con35 = Constraint(expr=b[7]-model.y7>=0)
model.con36 = Constraint(expr=b[8]-model.y8>=0)
model.con37 = Constraint(expr=b[9]-model.y9>=0)
model.con38 = Constraint(expr=b[10]-model.y10>=0)
model.con39 = Constraint(expr=b[11]-model.y11>=0)
model.con40 = Constraint(expr=b[12]-model.y12>=0)
model.con41 = Constraint(expr=b[13]-model.y13>=0)
model.con42 = Constraint(expr=b[14]-model.y14>=0)
model.con43 = Constraint(expr=b[15]-model.y15>=0)
model.con44 = Constraint(expr=b[16]-model.y16>=0)
model.con45 = Constraint(expr=b[17]-model.y17>=0)
model.con46 = Constraint(expr=model.y4-.28/.72*model.y5>=0)
model.con47 = Constraint(expr=21-3496.*model.y2/model.c12>=0)
model.con48 = Constraint(expr=62212./model.c17-110.6-model.y1>=0)
