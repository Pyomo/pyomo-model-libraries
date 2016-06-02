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
#   Problem:
#   ********
#   The objective function to be minimized represents the total cost of
#   the development and launching of a 3 stages space launching vehicle.
#   Constraints are imposed on physical interrelations between the variables
#   and performance.
#   The problem is highly non-convex. 
#   Source:
#   B. Rush, J. Bracken and G. McCormick,
#   "A nonliner programming model for launch vehicle design and costing",
#   Operations Research, pp. 185-210, 1967.
#   SIF input: P. Driscoll, Virginia Tech., April 1993,
#              corrected and simplified by Ph. L. Toint, May 1993.
#   classification OOR2-MY-25-28
#   Cost of stage 1
#   Cost of stage 2
#   Cost of stage 3
#   Instrumentation cost
#   Launch operating costs
#XN LAUN      'SCALE'   0.039215686
#   Relations between airframe weights and inert weights
#   Definition of stage mass fractions
#   Relation between stage thrust and single engine thrust
#   Constraints on structural integrity (stage weight vs propellant weight)
#   Constraints expression the ratio of thrust to initial weight for a given 
#   payload
#   Constraints on the stage mass fraction of the 3 stages
#   Constraints on the specific impulse
#   Total vehicle launch constraint
#   Objective function
#   Constraints
#   The starting point is very close to feasible
#   Elements for stage 1 modelling
#   a) airframe R&D
#   b) LOX/RP propulsion R&D
#   c) airframe production unit
#   d) LOX/RP propulsion production of 5 engines
#   Elements for stage 2 modelling
#   a) airframe R&D
#   b) LOX/RP propulsion R&D
#   c) airframe production unit
#   d) LOX/RP propulsion production of 5 engines
#   Elements for stage 3 modelling
#   a) airframe R&D
#   b) LOX/RP propulsion R&D
#   c) airframe production unit
#   d) LOX/RP propulsion production of 1 engine
#   Elements for constraints on the stage mass fraction
#   Constraints on specific impulse

from pyomo.core import *
model = ConcreteModel()

model.aw1 = Var(bounds=(1.0e-8,10000.0),initialize=68.0)
model.iw1 = Var(bounds=(1.0e-8,10000.0),initialize=136.0)
model.mf1 = Var(bounds=(0.25,0.3),initialize=0.29988744)
model.tt1 = Var(bounds=(1.0e-8,10000.0),initialize=3733.0)
model.pw1 = Var(bounds=(1.0e-8,10000.0),initialize=2177.0)
model.et1 = Var(bounds=(1.0e-8,10000.0),initialize=746.6)
model.s1l = Var(bounds=(125.0,150.0),initialize=125.0)
model.aw2 = Var(bounds=(1.0e-8,10000.0),initialize=28.2)
model.iw2 = Var(bounds=(1.0e-8,10000.0),initialize=47.0)
model.mf2 = Var(bounds=(0.24,0.29),initialize=0.28939109)
model.tt2 = Var(bounds=(1.0e-8,10000.0),initialize=480.0)
model.pw2 = Var(bounds=(1.0e-8,10000.0),initialize=566.0)
model.et2 = Var(bounds=(1.0e-8,10000.0),initialize=96.0)
model.s2l = Var(bounds=(75.0,100.0),initialize=75.0)
model.aw3 = Var(bounds=(1.0e-8,10000.0),initialize=11.2)
model.iw3 = Var(bounds=(1.0e-8,10000.0),initialize=16.0)
model.mf3 = Var(bounds=(0.16,0.21),initialize=0.20980926)
model.tt3 = Var(bounds=(1.0e-8,10000.0),initialize=129.0)
model.pw3 = Var(bounds=(1.0e-8,10000.0),initialize=145.0)
model.et3 = Var(bounds=(1.0e-8,10000.0),initialize=129.0)
model.s3l = Var(bounds=(50.0,70.0),initialize=50.0)
model.inw = Var(bounds=(2.5,4.0),initialize=2.5)
model.bt1 = Var(bounds=(1.0e-8,10000.0),initialize=155.0)
model.bt2 = Var(bounds=(1.0e-8,10000.0),initialize=314.0)
model.bt3 = Var(bounds=(1.0e-8,10000.0),initialize=403.0)

model.obj = Objective(expr=((5272.77*(model.aw1**1.2781) * (model.iw1**-0.1959) * (model.mf1**2.4242) * (model.tt1**0.38745) * (model.pw1**0.9904) + 160.909*(model.et1 / 1000.0 ) **-0.146 + 282.874*(model.et1 / 1000.0 ) **0.648 + 0.64570846*(model.aw1**0.3322) * (model.mf1**-1.5935) * (model.pw1**0.2363) * (model.s1l**0.1079) + 31.136196*(model.et1 / 1000.0 ) **0.736 + 12.092112*(model.et1 / 1000.0 ) **-0.229 + 31.136196*(model.et2 / 1000.0 ) **0.736 + 12.092112*(model.et2 / 1000.0 ) **-0.229 + (2.5870000000000005e-4)*model.et1 - 247.963)/(1.0e8)) + ((5272.77*(model.aw2**1.2781) * (model.iw2**-0.1959) * (model.mf2**2.4242) * (model.tt2**0.38745) * (model.pw2**0.9904) + 160.909*(model.et2 / 1000.0 ) **-0.146 + 282.874*(model.et2 / 1000.0 ) **0.648 + 0.64570846*(model.aw2**0.3322) * (model.mf2**-1.5935) * (model.pw2**0.2363) * (model.s2l**0.1079) + (2.5870000000000005e-4)*model.et2 - 247.963)/(1.0e8)) + ((5272.77*(model.aw3**1.2781) * (model.iw3**-0.1959) * (model.mf3**2.4242) * (model.tt3**0.38745) * (model.pw3**0.9904) + 181.806*(model.et3 / 1000.0 ) **0.539 + 232.57*(model.et3 / 1000.0 ) **0.772 + 0.49783215*(model.aw3**0.3322) * (model.mf3**-1.5935) * (model.pw3**0.2363) * (model.s3l**0.1079) - 0.22424514*(model.et3 / 100.0 ) **-1.33 + 20.708238*(model.et3 / 100.0 ) **0.498 + 0.001958*model.et3 - 32.591)/(1.0e8)) + ((47.040096*model.inw - 35.5)/(1.0e8)) + (((0.0030*model.pw1 + 0.0030*model.pw2 + 0.0030*model.pw3)**0.460)/(3.9215686e7)))

model.obj_bnd = Constraint(expr=0.0 <= ((5272.77*(model.aw1**1.2781) * (model.iw1**-0.1959) * (model.mf1**2.4242) * (model.tt1**0.38745) * (model.pw1**0.9904) + 160.909*(model.et1 / 1000.0 ) **-0.146 + 282.874*(model.et1 / 1000.0 ) **0.648 + 0.64570846*(model.aw1**0.3322) * (model.mf1**-1.5935) * (model.pw1**0.2363) * (model.s1l**0.1079) + 31.136196*(model.et1 / 1000.0 ) **0.736 + 12.092112*(model.et1 / 1000.0 ) **-0.229 + 31.136196*(model.et2 / 1000.0 ) **0.736 + 12.092112*(model.et2 / 1000.0 ) **-0.229 + (2.5870000000000005e-4)*model.et1 - 247.963)/(1.0e8)) + ((5272.77*(model.aw2**1.2781) * (model.iw2**-0.1959) * (model.mf2**2.4242) * (model.tt2**0.38745) * (model.pw2**0.9904) + 160.909*(model.et2 / 1000.0 ) **-0.146 + 282.874*(model.et2 / 1000.0 ) **0.648 + 0.64570846*(model.aw2**0.3322) * (model.mf2**-1.5935) * (model.pw2**0.2363) * (model.s2l**0.1079) + (2.5870000000000005e-4)*model.et2 - 247.963)/(1.0e8)) + ((5272.77*(model.aw3**1.2781) * (model.iw3**-0.1959) * (model.mf3**2.4242) * (model.tt3**0.38745) * (model.pw3**0.9904) + 181.806*(model.et3 / 1000.0 ) **0.539 + 232.57*(model.et3 / 1000.0 ) **0.772 + 0.49783215*(model.aw3**0.3322) * (model.mf3**-1.5935) * (model.pw3**0.2363) * (model.s3l**0.1079) - 0.22424514*(model.et3 / 100.0 ) **-1.33 + 20.708238*(model.et3 / 100.0 ) **0.498 + 0.001958*model.et3 - 32.591)/(1.0e8)) + ((47.040096*model.inw - 35.5)/(1.0e8)) + (((0.0030*model.pw1 + 0.0030*model.pw2 + 0.0030*model.pw3)**0.460)/(3.9215686e7)))

model.sgth1 = Constraint(expr=2.0*model.aw1 - model.iw1 == 0)
model.sgth3 = Constraint(expr=0.6*model.iw2 - model.aw2 == 0)
model.sgth5 = Constraint(expr=0.7*model.iw3 - model.aw3 == 0)
model.sgth2 = Constraint(expr=5.0*model.et1 - model.tt1 == 0)
model.sgth4 = Constraint(expr=5.0*model.et2 - model.tt2 == 0)
model.sgth6 = Constraint(expr=model.tt3 - model.et3 == 0)
model.sgsi1a = Constraint(expr=model.pw1 - 12.0*model.iw1>=0.0)
model.sgsi1b = Constraint(expr=model.pw1 - 17.0*model.iw1<=0.0)
model.sgsi2a = Constraint(expr=model.pw2 - 10.0*model.iw2>=0.0)
model.sgsi2b = Constraint(expr=model.pw2 - 13.0*model.iw2<=0.0)
model.sgsi3a = Constraint(expr=model.pw3 - 7.0*model.iw3>=0.0)
model.sgsi3b = Constraint(expr=model.pw3 - 10.0*model.iw3<=0.0)
model.ttiw1a = Constraint(expr=model.tt1 - 1.2*model.iw1 - 1.2*model.pw1 - 1.2*model.iw2 - 1.2*model.pw2 - 1.2*model.iw3 - 1.2*model.pw3 - 1.2*model.inw - 24.0 >=0.0)
model.ttiw1b = Constraint(expr=model.tt1 - 1.4*model.iw1 - 1.4*model.pw1 - 1.4*model.iw2 - 1.4*model.pw2 - 1.4*model.iw3 - 1.4*model.pw3 - 1.4*model.inw - 28.0<=0.0)
model.ttiw2a = Constraint(expr=model.tt2 - 0.6*model.iw2 - 0.6*model.pw2 - 0.6*model.iw3 - 0.6*model.pw3 - 0.6*model.inw - 12.0>=0.0)
model.ttiw2b = Constraint(expr=model.tt2 - 0.75*model.iw2 - 0.75*model.pw2 - 0.75*model.iw3 - 0.75*model.pw3 - 0.75*model.inw - 15.0<=0.0)
model.ttiw3a = Constraint(expr=model.tt3 - 0.7*model.iw3 - 0.7*model.pw3 - 0.7*model.inw - 14.0>=0.0)
model.ttiw3b = Constraint(expr=model.tt3 - 0.9*model.iw3 - 0.9*model.pw3 - 0.9*model.inw - 18.0<=0.0)
model.smf1 = Constraint(expr=(model.mf1) * (model.inw) + 20.0*model.mf1 - model.iw1 - model.iw2 - model.pw2 - model.iw3 - model.pw3 - model.inw - 20.0 == 0)
model.smf2 = Constraint(expr=(model.mf2) * (model.inw) + 20.0*model.mf2 - model.iw2 - model.iw3 - model.pw3 - model.inw - 20.0 == 0)
model.smf3 = Constraint(expr=(model.mf3) * (model.inw) + 20.0*model.mf3 - model.iw3 - model.inw - 20.0 == 0)
model.si1a = Constraint(expr=model.tt1 * model.bt1 - 240.0*model.pw1>=0.0)
model.si1b = Constraint(expr=model.tt1 * model.bt1 - 290.0*model.pw1<=0.0)
model.si2a = Constraint(expr=model.tt2 * model.bt2 - 240.0*model.pw2>=0.0)
model.si2b = Constraint(expr=model.tt2 * model.bt2 - 290.0*model.pw2<=0.0)
model.si3a = Constraint(expr=model.tt3 * model.bt3 - 340.0*model.pw3>=0.0)
model.si3b = Constraint(expr=model.tt3 * model.bt3 - 375.0*model.pw3<=0.0)
model.glgcon = Constraint(expr=0.0<=-32.0*(model.tt1 * model.bt1 * (log(model.mf1)) ) /model.pw1 - 32.0*(model.tt2 * model.bt2 * (log(model.mf2)) ) /model.pw2 - 32.0*(model.tt3 * model.bt3 * (log(model.mf3)) ) /model.pw3 - 35000.0 <= 15000.0)


