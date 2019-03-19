from copy import deepcopy


class Configuration:
    """
        Holds a board configuration as a matrix n*n with the empty space on coordinates (x,y)
    """

    def __init__(self, board, x, y):
        self.__size = len(board)
        self.__board = board[:]
        self.__emptyX = x
        self.__emptyY = y

    def getSize(self):
        return self.__size

    def getBoard(self):
        return self.__board[:]

    def getX(self):
        return self.__emptyX

    def getY(self):
        return self.__emptyY

    """
        Moves the empty space on all directions on the x and y axis
        in: the list of the next correct(possible) configuration
    """

    def nextConfig(self):
        children = []
        ip = [-1, 0, 1, 0]
        jp = [0, -1, 0, 1]

        for k in range(4):
            if 0 <= self.__emptyX + ip[k] < self.__size and 0 <= self.__emptyY + jp[k] < self.__size:
                newConfig = deepcopy(self.getBoard())
                aux = newConfig[self.__emptyX][self.__emptyY]
                newConfig[self.__emptyX][self.__emptyY] = newConfig[self.__emptyX + ip[k]][self.__emptyY + jp[k]]
                newConfig[self.__emptyX + ip[k]][self.__emptyY + jp[k]] = aux
                newX = self.__emptyX + ip[k]
                newY = self.__emptyY + jp[k]
                children.append(Configuration(newConfig, newX, newY))
        return children

    def __str__(self):
        s = ""
        for i in self.__board:
            s += str(i) + "\n"
        return s

    def __eq__(self, other):
        if not isinstance(other, Configuration):
            return False
        if self.__size != other.getSize():
            return False
        if self.__emptyY != other.getY():
            return False
        if self.__emptyX != other.getX():
            return False
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__board[i][j] != other.getBoard()[i][j]:
                    return False
        return True
