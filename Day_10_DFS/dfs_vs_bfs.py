"""
Day 10: Depth First Search (DFS)
Task: Implement DFS and compare its path to BFS on the same grid.
"""

from collections import deque

def visualize_grid(grid_size, path, obstacles, visited, title="Grid Visualization"):
    """Visualizes the grid, obstacles, and the found path."""
    print(f"\n{title}:")
    print("S = Start, G = Goal, # = Obstacle, * = Path, . = Explored, + = Unvisited")
    
    path_set = set(path) if path else set()
    
    for r in range(grid_size):
        row_str = ""
        for c in range(grid_size):
            pos = (r, c)
            if pos == (0, 0):
                row_str += " S "
            elif pos == (grid_size-1, grid_size-1):
                row_str += " G "
            elif pos in obstacles:
                row_str += " # "
            elif pos in path_set:
                row_str += " * "
            elif pos in visited:
                row_str += " . "
            else:
                row_str += " + "
        print(row_str)
    print()

def bfs(grid_size, start, goal, obstacles):
    """
    Finds the shortest path from start to goal in a grid using BFS.
    """
    queue = deque([(start, [start])])
    visited = {start}
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path, visited
        
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            
            if (0 <= nx < grid_size and 0 <= ny < grid_size and 
                neighbor not in obstacles and neighbor not in visited):
                
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None, visited

def dfs(grid_size, start, goal, obstacles):
    """
    Finds a path from start to goal in a grid using DFS (Stack-based).
    """
    # LIFO: Last In First Out
    stack = [(start, [start])]
    visited = {start}
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    while stack:
        current, path = stack.pop()
        
        if current == goal:
            return path, visited
        
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            
            if (0 <= nx < grid_size and 0 <= ny < grid_size and 
                neighbor not in obstacles and neighbor not in visited):
                
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
                
    return None, visited

if __name__ == "__main__":
    # Settings from Day 9 to make it comparable
    SIZE = 8
    START_POS = (0, 0)
    GOAL_POS = (SIZE-1, SIZE-1)
    
    # Same obstacles as Day 9 (corresponds to a narrow maze-like environment)
    # Using a variety of obstacles to force both algorithms to work hard
    OBSTACLES = {
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
        (3, 3), (4, 3), (5, 3), (6, 3), (2, 3),
        (5, 5), (5, 6), (5, 7), (4, 5)
    }
    
    print(f"--- Comparison: BFS vs DFS on {SIZE}x{SIZE} Grid ---")
    print(f"Start: {START_POS} | Goal: {GOAL_POS}")
    
    # Run BFS
    bfs_path, bfs_explored = bfs(SIZE, START_POS, GOAL_POS, OBSTACLES)
    
    # Run DFS
    dfs_path, dfs_explored = dfs(SIZE, START_POS, GOAL_POS, OBSTACLES)
    
    # RESULTS COMPARISON
    print("\n" + "="*40)
    print(f"{'Metric':<20} | {'BFS (Queue)':<12} | {'DFS (Stack)':<12}")
    print("-" * 50)
    print(f"{'Path Found?':<20} | {'Yes' if bfs_path else 'No':<12} | {'Yes' if dfs_path else 'No':<12}")
    print(f"{'Path Length':<20} | {len(bfs_path) if bfs_path else 'N/A':<12} | {len(dfs_path) if dfs_path else 'N/A':<12}")
    print(f"{'Nodes Explored':<20} | {len(bfs_explored):<12} | {len(dfs_explored):<12}")
    print("="*40)

    # VISUALIZATION
    if bfs_path:
        visualize_grid(SIZE, bfs_path, OBSTACLES, bfs_explored, "BFS Path (Shortest Guaranteed)")
    
    if dfs_path:
        visualize_grid(SIZE, dfs_path, OBSTACLES, dfs_explored, "DFS Path (First Branch Found)")

    print("\nReflections:")
    print("- BFS explores all neighbors layer by layer, guaranteeing the shortest path in unweighted grids.")
    print("- DFS dives deep down one branch. It might find a path VERY different from the shortest one.")
    print("- In BFS, we visited more nodes generally if the goal is far, but BFS is systematic.")
    print("- If we reordered the 'moves' list in DFS, we would get a completely different path.")
