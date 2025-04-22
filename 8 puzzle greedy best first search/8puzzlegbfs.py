import heapq

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
        """Manhattan distance heuristic"""
        dist = 0
        goal_positions = {self.goal[i][j]: (i, j) for i in range(self.n) for j in range(self.n)}
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] != 0:
                    x, y = goal_positions[self.board[i][j]]
                    dist += abs(x - i) + abs(y - j)
        return dist

    def get_neighbors(self):
        """Generate possible moves"""
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

def greedy_best_first_search(start, goal):
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

# Main code
if __name__ == "__main__":
    print("Enter the 8-puzzle start state (use 0 for empty space):")
    start_state = []
    for _ in range(3):
        start_state.append(list(map(int, input().split())))

    print("Enter the goal state:")
    goal_state = []
    for _ in range(3):
        goal_state.append(list(map(int, input().split())))

    print("\nSolving the puzzle using Greedy Best First Search...\n")
    greedy_best_first_search(start_state, goal_state)
