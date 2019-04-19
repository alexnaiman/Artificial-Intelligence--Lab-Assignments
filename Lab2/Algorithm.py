from Individ import Individ
from Population import Population
from copy import deepcopy


class Algorithm:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.populationSize, self.noIterations, self.mutationProbabilty, \
        self.xmin, self.xmax, self.ymin, self.ymax = self.readParameters()
        self.mutationProbabilty = float(self.mutationProbabilty / 100)
        self.population = Population(self.populationSize, self.xmin, self.xmax, self.ymin, self.ymax,
                                     self.mutationProbabilty)

    def readParameters(self):
        with open(self.__fileName, 'r') as f:
            return [int(x) for x in f.readlines()]

    def run(self):
        generations = []
        for i in range(self.noIterations):
            self.population.evaluate()
            self.population.naturalSelection()
            generations.append(deepcopy(self.population.best()))
            # print(self.population.best().fitness())
        return generations
