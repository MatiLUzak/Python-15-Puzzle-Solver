import time
from graf import Puzzle
from collections import deque
class BFS:
    def __init__(self):
        self.solution = -1
        self.visitNumber=0
        self.proceded=0
        self.depth=0
        self.time=0
    def bfs(self,graphToSolve,moveOrder,boardSize):
        start = time.time()
        puzzle=Puzzle(graphToSolve,boardSize)
        if puzzle.checkWin():
            self.solution=puzzle.depth
            self.visitNumber=1
            self.proceded=1
            self.time=time.time()-start
            return puzzle
        queue=deque([puzzle])
        visited = set([puzzle])
        while queue:
            puzzle=queue.popleft()
            self.proceded+=1
            self.depth=max(puzzle.depth,self.depth)
            if puzzle.checkWin():
                self.solution=puzzle.depth
                self.time = time.time() - start
                self.visitNumber= len(visited)
                return puzzle
            for neighbor in puzzle.generateNeighbours(moveOrder):
                if neighbor not in visited:
                    visited.add(neighbor)
                    self.depth = max(neighbor.depth, self.depth)
                    if neighbor.checkWin():
                        self.solution=neighbor.depth
                        self.time = time.time() - start
                        self.visitNumber = len(visited)
                        self.depth = max(neighbor.depth, self.depth)
                        return neighbor
                    queue.append(neighbor)

        self.time = time.time() - start
        print("No solution found.")
        return None

    def print_stats(self):
        print("Solution depth:", self.solution)
        print("Visited states:", self.visitNumber)
        print("Processed states:", self.proceded)
        print("Maximum recursion depth:", self.depth)
        print("Time (s):", f"{self.time:.3f}")



