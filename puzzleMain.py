from random import choice


class Puzzle:
    UP = (1, 0)
    DOWN = (-1, 0)
    LEFT = (0, 1)
    RIGHT = (0, -1)

    DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

    boardSize = 4
    blankSpot = (3, 3)

    def __init__(self):
        self.board = [[0] * Puzzle.boardSize for i in range(Puzzle.boardSize)]
        for i in range(Puzzle.boardSize):
            for j in range(Puzzle.boardSize):
                self.board[i][j] = i * Puzzle.boardSize + j + 1
        self.board[self.blankSpot[0]][self.blankSpot[1]]=0
        self.shuffle()

    def printBoard(self):
        for row in self.board:
            print(' '.join(str(cell).rjust(2, ' ') for cell in row))

    def __getitem__(self, item):
        return self.board[item]

    def shuffle(self):
        n = 1000
        for i in range(n):
            dirs = choice(self.DIRECTIONS)
            self.move(dirs)

    def move(self, dir):
        newBlankSpot = (self.blankSpot[0] + dir[0], self.blankSpot[1] + dir[1])
        if (newBlankSpot[0] < 0 or newBlankSpot[0] >= Puzzle.boardSize or newBlankSpot[1] < 0 or newBlankSpot[1] >= Puzzle.boardSize):
            return False
        self.board[self.blankSpot[0]][self.blankSpot[1]] = self.board[newBlankSpot[0]][newBlankSpot[1]]
        self.board[newBlankSpot[0]][newBlankSpot[1]] = 0
        self.blankSpot = newBlankSpot
        return True

    def checkWin(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if (self.board[i][j] != i * self.boardSize + j + 1 and self.board[i][j] != 0):
                    return False

        return True



def main():
    game = Puzzle()
    moves = {'u': Puzzle.UP, 'd': Puzzle.DOWN, 'l': Puzzle.LEFT, 'r': Puzzle.RIGHT}

    while(True):
     game.printBoard()
     move = input("Your move (u/d/l/r): ").lower()
     if move in moves:
         if not game.move(moves[move]):
             print("Invalid move, try again.")
     else:
         print("Invalid input, please use 'u', 'd', 'l', or 'r' to move.")


if __name__ == "__main__":
    main()