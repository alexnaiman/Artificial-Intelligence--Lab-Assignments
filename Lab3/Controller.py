from random import random, randint
from Swarm import Swarm
import matplotlib.pyplot as plt
import numpy as np


class Controller:
    def __init__(self):
        self.loadParameters()
        self.pop = Swarm(self.noParticles, self.dimParticle, self.vmin, self.vmax)
        self.result = [self.pop.getBestParticle().fitness]

    def iteration(self, neighbours, c1, c2, w):
        bestNeighbours = []
        for i in range(len(self.pop)):
            bestNeighbours.append(self.pop.getBestNeighbour(self.pop[i], neighbours))

        for i in range(len(self.pop)):
            for j in range(len(self.pop[0].velocity)):
                newVelocity = w * self.pop[i].velocity[j]
                newVelocity = newVelocity + c1 * random() * (bestNeighbours[i].pozition[j] - self.pop[i].pozition[j])
                newVelocity = newVelocity + c2 * random() * (self.pop[i].bestPozition[j] - self.pop[i].pozition[j])
                self.pop[i].velocity[j] = newVelocity

        for i in range(len(self.pop)):
            newPozition = []
            for j in range(len(self.pop[0].velocity)):
                newPozition.append(self.pop[i].pozition[j] + self.pop[i].velocity[j])
            self.pop[i].pozition = newPozition

        self.result.append(self.pop.getBestParticle().fitness)

    def selectNeighbours(self, nSize):
        if (nSize > len(self.pop)):
            nSize = len(self.pop)

        neighbours = {}
        for i in range(len(self.pop)):
            localNeighbour = []
            for j in range(nSize):
                x = randint(0, len(self.pop) - 1)
                while x in localNeighbour:
                    x = randint(0, len(self.pop) - 1)
                localNeighbour.append(self.pop[x])
            neighbours[self.pop[i]] = localNeighbour.copy()
        return neighbours

    def loadParameters(self):
        self.noParticles = 300
        self.dimParticle = 2
        self.vmin = -10
        self.vmax = 10
        self.w = 1.0
        self.c1 = 1.0
        self.c2 = 2.5
        self.sizeOfNeighbourhood = 20

    def runAlgorithm(self, noIteratii=1000):
        neighbourhoods = self.selectNeighbours(self.sizeOfNeighbourhood)

        for i in range(noIteratii):
            self.iteration(neighbourhoods, self.c1, self.c2, self.w / (i + 1))

        best = sorted(self.pop, key=lambda x: x.fitness)[0]
        arr = np.array(self.result)
        # m = np.mean(arr, axis=0)
        # plt.axhline(y=m, color='r', linestyle='-')
        # plt.scatter(len(self.result), best.fitness, edgecolors='g')
        # plt.show()
        plt.plot(range(0, noIteratii + 1), self.result)
        plt.show()
        print(best.fitness)
