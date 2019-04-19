from random import random
import numpy as np


class Particle:
    def __init__(self, n, vMin, vMax):
        """ constructor
                input--
                  n: the number of components
                  vmin: the minimum possible value
                  vmax: the maximum possible value
        """
        self.__position = [random() * (vMax - vMin) + vMin for x in range(n)]
        self.evaluate()
        self.velocity = [0 for i in range(0)]

        self.__bestPosition = self.__position.copy()
        self.__bestFitness = self.__fitness

    def fit(self):
        """
                Determine the fitness of an individual. Lower is better.(min problem)
                For this problem we have the Cross-in-tray function
        """
        x = self.__position[0]
        y = self.__position[1]
        f = -0.0001 * (np.abs(np.sin(x) * np.sin(y) * np.exp(100 - np.sqrt(x * x + y * y) / np.pi)) + 1) ** 0.1
        return f

    def evaluate(self):
        self.__fitness = self.fit()

    @property
    def position(self):
        return self.__position

    @property
    def fitness(self):
        return self.__fitness

    @property
    def bestPosition(self):
        return self.__bestPosition

    @property
    def bestFitness(self):
        return self.__bestFitness

    @position.setter
    def position(self, newPosition):
        self.__position = newPosition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if self.__fitness < self.__bestFitness:
            self.__bestPosition = self.__position
            self.__bestFitness = self.__fitness

    def __str__(self):
        return str(self.position[0]) + " " + str(self.position[1])
