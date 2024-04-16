from graf import Puzzle
from collections import deque
class BFS:
    @staticmethod
    def bfs(graphToSolve):
        puzzle=Puzzle(graphToSolve)
        if puzzle.checkWin():
            print("Starting position is the winning position.")
            return puzzle
        queue=deque([puzzle])
        visited = set([puzzle])
        while queue:
            puzzle=queue.popleft()
            if puzzle.checkWin():
                return puzzle
            for neighbor in puzzle.generateNeighbours():
                if neighbor not in visited:
                    if neighbor.checkWin():
                        return neighbor
                    visited.add(neighbor)
                    queue.append(neighbor)
        print("No solution found.")
        return None


