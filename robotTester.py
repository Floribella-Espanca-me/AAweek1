import time
import statistics

from Robot import *
#from lazyRobot import *
from RobotMatrix import *
from greedyRobot import greedyRobot



def measure(avrStepsToGoal,rewards,runTimes,runs,steps,seed):
    while 0 in avrStepsToGoal: avrStepsToGoal.remove(0)
    #print(str(avrStepsToGoal))
    averagerewardperstep = [x / steps for x in rewards]
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
    bp1 = ax1.boxplot(avrStepsToGoal,showmeans=True)
    ax1.set_xticklabels(
        ['Average Steps to Goal (seed=' + str(seed) + ' #runs=' + str(runs) + ' steps=' + str(steps) + ')'])
    #fig1.savefig('avrStepsToGoal.png', bbox_inches='tight')

    fig2 = plt.figure(2, figsize=(9, 6))
    ax2 = fig2.add_subplot(111)
    bp2 = ax2.boxplot(runTimes,showmeans=True)
    ax2.set_xticklabels(['RunTime (ms) (seed=' + str(seed) + ' #runs=' + str(runs) + ' steps=' + str(steps) + ')'])
    #fig2.savefig('runTime.png', bbox_inches='tight')


    fig3 = plt.figure(3, figsize=(9, 6))
    ax3 = fig3.add_subplot(111)
    bp3 = ax3.boxplot(rewards,showmeans=True)
    ax3.set_xticklabels(['Rewards (seed=' + str(seed) + ' #runs=' + str(runs) + ' steps=' + str(steps) + ')'])
    #fig3.savefig('Rewards.png', bbox_inches='tight')

    fig4 = plt.figure(4, figsize=(9, 6))
    ax4 = fig4.add_subplot(111)
    bp4 = ax4.boxplot(averagerewardperstep,showmeans=True)
    ax4.set_xticklabels(['Average Reward per Step (seed=' + str(seed) + ' #runs=' + str(runs) + ' steps=' + str(steps) + ')'])

    plt.show()


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
        runtime=(end-start)*1000
        runTimes.append(runtime)
        avrStepsToGoal.append(sum(WallE.stepsToGoal)/max(len(WallE.stepsToGoal),1))
        rewards.append(WallE.reward)

    measure(avrStepsToGoal,rewards,runTimes,runs,steps,seed)

def runEVA(runs, steps, testSpacing,testSteps,seed):
    nextseed=seed
    avrStepsToGoal=[]
    rewards=[]
    runTimes=[]
    testRewardPerStep=[]
    for i in range(runs):
        EVA=RobotMatrix()
        start=time.time()
        exe=EVA.runRobotWTest(steps,nextseed,testSpacing,testSteps)
        nextseed=exe[0]
        testRewardPerStep.append(exe[1])
        end=time.time()
        runtime=(end-start)*1000
        runTimes.append(runtime)
        avrStepsToGoal.append(sum(EVA.stepsToGoal) / max(len(EVA.stepsToGoal), 1))
        rewards.append(EVA.reward)
    EVA.matrix.printHeatMap()

    measure(avrStepsToGoal, rewards, runTimes, runs, steps, seed)
    measureTest(testRewardPerStep,testSpacing)


def measureTest(testRewardPerStep,spacing):
    averageRewardPerStep=[]
    stepsInExploration=[]
    for i in range(len(testRewardPerStep[0])):
        sum=0
        size=0
        for j in range(len(testRewardPerStep)):
            sum=sum+testRewardPerStep[j][i]
            size+=1
        averageRewardPerStep.append(sum/size)
        stepsInExploration.append(i*spacing)
    plt.scatter(stepsInExploration,averageRewardPerStep,marker='o')
    plt.xlabel('Steps Building the Matrix')
    plt.ylabel('Average Reward per Step')
    plt.grid()
    plt.show()

    #print("Reward per Step after "+str(spacing)+" matrix steps="+str(averageRewardPerStep))

def runMO(runs, steps, testSpacing,testSteps,seed):
    nextseed=seed
    avrStepsToGoal=[]
    rewards=[]
    runTimes=[]
    testRewardPerStep=[]
    for i in range(runs):
        MO=greedyRobot()
        start=time.time()
        exe=MO.runRobotWTest(steps,nextseed,testSpacing,testSteps)
        nextseed=exe[0]
        testRewardPerStep.append(exe[1])
        end=time.time()
        runtime=(end-start)*1000
        runTimes.append(runtime)
        avrStepsToGoal.append(sum(MO.stepsToGoal) / max(len(MO.stepsToGoal), 1))
        rewards.append(MO.reward)
    MO.matrix.printHeatMap()

    measure(avrStepsToGoal, rewards, runTimes, runs, steps, seed)
    measureTest(testRewardPerStep,testSpacing)



def runGreedyAlexa(runs,steps,seed,testSpacing,testSteps,greed):
    nextseed=seed
    avrStepsToGoal=[]
    rewards=[]
    runTimes=[]
    testRewardPerStep = []
    for i in range(runs):
        Alexa=greedyRobot(True,greed)
        start=time.time()
        exe=Alexa.runRobotWTest(steps,nextseed,testSpacing,testSteps)
        nextseed=exe[0]
        testRewardPerStep.append(exe[1])
        end=time.time()
        runtime=(end-start)*1000
        runTimes.append(runtime)
        avrStepsToGoal.append(sum(Alexa.stepsToGoal)/max(len(Alexa.stepsToGoal),1))
        rewards.append(Alexa.reward)

    Alexa.matrix.printHeatMap()
    measure(avrStepsToGoal,rewards,runTimes,runs,steps,seed)
    measureTest(testRewardPerStep, testSpacing)

def runSmartAlexa(runs,steps,seed,greed,greedIncrement,testSpacing,testSteps):
    nextseed = seed
    avrStepsToGoal = []
    rewards = []
    runTimes = []
    testRewardPerStep = []
    for i in range(runs):
        Alexa = greedyRobot(True, greed)
        start = time.time()
        exe=Alexa.runSmartGreedyRobot(steps,nextseed,greed,greedIncrement,testSpacing,testSteps)
        nextseed=exe[0]
        testRewardPerStep.append(exe[1])
        end = time.time()
        runtime = (end - start) * 1000
        runTimes.append(runtime)
        avrStepsToGoal.append(sum(Alexa.stepsToGoal) / max(len(Alexa.stepsToGoal), 1))
        rewards.append(Alexa.reward)

    Alexa.matrix.printHeatMap()
    measure(avrStepsToGoal, rewards, runTimes, runs, steps, seed)
    measureTest(testRewardPerStep, testSpacing)

def runSmartAlexaTHEWALL(runs,steps,seed,greed,greedIncrement,testSpacing,testSteps):
    nextseed = seed
    avrStepsToGoal = []
    rewards = []
    runTimes = []
    testRewardPerStep = []
    for i in range(runs):
        Alexa = greedyRobot(True, greed)
        start = time.time()
        exe=Alexa.runSmartGreedyRobotTHEWALL(steps,nextseed,greed,greedIncrement,testSpacing,testSteps)
        nextseed = exe[0]
        testRewardPerStep.append(exe[1])
        end = time.time()
        runtime = (end - start) * 1000
        runTimes.append(runtime)
        avrStepsToGoal.append(sum(Alexa.stepsToGoal) / max(len(Alexa.stepsToGoal), 1))
        rewards.append(Alexa.reward)

    Alexa.matrix.printHeatMap()
    measure(avrStepsToGoal, rewards, runTimes, runs, steps, seed)
    measureTest(testRewardPerStep, testSpacing)


def listavr(list):
    return sum(list) / max(len(list), 1)