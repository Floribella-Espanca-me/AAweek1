from Thing import *
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





