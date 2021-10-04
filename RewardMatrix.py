import math

import numpy as np
from matplotlib import pyplot as plt

import Thing
import seaborn as sns


class RewardMatrix:

    global alpha
    alpha=0.7
    global discount
    discount=0.99

    def __init__(self):
        self.positionList=[]
        for i in range(100):
            positionMatrix=[0,0,0,0]
            self.positionList.append(positionMatrix)


    def updatePosition(self,position,directional):
        newPostion = Thing.f(position, directional)
        if newPostion!=position:
            self.positionList[position-1][self.getDirectionalIndex(directional)]=(1-alpha)*self.positionList[position-1][self.getDirectionalIndex(directional)]+alpha*(Thing.rewardPos(newPostion)+discount*max(self.positionList[newPostion-1]))
        else:
            self.positionList[position - 1][self.getDirectionalIndex(directional)]=0
        return newPostion

    def getDirectionalIndex(self,directional):
        if directional == 'Up':
            return 0
        if directional == 'Down':
            return 1
        if directional == 'Left':
            return 2
        if directional == 'Right':
            return 3

    def printHeatMap(self):
        self.positionList[99] = [100, 100, 100, 100]
        maxList=[]
        for i in self.positionList:
            maxList.append(max(i))

        x = np.array((maxList))
        #print(x)
        dim=int(math.sqrt(len(x)))
        #print(dim)
        x_res = x.reshape(dim, dim)
        fig, ax = plt.subplots(figsize=(15, 15))
        sns.heatmap(x_res, square=True, ax=ax)
        plt.yticks(rotation=0, fontsize=16);
        plt.xticks(fontsize=12);
        plt.tight_layout()
        plt.savefig('colorlist.png')




