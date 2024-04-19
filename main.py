from dfs import DFS
from graf import Puzzle
from bfs import BFS

if __name__ == '__main__':
    initial_setup = [
        [1, 2, 3, 4],
        [5, 0, 6, 8],
        [9, 10, 7, 11],
        [13, 14, 15, 12]
    ]
    bfsSolver=BFS()
    solution=bfsSolver.bfs(initial_setup,"UDLR")
    solution.printBoard()
    bfsSolver.print_stats()
    print(solution.moves)

    dfsSolver=DFS()
    solution=dfsSolver.dfs(initial_setup,"UDLR")
    solution.printBoard()
    dfsSolver.print_stats()
    print(solution.moves)

   # main()
