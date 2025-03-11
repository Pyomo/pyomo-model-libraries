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

'''
Created on Dec 2, 2010

@author: kiel.martin
'''

import numpy #http://www.lfd.uci.edu/~gohlke/pythonlibs/
import shutil

#Reference data file containing all deterministic data
fname_det = 'DeterministicData.dat'

#Problem data
numTimes = 5
numPeriods = 4
numLevels = 3
numSamples = 81
levels = [0.05, 0.10, 0.15]
#damage = [range(numPeriods)][range(numLevels)]
count = 0


#Initialize set of scenarios 
for i in range(numLevels):
    for j in range(numLevels):
        for k in range(numLevels):
            for m in range(numLevels):
                count += 1
                fname = 'Scenario' + str(count) + '.dat'
                shutil.copyfile(fname_det, fname)
                f = open(fname,'a')
                f.write('\n #Stochastic Data \n')
                f.write('param damage1 := \n')
                f.write('0 ;\n') #no damage at initial time
                f.write('param damage2 := \n')
                f.write(str(levels[i]) + ';\n')
                f.write('param damage3 := \n')
                f.write(str(levels[j]) + ';\n')
                f.write('param damage4 := \n')
                f.write(str(levels[k]) + ';\n')
                f.write('param damage5 := \n')
                f.write(str(levels[m]) + ';\n')
                f.close
