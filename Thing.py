import random
import numpy as np
import matplotlib.pyplot as plt
import time


def f(i, a):
    if (a == 'Left'):
        if (i % 10 == 1):
            return i
        else:
            return i - 1
    if (a == 'Right'):
        if (i % 10 == 0):
            return i
        else:
            return i + 1
    if (a == 'Up'):
        if (i <= 10):
            return i
        else:
            return i - 10
    if (a == 'Down'):
        if (i >= 91):
            return i
        else:
            return i + 10
    else:
        print('Invalid positional')


def reward(i):
    if (i == 100):
        return 100
    else:
        return 0


def randomAction():
    r = random.uniform(0, 4)
    if (0 <= r <= 1):
        return 'Up'
    if (1 < r <= 2):
        return 'Down'
    if (2 < r <= 3):
        return 'Left'
    if (3 < r <= 4):
        return 'Right'


def runRobot():
    state = 1
    r = 0
    for i in range(0, 1000, 1):
        action = randomAction()
        state = f(state, action)
        if (state == 100):
            r = r + reward(state)
            state = 1
            print('CHEGUEI')
    print(r)
    return r