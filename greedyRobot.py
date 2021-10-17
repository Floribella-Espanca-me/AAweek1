from lazyRobot import lazyRobot

from RewardMatrix import *
from ScenarioRules import *
import math

class greedyRobot:

    global goalPos
    goalPos=100
    global startPos
    startPos=1

    def __init__(self,greedy=False,greed=0.9):
        self.reward = 0
        self.position = 1
        self.stepsToGoal = []
        self.currentStep = 0
        self.matrix = RewardMatrix()
        self.greedy=greedy
        self.greed=greed

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
        return [nextseed,testRewardResult]

    def changeGreed(self,greed):
        if not self.greedy:
            print("im not greedy >:(")
        else:
            self.greed=greed

    def runSmartGreedyRobot(self,steps,seed,initialGreed,percentageChange,spacing,testSteps):
        nextseed=seed
        firstchange= math.ceil(steps * percentageChange)
        testRewardResult = []
        self.changeGreed(initialGreed)
        for i in range(firstchange):
            nextseed=self.matrixStep(nextseed)
            if i%spacing==0:
                #print(i)
                MO = lazyRobot(self.matrix)
                nextseed = MO.runRobot(testSteps, nextseed)
                testRewardResult.append(MO.reward/testSteps)
        increasePerStep=(1-initialGreed)/(steps-firstchange)
        for j in range(steps-firstchange):
            nextseed = self.matrixStep(nextseed)
            if j%spacing==0:
                #print(i)
                MO = lazyRobot(self.matrix)
                nextseed = MO.runRobot(testSteps, nextseed)
                testRewardResult.append(MO.reward/testSteps)
            self.changeGreed(self.greed+increasePerStep)
        return [nextseed,testRewardResult]

    def runSmartGreedyRobotTHEWALL(self,steps,seed,initialGreed,percentageChange,spacing,testSteps):
        nextseed=seed
        firstchange= math.ceil(steps * percentageChange)
        testRewardResult = []
        self.changeGreed(initialGreed)
        for i in range(firstchange):
            nextseed=self.matrixStepTHEWALL(nextseed)
            if i%spacing==0:
                #print(i)
                MO = lazyRobot(self.matrix)
                nextseed = MO.runRobot(testSteps, nextseed)
                testRewardResult.append(MO.reward/testSteps)
        increasePerStep=(1-initialGreed)/(steps-firstchange)
        for j in range(steps-firstchange):
            nextseed = self.matrixStepTHEWALL(nextseed)
            self.changeGreed(self.greed+increasePerStep)
            if j%spacing==0:
                #print(i)
                MO = lazyRobot(self.matrix)
                nextseed = MO.runRobot(testSteps, nextseed)
                testRewardResult.append(MO.reward/testSteps)
        return [nextseed,testRewardResult]

    def matrixStepTHEWALL(self,seed):
        action=[]
        pos='something'
        nextseed=seed

        if not self.greedy:
            action = self.bestAction(nextseed)
            pos = action[0]
            nextseed = action[1]
        else:
            random.seed(nextseed)
            r=random.random()
            nextseed=r
            if r>self.greed:
                action = randomAction(nextseed)
                pos = action[0]
                nextseed = action[1]
            else:
                action = self.bestAction(nextseed)
                pos = action[0]
                nextseed = action[1]
        #print(pos)
        nextposition = self.matrix.updatePositionTHEWALL(self.position,pos)
        self.currentStep+=1
        self.reward =self.reward+rewardPosTHEWALL(self.position,nextposition)
        self.position=nextposition

        #print(self.position)
        if(self.position==goalPos):
            self.position=startPos
            self.stepsToGoal.append(self.currentStep)
            self.currentStep=0
        return nextseed

    def matrixStep(self,seed):
        action=[]
        pos='something'
        nextseed=seed

        if not self.greedy:
            action = self.bestAction(nextseed)
            pos = action[0]
            nextseed = action[1]
        else:
            random.seed(nextseed)
            r=random.random()
            nextseed=r
            if r>self.greed:
                action = randomAction(nextseed)
                pos = action[0]
                nextseed = action[1]
            else:
                action = self.bestAction(nextseed)
                pos = action[0]
                nextseed = action[1]
        #print(pos)
        self.position = self.matrix.updatePosition(self.position,pos)
        self.currentStep+=1
        self.reward =self.reward+rewardPos(self.position)
        #print(self.position)
        if(self.position==goalPos):
            self.position=startPos
            self.stepsToGoal.append(self.currentStep)
            self.currentStep=0
        return nextseed


    def bestAction(self,seed):
        directional=self.matrix.bestAction(self.position,seed)[0]
        nextseed=self.matrix.bestAction(self.position,seed)[1]
        return [directional,nextseed]

