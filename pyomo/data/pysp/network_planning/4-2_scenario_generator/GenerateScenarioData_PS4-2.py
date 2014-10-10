import shutil
import random

#Reference data file containing all deterministic data
fname_det = 'DeterministicData.dat'

#Problem data
numDemand = 10
numArcs = 7

demandCMF=[[0,0.05,0.25,0.75,0.95,0.95,1.0],
           [0,0.1,0.5,0.9,1.0,1.0,1.0]]
demandType= [1,2,2,2,1,1,1,2,2,2]

demandLevels = [ 0, 1, 2, 3, 4, 5]
numDemandLevels = len(demandLevels)



arcType = [1,2,1,2,1,1,2]  #1 is 70% reliable, 2 is %100 reliable

demand = [0 for i in range(numDemand)]  
r = [0 for i in range(numArcs)]
             
numSamples = 2000
#Write data files for each scenario
for s in range(numSamples):
    
    #Initialize each scenario demand
    
    for i in range(numDemand):
        rand = random.random()
        if demandType[i] == 1:
            for k in range(numDemandLevels):
                if demandCMF[0][k] < rand and rand <= demandCMF[0][k+1]:
                    demand[i] = demandLevels[k]
        elif demandType[i] == 2:
            for k in range(numDemandLevels):
                if demandCMF[1][k] < rand and rand <= demandCMF[1][k+1]:
                    demand[i] = demandLevels[k]


    fname = 'Scenario' + str(s+1) + '.dat'
    shutil.copyfile(fname_det, fname)
    f = open(fname,'a')
    f.write('\n\n#point to point demand' + str(s+1) + '\n')
    f.write('param ppDemand :=\n')
    for i in range(numDemand):
        f.write('I' + str(i+1) + ' ' + str(demand[i]) + '\n')
    f.write(';')
    
    #Initialize each scenario arc reliability
    for i in range(numArcs):
        if arcType[i] == 1:
            rand = random.random()
            if rand < .7:
                r[i] = 1
            else:
                r[i] = 0
        elif arcType[i] == 2:
            r[i] = 1
                
    f.write('\n\n#Arc reliability' + str(s+1) + '\n')
    f.write('param R :=\n')
    for i in range(numArcs):
        f.write('K' + str(i+1) + ' ' + str(r[i])  + '\n')
    f.write(';')
    
    f.close
