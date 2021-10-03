import random

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


def rewardPos(i):
    if (i == 100):
        return 100
    else:
        return 0


def randomAction(seed):
    random.seed(seed)
    r = random.random()
    r = r*4
    if (0 <= r <= 1):
        return ['Up',r]
    if (1 < r <= 2):
        return ['Down',r]
    if (2 < r <= 3):
        return ['Left',r]
    if (3 < r <= 4):
        return ['Right',r]
