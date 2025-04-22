from queue import Queue 

# Function to get the graph as input from the user
def get_graph_input():
    num_cities = int(input("Enter the number of cities: "))
    graph = []
    for i in range(num_cities):
        row = list(map(int, input(f"Enter the distances from city {i} to others (comma separated): ").split(',')))
        graph.append(row)
    return graph, num_cities

# Function to calculate the cost of a path
def calculate_path_cost(path, graph): 
    cost = 0 
    for i in range(len(path) - 1): 
        cost += graph[path[i]][path[i + 1]] 
    cost += graph[path[-1]][path[0]]  # Return to the starting city 
    return cost

# Depth-First Search (DFS) for TSP
def dfs_tsp(graph, num_cities, start): 
    stack = [(start, [start])]  # (current city, path) 
    min_cost = float('inf') 
    best_path = None
    dfs_iterations = 0

    while stack: 
        city, path = stack.pop()
        dfs_iterations += 1

        if len(path) == num_cities:  # All cities visited 
            path_cost = calculate_path_cost(path, graph) 
            if path_cost < min_cost: 
                min_cost = path_cost 
                best_path = path 
        else: 
            for next_city in range(num_cities): 
                if next_city not in path: 
                    stack.append((next_city, path + [next_city])) 

    return best_path, min_cost, dfs_iterations

# Breadth-First Search (BFS) for TSP
def bfs_tsp(graph, num_cities, start): 
    queue = Queue() 
    queue.put((start, [start]))  # (current city, path) 
    min_cost = float('inf') 
    best_path = None
    bfs_iterations = 0

    while not queue.empty(): 
        city, path = queue.get()
        bfs_iterations += 1

        if len(path) == num_cities:  # All cities visited 
            path_cost = calculate_path_cost(path, graph) 
            if path_cost < min_cost: 
                min_cost = path_cost 
                best_path = path 
        else: 
            for next_city in range(num_cities): 
                if next_city not in path: 
                    queue.put((next_city, path + [next_city])) 

    return best_path, min_cost, bfs_iterations

# Main function
def main():
    # Get user input for graph
    graph, num_cities = get_graph_input()

    start_city = int(input("Enter the starting city (0 to {}): ".format(num_cities - 1)))

    # Run DFS and BFS
    dfs_result = dfs_tsp(graph, num_cities, start_city) 
    bfs_result = bfs_tsp(graph, num_cities, start_city) 

    # Print results
    print("\nDFS Result:")
    print("Best Path:", dfs_result[0], "with Cost:", dfs_result[1], "in", dfs_result[2], "iterations")

    print("\nBFS Result:")
    print("Best Path:", bfs_result[0], "with Cost:", bfs_result[1], "in", bfs_result[2], "iterations")

if __name__ == "__main__":
    main()
