class Puzzle:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, +1)
    DIRECTIONS = {'U': UP, 'D': DOWN, 'L': LEFT, 'R': RIGHT}

    def __init__(self, initial, boardSize, depth=0, moves=''):
        self.boardSize = boardSize
        self.depth = depth
        self.moves = moves
        self.board = [[0] * self.boardSize for _ in range(self.boardSize)]
        self.winHash = hash(tuple(range(1, self.boardSize * self.boardSize)) + (0,))
        self.blankSpot = None
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                self.board[i][j] = initial[i][j]
                if self.board[i][j] == 0:
                    self.blankSpot = (i, j)

    def printBoard(self):
        for row in self.board:
            print(' '.join(str(cell).rjust(2, ' ') for cell in row))

    def moveAndCreate(self, dir, move):
        x, y = self.blankSpot
        nx, ny = x + dir[0], y + dir[1]
        if 0 <= nx < self.boardSize and 0 <= ny < self.boardSize:
            new_board = [row[:] for row in self.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            return Puzzle(new_board, self.boardSize, self.depth + 1, self.moves + move)
        return None

    def checkWin(self):
        return hash(tuple(self.board[i][j] for i in range(self.boardSize) for j in range(self.boardSize))) == self.winHash

    def __hash__(self):
        return hash((tuple(self.board[i][j] for i in range(self.boardSize) for j in range(self.boardSize)), self.depth))

    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.board == other.board

    def generateNeighbours(self, moveOrder):
        neighset = list()
        for move in moveOrder:
            dir = Puzzle.DIRECTIONS[move]
            neighbour = self.moveAndCreate(dir, move)
            if neighbour is not None:
                neighset.append(neighbour)
        return neighset

    def hamming(self):
        distance = 0
        x = 1
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if (x != self.board[i][j] and self.board[i][j] != 0):
                    distance += 1
                x += 1
        return distance

    def manhattan(self):
        distance = 0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                val = self.board[i][j]
                if val != 0:
                    x = (val - 1) // self.boardSize
                    y = (val - 1) % self.boardSize
                    distance += abs(x - i) + abs(y - j)
        return distance

    def calculate_total_cost(self, heuristic_method):
        g = self.depth
        h = self.hamming() if heuristic_method == 'hamm' else self.manhattan()
        return g + h
