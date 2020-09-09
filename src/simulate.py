import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from population import Population
from landscape import NKLandscape

k = int(sys.argv[1])
reps = int(sys.argv[2])

# Params
popsize = 50
n = 15
lamarckian = False
genesize = n
recombProb = 0.5
mutatProb = 1/n
eliteprop = 0.1

if len(sys.argv) > 3:
    steep_checks = int(sys.argv[3])
else:
    steep_checks = n

learnConds = [0,1,4,9,19,49,100]
reproduceConds = [100,50,20,10,5,2,0]
condNum = len(learnConds)
conditions = list(zip(learnConds, reproduceConds))
totalTime = 100

# Save directory
saveDir = 'nonlamarckian'
if not os.path.exists(saveDir):
    os.mkdir(saveDir)

# Data structure
best_fitnesses = np.zeros((reps, condNum, totalTime))
avg_fitnesses = np.zeros((reps, condNum, totalTime))

def constructSchedule(numLearn, numRepr, totalTime):
    '''
    Returns a binary list of size totalTime, where 0 indicates
    a learning event and 1 indicates a reproduction event
    '''
    schedule = []
    if numRepr == 0:
        schedule = [0] * totalTime
    else:
        for repEvent in range(numRepr):
            for learnEvent in range(numLearn):
                schedule.append(0)
            schedule.append(1)

    return schedule


for rep in range(reps):
    # Reset the landscape for each repitition
    landscape = NKLandscape(n, k)

    for cond, (numLearn, numRepr) in enumerate(conditions):
        pop = Population(popsize, genesize, landscape, recombProb, mutatProb, eliteprop, lamarckian, steep_checks)
        schedule = constructSchedule(numLearn, numRepr, totalTime)

        for step, event in enumerate(schedule):
            if event == 0:
                pop.steepLearn()
            elif event == 1:
                pop.reproduce()

            best_fitnesses[rep][cond][step], avg_fitnesses[rep][cond][step] = pop.stats()


np.save(os.path.join(saveDir, "bh_{}_{}.npy".format(k, steep_checks)), best_fitnesses)
np.save(os.path.join(saveDir, "ah_{}_{}.npy".format(k, steep_checks)), avg_fitnesses)
