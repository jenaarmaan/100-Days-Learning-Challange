"""
Day 9: Breadth First Search (BFS)
Task: Implement BFS and find the shortest path in an unweighted grid with obstacles.
"""

from collections import deque

def visualize_grid(grid_size, path, obstacles, visited):
    """Visualizes the grid, obstacles, and the found path."""
    print("\nGrid Visualization:")
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

def bfs_shortest_path(grid_size, start, goal, obstacles):
    """
    Finds the shortest path from start to goal in a grid using BFS.
    """
    # Each element in the queue stores (current_node, path_to_current)
    queue = deque([(start, [start])])
    
    # We mark visited nodes to avoid cycles and redundant work
    visited = {start}
    
    moves = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0)   # Up
    ]
    
    while queue:
        current, path = queue.popleft()
        
        # If we reached the goal, BFS guarantees this path is the shortest!
        if current == goal:
            return path, visited
        
        # Explore neighbors
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            
            # Check boundaries, obstacles, and visited set
            if (0 <= nx < grid_size and 0 <= ny < grid_size and 
                neighbor not in obstacles and neighbor not in visited):
                
                visited.add(neighbor)
                # BFS stores the entire path in the queue for simplicity here,
                # though usually we store parent pointers for memory efficiency.
                queue.append((neighbor, path + [neighbor]))
                
    return None, visited

if __name__ == "__main__":
    # Settings
    SIZE = 8
    START_POS = (0, 0)
    GOAL_POS = (SIZE-1, SIZE-1)
    
    # Obstacles to force a non-trivial path
    OBSTACLES = {
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
        (3, 3), (4, 3), (5, 3), (6, 3), (2, 3),
        (5, 5), (5, 6), (5, 7), (4, 5)
    }
    
    print(f"--- BFS on {SIZE}x{SIZE} Grid ---")
    print(f"Start: {START_POS} | Goal: {GOAL_POS}")
    
    final_path, explored_nodes = bfs_shortest_path(SIZE, START_POS, GOAL_POS, OBSTACLES)
    
    if final_path:
        print(f"Shortest Path Found! Length: {len(final_path)}")
        print(f"Path taken: {final_path}")
        print(f"Total Nodes Explored: {len(explored_nodes)}")
        visualize_grid(SIZE, final_path, OBSTACLES, explored_nodes)
    else:
        print("No path found.")
        visualize_grid(SIZE, [], OBSTACLES, explored_nodes)
        
    print("\nObservation:")
    print("- BFS explores level by level (ripples).")
    print("- Notice how many '.' (explored) nodes there are compared to '*' (path) nodes.")
    print("- This illustrates why BFS uses a lot of memory: it keeps track of the 'frontier'.")
