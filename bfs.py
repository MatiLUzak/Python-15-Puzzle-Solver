from graf import Puzzle
from collections import deque
class bfs:
    @staticmethod
    def bfs(graphToSolve):
        puzzle=Puzzle(graphToSolve)
        if puzzle.checkWin():
            print("Starting position is the winning position.")
            return graphToSolve
        queue=deque()
        queue.append(puzzle)
        visited = set([puzzle])
        while queue:
            puzzle=queue.popleft()
            if puzzle.checkWin():
                return puzzle
            for neighbor in puzzle.generateNeighbours():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print("No solution found.")
        return None


