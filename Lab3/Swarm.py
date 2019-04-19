from Particle import Particle


class Swarm:
    def __init__(self, count, n, vmin, vmax):
        self.noOfParticles = count
        self.v = self.population(count, n, vmin, vmax)

    def __len__(self):
        return len(self.v)

    def population(self, count, n, vmin, vmax):
        return [Particle(n, vmin, vmax) for x in range(count)]

    def getBestNeighbour(self, particle, neighbours):
        return min(neighbours[particle], key=lambda x: x.fitness)

    def getBestParticle(self):
        # print the best individual
        return min(self.v, key=lambda x: x.fitness)

    def __getitem__(self, item):
        return self.v[item]

    def __setitem__(self, key, c):
        self.v[key] = c

    def __str__(self):
        s = ""
        for i in range(len(self.v)):
            s += " " + str(self.v[i].position) + " ->" + str(self.v[i].bestFitness) + " "
        return s
