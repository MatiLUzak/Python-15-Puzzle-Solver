import heapq
import time
from graf import Puzzle
class PuzzleNode:
    def __init__(self, puzzle, cost):
        self.puzzle = puzzle
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class AStar:
    def __init__(self):
        self.solution_depth = -1
        self.visited_states = 0
        self.processed_states = 0
        self.max_depth = 0
        self.execution_time = 0

    def solve(self, initial, move_order, heuristic_method='manh'):
        start_time = time.time()
        start_state = Puzzle(initial)
        start_node = PuzzleNode(start_state, start_state.calculate_total_cost(heuristic_method))

        priority_queue = []
        heapq.heappush(priority_queue, start_node)

        visited = set()

        while priority_queue:
            current_node = heapq.heappop(priority_queue)
            current_state = current_node.puzzle
            self.processed_states += 1
            self.max_depth = max(self.max_depth, current_state.depth)

            if current_state.checkWin():
                self.solution_depth = current_state.depth
                self.execution_time = time.time() - start_time
                return current_state

            visited.add(current_state)

            for move in move_order:
                neighbor = current_state.moveAndCreate(Puzzle.DIRECTIONS[move], move)
                if neighbor and neighbor not in visited:
                    neighbor_node = PuzzleNode(neighbor, neighbor.calculate_total_cost(heuristic_method))
                    heapq.heappush(priority_queue, neighbor_node)
                    visited.add(neighbor)

        self.execution_time = time.time() - start_time
        return None

    def print_stats(self):
        print("Solution depth:", self.solution_depth)
        print("Visited states:", self.visited_states)
        print("Processed states:", self.processed_states)
        print("Maximum depth reached:", self.max_depth)
        print("Time (s):", f"{self.execution_time:.3f}")
