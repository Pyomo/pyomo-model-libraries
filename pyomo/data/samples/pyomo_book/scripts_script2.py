from pyomo.core import DataPortal
from pyomo.opt import SolverFactory
from DiseaseEstimation import model

model.pprint()

data = DataPortal(model=model)
data.load(filename='DiseaseEstimation.dat')
data.load(filename='DiseasePop.dat')

instance = model.create(data)
instance.pprint()

opt = SolverFactory("ipopt")
results = opt.solve(instance)

results.write()
