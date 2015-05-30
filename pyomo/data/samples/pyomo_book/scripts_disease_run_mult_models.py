from pyomo.environ import *
from pyutilib.misc import Options
from DiseaseEasy import model as easy_model
from DiseaseHard import model as hard_model

easy_instance = easy_model.create('DiseaseEstimation.dat')
hard_instance = hard_model.create('DiseaseEstimation.dat')

options = Options()
options.solver = 'ipopt'
options.quiet = True

# solve the easier problem
results, opt = scripting.util.apply_optimizer(options, easy_instance)

# load the results into the hard instance to provide
# a good initial point
hard_instance.load(results)

# solve the hard problem with the new initialization
results, opt = scripting.util.apply_optimizer(options, hard_instance)

# print the final results
print results
