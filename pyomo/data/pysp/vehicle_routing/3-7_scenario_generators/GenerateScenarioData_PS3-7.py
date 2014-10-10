'''
Created on Dec 2, 2010

@author: kiel.martin
'''

import random
import shutil

#Reference data file containing all deterministic data
fname_det = 'DeterministicData.dat'

#Problem data

# ArcData [(i,j),arcNumber,revenue,cost,demandtype]
arcData = [((1,11),1,327,81,4),
((1,6),2,211,67,10),
((1,7),3,243,70,1),
((1,8),4,268,70,7),
((2,11),5,301,75,10),
((2,6),6,204,73,3),
((2,12),7,356,95,8),
((2,7),8,190,63,5),
((2,8),9,225,69,1),
((3,7),10,198,66,1),
((3,12),11,343,85,2),
((3,8),12,261,80,3),
((3,9),13,255,73,7),
((4,8),14,265,76,3),
((4,13),15,360,105,9),
((4,9),16,161,60,10),
((4,10),17,264,78,8),
((5,14),18,348,86,10),
((5,10),19,267,78,8),
((6,11),20,146,54,7),
((6,15),21,330,86,4),
((6,16),22,352,93,2),
((6,12),23,188,61,6),
((7,11),24,225,74,3),
((7,12),25,177,63,9),
((7,13),26,348,91,10),
((8,12),27,148,51,10),
((8,16),28,312,76,8),
((8,17),29,332,83,9),
((8,13),30,284,75,3),
((9,13),31,317,76,6),
((9,18),32,367,103,6),
((9,14),33,329,81,2),
((10,14),34,214,65,9),
((10,19),35,326,78,1),
((11,15),36,263,93,4),
((11,16),37,285,98,7),
((12,15),38,281,99,7),
((12,16),39,242,87,1),
((12,17),40,301,108,6),
((13,16),41,277,93,4),
((13,17),42,168,77,5),
((13,18),43,175,78,7),
((14,17),44,273,94,8),
((14,18),45,252,87,3),
((14,19),46,252,88,2),
((15,20),47,0,0,11),
((16,20),48,0,0,11),
((17,20),49,0,0,11),
((18,20),50,0,0,11),
((19,20),51,0,0,11)]

numArcs = len(arcData)

#DemandPMF's by type
DemandPMF=[[0.4 ,0.3, 0.3 , 0.0,0.0],
           [0.40,0.25,0.20,0.15,0.0],
           [0.35,0.25,0.2 ,0.2 ,0],
           [0.3 ,0.25,0.2 ,0.15,0.1],
           [0.35,0.2 ,0.15,0.15,0.15],
           [0.0 ,0.45,0.35,0.2 ,0],
           [0.0 ,0.4 ,0.35,0.25,0],
           [0.0 ,0.45,0.2 ,0.2 ,0.15],
           [0.0 ,0.4 ,0.25,0.2 ,0.15],
           [0.0 ,0.0 ,0.4 ,0.3 ,0.3],
           [1.0 ,0.0 ,0.0 ,0.0 ,0.0]]

numDemandTypes = len(DemandPMF[:])
numDemandLevels = len(DemandPMF[0][:])

DemandCMF = [[0 for i in range(numDemandLevels+1)] for j in range(numDemandTypes)]

for i in range(numDemandTypes):
    DemandCMF[i][0] = 0
    DemandCMF[i][1] = DemandPMF[i][0]
    
for i in range(numDemandTypes):
    for j in range(1,numDemandLevels):
        DemandCMF[i][j+1] = DemandPMF[i][j] + DemandCMF[i][j]
#    print DemandCMF[i] 
    


numSamples = 500
arcDemand = [0 for i in range(numArcs)]

#for i in range(numArcs):
#    for j in range(numDemandTypes):
#        if arcData[i][4] == j+1:
#            rand = random.random()
#            print rand
#            for k in range(numDemandLevels):
#                if DemandCMF[j][k] < rand and rand <= DemandCMF[j][k+1]:
#                    arcDemand[i] = [arcData[i][0],k]
#                    print arcDemand[i]      

#Write data files for each scenario
for s in range(numSamples):
    
    #Initialize each scenario random demands
    for i in range(numArcs):
        for j in range(numDemandTypes):
            if arcData[i][4] == j+1:
                rand = random.random()
                for k in range(numDemandLevels):
                    if DemandCMF[j][k] < rand and rand <= DemandCMF[j][k+1]:
                        arcDemand[i] = [arcData[i][0],k]
#                        print arcDemand[i]

    fname = 'Scenario' + str(s+1) + '.dat'
    shutil.copyfile(fname_det, fname)
    f = open(fname,'a')
    f.write('\n\n#Demand' + str(s+1) + '\n')
    f.write('param ArcDemand default 0.0 :=\n')
    for i in range(numArcs-5):
        f.write(str(arcDemand[i][0][0]) + ' ' + str(arcDemand[i][0][1]) + ' ' + str(arcDemand[i][1])  + '\n')
    f.write(';')
    f.close
