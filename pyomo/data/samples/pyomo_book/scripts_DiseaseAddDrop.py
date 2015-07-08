from pyomo.environ import *
from pyutilib.misc import Options

model = AbstractModel()

model.S_SI = Set(ordered=True)

model.P_REP_CASES = Param(model.S_SI)
model.P_POP = Param()

model.I = Var(model.S_SI, bounds=(0,model.P_POP), initialize=1)
model.S = Var(model.S_SI, bounds=(0,model.P_POP), initialize=300)
model.beta = Var(bounds=(0.05, 70))
model.alpha = Var(bounds=(0.5, 1.5))
model.eps_I = Var(model.S_SI, initialize=0.0)

def _objective(model):
    return sum((model.eps_I[i])**2 for i in model.S_SI)
model.objective = Objective(rule=_objective, sense=minimize)

def _InfDynamics(model, i):
    if i != 1:
        return model.I[i] == (model.beta * model.S[i-1] * model.I[i-1]**model.alpha)/model.P_POP
    return Constraint.Skip
model.InfDynamics = Constraint(model.S_SI, rule=_InfDynamics)

def _EasierInfDynamics(model, i):
    if i != 1:
        return model.I[i] == (model.beta * model.S[i-1] * model.P_REP_CASES[i-1])/model.P_POP
    return Constraint.Skip
model.EasierInfDynamics = Constraint(model.S_SI, rule=_EasierInfDynamics)

def _SusDynamics(model, i):
    if i != 1:
        return model.S[i] == model.S[i-1] - model.I[i]
    return Constraint.Skip
model.SusDynamics = Constraint(model.S_SI, rule=_SusDynamics)

def _Data(model, i):
    return model.P_REP_CASES[i] == model.I[i]+model.eps_I[i]
model.Data = Constraint(model.S_SI, rule=_Data)

instance = model.create('DiseaseEstimation.dat');

options = Options()
options.solver = 'ipopt'
options.quiet = True

# disable the hard constraints
instance.InfDynamics.deactivate()

# solve the problem with the easy constraints
print "*** Solving the \"easy\" problem"
results, opt = scripting.util.apply_optimizer(options, instance)

# load the results so that they become the initial conditions 
# for the more difficult solve
instance.load(results)
print "beta from easy problem: " + str(instance.beta.value)
print "alpha from easy problem: " + str(instance.alpha.value)
print

# enable the hard constraints and 
# disable the easy constraints
instance.InfDynamics.activate()
instance.EasierInfDynamics.deactivate()

# solve the problem with the hard constraints
print "*** Solving the \"hard\" problem"
results, opt = scripting.util.apply_optimizer(options, instance)
instance.load(results)
print "beta from hard problem: " + str(instance.beta.value)
print "alpha from hard problem: " + str(instance.alpha.value)

