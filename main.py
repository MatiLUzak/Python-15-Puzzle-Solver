from graf import Puzzle
from bfs import BFS
def main():
    initial_setup = [
        [1, 2, 3, 4],
        [5, 0, 6, 8],
        [9, 10, 7, 11],
        [13, 14, 15, 12]
    ]
    game = Puzzle(initial=initial_setup)  # rdrd
    moves = {'u': Puzzle.UP, 'd': Puzzle.DOWN, 'l': Puzzle.LEFT, 'r': Puzzle.RIGHT}

    while True:
        game.printBoard()
        move = input("Your move (u/d/l/r): ").lower()
        if move in moves:
            if not game.move(moves[move]):
                print("Invalid move, try again.")
        else:
            print("Invalid input, please use 'u', 'd', 'l', or 'r' to move.")


if __name__ == '__main__':#move źle działa
    initial_setup = [
        [1, 2, 3, 4],
        [5, 0, 6, 8],
        [9, 10, 7, 11],
        [13, 14, 15, 12]
    ]
    solution=BFS.bfs(initial_setup)
    solution.printBoard()
   # main()
