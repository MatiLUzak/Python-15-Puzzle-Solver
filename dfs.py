import time
from collections import deque
from graf import Puzzle
class DFS:
    def __init__(self):
        self.solution = -1
        self.visitNumber = 0
        self.proceded = 0
        self.depth = 0
        self.time = 0
        self.max_depth_limit = 20

    def dfs(self, graphToSolve, moveOrder):
        start = time.time()
        puzzle=Puzzle(graphToSolve)
        if puzzle.checkWin():
            self.solution=puzzle.depth
            self.visitNumber= 1
            self.proceded=1
            self.time = time.time() - start
            return puzzle
        stack = deque([puzzle])
        visited = set([puzzle])
        self.visitNumber=1
        while stack:
            puzzle = stack.pop()
            self.depth = max(self.depth, puzzle.depth)
            if puzzle.depth > self.max_depth_limit:
                continue
            self.proceded+=1
            if puzzle.checkWin():
                self.solution = puzzle.depth
                self.time = time.time() - start
                self.visitNumber = len(visited)
                return puzzle
            for neighbor in puzzle.generateNeighbours(moveOrder):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    if neighbor.checkWin():
                        self.solution = neighbor.depth
                        self.time = time.time() - start
                        self.visitNumber = len(visited)
                        return neighbor

        self.time = time.time() - start
        print("No solution found.")
        return None

    def print_stats(self):
        print("Solution depth:", self.solution)
        print("Visited states:", self.visitNumber)
        print("Processed states:", self.proceded)
        print("Maximum recursion depth:", self.depth)
        print("Time (s):", f"{self.time:.3f}")
