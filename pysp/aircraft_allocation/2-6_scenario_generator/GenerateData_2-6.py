#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2025
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________


import numpy #http://www.lfd.uci.edu/~gohlke/pythonlibs/
import shutil

#Reference data file containing all deterministic data
fname_det = 'DeterministicData.dat'

#Problem data
numRoutes = 5;
numSamples = 100;
d_min = [200, 50, 140, 10, 580]
d_max = [300, 150, 220, 340, 620]
discDemand = range(numRoutes)

#Initialize set of scenarios 
for i in range(numRoutes):
    discDemand[i] = numpy.linspace( d_min[i], d_max[i], numSamples) # 100 numbers from d_min t0 d_max

#Write data files for each scenario
for i in range(numSamples):
    fname = 'Scenario' + str(i+1) + '.dat'
    shutil.copyfile(fname_det, fname)
    f = open(fname,'a')
    f.write('\n\n#Demand' + str(i+1) + '\n')
    f.write('param D :=\n')
    for j in range(numRoutes):
        f.write('R' + str(j+1) + ' ' + str(discDemand[j][i]) + '\n')
    f.write(';')
    f.close
    print fname
