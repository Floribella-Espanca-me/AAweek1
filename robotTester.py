import numpy as np
import matplotlib.pyplot as plt
import time
import statistics
from Robot import *



def runWallE(runs,steps,seed):
    #TODO codigo muito feio, mas é só prints, arranjar?
    nextseed=seed
    avrStepsToGoal=[]
    rewards=[]
    runTimes=[]
    for i in range(runs):
        WallE=Robot()

        #print('Wall-E #' + str(i))
        #print('     seed: ' + str(nextseed))

        start=time.time()

        nextseed=WallE.runRobot(steps,nextseed)

        end=time.time()
        runtime=end-start
        runTimes.append(runtime*1000)

        avrStepsToGoal.append(sum(WallE.stepsToGoal)/max(len(WallE.stepsToGoal),1))
        rewards.append(WallE.reward)

        #print('     Reward='+str(WallE.reward))
        #print('     Average Step To Goal=' + str(avrStepsToGoal[i]))

    avrStepsToGoal.remove(0)
    print('GLOBAL REPORT:')
    print(' Seed='+str(seed))
    print('     Rewards:')
    print('            Average='+str(listavr(rewards)))
    print('            Standard-Deviation=' + str(statistics.stdev(rewards)))
    print('     Steps to Goal:')
    print('            Average=' + str(listavr(avrStepsToGoal)))
    print('            Standard-Deviation=' + str(statistics.stdev(avrStepsToGoal)))
    print('     Runtime(ms):')
    print('            Average:' + str(listavr(runTimes)))
    print('            Standard-Deviation:' + str(statistics.stdev(runTimes)))

    fig1 = plt.figure(1, figsize=(9, 6))
    ax1 = fig1.add_subplot(111)
    bp1 = ax1.boxplot(avrStepsToGoal)
    ax1.set_xticklabels(['Average Steps to Goal (seed='+str(seed)+' #runs='+str(runs)+' steps=' +str(steps)+')'])
    fig1.savefig('avrStepsToGoal.png', bbox_inches='tight')

    fig2 = plt.figure(2, figsize=(9, 6))
    ax2 = fig2.add_subplot(111)
    bp2 = ax2.boxplot(runTimes)
    ax2.set_xticklabels(['RunTime (ms) (seed='+str(seed)+' #runs='+str(runs)+' steps=' +str(steps)+')'])
    fig2.savefig('runTime.png', bbox_inches='tight')

    fig3 = plt.figure(3, figsize=(9, 6))
    ax3 = fig3.add_subplot(111)
    bp3 = ax3.boxplot(rewards)
    ax3.set_xticklabels(['Rewards (seed='+str(seed)+' #runs='+str(runs)+' steps=' +str(steps)+')'])
    fig3.savefig('Rewards.png', bbox_inches='tight')

def listavr(list):
    return sum(list) / max(len(list), 1)