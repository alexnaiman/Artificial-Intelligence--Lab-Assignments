from Domain.Configuration import Configuration


class State:
    """
        Holds a list of configurations => the path that leads to the solution
    """

    def __init__(self):
        self.__values = []

    def setValues(self, values):
        self.__values = values[:]

    def getValues(self):
        return self.__values[:]

    def __str__(self):
        s = ''
        for x in self.__values:
            s += str(x) + "\n"
        return s

    def __add__(self, something):
        aux = State()
        if isinstance(something, State):
            aux.setValues(self.__values + something.getValues())
        elif isinstance(something, Configuration):
            aux.setValues(self.__values + [something])
        else:
            aux.setValues(self.__values)
        return aux

    def __lt__(self, o):
        if not isinstance(o, State):
            return False
        if len(o.getValues()) < len(self.getValues()):
            return False
        return True
