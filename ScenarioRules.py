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

def fRandom5(i, a,seed):
    random.seed(seed)
    r = random.random()
    nextseed=r
    if r>=0.95:
        return r
    else:
        if (a == 'Left'):
            if (i % 10 == 1):
                return [i,nextseed]
            else:
                return [i - 1,nextseed]
        if (a == 'Right'):
            if (i % 10 == 0):
                return [i,nextseed]
            else:
                return [i + 1,nextseed]
        if (a == 'Up'):
            if (i <= 10):
                return [i,nextseed]
            else:
                return [i - 10,nextseed]
        if (a == 'Down'):
            if (i >= 91):
                return [i,nextseed]
            else:
                return [i + 10,nextseed]
        else:
            print('Invalid positional')

#def randomneighboor(i,seed):


def fTHEWALL(i, a):
    r=-1
    if (a == 'Left'):
        if (i % 10 == 1):
            r=i
        else:
            r= i - 1
        if (r%10==4 and r!=94) or (r%10==7 and r!=7):
            return i
        else:
            return r
    if (a == 'Right'):
        if (i % 10 == 0):
            r= i
        else:
            r= i + 1
        if (r%10==4 and r!=94) or (r%10==7 and r!=7):
            return i
        else:
            return r
    if (a == 'Up'):
        if (i <= 10):
            r= i
        else:
            r=i - 10
        if (r%10==4 and r!=94) or (r%10==7 and r!=7):
            return i
        else:
            return r
    if (a == 'Down'):
        if (i >= 91):
            r= i
        else:
            r= i + 10
        if (r%10==4 and r!=94) or (r%10==7 and r!=7):
            return i
        else:
            return r
    else:
        print('Invalid positional')

def rewardPos(i):
    if (i == 100):
        return 100
    else:
        return 0

def rewardPosTHEWALL(current,next):
    if(next==100):
        return 100
    if(current==next):
        return -0.1
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
