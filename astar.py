import heapq
import time
from graf import Puzzle

class PuzzleNode:
    def __init__(self, puzzle, heuristic_method):
        self.puzzle = puzzle
        self.cost = puzzle.calculate_total_cost(heuristic_method)

    def __lt__(self, other):
        return self.cost < other.cost

class AStar:
    def __init__(self):
        self.solution = -1
        self.visitNumber = 0
        self.proceded = 0
        self.depth = 0
        self.time = 0

    def solve(self, graphToSolve, heuristic_method,boardSize):
        start =time.time()
        puzzle = Puzzle(graphToSolve,boardSize)
        puzzleNode = PuzzleNode(puzzle, heuristic_method)
        priorityQueue = []
        heapq.heappush(priorityQueue, puzzleNode)
        visited = set()
        while priorityQueue:
            puzzleNode = heapq.heappop(priorityQueue)
            puzzle = puzzleNode.puzzle
            self.proceded += 1
            if puzzle not in visited:
                visited.add(puzzle)
                self.depth = max(self.depth, puzzle.depth)
                if puzzle.checkWin():
                    self.solution = puzzle.depth
                    self.time = time.time() - start
                    self.visitNumber = len(visited)
                    return puzzle
            for move in 'UDLR':
                neighbor = puzzle.moveAndCreate(Puzzle.DIRECTIONS[move], move)
                if neighbor and neighbor not in visited:
                    if neighbor.checkWin():
                        self.solution = neighbor.depth
                        self.time = time.time() - start
                        self.visitNumber = len(visited)
                        self.depth = max(self.depth, neighbor.depth)
                        return neighbor
                    neighbor_node = PuzzleNode(neighbor, heuristic_method)
                    heapq.heappush(priorityQueue, neighbor_node)
        self.time = time.time() - start
        return None

    def print_stats(self):
        print("Solution depth:", self.solution)
        print("Visited states:", self.visitNumber)
        print("Processed states:", self.proceded)
        print("Maximum depth reached:", self.depth)
        print("Time (s):", f"{self.time:.3f}")

