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

import shutil
import random

#Reference data file containing all deterministic data
fname_det = 'DeterministicData.dat'

#Problem data
numMachineTypes = 27;
numWaferTypes = 10;

# ArcData [(i,j),arcNumber,revenue,cost,demandtype]
prodTimes = [(('W1','S1','M1'),5),
(('W1','S2','M4'),2),
(('W1','S4','M8'),4),
(('W1','S1','M2'),7),
(('W1','S2','M5'),2),
(('W1','S4','M9'),4),
(('W1','S1','M27'),4),
(('W1','S3','M6'),5),
(('W1','S4','M10'),4),
(('W1','S2','M3'),3),
(('W1','S3','M7'),4),
(('W2','S1','M2'),6),
(('W2','S3','M11'),3),
(('W2','S2','M3'),3),
(('W2','S3','M12'),3),
(('W2','S2','M4'),2),
(('W2','S4','M13'),6),
(('W2','S1','M1'),4),
(('W2','S2','M5'),2),
(('W2','S4','M14'),7),
(('W3','S1','M15'),5),
(('W3','S3','M6'),5),
(('W3','S1','M16'),6),
(('W3','S3','M7'),5),
(('W3','S2','M17'),4),
(('W3','S4','M8'),3),
(('W3','S2','M18'),3),
(('W3','S4','M10'),5),
(('W4','S1','M1'),7),
(('W4','S2','M18'),4),
(('W4','S4','M14'),8),
(('W4','S1','M15'),5),
(('W4','S3','M11'),5),
(('W4','S1','M27'),4),
(('W4','S3','M12'),3),
(('W4','S2','M3'),3),
(('W4','S4','M13'),6),
(('W5','S2','M4'),2),
(('W5','S4','M8'),8),
(('W5','S1','M2'),8),
(('W5','S2','M5'),3),
(('W5','S4','M14'),9),
(('W5','S1','M16'),7),
(('W5','S3','M6'),5),
(('W5','S2','M3'),3),
(('W5','S3','M7'),6),
(('W6','S1','M16'),7),
(('W6','S3','M19'),10),
(('W6','S2','M4'),3),
(('W6','S3','M20'),11),
(('W6','S1','M2'),4),
(('W6','S2','M5'),2),
(('W6','S4','M21'),3),
(('W6','S1','M15'),5),
(('W6','S2','M17'),4),
(('W6','S4','M22'),4),
(('W7','S1','M15'),3),
(('W7','S2','M5'),5),
(('W7','S4','M22'),4),
(('W7','S6','M18'),4),
(('W7','S1','M16'),2),
(('W7','S3','M23'),2),
(('W7','S5','M1'),6),
(('W7','S7','M8'),6),
(('W7','S2','M3'),5),
(('W7','S3','M24'),2),
(('W7','S5','M2'),5),
(('W7','S7','M10'),5),
(('W7','S2','M4'),4),
(('W7','S4','M21'),3),
(('W7','S6','M17'),3),
(('W8','S1','M2'),3),
(('W8','S2','M24'),10),
(('W8','S4','M9'),4),
(('W8','S6','M21'),3),
(('W8','S1','M15'),3),
(('W8','S3','M11'),3),
(('W8','S4','M10'),3),
(('W8','S6','M22'),5),
(('W8','S1','M16'),3),
(('W8','S3','M12'),7),
(('W8','S5','M25'),6),
(('W8','S7','M13'),5),
(('W8','S1','M1'),3),
(('W8','S2','M23'),6),
(('W8','S4','M8'),8),
(('W8','S5','M26'),4),
(('W8','S7','M14'),7),
(('W9','S1','M1'),5),
(('W9','S3','M6'),6),
(('W9','S5','M3'),4),
(('W9','S7','M21'),4),
(('W9','S1','M15'),6),
(('W9','S3','M11'),4),
(('W9','S5','M5'),3),
(('W9','S7','M22'),5),
(('W9','S2','M3'),3),
(('W9','S4','M25'),7),
(('W9','S6','M8'),4),
(('W9','S2','M17'),3),
(('W9','S4','M26'),5),
(('W9','S6','M14'),6),
(('W10','S2','M4'),2),
(('W10','S4','M12'),4),
(('W10','S6','M26'),4),
(('W10','S2','M18'),3),
(('W10','S5','M4'),2),
(('W10','S7','M8'),8),
(('W10','S1','M2'),9),
(('W10','S3','M7'),5),
(('W10','S5','M5'),4),
(('W10','S7','M9'),7),
(('W10','S1','M16'),8),
(('W10','S4','M11'),3),
(('W10','S6','M25'),7),
(('W10','S7','M10'),6)]

numProdTimes = len(prodTimes)

demandCMF = [0, 0.1, 0.2, 0.5, 0.9, 1.0]
demandLevels = [ 75, 100, 125, 150, 175]
numDemandLevels = len(demandLevels)

numSamples = 100
sampleProdTimes = [0 for i in range(numProdTimes)]
demand = [0 for i in range(numWaferTypes)]

#Write data files for each scenario
for s in range(numSamples):
    
    #Initialize each scenario random production times
    
    for i in range(numProdTimes):
        rand = random.random()
        if rand < .5:
            factor = .75
        else:
            factor = 1.25
        sampleProdTimes[i] = factor*prodTimes[i][1]

    fname = 'Scenario' + str(s+1) + '.dat'
    shutil.copyfile(fname_det, fname)
    f = open(fname,'a')
    f.write('\n\n#Sample production times' + str(s+1) + '\n')
    f.write('param ProdTime default 0.0 :=\n')
    for i in range(numProdTimes):
        f.write(prodTimes[i][0][0] + ' ' + prodTimes[i][0][1] + ' ' + prodTimes[i][0][2] + ' ' + str(sampleProdTimes[i])  + '\n')
    f.write(';')
    
    #Initialize each scenario random demands
    for i in range(numWaferTypes):
        rand = random.random()
        for k in range(numDemandLevels):
            if demandCMF[k] < rand and rand <= demandCMF[k+1]:
                demand[i] = [i+1,demandLevels[k]]
                
    f.write('\n\n#Wafer demands' + str(s+1) + '\n')
    f.write('param Demand default 0.0 :=\n')
    for i in range(numWaferTypes):
        f.write('W' + str(demand[i][0]) + ' ' + str(demand[i][1])  + '\n')
    f.write(';')
    
    f.close
