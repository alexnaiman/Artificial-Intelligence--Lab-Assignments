from Domain.Configuration import Configuration
from Domain.State import State


class Problem:
    """
        Our problem class that holds the initial state, the final state and the heuristic model
    """

    def __init__(self, fileName):
        self.__fileName = fileName
        self.__initialConfig = self.__readFromFile()
        self.__initialState = State()
        self.__initialState.setValues([self.__initialConfig])
        self.__finalConfig = self.__generateFinalConfig(self.__initialConfig.getSize())

    def getInitial(self):
        return self.__initialState

    def getFinal(self):
        return self.__finalConfig

    def __generateFinalConfig(self, size):
        l = [[str(x + y * size) for x in range(size)] for y in range(size)]
        l[0][0] = '*'
        return Configuration(l, 0, 0)

    """
    Heuristic method that uses the Manhattan distance method to get the score of the given state
    The Manhattan distance of one tile is the number of moves that would be required to move that tile to its goal location
    if it could be moved over any other tiles
    in: the state foe which we compute the heuristic and its final desired config
    out: the sum of all Manhattan distances for all tiles
    """

    def heuristic(self, state, finalConfig):
        difference = 0
        length = finalConfig.getSize()
        for i in range(length):
            for j in range(length):
                if state.getValues()[-1].getBoard()[i][j] != '*':
                    difference += abs(i - int(int(state.getValues()[-1].getBoard()[i][j]) / length)) + abs(
                        j - int(state.getValues()[-1].getBoard()[i][j]) % 3)
        return difference

    """
        Expands the given state into is next for possible configurations
    """

    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]
        for x in currentConfig.nextConfig():
            myList.append(currentState + x)
        return myList

    """
        Return the coordinates of the empty space
        out: tuple of form (int,int)
    """

    def __findEmptySpace(self, initialState):
        n = len(initialState[0])
        for i in range(n):
            for j in range(n):
                if initialState[i][j] == '*':
                    return i, j

    """
        Reads from file a configuration and returns it
        out: Configuration based on the file given through fileName
    """

    def __readFromFile(self):
        state = []
        try:
            with open(self.__fileName) as f:
                for line in f:
                    line.strip()
                    state.append(line.split())
            x, y = self.__findEmptySpace(state)
            return Configuration(state, x, y)
        except IOError:
            raise Exception("File is missing")
