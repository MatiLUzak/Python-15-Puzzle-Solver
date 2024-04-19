class Puzzle:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, +1)
    DIRECTIONS = {'U': UP, 'D': DOWN, 'L': LEFT, 'R': RIGHT}
    boardSize = 4
    blankSpot = (3, 3)
    winHash=hash(tuple(range(1,boardSize*boardSize))+(0,))

    def __init__(self, initial,depth=0,moves=''):
        self.depth = depth
        self.moves = moves
        self.board = [[0] * Puzzle.boardSize for _ in range(Puzzle.boardSize)]
        for i in range(Puzzle.boardSize):
            for j in range(Puzzle.boardSize):
                self.board[i][j] = initial[i][j]
                if self.board[i][j] == 0:
                    self.blankSpot = (i, j)
    def printBoard(self):
        for row in self.board:
            print(' '.join(str(cell).rjust(2, ' ') for cell in row))

    def moveAndCreate(self, dir,move):
        x, y = self.blankSpot
        nx, ny = x + dir[0], y + dir[1]
        if 0 <= nx < Puzzle.boardSize and 0 <= ny < Puzzle.boardSize:
            new_board = [row[:] for row in self.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            return Puzzle(new_board,self.depth+1,self.moves+move)
        return None

    def checkWin(self):
        return hash(tuple(self.board[i][j] for i in range(self.boardSize) for j in range(self.boardSize)))==Puzzle.winHash

    def __hash__(self):
        return hash(tuple(self.board[i][j] for i in range(self.boardSize) for j in range(self.boardSize)))
    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.board == other.board
    def generateNeighbours(self,moveOrder):
        neighset=set()
        for move in moveOrder:
            dir=Puzzle.DIRECTIONS[move]
            neighbour=self.moveAndCreate(dir,move)
            if neighbour is not None:
             neighset.add(neighbour)
        return neighset



