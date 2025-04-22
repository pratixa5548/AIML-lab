import heapq

# A* Algorithm for Water Jug Problem
class WaterJug:
    def __init__(self, j1, j2):
        self.j1_capacity = j1
        self.j2_capacity = j2
        self.target_jug = None
        self.target_amount = None

    def set_target(self):
        self.target_jug = int(input("Choose the jug to place the target amount (1 or 2): "))
        if self.target_jug == 1:
            self.target_amount = int(input(f"Enter the target amount of water for Jug 1 (0 to {self.j1_capacity}): "))
        elif self.target_jug == 2:
            self.target_amount = int(input(f"Enter the target amount of water for Jug 2 (0 to {self.j2_capacity}): "))
        else:
            print("Invalid choice. Please choose Jug 1 or Jug 2.")
            self.set_target()

    def heuristic(self, state):
        if self.target_jug == 1:
            return abs(state[0] - self.target_amount)
        else:
            return abs(state[1] - self.target_amount)

    def get_neighbors(self, state):
        x, y = state
        neighbors = set()
        # Fill jugs
        neighbors.add((self.j1_capacity, y))
        neighbors.add((x, self.j2_capacity))
        # Empty jugs
        neighbors.add((0, y))
        neighbors.add((x, 0))
        # Pour from j1 to j2
        pour_j1_j2 = min(x, self.j2_capacity - y)
        neighbors.add((x - pour_j1_j2, y + pour_j1_j2))
        # Pour from j2 to j1
        pour_j2_j1 = min(y, self.j1_capacity - x)
        neighbors.add((x + pour_j2_j1, y - pour_j2_j1))
        return list(neighbors)

    def a_star_search(self):
        start_state = (0, 0)
        pq = [(self.heuristic(start_state), 0, start_state)]
        visited = set()
        iteration_count = 0

        while pq:
            iteration_count += 1
            _, cost, current = heapq.heappop(pq)
            if current in visited:
                continue
            visited.add(current)
            print(f"Iteration {iteration_count}: Current state: {current}")
            if (self.target_jug == 1 and current[0] == self.target_amount) or (self.target_jug == 2 and current[1] == self.target_amount):
                print(f"Solution found in {iteration_count} iterations: {current}")
                return True
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    heapq.heappush(pq, (self.heuristic(neighbor) + cost + 1, cost + 1, neighbor))
        print("No solution found.")
        return False

# A* Algorithm for 8 Puzzle Problem
class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.n = len(board)
        self.empty_tile = self.find_empty()

    def find_empty(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def heuristic(self):
        dist = 0
        goal_positions = {self.goal[i][j]: (i, j) for i in range(self.n) for j in range(self.n)}
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] != 0:
                    x, y = goal_positions[self.board[i][j]]
                    dist += abs(x - i) + abs(y - j)
        return dist

    def get_neighbors(self):
        x, y = self.empty_tile
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbor = Puzzle(new_board, self.goal)
                neighbors.append(neighbor)
        return neighbors

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

    def print_board(self):
        for row in self.board:
            print(row)
        print()

def a_star_puzzle(start, goal):
    start_puzzle = Puzzle(start, goal)
    goal_puzzle = Puzzle(goal, goal)
    open_list = []
    heapq.heappush(open_list, (start_puzzle.heuristic(), start_puzzle))
    visited = set()
    iteration_count = 0

    while open_list:
        iteration_count += 1
        _, current = heapq.heappop(open_list)
        if current.board == goal_puzzle.board:
            print(f"Solution found in {iteration_count} iterations:")
            current.print_board()
            return True

        visited.add(current)

        for neighbor in current.get_neighbors():
            if neighbor not in visited:
                heapq.heappush(open_list, (neighbor.heuristic(), neighbor))

    print("No solution found.")
    return False

# Example
if __name__ == "__main__":
    print("Solving Water Jug Problem with A* Algorithm")
    j1_capacity = int(input("Enter the capacity of the first jug: "))
    j2_capacity = int(input("Enter the capacity of the second jug: "))
    
    water_jug = WaterJug(j1_capacity, j2_capacity)
    water_jug.set_target()
    water_jug.a_star_search()

    print("\nSolving 8 Puzzle Problem with A* Algorithm")
    start_state = []
    print("Enter the start state (3x3 grid):")
    for _ in range(3):
        start_state.append(list(map(int, input().split())))
    
    goal_state = []
    print("Enter the goal state (3x3 grid):")
    for _ in range(3):
        goal_state.append(list(map(int, input().split())))

    a_star_puzzle(start_state, goal_state)
