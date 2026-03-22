"""
Day 11: Depth-Limited Search (DLS) + Iterative Deepening Search (IDS)
Task: Implement IDS on a grid and observe the depth at which the solution is found.
"""

def visualize_grid(grid_size, grid, path, title="Grid Visualization"):
    """Visualizes the grid, obstacles, and the found path."""
    print(f"\n{title}:")
    print("S = Start, G = Goal, # = Obstacle, * = Path, + = Unvisited")
    
    path_set = set(path) if path else set()
    
    for r in range(grid_size):
        row_str = ""
        for c in range(grid_size):
            pos = (r, c)
            if pos == (0, 0):
                row_str += " S "
            elif pos == (grid_size-1, grid_size-1):
                row_str += " G "
            elif grid[r][c] == 1:
                row_str += " # "
            elif pos in path_set:
                row_str += " * "
            else:
                row_str += " + "
        print(row_str)
    print()

def dls(pos, goal, limit, visited, path, grid, nodes_explored_counter):
    nodes_explored_counter[0] += 1
    
    if pos == goal:
        return path
    if limit <= 0:
        return None

    visited.add(pos)
    x, y = pos
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        neighbor = (nx, ny)
        
        # Grid boundaries and obstacle check
        if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and 
            grid[nx][ny] == 0 and neighbor not in visited):
            
            result = dls(neighbor, goal, limit - 1, visited.copy(), path + [neighbor], grid, nodes_explored_counter)
            if result:
                return result
                
    return None

def iterative_deepening_search(start, goal, grid, max_depth=50):
    total_nodes_explored = 0
    
    for depth in range(max_depth):
        print(f"Searching at depth limit: {depth}...", end="\r")
        nodes_at_this_depth = [0]
        # In IDS, we reset visited set per iteration if we want to find the shallowest path accurately 
        # or if we're simulating a fresh DFS search at each depth limit.
        # Actually, using a fresh visited set *during* each DLS path is traditional for DFS.
        result = dls(start, goal, depth, set(), [start], grid, nodes_at_this_depth)
        
        total_nodes_explored += nodes_at_this_depth[0]
        
        if result:
            print(f"\nGoal found at depth: {depth}!")
            return result, depth, total_nodes_explored
            
    print("\nGoal not found within max depth.")
    return None, None, total_nodes_explored

if __name__ == "__main__":
    # Grid Setup (6x6)
    SIZE = 6
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    
    # Placing Obstacles as per task
    grid[2][2] = 1
    grid[3][2] = 1
    grid[4][4] = 1
    
    START_POS = (0, 0)
    GOAL_POS = (SIZE-1, SIZE-1)
    
    print(f"--- Iterative Deepening Search (IDS) on {SIZE}x{SIZE} Grid ---")
    print(f"Start: {START_POS} | Goal: {GOAL_POS}")
    
    path, depth_found, total_explored = iterative_deepening_search(START_POS, GOAL_POS, grid)
    
    if path:
        print(f"\nFinal Results:")
        print(f"Shallowest Path Depth: {depth_found}")
        print(f"Total Nodes Processed (all iterations): {total_explored}")
        print(f"Path Taken: {path}")
        
        visualize_grid(SIZE, grid, path, "IDS Final Path")
    else:
        print("No path found.")

    print("\nObservation:")
    print("- IDS behaves like BFS by finding the shallowest solution first.")
    print("- IDS behaves like DFS in terms of memory: it doesn't store the entire frontier.")
    print("- The drawback is re-exploring nodes at shallow depths for each new limit.")

