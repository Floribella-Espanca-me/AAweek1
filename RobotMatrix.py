from lazyRobot import lazyRobot

from ScenarioRules import *
from RewardMatrix import *

class RobotMatrix:

    global goalPos
    goalPos=100
    global startPos
    startPos=1

    def __init__(self):
        self.reward=0
        self.position=1
        self.stepsToGoal=[]
        self.currentStep=0
        self.matrix=RewardMatrix()


    def runRobot(self,steps,seed):
        nextseed=seed
        for i in range(steps):
            nextseed=self.matrixStep(nextseed)
        return nextseed

    def runRobotWTest(self,steps,seed,spacing,testSteps):
        nextseed=seed
        testRewardResult=[]
        for i in range(steps):
            nextseed=self.matrixStep(nextseed)
            if i%spacing==0:
                #print(i)
                MO = lazyRobot(self.matrix)
                nextseed = MO.runRobot(testSteps, nextseed)
                testRewardResult.append(MO.reward/testSteps)
            #if i==2750:
                #self.matrix.printHeatMap()
            #if i == 5000:
                #self.matrix.printHeatMap()
        return [nextseed,testRewardResult]

    def matrixStep(self,seed):
        randomness = randomAction(seed)
        pos = randomness[0]
        nextseed = randomness[1]
        self.position = self.matrix.updatePosition(self.position,pos)
        self.currentStep+=1
        self.reward =self.reward+rewardPos(self.position)
        #print(self.position)
        if(self.position==goalPos):
            self.position=startPos
            self.stepsToGoal.append(self.currentStep)
            self.currentStep=0
        return nextseed





