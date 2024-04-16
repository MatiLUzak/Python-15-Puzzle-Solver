class Puzzle:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, +1)
    DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
    boardSize = 4
    blankSpot = (3, 3)

    def __init__(self, initial):
        self.board = [[0] * Puzzle.boardSize for _ in range(Puzzle.boardSize)]
        for i in range(Puzzle.boardSize):
            for j in range(Puzzle.boardSize):
                self.board[i][j] = initial[i][j]
                if self.board[i][j] == 0:
                    self.blankSpot = (i, j)
    def printBoard(self):
        for row in self.board:
            print(' '.join(str(cell).rjust(2, ' ') for cell in row))

    def move(self, dir):
        newBlankSpot = (self.blankSpot[0] + dir[0], self.blankSpot[1] + dir[1])
        if 0 <= newBlankSpot[0] < Puzzle.boardSize and 0 <= newBlankSpot[1] < Puzzle.boardSize:
            self.board[self.blankSpot[0]][self.blankSpot[1]] = self.board[newBlankSpot[0]][newBlankSpot[1]]
            self.board[newBlankSpot[0]][newBlankSpot[1]] = 0
            self.blankSpot = newBlankSpot
            return True
        return False

    def checkWin(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] != i * self.boardSize + j + 1 and self.board[i][j] != 0:
                    return False
        return True

    def __hash__(self):
        return hash(tuple(tuple(row)for row in self.board))
    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.board == other.board


