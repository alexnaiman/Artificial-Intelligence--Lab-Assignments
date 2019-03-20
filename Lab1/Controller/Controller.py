from queue import PriorityQueue


class Controller:
    """
        The Controller class used to manage the method of searching
    """

    def __init__(self, problem):
        self.__problem = problem

    """
        Returns a solution found through breadth first search algorithm - uninformed search
    """

    def BFS(self, root):

        queue = [root]
        while len(queue) > 0:
            currentState = queue.pop(0)
            if currentState.getValues()[-1] == self.__problem.getFinal():
                return currentState
            queue = queue + self.__problem.expand(currentState)

    """
        Returns a solution found through greedy breadth first search algorithm - informed search
    """

    def GBFS(self, root):
        visited = []
        queue = PriorityQueue()
        queue.put((self.__problem.heuristic(root, self.__problem.getFinal()), root))
        while not queue.empty():
            node = queue.get()[1]
            visited = visited + node.getValues()
            if node.getValues()[-1] == self.__problem.getFinal():
                return node
            aux = []
            for x in self.__problem.expand(node):
                if x.getValues()[-1] not in visited:
                    aux.append(x)
            for x in aux:
                score = self.__problem.heuristic(x, self.__problem.getFinal())
                queue.put((score, x))
