#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Juan Lopez
# Taken from:
#
#**************************
# SET UP THE INITIAL DATA *
#**************************
#   Problem:
#   ********
#   A problem of water resource management in Canada, which may be 
#   formulated as
#
#   Min  SUM   SUM  (T(i,j)- R(i,j))^2 + (O(i,j)-R(N+i,j))^2)
#       i=1,N j=1,5 
#
#   subject to
#
#   T(i+1,1)-T(i,1)+O(i,1)        =  G(i,1)
#   T(i+1,2)-T(i,2)-O(i,1)+O(i,2) =  G(i,2)
#   T(i+1,3)-T(i,3)-O(i,2)+O(i,3) =  G(i,3)
#   T(i+1,4)-T(i,4)-O(i,3)+O(i,4) =  G(i,4)
#   T(i+1,5)-T(i,5)-O(i,4)+O(i,5) =  G(i,5) 
#
#   i=1,N and T(N+1,j) = T(1,j)  for j=1,5
#
#   O(i,2)-a*((T(i,2)/480.8+T(i,3)/4.6)/2-543.4)^2 * 
#   (T(i,2)/480.8-T(i,3)/4.6)^.5=0
#   O(i,3)-b*((T(i,3)/4.6-543.4)^2*(T(i,3)/4.6-T(i,4)/105.15)^0.5) = 0
#   O(i,4)-c*(T(i,4)/105.15-550.11)^2.2 = 0
#
#   where T(i,j) and O(i,j) are variables, R(i,j) are given and
#   a=.0841168  b=.1280849 and c=0.2605.
#
#   Extra variables 
#   
#   v(i,2) = T(i,2) / 961.6 + T(i,3) / 9.2 - 543.4
#   w(i,2) = T(i,2) / 480.8 - T(i,3) / 4.6
#   v(i,3) = T(i,3) / 4.6 - 543.4
#   w(i,3) = T(i,3) / 4.6 - T(i,4) / 105.15
#   v(i,4) = T(i,4) / 105.15 - 550.11
#
#   are introduced so that the nonlinear constraints may be rewritten as
#
#   O(i,2)-a*v(i,2)^2 * w(i,2)^0.5 = 0 ; w(i,2) > 0
#   O(i,3)-b*v(i,3)^2 * w(i,3)^0.5 = 0 ; w(i,3) > 0
#   O(i,4)-c*v(i,4)^2.2 = 0 ; v(i,4) > 0
#
#   Source:
#   S Jafar Sadjadi
#   Dept. of Systems Design Engineering
#   University of Waterloo
#   Ontario, N2L 3G1 Canada
#   SIF input: Nick Gould and Jafar Sadjadi, November 1995
#   classification QOR2-RN-90-78
# Target value S_hat and O_hat
# Defining the variables
#  Objective function groups
# Linear Constraints
# Nonlinear constraints
# Artificial linear constraints

from pyomo.core import *
model = ConcreteModel()

n = 6
nm1 = -1 + (6)
np1 = 1 + (6)
nn = 2 * (6)
s1s1 = 202761.072
s1s2 = 277791.816
s1s3 = 2636.996
s1s4 = 59987.0235
s1s5 = 19490.4
s2s1 = 202703.646
s2s2 = 277849.512
s2s3 = 2638.1
s2s4 = 59998.59
s2s5 = 19555.2
s3s1 = 202720.536
s3s2 = 277955.288
s3s3 = 2639.894
s3s4 = 60046.959
s3s5 = 19597.6
s4s1 = 202808.364
s4s2 = 278104.336
s4s3 = 2640.906
s4s4 = 60074.298
s4s5 = 19652.8
s5s1 = 202916.46
s5s2 = 278224.536
s5s3 = 2641.458
s5s4 = 60091.122
s5s5 = 19708.8
s6s1 = 202953.618
s6s2 = 278277.424
s6s3 = 2641.458
s6s4 = 60082.71
s6s5 = 19706.4
o1o1 = 83.728
o1o2 = 174.665
o1o3 = 180.539
o1o4 = 211.558
o1o5 = 232.252
o2o1 = 83.789
o2o2 = 173.255
o2o3 = 179.917
o2o4 = 210.585
o2o5 = 215.254
o3o1 = 82.916
o3o2 = 173.721
o3o3 = 182.676
o3o4 = 207.838
o3o5 = 203.855
o4o1 = 80.134
o4o2 = 178.654
o4o3 = 185.917
o4o4 = 206.416
o4o5 = 186.308
o5o1 = 65.345
o5o2 = 188.01
o5o3 = 192.568
o5o4 = 204.3
o5o5 = 201.1
o6o1 = 72.005
o6o2 = 193.833
o6o3 = 196.651
o6o4 = 204.25
o6o5 = 241.079
npi = (6) + (6)
kp1 = 1 + (5)
jm1 = -1 + (5)
c = 1.0 / (105.15)

model.t1_1 = Var(initialize=1.0)
t1_1 = model.t1_1
model.o1_1 = Var(initialize=1.0)
o1_1 = model.o1_1
model.t1_2 = Var(initialize=1.0)
t1_2 = model.t1_2
model.o1_2 = Var(initialize=1.0)
o1_2 = model.o1_2
model.t1_3 = Var(initialize=1.0)
t1_3 = model.t1_3
model.o1_3 = Var(initialize=1.0)
o1_3 = model.o1_3
model.t1_4 = Var(initialize=1.0)
t1_4 = model.t1_4
model.o1_4 = Var(initialize=1.0)
o1_4 = model.o1_4
model.t1_5 = Var(initialize=1.0)
t1_5 = model.t1_5
model.o1_5 = Var(initialize=1.0)
o1_5 = model.o1_5
model.v1_2 = Var(initialize=1.0)
v1_2 = model.v1_2
model.w1_2 = Var(initialize=1.0, bounds=(0.0001,None))
w1_2 = model.w1_2
model.v1_3 = Var(initialize=1.0)
v1_3 = model.v1_3
model.w1_3 = Var(initialize=1.0, bounds=(0.0001,None))
w1_3 = model.w1_3
model.v1_4 = Var(initialize=1.0, bounds=(0.0001,None))
v1_4 = model.v1_4
model.t2_1 = Var(initialize=1.0)
t2_1 = model.t2_1
model.o2_1 = Var(initialize=1.0)
o2_1 = model.o2_1
model.t2_2 = Var(initialize=1.0)
t2_2 = model.t2_2
model.o2_2 = Var(initialize=1.0)
o2_2 = model.o2_2
model.t2_3 = Var(initialize=1.0)
t2_3 = model.t2_3
model.o2_3 = Var(initialize=1.0)
o2_3 = model.o2_3
model.t2_4 = Var(initialize=1.0)
t2_4 = model.t2_4
model.o2_4 = Var(initialize=1.0)
o2_4 = model.o2_4
model.t2_5 = Var(initialize=1.0)
t2_5 = model.t2_5
model.o2_5 = Var(initialize=1.0)
o2_5 = model.o2_5
model.v2_2 = Var(initialize=1.0)
v2_2 = model.v2_2
model.w2_2 = Var(initialize=1.0, bounds=(0.0001,None))
w2_2 = model.w2_2
model.v2_3 = Var(initialize=1.0)
v2_3 = model.v2_3
model.w2_3 = Var(initialize=1.0, bounds=(0.0001,None))
w2_3 = model.w2_3
model.v2_4 = Var(initialize=1.0, bounds=(0.0001,None))
v2_4 = model.v2_4
model.t3_1 = Var(initialize=1.0)
t3_1 = model.t3_1
model.o3_1 = Var(initialize=1.0)
o3_1 = model.o3_1
model.t3_2 = Var(initialize=1.0)
t3_2 = model.t3_2
model.o3_2 = Var(initialize=1.0)
o3_2 = model.o3_2
model.t3_3 = Var(initialize=1.0)
t3_3 = model.t3_3
model.o3_3 = Var(initialize=1.0)
o3_3 = model.o3_3
model.t3_4 = Var(initialize=1.0)
t3_4 = model.t3_4
model.o3_4 = Var(initialize=1.0)
o3_4 = model.o3_4
model.t3_5 = Var(initialize=1.0)
t3_5 = model.t3_5
model.o3_5 = Var(initialize=1.0)
o3_5 = model.o3_5
model.v3_2 = Var(initialize=1.0)
v3_2 = model.v3_2
model.w3_2 = Var(initialize=1.0, bounds=(0.0001,None))
w3_2 = model.w3_2
model.v3_3 = Var(initialize=1.0)
v3_3 = model.v3_3
model.w3_3 = Var(initialize=1.0, bounds=(0.0001,None))
w3_3 = model.w3_3
model.v3_4 = Var(initialize=1.0, bounds=(0.0001,None))
v3_4 = model.v3_4
model.t4_1 = Var(initialize=1.0)
t4_1 = model.t4_1
model.o4_1 = Var(initialize=1.0)
o4_1 = model.o4_1
model.t4_2 = Var(initialize=1.0)
t4_2 = model.t4_2
model.o4_2 = Var(initialize=1.0)
o4_2 = model.o4_2
model.t4_3 = Var(initialize=1.0)
t4_3 = model.t4_3
model.o4_3 = Var(initialize=1.0)
o4_3 = model.o4_3
model.t4_4 = Var(initialize=1.0)
t4_4 = model.t4_4
model.o4_4 = Var(initialize=1.0)
o4_4 = model.o4_4
model.t4_5 = Var(initialize=1.0)
t4_5 = model.t4_5
model.o4_5 = Var(initialize=1.0)
o4_5 = model.o4_5
model.v4_2 = Var(initialize=1.0)
v4_2 = model.v4_2
model.w4_2 = Var(initialize=1.0, bounds=(0.0001,None))
w4_2 = model.w4_2
model.v4_3 = Var(initialize=1.0)
v4_3 = model.v4_3
model.w4_3 = Var(initialize=1.0, bounds=(0.0001,None))
w4_3 = model.w4_3
model.v4_4 = Var(initialize=1.0, bounds=(0.0001,None))
v4_4 = model.v4_4
model.t5_1 = Var(initialize=1.0)
t5_1 = model.t5_1
model.o5_1 = Var(initialize=1.0)
o5_1 = model.o5_1
model.t5_2 = Var(initialize=1.0)
t5_2 = model.t5_2
model.o5_2 = Var(initialize=1.0)
o5_2 = model.o5_2
model.t5_3 = Var(initialize=1.0)
t5_3 = model.t5_3
model.o5_3 = Var(initialize=1.0)
o5_3 = model.o5_3
model.t5_4 = Var(initialize=1.0)
t5_4 = model.t5_4
model.o5_4 = Var(initialize=1.0)
o5_4 = model.o5_4
model.t5_5 = Var(initialize=1.0)
t5_5 = model.t5_5
model.o5_5 = Var(initialize=1.0)
o5_5 = model.o5_5
model.v5_2 = Var(initialize=1.0)
v5_2 = model.v5_2
model.w5_2 = Var(initialize=1.0, bounds=(0.0001,None))
w5_2 = model.w5_2
model.v5_3 = Var(initialize=1.0)
v5_3 = model.v5_3
model.w5_3 = Var(initialize=1.0, bounds=(0.0001,None))
w5_3 = model.w5_3
model.v5_4 = Var(initialize=1.0, bounds=(0.0001,None))
v5_4 = model.v5_4
model.t6_1 = Var(initialize=1.0)
t6_1 = model.t6_1
model.o6_1 = Var(initialize=1.0)
o6_1 = model.o6_1
model.t6_2 = Var(initialize=1.0)
t6_2 = model.t6_2
model.o6_2 = Var(initialize=1.0)
o6_2 = model.o6_2
model.t6_3 = Var(initialize=1.0)
t6_3 = model.t6_3
model.o6_3 = Var(initialize=1.0)
o6_3 = model.o6_3
model.t6_4 = Var(initialize=1.0)
t6_4 = model.t6_4
model.o6_4 = Var(initialize=1.0)
o6_4 = model.o6_4
model.t6_5 = Var(initialize=1.0)
t6_5 = model.t6_5
model.o6_5 = Var(initialize=1.0)
o6_5 = model.o6_5
model.v6_2 = Var(initialize=1.0)
v6_2 = model.v6_2
model.w6_2 = Var(initialize=1.0, bounds=(0.0001,None))
w6_2 = model.w6_2
model.v6_3 = Var(initialize=1.0)
v6_3 = model.v6_3
model.w6_3 = Var(initialize=1.0, bounds=(0.0001,None))
w6_3 = model.w6_3
model.v6_4 = Var(initialize=1.0, bounds=(0.0001,None))
v6_4 = model.v6_4

model.obj = Objective(expr=\
    (t1_1 - 202761.072)*(t1_1 - 202761.072) + (o1_1 - 232.252)*(o1_1 - 232.252) + \
    (t1_2 - 277791.816)*(t1_2 - 277791.816) + (o1_2 - 174.665)*(o1_2 - 174.665) + \
    (t1_3 - 2636.996)*(t1_3 - 2636.996) + (o1_3 - 180.539)*(o1_3 - 180.539) + (t1_4 \
    - 59987.0235)*(t1_4 - 59987.0235) + (o1_4 - 211.558)*(o1_4 - 211.558) + (t1_5 - \
    19490.4)*(t1_5 - 19490.4) + (o1_5 - 232.252)*(o1_5 - 232.252) + (t2_1 - \
    202703.646)*(t2_1 - 202703.646) + (o2_1 - 83.789)*(o2_1 - 83.789) + (t2_2 - \
    277849.512)*(t2_2 - 277849.512) + (o2_2 - 173.255)*(o2_2 - 173.255) + (t2_3 - \
    2638.1)*(t2_3 - 2638.1) + (o2_3 - 179.917)*(o2_3 - 179.917) + (t2_4 - \
    59998.59)*(t2_4 - 59998.59) + (o2_4 - 210.585)*(o2_4 - 210.585) + (t2_5 - \
    19555.2)*(t2_5 - 19555.2) + (o2_5 - 215.254)*(o2_5 - 215.254) + (t3_1 - \
    202720.536)*(t3_1 - 202720.536) + (o3_1 - 82.916)*(o3_1 - 82.916) + (t3_2 - \
    277955.288)*(t3_2 - 277955.288) + (o3_2 - 173.721)*(o3_2 - 173.721) + (t3_3 - \
    2639.894)*(t3_3 - 2639.894) + (o3_3 - 182.676)*(o3_3 - 182.676) + (t3_4 - \
    60046.959)*(t3_4 - 60046.959) + (o3_4 - 207.838)*(o3_4 - 207.838) + (t3_5 - \
    19597.6)*(t3_5 - 19597.6) + (o3_5 - 203.855)*(o3_5 - 203.855) + (t4_1 - \
    202808.364)*(t4_1 - 202808.364) + (o4_1 - 80.134)*(o4_1 - 80.134) + (t4_2 - \
    278104.336)*(t4_2 - 278104.336) + (o4_2 - 178.654)*(o4_2 - 178.654) + (t4_3 - \
    2640.906)*(t4_3 - 2640.906) + (o4_3 - 185.917)*(o4_3 - 185.917) + (t4_4 - \
    60074.298)*(t4_4 - 60074.298) + (o4_4 - 206.416)*(o4_4 - 206.416) + (t4_5 - \
    19652.8)*(t4_5 - 19652.8) + (o4_5 - 186.308)*(o4_5 - 186.308) + (t5_1 - \
    202916.46)*(t5_1 - 202916.46) + (o5_1 - 65.345)*(o5_1 - 65.345) + (t5_2 - \
    278224.536)*(t5_2 - 278224.536) + (o5_2 - 188.01)*(o5_2 - 188.01) + (t5_3 - \
    2641.458)*(t5_3 - 2641.458) + (o5_3 - 192.568)*(o5_3 - 192.568) + (t5_4 - \
    60091.122)*(t5_4 - 60091.122) + (o5_4 - 204.3)*(o5_4 - 204.3) + (t5_5 - \
    19708.8)*(t5_5 - 19708.8) + (o5_5 - 201.1)*(o5_5 - 201.1) + (t6_1 - \
    202953.618)*(t6_1 - 202953.618) + (o6_1 - 72.005)*(o6_1 - 72.005) + (t6_2 - \
    278277.424)*(t6_2 - 278277.424) + (o6_2 - 193.833)*(o6_2 - 193.833) + (t6_3 - \
    2641.458)*(t6_3 - 2641.458) + (o6_3 - 196.651)*(o6_3 - 196.651) + (t6_4 - \
    60082.71)*(t6_4 - 60082.71) + (o6_4 - 204.25)*(o6_4 - 204.25) + (t6_5 - \
    19706.4)*(t6_5 - 19706.4) + (o6_5 - 241.079)*(o6_5 - 241.079))

model.consg1_1 = Constraint(expr=t2_1 - t1_1 + o1_1 + 22.0 == 0)
model.consg1_2 = Constraint(expr=t2_2 - t1_2 + o1_2 - o1_1 + 1.0 == 0)
model.consg1_3 = Constraint(expr=t2_3 - t1_3 + o1_3 - o1_2 - 3.0 == 0)
model.consg1_4 = Constraint(expr=t2_4 - t1_4 + o1_4 - o1_3 + 27.2 == 0)
model.consg1_5 = Constraint(expr=t2_5 - t1_5 + o1_5 - o1_4 - 51.5 == 0)
model.consg2_1 = Constraint(expr=t3_1 - t2_1 + o2_1 - 44.0 == 0)
model.consg2_2 = Constraint(expr=t3_2 - t2_2 + o2_2 - o2_1 - 162.0 == 0)
model.consg2_3 = Constraint(expr=t3_3 - t2_3 + o2_3 - o2_2 - 8.0 == 0)
model.consg2_4 = Constraint(expr=t3_4 - t2_4 + o2_4 - o2_3 - 12.5 == 0)
model.consg2_5 = Constraint(expr=t3_5 - t2_5 + o2_5 - o2_4 - 53.5 == 0)
model.consg3_1 = Constraint(expr=t4_1 - t3_1 + o3_1 + 11.0 == 0)
model.consg3_2 = Constraint(expr=t4_2 - t3_2 + o3_2 - o3_1 - 60.0 == 0)
model.consg3_3 = Constraint(expr=t4_3 - t3_3 + o3_3 - o3_2 - 10.0 == 0)
model.consg3_4 = Constraint(expr=t4_4 - t3_4 + o3_4 - o3_3 - 18.0 == 0)
model.consg3_5 = Constraint(expr=t4_5 - t3_5 + o3_5 - o3_4 - 39.0 == 0)
model.consg4_1 = Constraint(expr=t5_1 - t4_1 + o4_1 - 124.0 == 0)
model.consg4_2 = Constraint(expr=t5_2 - t4_2 + o4_2 - o4_1 - 246.0 == 0)
model.consg4_3 = Constraint(expr=t5_3 - t4_3 + o4_3 - o4_2 - 6.0 == 0)
model.consg4_4 = Constraint(expr=t5_4 - t4_4 + o4_4 - o4_3 - 9.7 == 0)
model.consg4_5 = Constraint(expr=t5_5 - t4_5 + o4_5 - o4_4 - 17.2 == 0)
model.consg5_1 = Constraint(expr=t6_1 - t5_1 + o5_1 - 127.0 == 0)
model.consg5_2 = Constraint(expr=t6_2 - t5_2 + o5_2 - o5_1 - 175.0 == 0)
model.consg5_3 = Constraint(expr=t6_3 - t5_3 + o5_3 - o5_2 - 3.0 == 0)
model.consg5_4 = Constraint(expr=t6_4 - t5_4 + o5_4 - o5_3 - 10.0 == 0)
model.consg5_5 = Constraint(expr=t6_5 - t5_5 + o5_5 - o5_4 - 30.2 == 0)
model.consg6_1 = Constraint(expr=t1_1 - t6_1 + o6_1 - 78.0 == 0)
model.consg6_2 = Constraint(expr=t1_2 - t6_2 + o6_2 - o6_1 - 156.0 == 0)
model.consg6_3 = Constraint(expr=t1_3 - t6_3 + o6_3 - o6_2 - 3.0 == 0)
model.consg6_4 = Constraint(expr=t1_4 - t6_4 + o6_4 - o6_3 - 14.0 == 0)
model.consg6_5 = Constraint(expr=t1_5 - t6_5 + o6_5 - o6_4 - 23.2 == 0)
model.consa1_1 = Constraint(expr=0.0841168 * v1_2**2 * w1_2**0.5 - o1_2 == 0)
model.consa1_2 = Constraint(expr=0.1280849 * v1_3**2 * w1_3**0.5 - o1_3 == 0)
model.consa1_3 = Constraint(expr=0.2605 * v1_4**2.2 - o1_4 == 0)
model.consv1_2 = Constraint(expr=-v1_2 + 0.0010399334442595673*t1_2 + 0.10869565217391305*t1_3 - 543.4 == 0)
model.consw1_2 = Constraint(expr=-w1_2 + 0.0020798668885191347*t1_2 - 0.2173913043478261*t1_3 == 0)
model.consv1_3 = Constraint(expr=-v1_3 + 0.2173913043478261*t1_3 - 543.4 == 0)
model.consw1_3 = Constraint(expr=-w1_3 + 0.2173913043478261*t1_3 - 0.009510223490252021*t1_4 == 0)
model.consv1_4 = Constraint(expr=-v1_4 + 0.009510223490252021*t1_4 - 550.11 == 0)
model.consa2_1 = Constraint(expr=0.0841168 * v2_2**2 * w2_2**0.5 - o2_2 == 0)
model.consa2_2 = Constraint(expr=0.1280849 * v2_3**2 * w2_3**0.5 - o2_3 == 0)
model.consa2_3 = Constraint(expr=0.2605 * v2_4**2.2 - o2_4 == 0)
model.consv2_2 = Constraint(expr=-v2_2 + 0.0010399334442595673*t2_2 + 0.10869565217391305*t2_3 - 543.4 == 0)
model.consw2_2 = Constraint(expr=-w2_2 + 0.0020798668885191347*t2_2 - 0.2173913043478261*t2_3 == 0)
model.consv2_3 = Constraint(expr=-v2_3 + 0.2173913043478261*t2_3 - 543.4 == 0)
model.consw2_3 = Constraint(expr=-w2_3 + 0.2173913043478261*t2_3 - 0.009510223490252021*t2_4 == 0)
model.consv2_4 = Constraint(expr=-v2_4 + 0.009510223490252021*t2_4 - 550.11 == 0)
model.consa3_1 = Constraint(expr=0.0841168 * v3_2**2 * w3_2**0.5 - o3_2 == 0)
model.consa3_2 = Constraint(expr=0.1280849 * v3_3**2 * w3_3**0.5 - o3_3 == 0)
model.consa3_3 = Constraint(expr=0.2605 * v3_4**2.2 - o3_4 == 0)
model.consv3_2 = Constraint(expr=-v3_2 + 0.0010399334442595673*t3_2 + 0.10869565217391305*t3_3 - 543.4 == 0)
model.consw3_2 = Constraint(expr=-w3_2 + 0.0020798668885191347*t3_2 - 0.2173913043478261*t3_3 == 0)
model.consv3_3 = Constraint(expr=-v3_3 + 0.2173913043478261*t3_3 - 543.4 == 0)
model.consw3_3 = Constraint(expr=-w3_3 + 0.2173913043478261*t3_3 - 0.009510223490252021*t3_4 == 0)
model.consv3_4 = Constraint(expr=-v3_4 + 0.009510223490252021*t3_4 - 550.11 == 0)
model.consa4_1 = Constraint(expr=0.0841168 * v4_2**2 * w4_2**0.5 - o4_2 == 0)
model.consa4_2 = Constraint(expr=0.1280849 * v4_3**2 * w4_3**0.5 - o4_3 == 0)
model.consa4_3 = Constraint(expr=0.2605 * v4_4**2.2 - o4_4 == 0)
model.consv4_2 = Constraint(expr=-v4_2 + 0.0010399334442595673*t4_2 + 0.10869565217391305*t4_3 - 543.4 == 0)
model.consw4_2 = Constraint(expr=-w4_2 + 0.0020798668885191347*t4_2 - 0.2173913043478261*t4_3 == 0)
model.consv4_3 = Constraint(expr=-v4_3 + 0.2173913043478261*t4_3 - 543.4 == 0)
model.consw4_3 = Constraint(expr=-w4_3 + 0.2173913043478261*t4_3 - 0.009510223490252021*t4_4 == 0)
model.consv4_4 = Constraint(expr=-v4_4 + 0.009510223490252021*t4_4 - 550.11 == 0)
model.consa5_1 = Constraint(expr=0.0841168 * v5_2**2 * w5_2**0.5 - o5_2 == 0)
model.consa5_2 = Constraint(expr=0.1280849 * v5_3**2 * w5_3**0.5 - o5_3 == 0)
model.consa5_3 = Constraint(expr=0.2605 * v5_4**2.2 - o5_4 == 0)
model.consv5_2 = Constraint(expr=-v5_2 + 0.0010399334442595673*t5_2 + 0.10869565217391305*t5_3 - 543.4 == 0)
model.consw5_2 = Constraint(expr=-w5_2 + 0.0020798668885191347*t5_2 - 0.2173913043478261*t5_3 == 0)
model.consv5_3 = Constraint(expr=-v5_3 + 0.2173913043478261*t5_3 - 543.4 == 0)
model.consw5_3 = Constraint(expr=-w5_3 + 0.2173913043478261*t5_3 - 0.009510223490252021*t5_4 == 0)
model.consv5_4 = Constraint(expr=-v5_4 + 0.009510223490252021*t5_4 - 550.11 == 0)
model.consa6_1 = Constraint(expr=0.0841168 * v6_2**2 * w6_2**0.5 - o6_2 == 0)
model.consa6_2 = Constraint(expr=0.1280849 * v6_3**2 * w6_3**0.5 - o6_3 == 0)
model.consa6_3 = Constraint(expr=0.2605 * v6_4**2.2 - o6_4 == 0)
model.consv6_2 = Constraint(expr=-v6_2 + 0.0010399334442595673*t6_2 + 0.10869565217391305*t6_3 - 543.4 == 0)
model.consw6_2 = Constraint(expr=-w6_2 + 0.0020798668885191347*t6_2 - 0.2173913043478261*t6_3 == 0)
model.consv6_3 = Constraint(expr=-v6_3 + 0.2173913043478261*t6_3 - 543.4 == 0)
model.consw6_3 = Constraint(expr=-w6_3 + 0.2173913043478261*t6_3 - 0.009510223490252021*t6_4 == 0)
model.consv6_4 = Constraint(expr=-v6_4 + 0.009510223490252021*t6_4 - 550.11 == 0)

# Initialize constraint duals to 1.0
model.dual = Suffix(direction=Suffix.EXPORT)
model.dual.update((constraint,1) for constraint in model.component_data_objects(Constraint, active=True))
