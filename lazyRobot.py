import RewardMatrix
from ScenarioRules import *

class lazyRobot:

    global goalPos
    goalPos = 100
    global startPos
    startPos = 1

    def __init__(self,matrix):
        self.reward=0
        self.position=1
        self.stepsToGoal=[]
        self.currentStep=0
        self.matrix=matrix

    def runRobot(self, steps, seed):
        nextseed = seed
        for i in range(steps):
            nextseed = self.lazyStep(nextseed)

        return nextseed

    def lazyStep(self,seed):
        bestness = self.bestAction(seed)
        pos = bestness[0]
        #print(str(pos))
        nextseed = bestness[1]
        self.position = f(self.position, pos)
        self.currentStep+=1
        self.reward =self.reward+rewardPos(self.position)
        #print(self.position)
        if(self.position==goalPos):
            #print('CHEGUEI')
            self.position=startPos
            self.stepsToGoal.append(self.currentStep)
            self.currentStep=0
        return nextseed

    def bestAction(self,seed):
        directional=self.matrix.bestAction(self.position,seed)[0]
        nextseed=self.matrix.bestAction(self.position,seed)[1]
        return [directional,nextseed]




