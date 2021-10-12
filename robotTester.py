import numpy as np
import matplotlib.pyplot as plt
import time
import statistics
from Robot import *
#from lazyRobot import *
from RobotMatrix import *
from greedyRobot import greedyRobot



def measure(avrStepsToGoal,rewards,runTimes,runs,steps,seed):
    avrStepsToGoal.remove(0)
    print('GLOBAL REPORT:')
    print(' Seed=' + str(seed))
    print(' #Runs=' +str(runs))
    print(' #Steps='+str(steps))
    print('     Rewards:')
    print('            Average=' + str(listavr(rewards)))
    print('            Standard-Deviation=' + str(statistics.stdev(rewards)))
    print('            AverageRewardPerStep='+str(listavr(rewards)/steps))
    print('     Steps to Goal:')
    print('            Average=' + str(listavr(avrStepsToGoal)))
    print('            Standard-Deviation=' + str(statistics.stdev(avrStepsToGoal)))
    print('     Runtime(ms):')
    print('            Average:' + str(listavr(runTimes)))
    print('            Standard-Deviation:' + str(statistics.stdev(runTimes)))

    fig1 = plt.figure(1, figsize=(9, 6))
    ax1 = fig1.add_subplot(111)
    bp1 = ax1.boxplot(avrStepsToGoal)
    ax1.set_xticklabels(
        ['Average Steps to Goal (seed=' + str(seed) + ' #runs=' + str(runs) + ' steps=' + str(steps) + ')'])
    fig1.savefig('avrStepsToGoal.png', bbox_inches='tight')

    fig2 = plt.figure(2, figsize=(9, 6))
    ax2 = fig2.add_subplot(111)
    bp2 = ax2.boxplot(runTimes)
    ax2.set_xticklabels(['RunTime (ms) (seed=' + str(seed) + ' #runs=' + str(runs) + ' steps=' + str(steps) + ')'])
    fig2.savefig('runTime.png', bbox_inches='tight')

    fig3 = plt.figure(3, figsize=(9, 6))
    ax3 = fig3.add_subplot(111)
    bp3 = ax3.boxplot(rewards)
    ax3.set_xticklabels(['Rewards (seed=' + str(seed) + ' #runs=' + str(runs) + ' steps=' + str(steps) + ')'])
    fig3.savefig('Rewards.png', bbox_inches='tight')


def runWallE(runs,steps,seed):
    nextseed=seed
    avrStepsToGoal=[]
    rewards=[]
    runTimes=[]
    for i in range(runs):
        WallE=Robot()
        start=time.time()
        nextseed=WallE.runRobot(steps,nextseed)
        end=time.time()
        runtime=end-start
        runTimes.append(runtime*1000)
        avrStepsToGoal.append(sum(WallE.stepsToGoal)/max(len(WallE.stepsToGoal),1))
        rewards.append(WallE.reward)

    measure(avrStepsToGoal,rewards,runTimes,runs,steps,seed)

def runMO(stepsBuild,stepsrun,seed):
    nextseed = seed
    EVA = RobotMatrix()
    EVA.runRobot(stepsBuild, nextseed)
    matrix = EVA.matrix
    matrix.printHeatMap()
    MO=lazyRobot(matrix)
    nextseed=MO.runRobot(stepsrun,nextseed)
    print(str(MO.reward))

def runAlexa(steps,seed):
    nextseed=seed
    Alexa=greedyRobot()
    nextseed=Alexa.runRobot(steps,nextseed)
    print(str(Alexa.reward))
    Alexa.matrix.printHeatMap()

def runGreedyAlexa(steps,seed,greed):
    nextseed=seed
    Alexa=greedyRobot(True,greed)
    nextseed=Alexa.runRobot(steps,nextseed)
    print(str(Alexa.reward))
    Alexa.matrix.printHeatMap()

def runSmartAlexa(steps,seed,greed,greedIncrement):
    nextseed=seed
    Alexa=greedyRobot(True,greed)
    nextseed=Alexa.runSmartGreedyRobot(steps,nextseed,greed,greedIncrement)
    Alexa.matrix.printHeatMap()

def runSmartAlexaTHEWALL(steps,seed,greed,greedIncrement):
    nextseed=seed
    Alexa=greedyRobot(True,greed)
    nextseed=Alexa.runSmartGreedyRobotTHEWALL(steps,nextseed,greed,greedIncrement)
    Alexa.matrix.printHeatMap()


def listavr(list):
    return sum(list) / max(len(list), 1)