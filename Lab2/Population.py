from random import random, randint
from Individ import Individ


class Population:
    def __init__(self, n, xmin, xmax, ymin, ymax, mutationProbability):
        self.n = n
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.individs = self.population(n, xmin, xmax, ymin, ymax)
        self.mutationProbability = mutationProbability

    def population(self, count, xmin, xmax, ymin, ymax):
        """
            Create a number of individuals (i.e. a population).

            count: the number of individuals in the population
            xmin: the minimum possible value for x
            xmax: the maximum possible value for x
            ymin: the minimum possible value for y
            ymax: the maximum possible value for y
        """
        return [Individ(xmin, xmax, ymin, ymax) for i in range(count)]

    def setFirst(self):
        self.individs = self.individs[:100]

    def getLen(self):
        return len(self.individs)

    def put(self, c):
        self.individs.append(c)

    def evaluate(self):
        self.__crossoverPopulation()
        self.__mutation()

    def __crossoverPopulation(self):
        population = self.individs
        for i in range(self.n):
            parent1 = self.__selectParent()
            parent2 = self.__selectParent()
            child = parent1.blendCrossover(parent2)
            population.append(child)
        self.individs = population

    def __selectParent(self):
        tournament = []
        tournamentSize = 15
        for i in range(tournamentSize):
            p = randint(0, self.n - 1)
            tournament += [self.individs[p]]
        tournament.sort(key=lambda x: x.fitness())
        return tournament[0]

    def __mutation(self):
        for i in range(len(self.individs)):
            self.individs[i].mutate(self.mutationProbability, self.xmin, self.xmax, self.ymin, self.ymax)

    def best(self):
        return sorted(self.individs, key=lambda x: x.fitness())[0]

    def naturalSelection(self):
        self.individs = sorted(self.individs, key=lambda x: x.fitness())[:self.n]
