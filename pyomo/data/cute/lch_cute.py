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
#  Formulated in pyomo by Logan Barnes. Taken from:

#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem :
#   *********
#   A minimum energy problem in quantum physics.
#   Source:
#   Leonor Cruzeiro-Hasson (private communication).
#   SIF input: Nick Gould, Feb 1991.
#   classification OOR2-MY-V-1
#   N is the number of discretization points.
#IE N                   10
#IE N                   50
#IE N                   100
#   problem constants
#   Define useful parameters
#   first contributions to the objective function
#   first contributions to the nonlinear constraint
#   general contributions to the objective function
#   general contributions to the nonlinear constraint
#   last contributions to the objective function
#   last contributions to the nonlinear constraint
#   Solution
#LO SOLTN(10)          -3.7565286
#LO SOLTN(50)          -4.2295940
#LO SOLTN(100)         -4.2887306

from pyomo.core import *
model = ConcreteModel()

model.pr1 = Var(initialize=0.05)
model.pi1 = Var(initialize=0.05)
model.u1 = Var(initialize=0.1)
model.pr2 = Var(initialize=0.05)
model.pi2 = Var(initialize=0.05)
model.u2 = Var(initialize=0.2)
model.pr3 = Var(initialize=0.05)
model.pi3 = Var(initialize=0.05)
model.u3 = Var(initialize=0.3)
model.pr4 = Var(initialize=0.05)
model.pi4 = Var(initialize=0.05)
model.u4 = Var(initialize=0.4)
model.pr5 = Var(initialize=0.05)
model.pi5 = Var(initialize=0.05)
model.u5 = Var(initialize=0.5)
model.pr6 = Var(initialize=0.05)
model.pi6 = Var(initialize=0.05)
model.u6 = Var(initialize=0.6)
model.pr7 = Var(initialize=0.05)
model.pi7 = Var(initialize=0.05)
model.u7 = Var(initialize=0.7)
model.pr8 = Var(initialize=0.05)
model.pi8 = Var(initialize=0.05)
model.u8 = Var(initialize=0.7999999999999999)
model.pr9 = Var(initialize=0.05)
model.pi9 = Var(initialize=0.05)
model.u9 = Var(initialize=0.8999999999999999)
model.pr10 = Var(initialize=0.05)
model.pi10 = Var(initialize=0.05)
model.u10 = Var(initialize=0.9999999999999999)
model.pr11 = Var(initialize=0.05)
model.pi11 = Var(initialize=0.05)
model.u11 = Var(initialize=1.0999999999999999)
model.pr12 = Var(initialize=0.05)
model.pi12 = Var(initialize=0.05)
model.u12 = Var(initialize=1.2)
model.pr13 = Var(initialize=0.05)
model.pi13 = Var(initialize=0.05)
model.u13 = Var(initialize=1.3)
model.pr14 = Var(initialize=0.05)
model.pi14 = Var(initialize=0.05)
model.u14 = Var(initialize=1.4000000000000001)
model.pr15 = Var(initialize=0.05)
model.pi15 = Var(initialize=0.05)
model.u15 = Var(initialize=1.5000000000000002)
model.pr16 = Var(initialize=0.05)
model.pi16 = Var(initialize=0.05)
model.u16 = Var(initialize=1.6000000000000003)
model.pr17 = Var(initialize=0.05)
model.pi17 = Var(initialize=0.05)
model.u17 = Var(initialize=1.7000000000000004)
model.pr18 = Var(initialize=0.05)
model.pi18 = Var(initialize=0.05)
model.u18 = Var(initialize=1.8000000000000005)
model.pr19 = Var(initialize=0.05)
model.pi19 = Var(initialize=0.05)
model.u19 = Var(initialize=1.9000000000000006)
model.pr20 = Var(initialize=0.05)
model.pi20 = Var(initialize=0.05)
model.u20 = Var(initialize=2.0000000000000004)
model.pr21 = Var(initialize=0.05)
model.pi21 = Var(initialize=0.05)
model.u21 = Var(initialize=2.1000000000000005)
model.pr22 = Var(initialize=0.05)
model.pi22 = Var(initialize=0.05)
model.u22 = Var(initialize=2.2000000000000006)
model.pr23 = Var(initialize=0.05)
model.pi23 = Var(initialize=0.05)
model.u23 = Var(initialize=2.3000000000000007)
model.pr24 = Var(initialize=0.05)
model.pi24 = Var(initialize=0.05)
model.u24 = Var(initialize=2.400000000000001)
model.pr25 = Var(initialize=0.05)
model.pi25 = Var(initialize=0.05)
model.u25 = Var(initialize=2.500000000000001)
model.pr26 = Var(initialize=0.05)
model.pi26 = Var(initialize=0.05)
model.u26 = Var(initialize=2.600000000000001)
model.pr27 = Var(initialize=0.05)
model.pi27 = Var(initialize=0.05)
model.u27 = Var(initialize=2.700000000000001)
model.pr28 = Var(initialize=0.05)
model.pi28 = Var(initialize=0.05)
model.u28 = Var(initialize=2.800000000000001)
model.pr29 = Var(initialize=0.05)
model.pi29 = Var(initialize=0.05)
model.u29 = Var(initialize=2.9000000000000012)
model.pr30 = Var(initialize=0.05)
model.pi30 = Var(initialize=0.05)
model.u30 = Var(initialize=3.0000000000000013)
model.pr31 = Var(initialize=0.05)
model.pi31 = Var(initialize=0.05)
model.u31 = Var(initialize=3.1000000000000014)
model.pr32 = Var(initialize=0.05)
model.pi32 = Var(initialize=0.05)
model.u32 = Var(initialize=3.2000000000000015)
model.pr33 = Var(initialize=0.05)
model.pi33 = Var(initialize=0.05)
model.u33 = Var(initialize=3.3000000000000016)
model.pr34 = Var(initialize=0.05)
model.pi34 = Var(initialize=0.05)
model.u34 = Var(initialize=3.4000000000000017)
model.pr35 = Var(initialize=0.05)
model.pi35 = Var(initialize=0.05)
model.u35 = Var(initialize=3.5000000000000018)
model.pr36 = Var(initialize=0.05)
model.pi36 = Var(initialize=0.05)
model.u36 = Var(initialize=3.600000000000002)
model.pr37 = Var(initialize=0.05)
model.pi37 = Var(initialize=0.05)
model.u37 = Var(initialize=3.700000000000002)
model.pr38 = Var(initialize=0.05)
model.pi38 = Var(initialize=0.05)
model.u38 = Var(initialize=3.800000000000002)
model.pr39 = Var(initialize=0.05)
model.pi39 = Var(initialize=0.05)
model.u39 = Var(initialize=3.900000000000002)
model.pr40 = Var(initialize=0.05)
model.pi40 = Var(initialize=0.05)
model.u40 = Var(initialize=4.000000000000002)
model.pr41 = Var(initialize=0.05)
model.pi41 = Var(initialize=0.05)
model.u41 = Var(initialize=4.100000000000001)
model.pr42 = Var(initialize=0.05)
model.pi42 = Var(initialize=0.05)
model.u42 = Var(initialize=4.200000000000001)
model.pr43 = Var(initialize=0.05)
model.pi43 = Var(initialize=0.05)
model.u43 = Var(initialize=4.300000000000001)
model.pr44 = Var(initialize=0.05)
model.pi44 = Var(initialize=0.05)
model.u44 = Var(initialize=4.4)
model.pr45 = Var(initialize=0.05)
model.pi45 = Var(initialize=0.05)
model.u45 = Var(initialize=4.5)
model.pr46 = Var(initialize=0.05)
model.pi46 = Var(initialize=0.05)
model.u46 = Var(initialize=4.6)
model.pr47 = Var(initialize=0.05)
model.pi47 = Var(initialize=0.05)
model.u47 = Var(initialize=4.699999999999999)
model.pr48 = Var(initialize=0.05)
model.pi48 = Var(initialize=0.05)
model.u48 = Var(initialize=4.799999999999999)
model.pr49 = Var(initialize=0.05)
model.pi49 = Var(initialize=0.05)
model.u49 = Var(initialize=4.899999999999999)
model.pr50 = Var(initialize=0.05)
model.pi50 = Var(initialize=0.05)
model.u50 = Var(initialize=4.999999999999998)
model.pr51 = Var(initialize=0.05)
model.pi51 = Var(initialize=0.05)
model.u51 = Var(initialize=5.099999999999998)
model.pr52 = Var(initialize=0.05)
model.pi52 = Var(initialize=0.05)
model.u52 = Var(initialize=5.1999999999999975)
model.pr53 = Var(initialize=0.05)
model.pi53 = Var(initialize=0.05)
model.u53 = Var(initialize=5.299999999999997)
model.pr54 = Var(initialize=0.05)
model.pi54 = Var(initialize=0.05)
model.u54 = Var(initialize=5.399999999999997)
model.pr55 = Var(initialize=0.05)
model.pi55 = Var(initialize=0.05)
model.u55 = Var(initialize=5.4999999999999964)
model.pr56 = Var(initialize=0.05)
model.pi56 = Var(initialize=0.05)
model.u56 = Var(initialize=5.599999999999996)
model.pr57 = Var(initialize=0.05)
model.pi57 = Var(initialize=0.05)
model.u57 = Var(initialize=5.699999999999996)
model.pr58 = Var(initialize=0.05)
model.pi58 = Var(initialize=0.05)
model.u58 = Var(initialize=5.799999999999995)
model.pr59 = Var(initialize=0.05)
model.pi59 = Var(initialize=0.05)
model.u59 = Var(initialize=5.899999999999995)
model.pr60 = Var(initialize=0.05)
model.pi60 = Var(initialize=0.05)
model.u60 = Var(initialize=5.999999999999995)
model.pr61 = Var(initialize=0.05)
model.pi61 = Var(initialize=0.05)
model.u61 = Var(initialize=6.099999999999994)
model.pr62 = Var(initialize=0.05)
model.pi62 = Var(initialize=0.05)
model.u62 = Var(initialize=6.199999999999994)
model.pr63 = Var(initialize=0.05)
model.pi63 = Var(initialize=0.05)
model.u63 = Var(initialize=6.299999999999994)
model.pr64 = Var(initialize=0.05)
model.pi64 = Var(initialize=0.05)
model.u64 = Var(initialize=6.399999999999993)
model.pr65 = Var(initialize=0.05)
model.pi65 = Var(initialize=0.05)
model.u65 = Var(initialize=6.499999999999993)
model.pr66 = Var(initialize=0.05)
model.pi66 = Var(initialize=0.05)
model.u66 = Var(initialize=6.5999999999999925)
model.pr67 = Var(initialize=0.05)
model.pi67 = Var(initialize=0.05)
model.u67 = Var(initialize=6.699999999999992)
model.pr68 = Var(initialize=0.05)
model.pi68 = Var(initialize=0.05)
model.u68 = Var(initialize=6.799999999999992)
model.pr69 = Var(initialize=0.05)
model.pi69 = Var(initialize=0.05)
model.u69 = Var(initialize=6.8999999999999915)
model.pr70 = Var(initialize=0.05)
model.pi70 = Var(initialize=0.05)
model.u70 = Var(initialize=6.999999999999991)
model.pr71 = Var(initialize=0.05)
model.pi71 = Var(initialize=0.05)
model.u71 = Var(initialize=7.099999999999991)
model.pr72 = Var(initialize=0.05)
model.pi72 = Var(initialize=0.05)
model.u72 = Var(initialize=7.19999999999999)
model.pr73 = Var(initialize=0.05)
model.pi73 = Var(initialize=0.05)
model.u73 = Var(initialize=7.29999999999999)
model.pr74 = Var(initialize=0.05)
model.pi74 = Var(initialize=0.05)
model.u74 = Var(initialize=7.39999999999999)
model.pr75 = Var(initialize=0.05)
model.pi75 = Var(initialize=0.05)
model.u75 = Var(initialize=7.499999999999989)
model.pr76 = Var(initialize=0.05)
model.pi76 = Var(initialize=0.05)
model.u76 = Var(initialize=7.599999999999989)
model.pr77 = Var(initialize=0.05)
model.pi77 = Var(initialize=0.05)
model.u77 = Var(initialize=7.699999999999989)
model.pr78 = Var(initialize=0.05)
model.pi78 = Var(initialize=0.05)
model.u78 = Var(initialize=7.799999999999988)
model.pr79 = Var(initialize=0.05)
model.pi79 = Var(initialize=0.05)
model.u79 = Var(initialize=7.899999999999988)
model.pr80 = Var(initialize=0.05)
model.pi80 = Var(initialize=0.05)
model.u80 = Var(initialize=7.999999999999988)
model.pr81 = Var(initialize=0.05)
model.pi81 = Var(initialize=0.05)
model.u81 = Var(initialize=8.099999999999987)
model.pr82 = Var(initialize=0.05)
model.pi82 = Var(initialize=0.05)
model.u82 = Var(initialize=8.199999999999987)
model.pr83 = Var(initialize=0.05)
model.pi83 = Var(initialize=0.05)
model.u83 = Var(initialize=8.299999999999986)
model.pr84 = Var(initialize=0.05)
model.pi84 = Var(initialize=0.05)
model.u84 = Var(initialize=8.399999999999986)
model.pr85 = Var(initialize=0.05)
model.pi85 = Var(initialize=0.05)
model.u85 = Var(initialize=8.499999999999986)
model.pr86 = Var(initialize=0.05)
model.pi86 = Var(initialize=0.05)
model.u86 = Var(initialize=8.599999999999985)
model.pr87 = Var(initialize=0.05)
model.pi87 = Var(initialize=0.05)
model.u87 = Var(initialize=8.699999999999985)
model.pr88 = Var(initialize=0.05)
model.pi88 = Var(initialize=0.05)
model.u88 = Var(initialize=8.799999999999985)
model.pr89 = Var(initialize=0.05)
model.pi89 = Var(initialize=0.05)
model.u89 = Var(initialize=8.899999999999984)
model.pr90 = Var(initialize=0.05)
model.pi90 = Var(initialize=0.05)
model.u90 = Var(initialize=8.999999999999984)
model.pr91 = Var(initialize=0.05)
model.pi91 = Var(initialize=0.05)
model.u91 = Var(initialize=9.099999999999984)
model.pr92 = Var(initialize=0.05)
model.pi92 = Var(initialize=0.05)
model.u92 = Var(initialize=9.199999999999983)
model.pr93 = Var(initialize=0.05)
model.pi93 = Var(initialize=0.05)
model.u93 = Var(initialize=9.299999999999983)
model.pr94 = Var(initialize=0.05)
model.pi94 = Var(initialize=0.05)
model.u94 = Var(initialize=9.399999999999983)
model.pr95 = Var(initialize=0.05)
model.pi95 = Var(initialize=0.05)
model.u95 = Var(initialize=9.499999999999982)
model.pr96 = Var(initialize=0.05)
model.pi96 = Var(initialize=0.05)
model.u96 = Var(initialize=9.599999999999982)
model.pr97 = Var(initialize=0.05)
model.pi97 = Var(initialize=0.05)
model.u97 = Var(initialize=9.699999999999982)
model.pr98 = Var(initialize=0.05)
model.pi98 = Var(initialize=0.05)
model.u98 = Var(initialize=9.799999999999981)
model.pr99 = Var(initialize=0.05)
model.pi99 = Var(initialize=0.05)
model.u99 = Var(initialize=9.89999999999998)
model.pr100 = Var(initialize=0.05)
model.pi100 = Var(initialize=0.05)
model.u100 = Var(initialize=9.99999999999998)
model.pr101 = Var(initialize=0.05)
model.pi101 = Var(initialize=0.05)
model.u101 = Var(initialize=10.09999999999998)
model.pr102 = Var(initialize=0.05)
model.pi102 = Var(initialize=0.05)
model.u102 = Var(initialize=10.19999999999998)
model.pr103 = Var(initialize=0.05)
model.pi103 = Var(initialize=0.05)
model.u103 = Var(initialize=10.29999999999998)
model.pr104 = Var(initialize=0.05)
model.pi104 = Var(initialize=0.05)
model.u104 = Var(initialize=10.399999999999979)
model.pr105 = Var(initialize=0.05)
model.pi105 = Var(initialize=0.05)
model.u105 = Var(initialize=10.499999999999979)
model.pr106 = Var(initialize=0.05)
model.pi106 = Var(initialize=0.05)
model.u106 = Var(initialize=10.599999999999978)
model.pr107 = Var(initialize=0.05)
model.pi107 = Var(initialize=0.05)
model.u107 = Var(initialize=10.699999999999978)
model.pr108 = Var(initialize=0.05)
model.pi108 = Var(initialize=0.05)
model.u108 = Var(initialize=10.799999999999978)
model.pr109 = Var(initialize=0.05)
model.pi109 = Var(initialize=0.05)
model.u109 = Var(initialize=10.899999999999977)
model.pr110 = Var(initialize=0.05)
model.pi110 = Var(initialize=0.05)
model.u110 = Var(initialize=10.999999999999977)
model.pr111 = Var(initialize=0.05)
model.pi111 = Var(initialize=0.05)
model.u111 = Var(initialize=11.099999999999977)
model.pr112 = Var(initialize=0.05)
model.pi112 = Var(initialize=0.05)
model.u112 = Var(initialize=11.199999999999976)
model.pr113 = Var(initialize=0.05)
model.pi113 = Var(initialize=0.05)
model.u113 = Var(initialize=11.299999999999976)
model.pr114 = Var(initialize=0.05)
model.pi114 = Var(initialize=0.05)
model.u114 = Var(initialize=11.399999999999975)
model.pr115 = Var(initialize=0.05)
model.pi115 = Var(initialize=0.05)
model.u115 = Var(initialize=11.499999999999975)
model.pr116 = Var(initialize=0.05)
model.pi116 = Var(initialize=0.05)
model.u116 = Var(initialize=11.599999999999975)
model.pr117 = Var(initialize=0.05)
model.pi117 = Var(initialize=0.05)
model.u117 = Var(initialize=11.699999999999974)
model.pr118 = Var(initialize=0.05)
model.pi118 = Var(initialize=0.05)
model.u118 = Var(initialize=11.799999999999974)
model.pr119 = Var(initialize=0.05)
model.pi119 = Var(initialize=0.05)
model.u119 = Var(initialize=11.899999999999974)
model.pr120 = Var(initialize=0.05)
model.pi120 = Var(initialize=0.05)
model.u120 = Var(initialize=11.999999999999973)
model.pr121 = Var(initialize=0.05)
model.pi121 = Var(initialize=0.05)
model.u121 = Var(initialize=12.099999999999973)
model.pr122 = Var(initialize=0.05)
model.pi122 = Var(initialize=0.05)
model.u122 = Var(initialize=12.199999999999973)
model.pr123 = Var(initialize=0.05)
model.pi123 = Var(initialize=0.05)
model.u123 = Var(initialize=12.299999999999972)
model.pr124 = Var(initialize=0.05)
model.pi124 = Var(initialize=0.05)
model.u124 = Var(initialize=12.399999999999972)
model.pr125 = Var(initialize=0.05)
model.pi125 = Var(initialize=0.05)
model.u125 = Var(initialize=12.499999999999972)
model.pr126 = Var(initialize=0.05)
model.pi126 = Var(initialize=0.05)
model.u126 = Var(initialize=12.599999999999971)
model.pr127 = Var(initialize=0.05)
model.pi127 = Var(initialize=0.05)
model.u127 = Var(initialize=12.69999999999997)
model.pr128 = Var(initialize=0.05)
model.pi128 = Var(initialize=0.05)
model.u128 = Var(initialize=12.79999999999997)
model.pr129 = Var(initialize=0.05)
model.pi129 = Var(initialize=0.05)
model.u129 = Var(initialize=12.89999999999997)
model.pr130 = Var(initialize=0.05)
model.pi130 = Var(initialize=0.05)
model.u130 = Var(initialize=12.99999999999997)
model.pr131 = Var(initialize=0.05)
model.pi131 = Var(initialize=0.05)
model.u131 = Var(initialize=13.09999999999997)
model.pr132 = Var(initialize=0.05)
model.pi132 = Var(initialize=0.05)
model.u132 = Var(initialize=13.199999999999969)
model.pr133 = Var(initialize=0.05)
model.pi133 = Var(initialize=0.05)
model.u133 = Var(initialize=13.299999999999969)
model.pr134 = Var(initialize=0.05)
model.pi134 = Var(initialize=0.05)
model.u134 = Var(initialize=13.399999999999968)
model.pr135 = Var(initialize=0.05)
model.pi135 = Var(initialize=0.05)
model.u135 = Var(initialize=13.499999999999968)
model.pr136 = Var(initialize=0.05)
model.pi136 = Var(initialize=0.05)
model.u136 = Var(initialize=13.599999999999968)
model.pr137 = Var(initialize=0.05)
model.pi137 = Var(initialize=0.05)
model.u137 = Var(initialize=13.699999999999967)
model.pr138 = Var(initialize=0.05)
model.pi138 = Var(initialize=0.05)
model.u138 = Var(initialize=13.799999999999967)
model.pr139 = Var(initialize=0.05)
model.pi139 = Var(initialize=0.05)
model.u139 = Var(initialize=13.899999999999967)
model.pr140 = Var(initialize=0.05)
model.pi140 = Var(initialize=0.05)
model.u140 = Var(initialize=13.999999999999966)
model.pr141 = Var(initialize=0.05)
model.pi141 = Var(initialize=0.05)
model.u141 = Var(initialize=14.099999999999966)
model.pr142 = Var(initialize=0.05)
model.pi142 = Var(initialize=0.05)
model.u142 = Var(initialize=14.199999999999966)
model.pr143 = Var(initialize=0.05)
model.pi143 = Var(initialize=0.05)
model.u143 = Var(initialize=14.299999999999965)
model.pr144 = Var(initialize=0.05)
model.pi144 = Var(initialize=0.05)
model.u144 = Var(initialize=14.399999999999965)
model.pr145 = Var(initialize=0.05)
model.pi145 = Var(initialize=0.05)
model.u145 = Var(initialize=14.499999999999964)
model.pr146 = Var(initialize=0.05)
model.pi146 = Var(initialize=0.05)
model.u146 = Var(initialize=14.599999999999964)
model.pr147 = Var(initialize=0.05)
model.pi147 = Var(initialize=0.05)
model.u147 = Var(initialize=14.699999999999964)
model.pr148 = Var(initialize=0.05)
model.pi148 = Var(initialize=0.05)
model.u148 = Var(initialize=14.799999999999963)
model.pr149 = Var(initialize=0.05)
model.pi149 = Var(initialize=0.05)
model.u149 = Var(initialize=14.899999999999963)
model.pr150 = Var(initialize=0.05)
model.pi150 = Var(initialize=0.05)
model.u150 = Var(initialize=14.999999999999963)
model.pr151 = Var(initialize=0.05)
model.pi151 = Var(initialize=0.05)
model.u151 = Var(initialize=15.099999999999962)
model.pr152 = Var(initialize=0.05)
model.pi152 = Var(initialize=0.05)
model.u152 = Var(initialize=15.199999999999962)
model.pr153 = Var(initialize=0.05)
model.pi153 = Var(initialize=0.05)
model.u153 = Var(initialize=15.299999999999962)
model.pr154 = Var(initialize=0.05)
model.pi154 = Var(initialize=0.05)
model.u154 = Var(initialize=15.399999999999961)
model.pr155 = Var(initialize=0.05)
model.pi155 = Var(initialize=0.05)
model.u155 = Var(initialize=15.499999999999961)
model.pr156 = Var(initialize=0.05)
model.pi156 = Var(initialize=0.05)
model.u156 = Var(initialize=15.59999999999996)
model.pr157 = Var(initialize=0.05)
model.pi157 = Var(initialize=0.05)
model.u157 = Var(initialize=15.69999999999996)
model.pr158 = Var(initialize=0.05)
model.pi158 = Var(initialize=0.05)
model.u158 = Var(initialize=15.79999999999996)
model.pr159 = Var(initialize=0.05)
model.pi159 = Var(initialize=0.05)
model.u159 = Var(initialize=15.89999999999996)
model.pr160 = Var(initialize=0.05)
model.pi160 = Var(initialize=0.05)
model.u160 = Var(initialize=15.99999999999996)
model.pr161 = Var(initialize=0.05)
model.pi161 = Var(initialize=0.05)
model.u161 = Var(initialize=16.09999999999996)
model.pr162 = Var(initialize=0.05)
model.pi162 = Var(initialize=0.05)
model.u162 = Var(initialize=16.19999999999996)
model.pr163 = Var(initialize=0.05)
model.pi163 = Var(initialize=0.05)
model.u163 = Var(initialize=16.29999999999996)
model.pr164 = Var(initialize=0.05)
model.pi164 = Var(initialize=0.05)
model.u164 = Var(initialize=16.399999999999963)
model.pr165 = Var(initialize=0.05)
model.pi165 = Var(initialize=0.05)
model.u165 = Var(initialize=16.499999999999964)
model.pr166 = Var(initialize=0.05)
model.pi166 = Var(initialize=0.05)
model.u166 = Var(initialize=16.599999999999966)
model.pr167 = Var(initialize=0.05)
model.pi167 = Var(initialize=0.05)
model.u167 = Var(initialize=16.699999999999967)
model.pr168 = Var(initialize=0.05)
model.pi168 = Var(initialize=0.05)
model.u168 = Var(initialize=16.79999999999997)
model.pr169 = Var(initialize=0.05)
model.pi169 = Var(initialize=0.05)
model.u169 = Var(initialize=16.89999999999997)
model.pr170 = Var(initialize=0.05)
model.pi170 = Var(initialize=0.05)
model.u170 = Var(initialize=16.99999999999997)
model.pr171 = Var(initialize=0.05)
model.pi171 = Var(initialize=0.05)
model.u171 = Var(initialize=17.099999999999973)
model.pr172 = Var(initialize=0.05)
model.pi172 = Var(initialize=0.05)
model.u172 = Var(initialize=17.199999999999974)
model.pr173 = Var(initialize=0.05)
model.pi173 = Var(initialize=0.05)
model.u173 = Var(initialize=17.299999999999976)
model.pr174 = Var(initialize=0.05)
model.pi174 = Var(initialize=0.05)
model.u174 = Var(initialize=17.399999999999977)
model.pr175 = Var(initialize=0.05)
model.pi175 = Var(initialize=0.05)
model.u175 = Var(initialize=17.49999999999998)
model.pr176 = Var(initialize=0.05)
model.pi176 = Var(initialize=0.05)
model.u176 = Var(initialize=17.59999999999998)
model.pr177 = Var(initialize=0.05)
model.pi177 = Var(initialize=0.05)
model.u177 = Var(initialize=17.69999999999998)
model.pr178 = Var(initialize=0.05)
model.pi178 = Var(initialize=0.05)
model.u178 = Var(initialize=17.799999999999983)
model.pr179 = Var(initialize=0.05)
model.pi179 = Var(initialize=0.05)
model.u179 = Var(initialize=17.899999999999984)
model.pr180 = Var(initialize=0.05)
model.pi180 = Var(initialize=0.05)
model.u180 = Var(initialize=17.999999999999986)
model.pr181 = Var(initialize=0.05)
model.pi181 = Var(initialize=0.05)
model.u181 = Var(initialize=18.099999999999987)
model.pr182 = Var(initialize=0.05)
model.pi182 = Var(initialize=0.05)
model.u182 = Var(initialize=18.19999999999999)
model.pr183 = Var(initialize=0.05)
model.pi183 = Var(initialize=0.05)
model.u183 = Var(initialize=18.29999999999999)
model.pr184 = Var(initialize=0.05)
model.pi184 = Var(initialize=0.05)
model.u184 = Var(initialize=18.39999999999999)
model.pr185 = Var(initialize=0.05)
model.pi185 = Var(initialize=0.05)
model.u185 = Var(initialize=18.499999999999993)
model.pr186 = Var(initialize=0.05)
model.pi186 = Var(initialize=0.05)
model.u186 = Var(initialize=18.599999999999994)
model.pr187 = Var(initialize=0.05)
model.pi187 = Var(initialize=0.05)
model.u187 = Var(initialize=18.699999999999996)
model.pr188 = Var(initialize=0.05)
model.pi188 = Var(initialize=0.05)
model.u188 = Var(initialize=18.799999999999997)
model.pr189 = Var(initialize=0.05)
model.pi189 = Var(initialize=0.05)
model.u189 = Var(initialize=18.9)
model.pr190 = Var(initialize=0.05)
model.pi190 = Var(initialize=0.05)
model.u190 = Var(initialize=19.0)
model.pr191 = Var(initialize=0.05)
model.pi191 = Var(initialize=0.05)
model.u191 = Var(initialize=19.1)
model.pr192 = Var(initialize=0.05)
model.pi192 = Var(initialize=0.05)
model.u192 = Var(initialize=19.200000000000003)
model.pr193 = Var(initialize=0.05)
model.pi193 = Var(initialize=0.05)
model.u193 = Var(initialize=19.300000000000004)
model.pr194 = Var(initialize=0.05)
model.pi194 = Var(initialize=0.05)
model.u194 = Var(initialize=19.400000000000006)
model.pr195 = Var(initialize=0.05)
model.pi195 = Var(initialize=0.05)
model.u195 = Var(initialize=19.500000000000007)
model.pr196 = Var(initialize=0.05)
model.pi196 = Var(initialize=0.05)
model.u196 = Var(initialize=19.60000000000001)
model.pr197 = Var(initialize=0.05)
model.pi197 = Var(initialize=0.05)
model.u197 = Var(initialize=19.70000000000001)
model.pr198 = Var(initialize=0.05)
model.pi198 = Var(initialize=0.05)
model.u198 = Var(initialize=19.80000000000001)
model.pr199 = Var(initialize=0.05)
model.pi199 = Var(initialize=0.05)
model.u199 = Var(initialize=19.900000000000013)
model.pr200 = Var(initialize=0.05)
model.pi200 = Var(initialize=0.05)
model.u200 = Var(initialize=20.000000000000014)

model.obj = Objective(expr=- 1.549429*(model.pr1) * (model.pr200+model.pr2) - 1.549429*(model.pi1) * (model.pi200+model.pi2) + (-62.0*model.u200+0.0*model.u1+62.0*model.u2) * (model.pr1*model.pr1+model.pi1*model.pi1) + 650.0*(model.u200-model.u1) * (model.u200-model.u1) - 1.549429*(model.pr2) * (model.pr1+model.pr3) - 1.549429*(model.pi2) * (model.pi1+model.pi3) + (-62.0*model.u1+0.0*model.u2+62.0*model.u3) * (model.pr2*model.pr2+model.pi2*model.pi2) + 650.0*(model.u1-model.u2) * (model.u1-model.u2) - 1.549429*(model.pr3) * (model.pr2+model.pr4) - 1.549429*(model.pi3) * (model.pi2+model.pi4) + (-62.0*model.u2+0.0*model.u3+62.0*model.u4) * (model.pr3*model.pr3+model.pi3*model.pi3) + 650.0*(model.u2-model.u3) * (model.u2-model.u3) - 1.549429*(model.pr4) * (model.pr3+model.pr5) - 1.549429*(model.pi4) * (model.pi3+model.pi5) + (-62.0*model.u3+0.0*model.u4+62.0*model.u5) * (model.pr4*model.pr4+model.pi4*model.pi4) + 650.0*(model.u3-model.u4) * (model.u3-model.u4) - 1.549429*(model.pr5) * (model.pr4+model.pr6) - 1.549429*(model.pi5) * (model.pi4+model.pi6) + (-62.0*model.u4+0.0*model.u5+62.0*model.u6) * (model.pr5*model.pr5+model.pi5*model.pi5) + 650.0*(model.u4-model.u5) * (model.u4-model.u5) - 1.549429*(model.pr6) * (model.pr5+model.pr7) - 1.549429*(model.pi6) * (model.pi5+model.pi7) + (-62.0*model.u5+0.0*model.u6+62.0*model.u7) * (model.pr6*model.pr6+model.pi6*model.pi6) + 650.0*(model.u5-model.u6) * (model.u5-model.u6) - 1.549429*(model.pr7) * (model.pr6+model.pr8) - 1.549429*(model.pi7) * (model.pi6+model.pi8) + 
    (-62.0*model.u6+0.0*model.u7+62.0*model.u8) * (model.pr7*model.pr7+model.pi7*model.pi7) + 650.0*(model.u6-model.u7) * (model.u6-model.u7) - 
    1.549429*(model.pr8) * (model.pr7+model.pr9) - 1.549429*(model.pi8) * (model.pi7+model.pi9) + 
    (-62.0*model.u7+0.0*model.u8+62.0*model.u9) * (model.pr8*model.pr8+model.pi8*model.pi8) + 650.0*(model.u7-model.u8) * (model.u7-model.u8) - 
    1.549429*(model.pr9) * (model.pr8+model.pr10) - 1.549429*(model.pi9) * (model.pi8+model.pi10) + 
    (-62.0*model.u8+0.0*model.u9+62.0*model.u10) * (model.pr9*model.pr9+model.pi9*model.pi9) + 650.0*(model.u8-model.u9) * (model.u8-model.u9) - 
    1.549429*(model.pr10) * (model.pr9+model.pr11) - 1.549429*(model.pi10) * (model.pi9+model.pi11) + 
    (-62.0*model.u9+0.0*model.u10+62.0*model.u11) * (model.pr10*model.pr10+model.pi10*model.pi10) + 650.0*(model.u9-model.u10) * (model.u9-model.u10) 
    - 1.549429*(model.pr11) * (model.pr10+model.pr12) - 1.549429*(model.pi11) * (model.pi10+model.pi12) + 
    (-62.0*model.u10+0.0*model.u11+62.0*model.u12) * (model.pr11*model.pr11+model.pi11*model.pi11) + 650.0*(model.u10-model.u11) * 
    (model.u10-model.u11) - 1.549429*(model.pr12) * (model.pr11+model.pr13) - 1.549429*(model.pi12) * (model.pi11+model.pi13) + 
    (-62.0*model.u11+0.0*model.u12+62.0*model.u13) * (model.pr12*model.pr12+model.pi12*model.pi12) + 650.0*(model.u11-model.u12) * 
    (model.u11-model.u12) - 1.549429*(model.pr13) * (model.pr12+model.pr14) - 1.549429*(model.pi13) * (model.pi12+model.pi14) + 
    (-62.0*model.u12+0.0*model.u13+62.0*model.u14) * (model.pr13*model.pr13+model.pi13*model.pi13) + 650.0*(model.u12-model.u13) * 
    (model.u12-model.u13) - 1.549429*(model.pr14) * (model.pr13+model.pr15) - 1.549429*(model.pi14) * (model.pi13+model.pi15) + 
    (-62.0*model.u13+0.0*model.u14+62.0*model.u15) * (model.pr14*model.pr14+model.pi14*model.pi14) + 650.0*(model.u13-model.u14) * 
    (model.u13-model.u14) - 1.549429*(model.pr15) * (model.pr14+model.pr16) - 1.549429*(model.pi15) * (model.pi14+model.pi16) + 
    (-62.0*model.u14+0.0*model.u15+62.0*model.u16) * (model.pr15*model.pr15+model.pi15*model.pi15) + 650.0*(model.u14-model.u15) * 
    (model.u14-model.u15) - 1.549429*(model.pr16) * (model.pr15+model.pr17) - 1.549429*(model.pi16) * (model.pi15+model.pi17) + 
    (-62.0*model.u15+0.0*model.u16+62.0*model.u17) * (model.pr16*model.pr16+model.pi16*model.pi16) + 650.0*(model.u15-model.u16) * 
    (model.u15-model.u16) - 1.549429*(model.pr17) * (model.pr16+model.pr18) - 1.549429*(model.pi17) * (model.pi16+model.pi18) + 
    (-62.0*model.u16+0.0*model.u17+62.0*model.u18) * (model.pr17*model.pr17+model.pi17*model.pi17) + 650.0*(model.u16-model.u17) * 
    (model.u16-model.u17) - 1.549429*(model.pr18) * (model.pr17+model.pr19) - 1.549429*(model.pi18) * (model.pi17+model.pi19) + 
    (-62.0*model.u17+0.0*model.u18+62.0*model.u19) * (model.pr18*model.pr18+model.pi18*model.pi18) + 650.0*(model.u17-model.u18) * 
    (model.u17-model.u18) - 1.549429*(model.pr19) * (model.pr18+model.pr20) - 1.549429*(model.pi19) * (model.pi18+model.pi20) + 
    (-62.0*model.u18+0.0*model.u19+62.0*model.u20) * (model.pr19*model.pr19+model.pi19*model.pi19) + 650.0*(model.u18-model.u19) * 
    (model.u18-model.u19) - 1.549429*(model.pr20) * (model.pr19+model.pr21) - 1.549429*(model.pi20) * (model.pi19+model.pi21) + 
    (-62.0*model.u19+0.0*model.u20+62.0*model.u21) * (model.pr20*model.pr20+model.pi20*model.pi20) + 650.0*(model.u19-model.u20) * 
    (model.u19-model.u20) - 1.549429*(model.pr21) * (model.pr20+model.pr22) - 1.549429*(model.pi21) * (model.pi20+model.pi22) + 
    (-62.0*model.u20+0.0*model.u21+62.0*model.u22) * (model.pr21*model.pr21+model.pi21*model.pi21) + 650.0*(model.u20-model.u21) * 
    (model.u20-model.u21) - 1.549429*(model.pr22) * (model.pr21+model.pr23) - 1.549429*(model.pi22) * (model.pi21+model.pi23) + 
    (-62.0*model.u21+0.0*model.u22+62.0*model.u23) * (model.pr22*model.pr22+model.pi22*model.pi22) + 650.0*(model.u21-model.u22) * 
    (model.u21-model.u22) - 1.549429*(model.pr23) * (model.pr22+model.pr24) - 1.549429*(model.pi23) * (model.pi22+model.pi24) + 
    (-62.0*model.u22+0.0*model.u23+62.0*model.u24) * (model.pr23*model.pr23+model.pi23*model.pi23) + 650.0*(model.u22-model.u23) * 
    (model.u22-model.u23) - 1.549429*(model.pr24) * (model.pr23+model.pr25) - 1.549429*(model.pi24) * (model.pi23+model.pi25) + 
    (-62.0*model.u23+0.0*model.u24+62.0*model.u25) * (model.pr24*model.pr24+model.pi24*model.pi24) + 650.0*(model.u23-model.u24) * 
    (model.u23-model.u24) - 1.549429*(model.pr25) * (model.pr24+model.pr26) - 1.549429*(model.pi25) * (model.pi24+model.pi26) + 
    (-62.0*model.u24+0.0*model.u25+62.0*model.u26) * (model.pr25*model.pr25+model.pi25*model.pi25) + 650.0*(model.u24-model.u25) * 
    (model.u24-model.u25) - 1.549429*(model.pr26) * (model.pr25+model.pr27) - 1.549429*(model.pi26) * (model.pi25+model.pi27) + 
    (-62.0*model.u25+0.0*model.u26+62.0*model.u27) * (model.pr26*model.pr26+model.pi26*model.pi26) + 650.0*(model.u25-model.u26) * 
    (model.u25-model.u26) - 1.549429*(model.pr27) * (model.pr26+model.pr28) - 1.549429*(model.pi27) * (model.pi26+model.pi28) + 
    (-62.0*model.u26+0.0*model.u27+62.0*model.u28) * (model.pr27*model.pr27+model.pi27*model.pi27) + 650.0*(model.u26-model.u27) * 
    (model.u26-model.u27) - 1.549429*(model.pr28) * (model.pr27+model.pr29) - 1.549429*(model.pi28) * (model.pi27+model.pi29) + 
    (-62.0*model.u27+0.0*model.u28+62.0*model.u29) * (model.pr28*model.pr28+model.pi28*model.pi28) + 650.0*(model.u27-model.u28) * 
    (model.u27-model.u28) - 1.549429*(model.pr29) * (model.pr28+model.pr30) - 1.549429*(model.pi29) * (model.pi28+model.pi30) + 
    (-62.0*model.u28+0.0*model.u29+62.0*model.u30) * (model.pr29*model.pr29+model.pi29*model.pi29) + 650.0*(model.u28-model.u29) * 
    (model.u28-model.u29) - 1.549429*(model.pr30) * (model.pr29+model.pr31) - 1.549429*(model.pi30) * (model.pi29+model.pi31) + 
    (-62.0*model.u29+0.0*model.u30+62.0*model.u31) * (model.pr30*model.pr30+model.pi30*model.pi30) + 650.0*(model.u29-model.u30) * 
    (model.u29-model.u30) - 1.549429*(model.pr31) * (model.pr30+model.pr32) - 1.549429*(model.pi31) * (model.pi30+model.pi32) + 
    (-62.0*model.u30+0.0*model.u31+62.0*model.u32) * (model.pr31*model.pr31+model.pi31*model.pi31) + 650.0*(model.u30-model.u31) * 
    (model.u30-model.u31) - 1.549429*(model.pr32) * (model.pr31+model.pr33) - 1.549429*(model.pi32) * (model.pi31+model.pi33) + 
    (-62.0*model.u31+0.0*model.u32+62.0*model.u33) * (model.pr32*model.pr32+model.pi32*model.pi32) + 650.0*(model.u31-model.u32) * 
    (model.u31-model.u32) - 1.549429*(model.pr33) * (model.pr32+model.pr34) - 1.549429*(model.pi33) * (model.pi32+model.pi34) + 
    (-62.0*model.u32+0.0*model.u33+62.0*model.u34) * (model.pr33*model.pr33+model.pi33*model.pi33) + 650.0*(model.u32-model.u33) * 
    (model.u32-model.u33) - 1.549429*(model.pr34) * (model.pr33+model.pr35) - 1.549429*(model.pi34) * (model.pi33+model.pi35) + 
    (-62.0*model.u33+0.0*model.u34+62.0*model.u35) * (model.pr34*model.pr34+model.pi34*model.pi34) + 650.0*(model.u33-model.u34) * 
    (model.u33-model.u34) - 1.549429*(model.pr35) * (model.pr34+model.pr36) - 1.549429*(model.pi35) * (model.pi34+model.pi36) + 
    (-62.0*model.u34+0.0*model.u35+62.0*model.u36) * (model.pr35*model.pr35+model.pi35*model.pi35) + 650.0*(model.u34-model.u35) * 
    (model.u34-model.u35) - 1.549429*(model.pr36) * (model.pr35+model.pr37) - 1.549429*(model.pi36) * (model.pi35+model.pi37) + 
    (-62.0*model.u35+0.0*model.u36+62.0*model.u37) * (model.pr36*model.pr36+model.pi36*model.pi36) + 650.0*(model.u35-model.u36) * 
    (model.u35-model.u36) - 1.549429*(model.pr37) * (model.pr36+model.pr38) - 1.549429*(model.pi37) * (model.pi36+model.pi38) + 
    (-62.0*model.u36+0.0*model.u37+62.0*model.u38) * (model.pr37*model.pr37+model.pi37*model.pi37) + 650.0*(model.u36-model.u37) * 
    (model.u36-model.u37) - 1.549429*(model.pr38) * (model.pr37+model.pr39) - 1.549429*(model.pi38) * (model.pi37+model.pi39) + 
    (-62.0*model.u37+0.0*model.u38+62.0*model.u39) * (model.pr38*model.pr38+model.pi38*model.pi38) + 650.0*(model.u37-model.u38) * 
    (model.u37-model.u38) - 1.549429*(model.pr39) * (model.pr38+model.pr40) - 1.549429*(model.pi39) * (model.pi38+model.pi40) + 
    (-62.0*model.u38+0.0*model.u39+62.0*model.u40) * (model.pr39*model.pr39+model.pi39*model.pi39) + 650.0*(model.u38-model.u39) * 
    (model.u38-model.u39) - 1.549429*(model.pr40) * (model.pr39+model.pr41) - 1.549429*(model.pi40) * (model.pi39+model.pi41) + 
    (-62.0*model.u39+0.0*model.u40+62.0*model.u41) * (model.pr40*model.pr40+model.pi40*model.pi40) + 650.0*(model.u39-model.u40) * 
    (model.u39-model.u40) - 1.549429*(model.pr41) * (model.pr40+model.pr42) - 1.549429*(model.pi41) * (model.pi40+model.pi42) + 
    (-62.0*model.u40+0.0*model.u41+62.0*model.u42) * (model.pr41*model.pr41+model.pi41*model.pi41) + 650.0*(model.u40-model.u41) * 
    (model.u40-model.u41) - 1.549429*(model.pr42) * (model.pr41+model.pr43) - 1.549429*(model.pi42) * (model.pi41+model.pi43) + 
    (-62.0*model.u41+0.0*model.u42+62.0*model.u43) * (model.pr42*model.pr42+model.pi42*model.pi42) + 650.0*(model.u41-model.u42) * 
    (model.u41-model.u42) - 1.549429*(model.pr43) * (model.pr42+model.pr44) - 1.549429*(model.pi43) * (model.pi42+model.pi44) + 
    (-62.0*model.u42+0.0*model.u43+62.0*model.u44) * (model.pr43*model.pr43+model.pi43*model.pi43) + 650.0*(model.u42-model.u43) * 
    (model.u42-model.u43) - 1.549429*(model.pr44) * (model.pr43+model.pr45) - 1.549429*(model.pi44) * (model.pi43+model.pi45) + 
    (-62.0*model.u43+0.0*model.u44+62.0*model.u45) * (model.pr44*model.pr44+model.pi44*model.pi44) + 650.0*(model.u43-model.u44) * 
    (model.u43-model.u44) - 1.549429*(model.pr45) * (model.pr44+model.pr46) - 1.549429*(model.pi45) * (model.pi44+model.pi46) + 
    (-62.0*model.u44+0.0*model.u45+62.0*model.u46) * (model.pr45*model.pr45+model.pi45*model.pi45) + 650.0*(model.u44-model.u45) * 
    (model.u44-model.u45) - 1.549429*(model.pr46) * (model.pr45+model.pr47) - 1.549429*(model.pi46) * (model.pi45+model.pi47) + 
    (-62.0*model.u45+0.0*model.u46+62.0*model.u47) * (model.pr46*model.pr46+model.pi46*model.pi46) + 650.0*(model.u45-model.u46) * 
    (model.u45-model.u46) - 1.549429*(model.pr47) * (model.pr46+model.pr48) - 1.549429*(model.pi47) * (model.pi46+model.pi48) + 
    (-62.0*model.u46+0.0*model.u47+62.0*model.u48) * (model.pr47*model.pr47+model.pi47*model.pi47) + 650.0*(model.u46-model.u47) * 
    (model.u46-model.u47) - 1.549429*(model.pr48) * (model.pr47+model.pr49) - 1.549429*(model.pi48) * (model.pi47+model.pi49) + 
    (-62.0*model.u47+0.0*model.u48+62.0*model.u49) * (model.pr48*model.pr48+model.pi48*model.pi48) + 650.0*(model.u47-model.u48) * 
    (model.u47-model.u48) - 1.549429*(model.pr49) * (model.pr48+model.pr50) - 1.549429*(model.pi49) * (model.pi48+model.pi50) + 
    (-62.0*model.u48+0.0*model.u49+62.0*model.u50) * (model.pr49*model.pr49+model.pi49*model.pi49) + 650.0*(model.u48-model.u49) * 
    (model.u48-model.u49) - 1.549429*(model.pr50) * (model.pr49+model.pr51) - 1.549429*(model.pi50) * (model.pi49+model.pi51) + 
    (-62.0*model.u49+0.0*model.u50+62.0*model.u51) * (model.pr50*model.pr50+model.pi50*model.pi50) + 650.0*(model.u49-model.u50) * 
    (model.u49-model.u50) - 1.549429*(model.pr51) * (model.pr50+model.pr52) - 1.549429*(model.pi51) * (model.pi50+model.pi52) + 
    (-62.0*model.u50+0.0*model.u51+62.0*model.u52) * (model.pr51*model.pr51+model.pi51*model.pi51) + 650.0*(model.u50-model.u51) * 
    (model.u50-model.u51) - 1.549429*(model.pr52) * (model.pr51+model.pr53) - 1.549429*(model.pi52) * (model.pi51+model.pi53) + 
    (-62.0*model.u51+0.0*model.u52+62.0*model.u53) * (model.pr52*model.pr52+model.pi52*model.pi52) + 650.0*(model.u51-model.u52) * 
    (model.u51-model.u52) - 1.549429*(model.pr53) * (model.pr52+model.pr54) - 1.549429*(model.pi53) * (model.pi52+model.pi54) + 
    (-62.0*model.u52+0.0*model.u53+62.0*model.u54) * (model.pr53*model.pr53+model.pi53*model.pi53) + 650.0*(model.u52-model.u53) * 
    (model.u52-model.u53) - 1.549429*(model.pr54) * (model.pr53+model.pr55) - 1.549429*(model.pi54) * (model.pi53+model.pi55) + 
    (-62.0*model.u53+0.0*model.u54+62.0*model.u55) * (model.pr54*model.pr54+model.pi54*model.pi54) + 650.0*(model.u53-model.u54) * 
    (model.u53-model.u54) - 1.549429*(model.pr55) * (model.pr54+model.pr56) - 1.549429*(model.pi55) * (model.pi54+model.pi56) + 
    (-62.0*model.u54+0.0*model.u55+62.0*model.u56) * (model.pr55*model.pr55+model.pi55*model.pi55) + 650.0*(model.u54-model.u55) * 
    (model.u54-model.u55) - 1.549429*(model.pr56) * (model.pr55+model.pr57) - 1.549429*(model.pi56) * (model.pi55+model.pi57) + 
    (-62.0*model.u55+0.0*model.u56+62.0*model.u57) * (model.pr56*model.pr56+model.pi56*model.pi56) + 650.0*(model.u55-model.u56) * 
    (model.u55-model.u56) - 1.549429*(model.pr57) * (model.pr56+model.pr58) - 1.549429*(model.pi57) * (model.pi56+model.pi58) + 
    (-62.0*model.u56+0.0*model.u57+62.0*model.u58) * (model.pr57*model.pr57+model.pi57*model.pi57) + 650.0*(model.u56-model.u57) * 
    (model.u56-model.u57) - 1.549429*(model.pr58) * (model.pr57+model.pr59) - 1.549429*(model.pi58) * (model.pi57+model.pi59) + 
    (-62.0*model.u57+0.0*model.u58+62.0*model.u59) * (model.pr58*model.pr58+model.pi58*model.pi58) + 650.0*(model.u57-model.u58) * 
    (model.u57-model.u58) - 1.549429*(model.pr59) * (model.pr58+model.pr60) - 1.549429*(model.pi59) * (model.pi58+model.pi60) + 
    (-62.0*model.u58+0.0*model.u59+62.0*model.u60) * (model.pr59*model.pr59+model.pi59*model.pi59) + 650.0*(model.u58-model.u59) * 
    (model.u58-model.u59) - 1.549429*(model.pr60) * (model.pr59+model.pr61) - 1.549429*(model.pi60) * (model.pi59+model.pi61) + 
    (-62.0*model.u59+0.0*model.u60+62.0*model.u61) * (model.pr60*model.pr60+model.pi60*model.pi60) + 650.0*(model.u59-model.u60) * 
    (model.u59-model.u60) - 1.549429*(model.pr61) * (model.pr60+model.pr62) - 1.549429*(model.pi61) * (model.pi60+model.pi62) + 
    (-62.0*model.u60+0.0*model.u61+62.0*model.u62) * (model.pr61*model.pr61+model.pi61*model.pi61) + 650.0*(model.u60-model.u61) * 
    (model.u60-model.u61) - 1.549429*(model.pr62) * (model.pr61+model.pr63) - 1.549429*(model.pi62) * (model.pi61+model.pi63) + 
    (-62.0*model.u61+0.0*model.u62+62.0*model.u63) * (model.pr62*model.pr62+model.pi62*model.pi62) + 650.0*(model.u61-model.u62) * 
    (model.u61-model.u62) - 1.549429*(model.pr63) * (model.pr62+model.pr64) - 1.549429*(model.pi63) * (model.pi62+model.pi64) + 
    (-62.0*model.u62+0.0*model.u63+62.0*model.u64) * (model.pr63*model.pr63+model.pi63*model.pi63) + 650.0*(model.u62-model.u63) * 
    (model.u62-model.u63) - 1.549429*(model.pr64) * (model.pr63+model.pr65) - 1.549429*(model.pi64) * (model.pi63+model.pi65) + 
    (-62.0*model.u63+0.0*model.u64+62.0*model.u65) * (model.pr64*model.pr64+model.pi64*model.pi64) + 650.0*(model.u63-model.u64) * 
    (model.u63-model.u64) - 1.549429*(model.pr65) * (model.pr64+model.pr66) - 1.549429*(model.pi65) * (model.pi64+model.pi66) + 
    (-62.0*model.u64+0.0*model.u65+62.0*model.u66) * (model.pr65*model.pr65+model.pi65*model.pi65) + 650.0*(model.u64-model.u65) * 
    (model.u64-model.u65) - 1.549429*(model.pr66) * (model.pr65+model.pr67) - 1.549429*(model.pi66) * (model.pi65+model.pi67) + 
    (-62.0*model.u65+0.0*model.u66+62.0*model.u67) * (model.pr66*model.pr66+model.pi66*model.pi66) + 650.0*(model.u65-model.u66) * 
    (model.u65-model.u66) - 1.549429*(model.pr67) * (model.pr66+model.pr68) - 1.549429*(model.pi67) * (model.pi66+model.pi68) + 
    (-62.0*model.u66+0.0*model.u67+62.0*model.u68) * (model.pr67*model.pr67+model.pi67*model.pi67) + 650.0*(model.u66-model.u67) * 
    (model.u66-model.u67) - 1.549429*(model.pr68) * (model.pr67+model.pr69) - 1.549429*(model.pi68) * (model.pi67+model.pi69) + 
    (-62.0*model.u67+0.0*model.u68+62.0*model.u69) * (model.pr68*model.pr68+model.pi68*model.pi68) + 650.0*(model.u67-model.u68) * 
    (model.u67-model.u68) - 1.549429*(model.pr69) * (model.pr68+model.pr70) - 1.549429*(model.pi69) * (model.pi68+model.pi70) + 
    (-62.0*model.u68+0.0*model.u69+62.0*model.u70) * (model.pr69*model.pr69+model.pi69*model.pi69) + 650.0*(model.u68-model.u69) * 
    (model.u68-model.u69) - 1.549429*(model.pr70) * (model.pr69+model.pr71) - 1.549429*(model.pi70) * (model.pi69+model.pi71) + 
    (-62.0*model.u69+0.0*model.u70+62.0*model.u71) * (model.pr70*model.pr70+model.pi70*model.pi70) + 650.0*(model.u69-model.u70) * 
    (model.u69-model.u70) - 1.549429*(model.pr71) * (model.pr70+model.pr72) - 1.549429*(model.pi71) * (model.pi70+model.pi72) + 
    (-62.0*model.u70+0.0*model.u71+62.0*model.u72) * (model.pr71*model.pr71+model.pi71*model.pi71) + 650.0*(model.u70-model.u71) * 
    (model.u70-model.u71) - 1.549429*(model.pr72) * (model.pr71+model.pr73) - 1.549429*(model.pi72) * (model.pi71+model.pi73) + 
    (-62.0*model.u71+0.0*model.u72+62.0*model.u73) * (model.pr72*model.pr72+model.pi72*model.pi72) + 650.0*(model.u71-model.u72) * 
    (model.u71-model.u72) - 1.549429*(model.pr73) * (model.pr72+model.pr74) - 1.549429*(model.pi73) * (model.pi72+model.pi74) + 
    (-62.0*model.u72+0.0*model.u73+62.0*model.u74) * (model.pr73*model.pr73+model.pi73*model.pi73) + 650.0*(model.u72-model.u73) * 
    (model.u72-model.u73) - 1.549429*(model.pr74) * (model.pr73+model.pr75) - 1.549429*(model.pi74) * (model.pi73+model.pi75) + 
    (-62.0*model.u73+0.0*model.u74+62.0*model.u75) * (model.pr74*model.pr74+model.pi74*model.pi74) + 650.0*(model.u73-model.u74) * 
    (model.u73-model.u74) - 1.549429*(model.pr75) * (model.pr74+model.pr76) - 1.549429*(model.pi75) * (model.pi74+model.pi76) + 
    (-62.0*model.u74+0.0*model.u75+62.0*model.u76) * (model.pr75*model.pr75+model.pi75*model.pi75) + 650.0*(model.u74-model.u75) * 
    (model.u74-model.u75) - 1.549429*(model.pr76) * (model.pr75+model.pr77) - 1.549429*(model.pi76) * (model.pi75+model.pi77) + 
    (-62.0*model.u75+0.0*model.u76+62.0*model.u77) * (model.pr76*model.pr76+model.pi76*model.pi76) + 650.0*(model.u75-model.u76) * 
    (model.u75-model.u76) - 1.549429*(model.pr77) * (model.pr76+model.pr78) - 1.549429*(model.pi77) * (model.pi76+model.pi78) + 
    (-62.0*model.u76+0.0*model.u77+62.0*model.u78) * (model.pr77*model.pr77+model.pi77*model.pi77) + 650.0*(model.u76-model.u77) * 
    (model.u76-model.u77) - 1.549429*(model.pr78) * (model.pr77+model.pr79) - 1.549429*(model.pi78) * (model.pi77+model.pi79) + 
    (-62.0*model.u77+0.0*model.u78+62.0*model.u79) * (model.pr78*model.pr78+model.pi78*model.pi78) + 650.0*(model.u77-model.u78) * 
    (model.u77-model.u78) - 1.549429*(model.pr79) * (model.pr78+model.pr80) - 1.549429*(model.pi79) * (model.pi78+model.pi80) + 
    (-62.0*model.u78+0.0*model.u79+62.0*model.u80) * (model.pr79*model.pr79+model.pi79*model.pi79) + 650.0*(model.u78-model.u79) * 
    (model.u78-model.u79) - 1.549429*(model.pr80) * (model.pr79+model.pr81) - 1.549429*(model.pi80) * (model.pi79+model.pi81) + 
    (-62.0*model.u79+0.0*model.u80+62.0*model.u81) * (model.pr80*model.pr80+model.pi80*model.pi80) + 650.0*(model.u79-model.u80) * 
    (model.u79-model.u80) - 1.549429*(model.pr81) * (model.pr80+model.pr82) - 1.549429*(model.pi81) * (model.pi80+model.pi82) + 
    (-62.0*model.u80+0.0*model.u81+62.0*model.u82) * (model.pr81*model.pr81+model.pi81*model.pi81) + 650.0*(model.u80-model.u81) * 
    (model.u80-model.u81) - 1.549429*(model.pr82) * (model.pr81+model.pr83) - 1.549429*(model.pi82) * (model.pi81+model.pi83) + 
    (-62.0*model.u81+0.0*model.u82+62.0*model.u83) * (model.pr82*model.pr82+model.pi82*model.pi82) + 650.0*(model.u81-model.u82) * 
    (model.u81-model.u82) - 1.549429*(model.pr83) * (model.pr82+model.pr84) - 1.549429*(model.pi83) * (model.pi82+model.pi84) + 
    (-62.0*model.u82+0.0*model.u83+62.0*model.u84) * (model.pr83*model.pr83+model.pi83*model.pi83) + 650.0*(model.u82-model.u83) * 
    (model.u82-model.u83) - 1.549429*(model.pr84) * (model.pr83+model.pr85) - 1.549429*(model.pi84) * (model.pi83+model.pi85) + 
    (-62.0*model.u83+0.0*model.u84+62.0*model.u85) * (model.pr84*model.pr84+model.pi84*model.pi84) + 650.0*(model.u83-model.u84) * 
    (model.u83-model.u84) - 1.549429*(model.pr85) * (model.pr84+model.pr86) - 1.549429*(model.pi85) * (model.pi84+model.pi86) + 
    (-62.0*model.u84+0.0*model.u85+62.0*model.u86) * (model.pr85*model.pr85+model.pi85*model.pi85) + 650.0*(model.u84-model.u85) * 
    (model.u84-model.u85) - 1.549429*(model.pr86) * (model.pr85+model.pr87) - 1.549429*(model.pi86) * (model.pi85+model.pi87) + 
    (-62.0*model.u85+0.0*model.u86+62.0*model.u87) * (model.pr86*model.pr86+model.pi86*model.pi86) + 650.0*(model.u85-model.u86) * 
    (model.u85-model.u86) - 1.549429*(model.pr87) * (model.pr86+model.pr88) - 1.549429*(model.pi87) * (model.pi86+model.pi88) + 
    (-62.0*model.u86+0.0*model.u87+62.0*model.u88) * (model.pr87*model.pr87+model.pi87*model.pi87) + 650.0*(model.u86-model.u87) * 
    (model.u86-model.u87) - 1.549429*(model.pr88) * (model.pr87+model.pr89) - 1.549429*(model.pi88) * (model.pi87+model.pi89) + 
    (-62.0*model.u87+0.0*model.u88+62.0*model.u89) * (model.pr88*model.pr88+model.pi88*model.pi88) + 650.0*(model.u87-model.u88) * 
    (model.u87-model.u88) - 1.549429*(model.pr89) * (model.pr88+model.pr90) - 1.549429*(model.pi89) * (model.pi88+model.pi90) + 
    (-62.0*model.u88+0.0*model.u89+62.0*model.u90) * (model.pr89*model.pr89+model.pi89*model.pi89) + 650.0*(model.u88-model.u89) * 
    (model.u88-model.u89) - 1.549429*(model.pr90) * (model.pr89+model.pr91) - 1.549429*(model.pi90) * (model.pi89+model.pi91) + 
    (-62.0*model.u89+0.0*model.u90+62.0*model.u91) * (model.pr90*model.pr90+model.pi90*model.pi90) + 650.0*(model.u89-model.u90) * 
    (model.u89-model.u90) - 1.549429*(model.pr91) * (model.pr90+model.pr92) - 1.549429*(model.pi91) * (model.pi90+model.pi92) + 
    (-62.0*model.u90+0.0*model.u91+62.0*model.u92) * (model.pr91*model.pr91+model.pi91*model.pi91) + 650.0*(model.u90-model.u91) * 
    (model.u90-model.u91) - 1.549429*(model.pr92) * (model.pr91+model.pr93) - 1.549429*(model.pi92) * (model.pi91+model.pi93) + 
    (-62.0*model.u91+0.0*model.u92+62.0*model.u93) * (model.pr92*model.pr92+model.pi92*model.pi92) + 650.0*(model.u91-model.u92) * 
    (model.u91-model.u92) - 1.549429*(model.pr93) * (model.pr92+model.pr94) - 1.549429*(model.pi93) * (model.pi92+model.pi94) + 
    (-62.0*model.u92+0.0*model.u93+62.0*model.u94) * (model.pr93*model.pr93+model.pi93*model.pi93) + 650.0*(model.u92-model.u93) * 
    (model.u92-model.u93) - 1.549429*(model.pr94) * (model.pr93+model.pr95) - 1.549429*(model.pi94) * (model.pi93+model.pi95) + 
    (-62.0*model.u93+0.0*model.u94+62.0*model.u95) * (model.pr94*model.pr94+model.pi94*model.pi94) + 650.0*(model.u93-model.u94) * 
    (model.u93-model.u94) - 1.549429*(model.pr95) * (model.pr94+model.pr96) - 1.549429*(model.pi95) * (model.pi94+model.pi96) + 
    (-62.0*model.u94+0.0*model.u95+62.0*model.u96) * (model.pr95*model.pr95+model.pi95*model.pi95) + 650.0*(model.u94-model.u95) * 
    (model.u94-model.u95) - 1.549429*(model.pr96) * (model.pr95+model.pr97) - 1.549429*(model.pi96) * (model.pi95+model.pi97) + 
    (-62.0*model.u95+0.0*model.u96+62.0*model.u97) * (model.pr96*model.pr96+model.pi96*model.pi96) + 650.0*(model.u95-model.u96) * 
    (model.u95-model.u96) - 1.549429*(model.pr97) * (model.pr96+model.pr98) - 1.549429*(model.pi97) * (model.pi96+model.pi98) + 
    (-62.0*model.u96+0.0*model.u97+62.0*model.u98) * (model.pr97*model.pr97+model.pi97*model.pi97) + 650.0*(model.u96-model.u97) * 
    (model.u96-model.u97) - 1.549429*(model.pr98) * (model.pr97+model.pr99) - 1.549429*(model.pi98) * (model.pi97+model.pi99) + 
    (-62.0*model.u97+0.0*model.u98+62.0*model.u99) * (model.pr98*model.pr98+model.pi98*model.pi98) + 650.0*(model.u97-model.u98) * 
    (model.u97-model.u98) - 1.549429*(model.pr99) * (model.pr98+model.pr100) - 1.549429*(model.pi99) * (model.pi98+model.pi100) + 
    (-62.0*model.u98+0.0*model.u99+62.0*model.u100) * (model.pr99*model.pr99+model.pi99*model.pi99) + 650.0*(model.u98-model.u99) * 
    (model.u98-model.u99) - 1.549429*(model.pr100) * (model.pr99+model.pr101) - 1.549429*(model.pi100) * (model.pi99+model.pi101) + 
    (-62.0*model.u99+0.0*model.u100+62.0*model.u101) * (model.pr100*model.pr100+model.pi100*model.pi100) + 650.0*(model.u99-model.u100) * 
    (model.u99-model.u100) - 1.549429*(model.pr101) * (model.pr100+model.pr102) - 1.549429*(model.pi101) * 
    (model.pi100+model.pi102) + (-62.0*model.u100+0.0*model.u101+62.0*model.u102) * (model.pr101*model.pr101+model.pi101*model.pi101) + 
    650.0*(model.u100-model.u101) * (model.u100-model.u101) - 1.549429*(model.pr102) * (model.pr101+model.pr103) - 
    1.549429*(model.pi102) * (model.pi101+model.pi103) + (-62.0*model.u101+0.0*model.u102+62.0*model.u103) * 
    (model.pr102*model.pr102+model.pi102*model.pi102) + 650.0*(model.u101-model.u102) * (model.u101-model.u102) - 1.549429*(model.pr103) 
    * (model.pr102+model.pr104) - 1.549429*(model.pi103) * (model.pi102+model.pi104) + 
    (-62.0*model.u102+0.0*model.u103+62.0*model.u104) * (model.pr103*model.pr103+model.pi103*model.pi103) + 650.0*(model.u102-model.u103) 
    * (model.u102-model.u103) - 1.549429*(model.pr104) * (model.pr103+model.pr105) - 1.549429*(model.pi104) * 
    (model.pi103+model.pi105) + (-62.0*model.u103+0.0*model.u104+62.0*model.u105) * (model.pr104*model.pr104+model.pi104*model.pi104) + 
    650.0*(model.u103-model.u104) * (model.u103-model.u104) - 1.549429*(model.pr105) * (model.pr104+model.pr106) - 
    1.549429*(model.pi105) * (model.pi104+model.pi106) + (-62.0*model.u104+0.0*model.u105+62.0*model.u106) * 
    (model.pr105*model.pr105+model.pi105*model.pi105) + 650.0*(model.u104-model.u105) * (model.u104-model.u105) - 1.549429*(model.pr106) 
    * (model.pr105+model.pr107) - 1.549429*(model.pi106) * (model.pi105+model.pi107) + 
    (-62.0*model.u105+0.0*model.u106+62.0*model.u107) * (model.pr106*model.pr106+model.pi106*model.pi106) + 650.0*(model.u105-model.u106) 
    * (model.u105-model.u106) - 1.549429*(model.pr107) * (model.pr106+model.pr108) - 1.549429*(model.pi107) * 
    (model.pi106+model.pi108) + (-62.0*model.u106+0.0*model.u107+62.0*model.u108) * (model.pr107*model.pr107+model.pi107*model.pi107) + 
    650.0*(model.u106-model.u107) * (model.u106-model.u107) - 1.549429*(model.pr108) * (model.pr107+model.pr109) - 
    1.549429*(model.pi108) * (model.pi107+model.pi109) + (-62.0*model.u107+0.0*model.u108+62.0*model.u109) * 
    (model.pr108*model.pr108+model.pi108*model.pi108) + 650.0*(model.u107-model.u108) * (model.u107-model.u108) - 1.549429*(model.pr109) 
    * (model.pr108+model.pr110) - 1.549429*(model.pi109) * (model.pi108+model.pi110) + 
    (-62.0*model.u108+0.0*model.u109+62.0*model.u110) * (model.pr109*model.pr109+model.pi109*model.pi109) + 650.0*(model.u108-model.u109) 
    * (model.u108-model.u109) - 1.549429*(model.pr110) * (model.pr109+model.pr111) - 1.549429*(model.pi110) * 
    (model.pi109+model.pi111) + (-62.0*model.u109+0.0*model.u110+62.0*model.u111) * (model.pr110*model.pr110+model.pi110*model.pi110) + 
    650.0*(model.u109-model.u110) * (model.u109-model.u110) - 1.549429*(model.pr111) * (model.pr110+model.pr112) - 
    1.549429*(model.pi111) * (model.pi110+model.pi112) + (-62.0*model.u110+0.0*model.u111+62.0*model.u112) * 
    (model.pr111*model.pr111+model.pi111*model.pi111) + 650.0*(model.u110-model.u111) * (model.u110-model.u111) - 1.549429*(model.pr112) 
    * (model.pr111+model.pr113) - 1.549429*(model.pi112) * (model.pi111+model.pi113) + 
    (-62.0*model.u111+0.0*model.u112+62.0*model.u113) * (model.pr112*model.pr112+model.pi112*model.pi112) + 650.0*(model.u111-model.u112) 
    * (model.u111-model.u112) - 1.549429*(model.pr113) * (model.pr112+model.pr114) - 1.549429*(model.pi113) * 
    (model.pi112+model.pi114) + (-62.0*model.u112+0.0*model.u113+62.0*model.u114) * (model.pr113*model.pr113+model.pi113*model.pi113) + 
    650.0*(model.u112-model.u113) * (model.u112-model.u113) - 1.549429*(model.pr114) * (model.pr113+model.pr115) - 
    1.549429*(model.pi114) * (model.pi113+model.pi115) + (-62.0*model.u113+0.0*model.u114+62.0*model.u115) * 
    (model.pr114*model.pr114+model.pi114*model.pi114) + 650.0*(model.u113-model.u114) * (model.u113-model.u114) - 1.549429*(model.pr115) 
    * (model.pr114+model.pr116) - 1.549429*(model.pi115) * (model.pi114+model.pi116) + 
    (-62.0*model.u114+0.0*model.u115+62.0*model.u116) * (model.pr115*model.pr115+model.pi115*model.pi115) + 650.0*(model.u114-model.u115) 
    * (model.u114-model.u115) - 1.549429*(model.pr116) * (model.pr115+model.pr117) - 1.549429*(model.pi116) * 
    (model.pi115+model.pi117) + (-62.0*model.u115+0.0*model.u116+62.0*model.u117) * (model.pr116*model.pr116+model.pi116*model.pi116) + 
    650.0*(model.u115-model.u116) * (model.u115-model.u116) - 1.549429*(model.pr117) * (model.pr116+model.pr118) - 
    1.549429*(model.pi117) * (model.pi116+model.pi118) + (-62.0*model.u116+0.0*model.u117+62.0*model.u118) * 
    (model.pr117*model.pr117+model.pi117*model.pi117) + 650.0*(model.u116-model.u117) * (model.u116-model.u117) - 1.549429*(model.pr118) 
    * (model.pr117+model.pr119) - 1.549429*(model.pi118) * (model.pi117+model.pi119) + 
    (-62.0*model.u117+0.0*model.u118+62.0*model.u119) * (model.pr118*model.pr118+model.pi118*model.pi118) + 650.0*(model.u117-model.u118) 
    * (model.u117-model.u118) - 1.549429*(model.pr119) * (model.pr118+model.pr120) - 1.549429*(model.pi119) * 
    (model.pi118+model.pi120) + (-62.0*model.u118+0.0*model.u119+62.0*model.u120) * (model.pr119*model.pr119+model.pi119*model.pi119) + 
    650.0*(model.u118-model.u119) * (model.u118-model.u119) - 1.549429*(model.pr120) * (model.pr119+model.pr121) - 
    1.549429*(model.pi120) * (model.pi119+model.pi121) + (-62.0*model.u119+0.0*model.u120+62.0*model.u121) * 
    (model.pr120*model.pr120+model.pi120*model.pi120) + 650.0*(model.u119-model.u120) * (model.u119-model.u120) - 1.549429*(model.pr121) 
    * (model.pr120+model.pr122) - 1.549429*(model.pi121) * (model.pi120+model.pi122) + 
    (-62.0*model.u120+0.0*model.u121+62.0*model.u122) * (model.pr121*model.pr121+model.pi121*model.pi121) + 650.0*(model.u120-model.u121) 
    * (model.u120-model.u121) - 1.549429*(model.pr122) * (model.pr121+model.pr123) - 1.549429*(model.pi122) * 
    (model.pi121+model.pi123) + (-62.0*model.u121+0.0*model.u122+62.0*model.u123) * (model.pr122*model.pr122+model.pi122*model.pi122) + 
    650.0*(model.u121-model.u122) * (model.u121-model.u122) - 1.549429*(model.pr123) * (model.pr122+model.pr124) - 
    1.549429*(model.pi123) * (model.pi122+model.pi124) + (-62.0*model.u122+0.0*model.u123+62.0*model.u124) * 
    (model.pr123*model.pr123+model.pi123*model.pi123) + 650.0*(model.u122-model.u123) * (model.u122-model.u123) - 1.549429*(model.pr124) 
    * (model.pr123+model.pr125) - 1.549429*(model.pi124) * (model.pi123+model.pi125) + 
    (-62.0*model.u123+0.0*model.u124+62.0*model.u125) * (model.pr124*model.pr124+model.pi124*model.pi124) + 650.0*(model.u123-model.u124) 
    * (model.u123-model.u124) - 1.549429*(model.pr125) * (model.pr124+model.pr126) - 1.549429*(model.pi125) * 
    (model.pi124+model.pi126) + (-62.0*model.u124+0.0*model.u125+62.0*model.u126) * (model.pr125*model.pr125+model.pi125*model.pi125) + 
    650.0*(model.u124-model.u125) * (model.u124-model.u125) - 1.549429*(model.pr126) * (model.pr125+model.pr127) - 
    1.549429*(model.pi126) * (model.pi125+model.pi127) + (-62.0*model.u125+0.0*model.u126+62.0*model.u127) * 
    (model.pr126*model.pr126+model.pi126*model.pi126) + 650.0*(model.u125-model.u126) * (model.u125-model.u126) - 1.549429*(model.pr127) 
    * (model.pr126+model.pr128) - 1.549429*(model.pi127) * (model.pi126+model.pi128) + 
    (-62.0*model.u126+0.0*model.u127+62.0*model.u128) * (model.pr127*model.pr127+model.pi127*model.pi127) + 650.0*(model.u126-model.u127) 
    * (model.u126-model.u127) - 1.549429*(model.pr128) * (model.pr127+model.pr129) - 1.549429*(model.pi128) * 
    (model.pi127+model.pi129) + (-62.0*model.u127+0.0*model.u128+62.0*model.u129) * (model.pr128*model.pr128+model.pi128*model.pi128) + 
    650.0*(model.u127-model.u128) * (model.u127-model.u128) - 1.549429*(model.pr129) * (model.pr128+model.pr130) - 
    1.549429*(model.pi129) * (model.pi128+model.pi130) + (-62.0*model.u128+0.0*model.u129+62.0*model.u130) * 
    (model.pr129*model.pr129+model.pi129*model.pi129) + 650.0*(model.u128-model.u129) * (model.u128-model.u129) - 1.549429*(model.pr130) 
    * (model.pr129+model.pr131) - 1.549429*(model.pi130) * (model.pi129+model.pi131) + 
    (-62.0*model.u129+0.0*model.u130+62.0*model.u131) * (model.pr130*model.pr130+model.pi130*model.pi130) + 650.0*(model.u129-model.u130) 
    * (model.u129-model.u130) - 1.549429*(model.pr131) * (model.pr130+model.pr132) - 1.549429*(model.pi131) * 
    (model.pi130+model.pi132) + (-62.0*model.u130+0.0*model.u131+62.0*model.u132) * (model.pr131*model.pr131+model.pi131*model.pi131) + 
    650.0*(model.u130-model.u131) * (model.u130-model.u131) - 1.549429*(model.pr132) * (model.pr131+model.pr133) - 
    1.549429*(model.pi132) * (model.pi131+model.pi133) + (-62.0*model.u131+0.0*model.u132+62.0*model.u133) * 
    (model.pr132*model.pr132+model.pi132*model.pi132) + 650.0*(model.u131-model.u132) * (model.u131-model.u132) - 1.549429*(model.pr133) 
    * (model.pr132+model.pr134) - 1.549429*(model.pi133) * (model.pi132+model.pi134) + 
    (-62.0*model.u132+0.0*model.u133+62.0*model.u134) * (model.pr133*model.pr133+model.pi133*model.pi133) + 650.0*(model.u132-model.u133) 
    * (model.u132-model.u133) - 1.549429*(model.pr134) * (model.pr133+model.pr135) - 1.549429*(model.pi134) * 
    (model.pi133+model.pi135) + (-62.0*model.u133+0.0*model.u134+62.0*model.u135) * (model.pr134*model.pr134+model.pi134*model.pi134) + 
    650.0*(model.u133-model.u134) * (model.u133-model.u134) - 1.549429*(model.pr135) * (model.pr134+model.pr136) - 
    1.549429*(model.pi135) * (model.pi134+model.pi136) + (-62.0*model.u134+0.0*model.u135+62.0*model.u136) * 
    (model.pr135*model.pr135+model.pi135*model.pi135) + 650.0*(model.u134-model.u135) * (model.u134-model.u135) - 1.549429*(model.pr136) 
    * (model.pr135+model.pr137) - 1.549429*(model.pi136) * (model.pi135+model.pi137) + 
    (-62.0*model.u135+0.0*model.u136+62.0*model.u137) * (model.pr136*model.pr136+model.pi136*model.pi136) + 650.0*(model.u135-model.u136) 
    * (model.u135-model.u136) - 1.549429*(model.pr137) * (model.pr136+model.pr138) - 1.549429*(model.pi137) * 
    (model.pi136+model.pi138) + (-62.0*model.u136+0.0*model.u137+62.0*model.u138) * (model.pr137*model.pr137+model.pi137*model.pi137) + 
    650.0*(model.u136-model.u137) * (model.u136-model.u137) - 1.549429*(model.pr138) * (model.pr137+model.pr139) - 
    1.549429*(model.pi138) * (model.pi137+model.pi139) + (-62.0*model.u137+0.0*model.u138+62.0*model.u139) * 
    (model.pr138*model.pr138+model.pi138*model.pi138) + 650.0*(model.u137-model.u138) * (model.u137-model.u138) - 1.549429*(model.pr139) 
    * (model.pr138+model.pr140) - 1.549429*(model.pi139) * (model.pi138+model.pi140) + 
    (-62.0*model.u138+0.0*model.u139+62.0*model.u140) * (model.pr139*model.pr139+model.pi139*model.pi139) + 650.0*(model.u138-model.u139) 
    * (model.u138-model.u139) - 1.549429*(model.pr140) * (model.pr139+model.pr141) - 1.549429*(model.pi140) * 
    (model.pi139+model.pi141) + (-62.0*model.u139+0.0*model.u140+62.0*model.u141) * (model.pr140*model.pr140+model.pi140*model.pi140) + 
    650.0*(model.u139-model.u140) * (model.u139-model.u140) - 1.549429*(model.pr141) * (model.pr140+model.pr142) - 
    1.549429*(model.pi141) * (model.pi140+model.pi142) + (-62.0*model.u140+0.0*model.u141+62.0*model.u142) * 
    (model.pr141*model.pr141+model.pi141*model.pi141) + 650.0*(model.u140-model.u141) * (model.u140-model.u141) - 1.549429*(model.pr142) 
    * (model.pr141+model.pr143) - 1.549429*(model.pi142) * (model.pi141+model.pi143) + 
    (-62.0*model.u141+0.0*model.u142+62.0*model.u143) * (model.pr142*model.pr142+model.pi142*model.pi142) + 650.0*(model.u141-model.u142) 
    * (model.u141-model.u142) - 1.549429*(model.pr143) * (model.pr142+model.pr144) - 1.549429*(model.pi143) * 
    (model.pi142+model.pi144) + (-62.0*model.u142+0.0*model.u143+62.0*model.u144) * (model.pr143*model.pr143+model.pi143*model.pi143) + 
    650.0*(model.u142-model.u143) * (model.u142-model.u143) - 1.549429*(model.pr144) * (model.pr143+model.pr145) - 
    1.549429*(model.pi144) * (model.pi143+model.pi145) + (-62.0*model.u143+0.0*model.u144+62.0*model.u145) * 
    (model.pr144*model.pr144+model.pi144*model.pi144) + 650.0*(model.u143-model.u144) * (model.u143-model.u144) - 1.549429*(model.pr145) 
    * (model.pr144+model.pr146) - 1.549429*(model.pi145) * (model.pi144+model.pi146) + 
    (-62.0*model.u144+0.0*model.u145+62.0*model.u146) * (model.pr145*model.pr145+model.pi145*model.pi145) + 650.0*(model.u144-model.u145) 
    * (model.u144-model.u145) - 1.549429*(model.pr146) * (model.pr145+model.pr147) - 1.549429*(model.pi146) * 
    (model.pi145+model.pi147) + (-62.0*model.u145+0.0*model.u146+62.0*model.u147) * (model.pr146*model.pr146+model.pi146*model.pi146) + 
    650.0*(model.u145-model.u146) * (model.u145-model.u146) - 1.549429*(model.pr147) * (model.pr146+model.pr148) - 
    1.549429*(model.pi147) * (model.pi146+model.pi148) + (-62.0*model.u146+0.0*model.u147+62.0*model.u148) * 
    (model.pr147*model.pr147+model.pi147*model.pi147) + 650.0*(model.u146-model.u147) * (model.u146-model.u147) - 1.549429*(model.pr148) 
    * (model.pr147+model.pr149) - 1.549429*(model.pi148) * (model.pi147+model.pi149) + 
    (-62.0*model.u147+0.0*model.u148+62.0*model.u149) * (model.pr148*model.pr148+model.pi148*model.pi148) + 650.0*(model.u147-model.u148) 
    * (model.u147-model.u148) - 1.549429*(model.pr149) * (model.pr148+model.pr150) - 1.549429*(model.pi149) * 
    (model.pi148+model.pi150) + (-62.0*model.u148+0.0*model.u149+62.0*model.u150) * (model.pr149*model.pr149+model.pi149*model.pi149) + 
    650.0*(model.u148-model.u149) * (model.u148-model.u149) - 1.549429*(model.pr150) * (model.pr149+model.pr151) - 
    1.549429*(model.pi150) * (model.pi149+model.pi151) + (-62.0*model.u149+0.0*model.u150+62.0*model.u151) * 
    (model.pr150*model.pr150+model.pi150*model.pi150) + 650.0*(model.u149-model.u150) * (model.u149-model.u150) - 1.549429*(model.pr151) 
    * (model.pr150+model.pr152) - 1.549429*(model.pi151) * (model.pi150+model.pi152) + 
    (-62.0*model.u150+0.0*model.u151+62.0*model.u152) * (model.pr151*model.pr151+model.pi151*model.pi151) + 650.0*(model.u150-model.u151) 
    * (model.u150-model.u151) - 1.549429*(model.pr152) * (model.pr151+model.pr153) - 1.549429*(model.pi152) * 
    (model.pi151+model.pi153) + (-62.0*model.u151+0.0*model.u152+62.0*model.u153) * (model.pr152*model.pr152+model.pi152*model.pi152) + 
    650.0*(model.u151-model.u152) * (model.u151-model.u152) - 1.549429*(model.pr153) * (model.pr152+model.pr154) - 
    1.549429*(model.pi153) * (model.pi152+model.pi154) + (-62.0*model.u152+0.0*model.u153+62.0*model.u154) * 
    (model.pr153*model.pr153+model.pi153*model.pi153) + 650.0*(model.u152-model.u153) * (model.u152-model.u153) - 1.549429*(model.pr154) 
    * (model.pr153+model.pr155) - 1.549429*(model.pi154) * (model.pi153+model.pi155) + 
    (-62.0*model.u153+0.0*model.u154+62.0*model.u155) * (model.pr154*model.pr154+model.pi154*model.pi154) + 650.0*(model.u153-model.u154) 
    * (model.u153-model.u154) - 1.549429*(model.pr155) * (model.pr154+model.pr156) - 1.549429*(model.pi155) * 
    (model.pi154+model.pi156) + (-62.0*model.u154+0.0*model.u155+62.0*model.u156) * (model.pr155*model.pr155+model.pi155*model.pi155) + 
    650.0*(model.u154-model.u155) * (model.u154-model.u155) - 1.549429*(model.pr156) * (model.pr155+model.pr157) - 
    1.549429*(model.pi156) * (model.pi155+model.pi157) + (-62.0*model.u155+0.0*model.u156+62.0*model.u157) * 
    (model.pr156*model.pr156+model.pi156*model.pi156) + 650.0*(model.u155-model.u156) * (model.u155-model.u156) - 1.549429*(model.pr157) 
    * (model.pr156+model.pr158) - 1.549429*(model.pi157) * (model.pi156+model.pi158) + 
    (-62.0*model.u156+0.0*model.u157+62.0*model.u158) * (model.pr157*model.pr157+model.pi157*model.pi157) + 650.0*(model.u156-model.u157) 
    * (model.u156-model.u157) - 1.549429*(model.pr158) * (model.pr157+model.pr159) - 1.549429*(model.pi158) * 
    (model.pi157+model.pi159) + (-62.0*model.u157+0.0*model.u158+62.0*model.u159) * (model.pr158*model.pr158+model.pi158*model.pi158) + 
    650.0*(model.u157-model.u158) * (model.u157-model.u158) - 1.549429*(model.pr159) * (model.pr158+model.pr160) - 
    1.549429*(model.pi159) * (model.pi158+model.pi160) + (-62.0*model.u158+0.0*model.u159+62.0*model.u160) * 
    (model.pr159*model.pr159+model.pi159*model.pi159) + 650.0*(model.u158-model.u159) * (model.u158-model.u159) - 1.549429*(model.pr160) 
    * (model.pr159+model.pr161) - 1.549429*(model.pi160) * (model.pi159+model.pi161) + 
    (-62.0*model.u159+0.0*model.u160+62.0*model.u161) * (model.pr160*model.pr160+model.pi160*model.pi160) + 650.0*(model.u159-model.u160) 
    * (model.u159-model.u160) - 1.549429*(model.pr161) * (model.pr160+model.pr162) - 1.549429*(model.pi161) * 
    (model.pi160+model.pi162) + (-62.0*model.u160+0.0*model.u161+62.0*model.u162) * (model.pr161*model.pr161+model.pi161*model.pi161) + 
    650.0*(model.u160-model.u161) * (model.u160-model.u161) - 1.549429*(model.pr162) * (model.pr161+model.pr163) - 
    1.549429*(model.pi162) * (model.pi161+model.pi163) + (-62.0*model.u161+0.0*model.u162+62.0*model.u163) * 
    (model.pr162*model.pr162+model.pi162*model.pi162) + 650.0*(model.u161-model.u162) * (model.u161-model.u162) - 1.549429*(model.pr163) 
    * (model.pr162+model.pr164) - 1.549429*(model.pi163) * (model.pi162+model.pi164) + 
    (-62.0*model.u162+0.0*model.u163+62.0*model.u164) * (model.pr163*model.pr163+model.pi163*model.pi163) + 650.0*(model.u162-model.u163) 
    * (model.u162-model.u163) - 1.549429*(model.pr164) * (model.pr163+model.pr165) - 1.549429*(model.pi164) * 
    (model.pi163+model.pi165) + (-62.0*model.u163+0.0*model.u164+62.0*model.u165) * (model.pr164*model.pr164+model.pi164*model.pi164) + 
    650.0*(model.u163-model.u164) * (model.u163-model.u164) - 1.549429*(model.pr165) * (model.pr164+model.pr166) - 
    1.549429*(model.pi165) * (model.pi164+model.pi166) + (-62.0*model.u164+0.0*model.u165+62.0*model.u166) * 
    (model.pr165*model.pr165+model.pi165*model.pi165) + 650.0*(model.u164-model.u165) * (model.u164-model.u165) - 1.549429*(model.pr166) 
    * (model.pr165+model.pr167) - 1.549429*(model.pi166) * (model.pi165+model.pi167) + 
    (-62.0*model.u165+0.0*model.u166+62.0*model.u167) * (model.pr166*model.pr166+model.pi166*model.pi166) + 650.0*(model.u165-model.u166) 
    * (model.u165-model.u166) - 1.549429*(model.pr167) * (model.pr166+model.pr168) - 1.549429*(model.pi167) * 
    (model.pi166+model.pi168) + (-62.0*model.u166+0.0*model.u167+62.0*model.u168) * (model.pr167*model.pr167+model.pi167*model.pi167) + 
    650.0*(model.u166-model.u167) * (model.u166-model.u167) - 1.549429*(model.pr168) * (model.pr167+model.pr169) - 
    1.549429*(model.pi168) * (model.pi167+model.pi169) + (-62.0*model.u167+0.0*model.u168+62.0*model.u169) * 
    (model.pr168*model.pr168+model.pi168*model.pi168) + 650.0*(model.u167-model.u168) * (model.u167-model.u168) - 1.549429*(model.pr169) 
    * (model.pr168+model.pr170) - 1.549429*(model.pi169) * (model.pi168+model.pi170) + 
    (-62.0*model.u168+0.0*model.u169+62.0*model.u170) * (model.pr169*model.pr169+model.pi169*model.pi169) + 650.0*(model.u168-model.u169) 
    * (model.u168-model.u169) - 1.549429*(model.pr170) * (model.pr169+model.pr171) - 1.549429*(model.pi170) * 
    (model.pi169+model.pi171) + (-62.0*model.u169+0.0*model.u170+62.0*model.u171) * (model.pr170*model.pr170+model.pi170*model.pi170) + 
    650.0*(model.u169-model.u170) * (model.u169-model.u170) - 1.549429*(model.pr171) * (model.pr170+model.pr172) - 
    1.549429*(model.pi171) * (model.pi170+model.pi172) + (-62.0*model.u170+0.0*model.u171+62.0*model.u172) * 
    (model.pr171*model.pr171+model.pi171*model.pi171) + 650.0*(model.u170-model.u171) * (model.u170-model.u171) - 1.549429*(model.pr172) 
    * (model.pr171+model.pr173) - 1.549429*(model.pi172) * (model.pi171+model.pi173) + 
    (-62.0*model.u171+0.0*model.u172+62.0*model.u173) * (model.pr172*model.pr172+model.pi172*model.pi172) + 650.0*(model.u171-model.u172) 
    * (model.u171-model.u172) - 1.549429*(model.pr173) * (model.pr172+model.pr174) - 1.549429*(model.pi173) * 
    (model.pi172+model.pi174) + (-62.0*model.u172+0.0*model.u173+62.0*model.u174) * (model.pr173*model.pr173+model.pi173*model.pi173) + 
    650.0*(model.u172-model.u173) * (model.u172-model.u173) - 1.549429*(model.pr174) * (model.pr173+model.pr175) - 
    1.549429*(model.pi174) * (model.pi173+model.pi175) + (-62.0*model.u173+0.0*model.u174+62.0*model.u175) * 
    (model.pr174*model.pr174+model.pi174*model.pi174) + 650.0*(model.u173-model.u174) * (model.u173-model.u174) - 1.549429*(model.pr175) 
    * (model.pr174+model.pr176) - 1.549429*(model.pi175) * (model.pi174+model.pi176) + 
    (-62.0*model.u174+0.0*model.u175+62.0*model.u176) * (model.pr175*model.pr175+model.pi175*model.pi175) + 650.0*(model.u174-model.u175) 
    * (model.u174-model.u175) - 1.549429*(model.pr176) * (model.pr175+model.pr177) - 1.549429*(model.pi176) * 
    (model.pi175+model.pi177) + (-62.0*model.u175+0.0*model.u176+62.0*model.u177) * (model.pr176*model.pr176+model.pi176*model.pi176) + 
    650.0*(model.u175-model.u176) * (model.u175-model.u176) - 1.549429*(model.pr177) * (model.pr176+model.pr178) - 
    1.549429*(model.pi177) * (model.pi176+model.pi178) + (-62.0*model.u176+0.0*model.u177+62.0*model.u178) * 
    (model.pr177*model.pr177+model.pi177*model.pi177) + 650.0*(model.u176-model.u177) * (model.u176-model.u177) - 1.549429*(model.pr178) 
    * (model.pr177+model.pr179) - 1.549429*(model.pi178) * (model.pi177+model.pi179) + 
    (-62.0*model.u177+0.0*model.u178+62.0*model.u179) * (model.pr178*model.pr178+model.pi178*model.pi178) + 650.0*(model.u177-model.u178) 
    * (model.u177-model.u178) - 1.549429*(model.pr179) * (model.pr178+model.pr180) - 1.549429*(model.pi179) * 
    (model.pi178+model.pi180) + (-62.0*model.u178+0.0*model.u179+62.0*model.u180) * (model.pr179*model.pr179+model.pi179*model.pi179) + 
    650.0*(model.u178-model.u179) * (model.u178-model.u179) - 1.549429*(model.pr180) * (model.pr179+model.pr181) - 
    1.549429*(model.pi180) * (model.pi179+model.pi181) + (-62.0*model.u179+0.0*model.u180+62.0*model.u181) * 
    (model.pr180*model.pr180+model.pi180*model.pi180) + 650.0*(model.u179-model.u180) * (model.u179-model.u180) - 1.549429*(model.pr181) 
    * (model.pr180+model.pr182) - 1.549429*(model.pi181) * (model.pi180+model.pi182) + 
    (-62.0*model.u180+0.0*model.u181+62.0*model.u182) * (model.pr181*model.pr181+model.pi181*model.pi181) + 650.0*(model.u180-model.u181) 
    * (model.u180-model.u181) - 1.549429*(model.pr182) * (model.pr181+model.pr183) - 1.549429*(model.pi182) * 
    (model.pi181+model.pi183) + (-62.0*model.u181+0.0*model.u182+62.0*model.u183) * (model.pr182*model.pr182+model.pi182*model.pi182) + 
    650.0*(model.u181-model.u182) * (model.u181-model.u182) - 1.549429*(model.pr183) * (model.pr182+model.pr184) - 
    1.549429*(model.pi183) * (model.pi182+model.pi184) + (-62.0*model.u182+0.0*model.u183+62.0*model.u184) * 
    (model.pr183*model.pr183+model.pi183*model.pi183) + 650.0*(model.u182-model.u183) * (model.u182-model.u183) - 1.549429*(model.pr184) 
    * (model.pr183+model.pr185) - 1.549429*(model.pi184) * (model.pi183+model.pi185) + 
    (-62.0*model.u183+0.0*model.u184+62.0*model.u185) * (model.pr184*model.pr184+model.pi184*model.pi184) + 650.0*(model.u183-model.u184) 
    * (model.u183-model.u184) - 1.549429*(model.pr185) * (model.pr184+model.pr186) - 1.549429*(model.pi185) * 
    (model.pi184+model.pi186) + (-62.0*model.u184+0.0*model.u185+62.0*model.u186) * (model.pr185*model.pr185+model.pi185*model.pi185) + 
    650.0*(model.u184-model.u185) * (model.u184-model.u185) - 1.549429*(model.pr186) * (model.pr185+model.pr187) - 
    1.549429*(model.pi186) * (model.pi185+model.pi187) + (-62.0*model.u185+0.0*model.u186+62.0*model.u187) * 
    (model.pr186*model.pr186+model.pi186*model.pi186) + 650.0*(model.u185-model.u186) * (model.u185-model.u186) - 1.549429*(model.pr187) 
    * (model.pr186+model.pr188) - 1.549429*(model.pi187) * (model.pi186+model.pi188) + 
    (-62.0*model.u186+0.0*model.u187+62.0*model.u188) * (model.pr187*model.pr187+model.pi187*model.pi187) + 650.0*(model.u186-model.u187) 
    * (model.u186-model.u187) - 1.549429*(model.pr188) * (model.pr187+model.pr189) - 1.549429*(model.pi188) * 
    (model.pi187+model.pi189) + (-62.0*model.u187+0.0*model.u188+62.0*model.u189) * (model.pr188*model.pr188+model.pi188*model.pi188) + 
    650.0*(model.u187-model.u188) * (model.u187-model.u188) - 1.549429*(model.pr189) * (model.pr188+model.pr190) - 
    1.549429*(model.pi189) * (model.pi188+model.pi190) + (-62.0*model.u188+0.0*model.u189+62.0*model.u190) * 
    (model.pr189*model.pr189+model.pi189*model.pi189) + 650.0*(model.u188-model.u189) * (model.u188-model.u189) - 1.549429*(model.pr190) 
    * (model.pr189+model.pr191) - 1.549429*(model.pi190) * (model.pi189+model.pi191) + 
    (-62.0*model.u189+0.0*model.u190+62.0*model.u191) * (model.pr190*model.pr190+model.pi190*model.pi190) + 650.0*(model.u189-model.u190) 
    * (model.u189-model.u190) - 1.549429*(model.pr191) * (model.pr190+model.pr192) - 1.549429*(model.pi191) * 
    (model.pi190+model.pi192) + (-62.0*model.u190+0.0*model.u191+62.0*model.u192) * (model.pr191*model.pr191+model.pi191*model.pi191) + 
    650.0*(model.u190-model.u191) * (model.u190-model.u191) - 1.549429*(model.pr192) * (model.pr191+model.pr193) - 
    1.549429*(model.pi192) * (model.pi191+model.pi193) + (-62.0*model.u191+0.0*model.u192+62.0*model.u193) * 
    (model.pr192*model.pr192+model.pi192*model.pi192) + 650.0*(model.u191-model.u192) * (model.u191-model.u192) - 1.549429*(model.pr193) 
    * (model.pr192+model.pr194) - 1.549429*(model.pi193) * (model.pi192+model.pi194) + 
    (-62.0*model.u192+0.0*model.u193+62.0*model.u194) * (model.pr193*model.pr193+model.pi193*model.pi193) + 650.0*(model.u192-model.u193) 
    * (model.u192-model.u193) - 1.549429*(model.pr194) * (model.pr193+model.pr195) - 1.549429*(model.pi194) * 
    (model.pi193+model.pi195) + (-62.0*model.u193+0.0*model.u194+62.0*model.u195) * (model.pr194*model.pr194+model.pi194*model.pi194) + 
    650.0*(model.u193-model.u194) * (model.u193-model.u194) - 1.549429*(model.pr195) * (model.pr194+model.pr196) - 
    1.549429*(model.pi195) * (model.pi194+model.pi196) + (-62.0*model.u194+0.0*model.u195+62.0*model.u196) * 
    (model.pr195*model.pr195+model.pi195*model.pi195) + 650.0*(model.u194-model.u195) * (model.u194-model.u195) - 1.549429*(model.pr196) 
    * (model.pr195+model.pr197) - 1.549429*(model.pi196) * (model.pi195+model.pi197) + 
    (-62.0*model.u195+0.0*model.u196+62.0*model.u197) * (model.pr196*model.pr196+model.pi196*model.pi196) + 650.0*(model.u195-model.u196) 
    * (model.u195-model.u196) - 1.549429*(model.pr197) * (model.pr196+model.pr198) - 1.549429*(model.pi197) * 
    (model.pi196+model.pi198) + (-62.0*model.u196+0.0*model.u197+62.0*model.u198) * (model.pr197*model.pr197+model.pi197*model.pi197) + 
    650.0*(model.u196-model.u197) * (model.u196-model.u197) - 1.549429*(model.pr198) * (model.pr197+model.pr199) - 
    1.549429*(model.pi198) * (model.pi197+model.pi199) + (-62.0*model.u197+0.0*model.u198+62.0*model.u199) * 
    (model.pr198*model.pr198+model.pi198*model.pi198) + 650.0*(model.u197-model.u198) * (model.u197-model.u198) - 1.549429*(model.pr199) 
    * (model.pr198+model.pr200) - 1.549429*(model.pi199) * (model.pi198+model.pi200) + 
    (-62.0*model.u198+0.0*model.u199+62.0*model.u200) * (model.pr199*model.pr199+model.pi199*model.pi199) + 650.0*(model.u198-model.u199) 
    * (model.u198-model.u199) - 1.549429*(model.pr200) * (model.pr199+model.pr1) - 1.549429*(model.pi200) * (model.pi199+model.pi1) 
    + (-62.0*model.u199+0.0*model.u200+62.0*model.u1) * (model.pr200*model.pr200+model.pi200*model.pi200) + 650.0*(model.u199-model.u200) 
    * (model.u199-model.u200))

model.con = Constraint(expr=model.pr1 * model.pr1 + model.pi1 * model.pi1 + model.pr2 * model.pr2 + model.pi2 * model.pi2 + model.pr3 * model.pr3 + model.pi3 * model.pi3 + model.pr4 * 
    model.pr4 + model.pi4 * model.pi4 + model.pr5 * model.pr5 + model.pi5 * model.pi5 + model.pr6 * model.pr6 + model.pi6 * model.pi6 + model.pr7 * model.pr7 + 
    model.pi7 * model.pi7 + model.pr8 * model.pr8 + model.pi8 * model.pi8 + model.pr9 * model.pr9 + model.pi9 * model.pi9 + model.pr10 * model.pr10 + model.pi10 
    * model.pi10 + model.pr11 * model.pr11 + model.pi11 * model.pi11 + model.pr12 * model.pr12 + model.pi12 * model.pi12 + model.pr13 * model.pr13 + 
    model.pi13 * model.pi13 + model.pr14 * model.pr14 + model.pi14 * model.pi14 + model.pr15 * model.pr15 + model.pi15 * model.pi15 + model.pr16 * 
    model.pr16 + model.pi16 * model.pi16 + model.pr17 * model.pr17 + model.pi17 * model.pi17 + model.pr18 * model.pr18 + model.pi18 * model.pi18 + 
    model.pr19 * model.pr19 + model.pi19 * model.pi19 + model.pr20 * model.pr20 + model.pi20 * model.pi20 + model.pr21 * model.pr21 + model.pi21 * 
    model.pi21 + model.pr22 * model.pr22 + model.pi22 * model.pi22 + model.pr23 * model.pr23 + model.pi23 * model.pi23 + model.pr24 * model.pr24 + 
    model.pi24 * model.pi24 + model.pr25 * model.pr25 + model.pi25 * model.pi25 + model.pr26 * model.pr26 + model.pi26 * model.pi26 + model.pr27 * 
    model.pr27 + model.pi27 * model.pi27 + model.pr28 * model.pr28 + model.pi28 * model.pi28 + model.pr29 * model.pr29 + model.pi29 * model.pi29 + 
    model.pr30 * model.pr30 + model.pi30 * model.pi30 + model.pr31 * model.pr31 + model.pi31 * model.pi31 + model.pr32 * model.pr32 + model.pi32 * 
    model.pi32 + model.pr33 * model.pr33 + model.pi33 * model.pi33 + model.pr34 * model.pr34 + model.pi34 * model.pi34 + model.pr35 * model.pr35 + 
    model.pi35 * model.pi35 + model.pr36 * model.pr36 + model.pi36 * model.pi36 + model.pr37 * model.pr37 + model.pi37 * model.pi37 + model.pr38 * 
    model.pr38 + model.pi38 * model.pi38 + model.pr39 * model.pr39 + model.pi39 * model.pi39 + model.pr40 * model.pr40 + model.pi40 * model.pi40 + 
    model.pr41 * model.pr41 + model.pi41 * model.pi41 + model.pr42 * model.pr42 + model.pi42 * model.pi42 + model.pr43 * model.pr43 + model.pi43 * 
    model.pi43 + model.pr44 * model.pr44 + model.pi44 * model.pi44 + model.pr45 * model.pr45 + model.pi45 * model.pi45 + model.pr46 * model.pr46 + 
    model.pi46 * model.pi46 + model.pr47 * model.pr47 + model.pi47 * model.pi47 + model.pr48 * model.pr48 + model.pi48 * model.pi48 + model.pr49 * 
    model.pr49 + model.pi49 * model.pi49 + model.pr50 * model.pr50 + model.pi50 * model.pi50 + model.pr51 * model.pr51 + model.pi51 * model.pi51 + 
    model.pr52 * model.pr52 + model.pi52 * model.pi52 + model.pr53 * model.pr53 + model.pi53 * model.pi53 + model.pr54 * model.pr54 + model.pi54 * 
    model.pi54 + model.pr55 * model.pr55 + model.pi55 * model.pi55 + model.pr56 * model.pr56 + model.pi56 * model.pi56 + model.pr57 * model.pr57 + 
    model.pi57 * model.pi57 + model.pr58 * model.pr58 + model.pi58 * model.pi58 + model.pr59 * model.pr59 + model.pi59 * model.pi59 + model.pr60 * 
    model.pr60 + model.pi60 * model.pi60 + model.pr61 * model.pr61 + model.pi61 * model.pi61 + model.pr62 * model.pr62 + model.pi62 * model.pi62 + 
    model.pr63 * model.pr63 + model.pi63 * model.pi63 + model.pr64 * model.pr64 + model.pi64 * model.pi64 + model.pr65 * model.pr65 + model.pi65 * 
    model.pi65 + model.pr66 * model.pr66 + model.pi66 * model.pi66 + model.pr67 * model.pr67 + model.pi67 * model.pi67 + model.pr68 * model.pr68 + 
    model.pi68 * model.pi68 + model.pr69 * model.pr69 + model.pi69 * model.pi69 + model.pr70 * model.pr70 + model.pi70 * model.pi70 + model.pr71 * 
    model.pr71 + model.pi71 * model.pi71 + model.pr72 * model.pr72 + model.pi72 * model.pi72 + model.pr73 * model.pr73 + model.pi73 * model.pi73 + 
    model.pr74 * model.pr74 + model.pi74 * model.pi74 + model.pr75 * model.pr75 + model.pi75 * model.pi75 + model.pr76 * model.pr76 + model.pi76 * 
    model.pi76 + model.pr77 * model.pr77 + model.pi77 * model.pi77 + model.pr78 * model.pr78 + model.pi78 * model.pi78 + model.pr79 * model.pr79 + 
    model.pi79 * model.pi79 + model.pr80 * model.pr80 + model.pi80 * model.pi80 + model.pr81 * model.pr81 + model.pi81 * model.pi81 + model.pr82 * 
    model.pr82 + model.pi82 * model.pi82 + model.pr83 * model.pr83 + model.pi83 * model.pi83 + model.pr84 * model.pr84 + model.pi84 * model.pi84 + 
    model.pr85 * model.pr85 + model.pi85 * model.pi85 + model.pr86 * model.pr86 + model.pi86 * model.pi86 + model.pr87 * model.pr87 + model.pi87 * 
    model.pi87 + model.pr88 * model.pr88 + model.pi88 * model.pi88 + model.pr89 * model.pr89 + model.pi89 * model.pi89 + model.pr90 * model.pr90 + 
    model.pi90 * model.pi90 + model.pr91 * model.pr91 + model.pi91 * model.pi91 + model.pr92 * model.pr92 + model.pi92 * model.pi92 + model.pr93 * 
    model.pr93 + model.pi93 * model.pi93 + model.pr94 * model.pr94 + model.pi94 * model.pi94 + model.pr95 * model.pr95 + model.pi95 * model.pi95 + 
    model.pr96 * model.pr96 + model.pi96 * model.pi96 + model.pr97 * model.pr97 + model.pi97 * model.pi97 + model.pr98 * model.pr98 + model.pi98 * 
    model.pi98 + model.pr99 * model.pr99 + model.pi99 * model.pi99 + model.pr100 * model.pr100 + model.pi100 * model.pi100 + model.pr101 * 
    model.pr101 + model.pi101 * model.pi101 + model.pr102 * model.pr102 + model.pi102 * model.pi102 + model.pr103 * model.pr103 + model.pi103 * 
    model.pi103 + model.pr104 * model.pr104 + model.pi104 * model.pi104 + model.pr105 * model.pr105 + model.pi105 * model.pi105 + model.pr106 * 
    model.pr106 + model.pi106 * model.pi106 + model.pr107 * model.pr107 + model.pi107 * model.pi107 + model.pr108 * model.pr108 + model.pi108 * 
    model.pi108 + model.pr109 * model.pr109 + model.pi109 * model.pi109 + model.pr110 * model.pr110 + model.pi110 * model.pi110 + model.pr111 * 
    model.pr111 + model.pi111 * model.pi111 + model.pr112 * model.pr112 + model.pi112 * model.pi112 + model.pr113 * model.pr113 + model.pi113 * 
    model.pi113 + model.pr114 * model.pr114 + model.pi114 * model.pi114 + model.pr115 * model.pr115 + model.pi115 * model.pi115 + model.pr116 * 
    model.pr116 + model.pi116 * model.pi116 + model.pr117 * model.pr117 + model.pi117 * model.pi117 + model.pr118 * model.pr118 + model.pi118 * 
    model.pi118 + model.pr119 * model.pr119 + model.pi119 * model.pi119 + model.pr120 * model.pr120 + model.pi120 * model.pi120 + model.pr121 * 
    model.pr121 + model.pi121 * model.pi121 + model.pr122 * model.pr122 + model.pi122 * model.pi122 + model.pr123 * model.pr123 + model.pi123 * 
    model.pi123 + model.pr124 * model.pr124 + model.pi124 * model.pi124 + model.pr125 * model.pr125 + model.pi125 * model.pi125 + model.pr126 * 
    model.pr126 + model.pi126 * model.pi126 + model.pr127 * model.pr127 + model.pi127 * model.pi127 + model.pr128 * model.pr128 + model.pi128 * 
    model.pi128 + model.pr129 * model.pr129 + model.pi129 * model.pi129 + model.pr130 * model.pr130 + model.pi130 * model.pi130 + model.pr131 * 
    model.pr131 + model.pi131 * model.pi131 + model.pr132 * model.pr132 + model.pi132 * model.pi132 + model.pr133 * model.pr133 + model.pi133 * 
    model.pi133 + model.pr134 * model.pr134 + model.pi134 * model.pi134 + model.pr135 * model.pr135 + model.pi135 * model.pi135 + model.pr136 * 
    model.pr136 + model.pi136 * model.pi136 + model.pr137 * model.pr137 + model.pi137 * model.pi137 + model.pr138 * model.pr138 + model.pi138 * 
    model.pi138 + model.pr139 * model.pr139 + model.pi139 * model.pi139 + model.pr140 * model.pr140 + model.pi140 * model.pi140 + model.pr141 * 
    model.pr141 + model.pi141 * model.pi141 + model.pr142 * model.pr142 + model.pi142 * model.pi142 + model.pr143 * model.pr143 + model.pi143 * 
    model.pi143 + model.pr144 * model.pr144 + model.pi144 * model.pi144 + model.pr145 * model.pr145 + model.pi145 * model.pi145 + model.pr146 * 
    model.pr146 + model.pi146 * model.pi146 + model.pr147 * model.pr147 + model.pi147 * model.pi147 + model.pr148 * model.pr148 + model.pi148 * 
    model.pi148 + model.pr149 * model.pr149 + model.pi149 * model.pi149 + model.pr150 * model.pr150 + model.pi150 * model.pi150 + model.pr151 * 
    model.pr151 + model.pi151 * model.pi151 + model.pr152 * model.pr152 + model.pi152 * model.pi152 + model.pr153 * model.pr153 + model.pi153 * 
    model.pi153 + model.pr154 * model.pr154 + model.pi154 * model.pi154 + model.pr155 * model.pr155 + model.pi155 * model.pi155 + model.pr156 * 
    model.pr156 + model.pi156 * model.pi156 + model.pr157 * model.pr157 + model.pi157 * model.pi157 + model.pr158 * model.pr158 + model.pi158 * 
    model.pi158 + model.pr159 * model.pr159 + model.pi159 * model.pi159 + model.pr160 * model.pr160 + model.pi160 * model.pi160 + model.pr161 * 
    model.pr161 + model.pi161 * model.pi161 + model.pr162 * model.pr162 + model.pi162 * model.pi162 + model.pr163 * model.pr163 + model.pi163 * 
    model.pi163 + model.pr164 * model.pr164 + model.pi164 * model.pi164 + model.pr165 * model.pr165 + model.pi165 * model.pi165 + model.pr166 * 
    model.pr166 + model.pi166 * model.pi166 + model.pr167 * model.pr167 + model.pi167 * model.pi167 + model.pr168 * model.pr168 + model.pi168 * 
    model.pi168 + model.pr169 * model.pr169 + model.pi169 * model.pi169 + model.pr170 * model.pr170 + model.pi170 * model.pi170 + model.pr171 * 
    model.pr171 + model.pi171 * model.pi171 + model.pr172 * model.pr172 + model.pi172 * model.pi172 + model.pr173 * model.pr173 + model.pi173 * 
    model.pi173 + model.pr174 * model.pr174 + model.pi174 * model.pi174 + model.pr175 * model.pr175 + model.pi175 * model.pi175 + model.pr176 * 
    model.pr176 + model.pi176 * model.pi176 + model.pr177 * model.pr177 + model.pi177 * model.pi177 + model.pr178 * model.pr178 + model.pi178 * 
    model.pi178 + model.pr179 * model.pr179 + model.pi179 * model.pi179 + model.pr180 * model.pr180 + model.pi180 * model.pi180 + model.pr181 * 
    model.pr181 + model.pi181 * model.pi181 + model.pr182 * model.pr182 + model.pi182 * model.pi182 + model.pr183 * model.pr183 + model.pi183 * 
    model.pi183 + model.pr184 * model.pr184 + model.pi184 * model.pi184 + model.pr185 * model.pr185 + model.pi185 * model.pi185 + model.pr186 * 
    model.pr186 + model.pi186 * model.pi186 + model.pr187 * model.pr187 + model.pi187 * model.pi187 + model.pr188 * model.pr188 + model.pi188 * 
    model.pi188 + model.pr189 * model.pr189 + model.pi189 * model.pi189 + model.pr190 * model.pr190 + model.pi190 * model.pi190 + model.pr191 * 
    model.pr191 + model.pi191 * model.pi191 + model.pr192 * model.pr192 + model.pi192 * model.pi192 + model.pr193 * model.pr193 + model.pi193 * 
    model.pi193 + model.pr194 * model.pr194 + model.pi194 * model.pi194 + model.pr195 * model.pr195 + model.pi195 * model.pi195 + model.pr196 * 
    model.pr196 + model.pi196 * model.pi196 + model.pr197 * model.pr197 + model.pi197 * model.pi197 + model.pr198 * model.pr198 + model.pi198 * 
    model.pi198 + model.pr199 * model.pr199 + model.pi199 * model.pi199 + model.pr200 * model.pr200 + model.pi200 * model.pi200 - 1.0 == 0)
