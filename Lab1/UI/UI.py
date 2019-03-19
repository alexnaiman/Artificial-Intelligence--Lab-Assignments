from time import time
from Controller.Controller import Controller


class UI:
    def __init__(self, problem):
        self.__problem = problem
        self.__controller = Controller(problem)

    def printMenu(self):
        s = ''
        s += "1 - find a path with BFS \n"
        s += "2 - find a path with GBFS\n"
        print(s)

    def run(self):
        while True:
            self.printMenu()
            try:
                command = int(input(">>"))
                if command == 0:
                    break
                elif command == 1:
                    start = time()
                    print(self.__controller.BFS(self.__problem.getInitial()))
                    print("Took {} seconds to complete.".format(time() - start))
                elif command == 2:
                    start = time()
                    print(self.__controller.GBFS(self.__problem.getInitial()))
                    print("Took {} seconds to complete.".format(time() - start))

                else:
                    print("Invalid input")
            except Exception as e:
                raise e
