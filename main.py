import sys
from bfs import BFS
from dfs import DFS
from astar import AStar

def get_user_input():
    algorithm = input("Podaj algorytm (bfs, dfs, astr): ")
    param = input("Podaj parametr dla algorytmu (np. UDLR dla bfs/dfs lub hamm/manh dla astr): ")
    input_file = input("Podaj ścieżkę do pliku wejściowego: ")
    solution_file = input("Podaj nazwę pliku wyjściowego z rozwiązaniem: ")
    stats_file = input("Podaj nazwę pliku wyjściowego ze statystykami: ")
    return algorithm, param, input_file, solution_file, stats_file

def main():
    if len(sys.argv) < 2:
        algorithm, param, input_file, solution_file, stats_file = get_user_input()
    else:
        _, algorithm, param, input_file, solution_file, stats_file = sys.argv

    initial_setup = read_initial_config(input_file)
    solution = None

    if algorithm.lower() == 'bfs':
        solver = BFS()
        solution = solver.bfs(initial_setup, param)
    elif algorithm.lower() == 'dfs':
        solver = DFS()
        solution = solver.dfs(initial_setup, param)
    elif algorithm.lower() == 'astar':
        solver = AStar()
        solution = solver.solve(initial_setup, param)

    if solution:
        write_solution(solution_file, solution)
        write_stats(stats_file, solver)
    else:
        write_no_solution(solution_file, stats_file)

def write_solution(solution_file, solution):
    with open(solution_file, 'w') as f:
        f.write(f"{len(solution.moves)}\n")
        f.write(''.join(solution.moves) + '\n')

def write_no_solution(solution_file, stats_file):
    with open(solution_file, 'w') as f:
        f.write("-1\n")
    with open(stats_file, 'w') as f:
        f.write("-1\n0\n0\n0\n0.000\n")

def write_stats(filename, solver):
    with open(filename, "w") as file:
        file.write(f"{solver.solution}\n")
        file.write(f"{solver.visitNumber}\n")
        file.write(f"{solver.proceded}\n")
        file.write(f"{solver.depth}\n")
        file.write(f"{solver.time:.3f}\n")

def read_initial_config(input_file):
    initial_setup = []
    with open(input_file, 'r') as file:
        dimensions = file.readline().strip().split()
        rows, cols = int(dimensions[0]), int(dimensions[1])
        for _ in range(rows):
            line = file.readline().strip().split()
            initial_setup.append([int(x) for x in line])
    return initial_setup

if __name__ == "__main__":
    main()
