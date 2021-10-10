from Thing import *

class Robot:

    global goalPos
    goalPos=100
    global startPos
    startPos=1

    def __init__(self):
        self.reward=0
        self.position=1
        self.stepsToGoal=[]
        self.currentStep=0

    def step(self,seed):
        randomness = randomAction(seed)
        pos = randomness[0]
        nextseed = randomness[1]
        self.position = f(self.position, pos)
        self.currentStep+=1
        self.reward =self.reward+rewardPos(self.position)
        #print(self.position)
        if(self.position==goalPos):
            self.position=startPos
            self.stepsToGoal.append(self.currentStep)
            self.currentStep=0
        return nextseed

    def runRobot(self,steps,seed):
        nextseed=seed
        for i in range(steps):
            nextseed=self.step(nextseed)
        return nextseed






