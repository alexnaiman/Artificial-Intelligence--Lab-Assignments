from Algorithm import Algorithm
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    algorithm = Algorithm('parameters')

    a = algorithm.run()
    values = np.array([x.fitness() for x in a])
    arr = np.array(values)
    m = np.mean(arr, axis=0)
    points = []

    print(m)
    plt.scatter([range(len(arr))], arr)
    plt.axhline(y=m, color='r', linestyle='-')
    plt.scatter(len(values), values[-1], edgecolors='r')
    plt.text(len(values), values[-1], '{}'.format(values[-1]))
    plt.show()
