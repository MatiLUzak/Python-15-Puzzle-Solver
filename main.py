from dfs import DFS
from bfs import BFS
from astar import AStar

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

    a_starSolver = AStar()
    heuristic_method = 'manh'  # Możesz wybrać 'hamm' dla heurystyki Hamminga.
    solution = a_starSolver.solve(initial_setup, heuristic_method)
    if solution:
        solution.printBoard()
        a_starSolver.print_stats()
        print("A* Solution moves:", solution.moves)
    else:
        print("A* No solution found.")
    # main()
