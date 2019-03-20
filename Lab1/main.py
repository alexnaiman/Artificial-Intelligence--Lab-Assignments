from Domain.Configuration import Configuration
from Domain.State import State
from Controller.Controller import Controller
from UI.UI import UI
from Domain.Problem import Problem

"""
    The sliding puzzle problem – solving techniques: BFS, GBFS
    For a given puzzle of n x n squares with numbers from 1 to (n x n-1) (one square is
    empty) in an initial configuration, find a sequence of movements for the numbers in order to
    reach a final given configuration, knowing that a number can move (horizontally or vertically) on
    an adjacent empty squareThe sliding puzzle problem – solving techniques: BFS, GBFS
    For a given puzzle of n x n squares with numbers from 1 to (n x n-1) (one square is
    empty) in an initial configuration, find a sequence of movements for the numbers in order to
    reach a final given configuration, knowing that a number can move (horizontally or vertically) on
    an adjacent empty square
"""


def tests():
    configuration = Configuration([['2', '1'], ['*', '3']], 1, 0)
    assert (configuration.getBoard() == [['2', '1'], ['*', '3']])
    assert (configuration.getSize() == 2)
    assert (configuration.getX() == 1)
    assert (configuration.getY() == 0)
    nextConfig1 = Configuration([['*', '1'], ['2', '3']], 0, 0)
    nextConfig2 = Configuration([['2', '1'], ['3', '*']], 1, 1)
    assert (configuration.nextConfig() == [nextConfig1, nextConfig2])

    state = State()
    assert (state.getValues() == [])
    state += 23
    assert (state.getValues() == [])
    state += configuration
    assert (state.getValues() == [configuration])
    state2 = State()
    assert (state2 < state)

    problem = Problem("data/2x2")
    assert (problem.getFinal() == Configuration([['*', '1'], ['2', '3']], 0, 0))
    assert (problem.getInitial().getValues() == state.getValues())
    assert (problem.heuristic(state, problem.getFinal()) == 4)
    assert (problem.expand(state)[0].getValues() == [configuration, nextConfig1])
    assert (problem.expand(state)[1].getValues() == [configuration, nextConfig2])

    controller = Controller(problem)
    state2 = State()
    state2.setValues([configuration, nextConfig1])
    assert (controller.BFS(state).getValues() == state2.getValues())
    assert (controller.GBFS(state).getValues() == state2.getValues())
    print("tests passed")


def main():
    problem = Problem("./data/3x3")
    ui = UI(problem)
    ui.run()


tests()
main()
