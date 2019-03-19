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


def main():
    problem = Problem("./data/3x3")
    ui = UI(problem)
    ui.run()


main()
