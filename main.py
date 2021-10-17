# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from robotTester import *
from RewardMatrix import *
from RobotMatrix import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #EXERCICIO 1: escolha aleatoria das acoes
    runWallE(30,20000,123)

    #EXERCICIO2A: contrucao da matriz Q com escolha aleatoria de acoes (EXPLORATION), testes da matriz Q a diferentes passos da execucao (EXPLOITATION)
    #runEVA(30,20000,400,1000,456)

    #EXERCICIO2b contrucao da matriz Q com escolha das melhores acoes, testes da matriz Q a diferentes passos da execucao
    #runMO(30,20000,400,1000,789)

    #EXERCICIO3 contrucao da matriz Q com acoes aleatorias/melhores acoes com sistema de greed (greed=0.1/0.5/0.9)
    #runGreedyAlexa(30,20000, 101112,400,1000, 0.1)
    #runGreedyAlexa(30, 20000, 131415,400,1000, 0.5)
    #runGreedyAlexa(30, 20000, 1617,400,1000, 0.9)
    #sistema de greed progressivo (greed inicial=0.3, aumenta a partir de 30% dos passos)
    #runSmartAlexa(30,20000,1819,0.30,0.30,400,1000)

    #EXERCICIO4 sistema de greed progressivo com paredes
    #runSmartAlexaTHEWALL(5,100000,10,0.30,0.30,1000,1000)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
