import random

def generate_next_states(state, max_a, max_b):
    a, b = state
    next_states = [
        (max_a, b, f"Fill Jug A ({max_a}, {b})"),  # Fill Jug A
        (a, max_b, f"Fill Jug B ({a}, {max_b})"),  # Fill Jug B
        (0, b, f"Empty Jug A (0, {b})"),  # Empty Jug A
        (a, 0, f"Empty Jug B ({a}, 0)"),  # Empty Jug B
    ]

    # Pour from A to B
    transfer_a_to_b = min(a, max_b - b)
    next_states.append((a - transfer_a_to_b, b + transfer_a_to_b, 
                        f"Pour from A to B ({a - transfer_a_to_b}, {b + transfer_a_to_b})"))

    # Pour from B to A
    transfer_b_to_a = min(b, max_a - a)
    next_states.append((a + transfer_b_to_a, b - transfer_b_to_a, 
                        f"Pour from B to A ({a + transfer_b_to_a}, {b - transfer_b_to_a})"))

    return next_states

def evaluate_distance(state, goal_amount):
    return abs(state[0] - goal_amount) + abs(state[1] - goal_amount)

def solve_water_jug(capacity_a, capacity_b, target, max_restarts=3):
    for attempt in range(max_restarts):
        current = (0, 0)
        explored = set()
        path = []

        while current[0] != target and current[1] != target:
            explored.add(current)
            possible_moves = generate_next_states(current, capacity_a, capacity_b)

            # Choose the best move based on heuristic (closest to target)
            next_move = min(
                [s for s in possible_moves if (s[0], s[1]) not in explored], 
                key=lambda s: evaluate_distance((s[0], s[1]), target), 
                default=None
            )

            if next_move is None or evaluate_distance((next_move[0], next_move[1]), target) >= evaluate_distance(current, target):
                break  # No better move found, local maximum reached

            current = (next_move[0], next_move[1])
            path.append(next_move[2])  # Store the action

        if current[0] == target or current[1] == target:
            print("\nSolution Found! Steps:")
            for step in path:
                print(step)
            print(f"Final State: {current}\n")
            return

        print(f"Restarting attempt {attempt + 1}/{max_restarts}...\n")

    print("No solution found after multiple attempts.")

# Take user input
capacity_a = int(input("Enter the capacity of Jug A: "))
capacity_b = int(input("Enter the capacity of Jug B: "))
goal_amount = int(input("Enter the target amount of water: "))

solve_water_jug(capacity_a, capacity_b, goal_amount)
