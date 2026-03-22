"""
Day 12: Uniform Cost Search (UCS)
Task: Implement UCS on a weighted grid and compare it with BFS.
"""

import numpy as np
import heapq
from collections import deque

def visualize_grid(grid, path, title="Grid Visualization"):
    """Visualizes the grid with its costs and the final path."""
    print(f"\n{title}:")
    print("S = Start, G = Goal, * = Path, [Cost] = Grid values")
    
    path_set = set(path) if path else set()
    rows, cols = grid.shape
    
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            pos = (r, c)
            val = int(grid[r, c])
            
            # Formatting: If on path, mark with *
            if pos == (0, 0):
                symbol = "S"
            elif pos == (rows-1, cols-1):
                symbol = "G"
            else:
                symbol = "*" if pos in path_set else " "
            
            row_str += f"|{symbol}{val:2} "
        print(row_str + "|")
    print()

def bfs_shortest_path(grid, start, goal):
    """BFS: Finds the path with minimum steps (ignoring costs)."""
    queue = deque([(start, [start])])
    visited = {start}
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            total_cost = sum(grid[px, py] for px, py in path) - grid[start]
            return total_cost, path
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return float('inf'), None

def uniform_cost_search(grid, start, goal):
    """UCS: Finds the path with minimum total cost (Dijkstra's essence)."""
    # Priority Queue stores (cost, current_node, path)
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = {} # visited stores the best cost to reach each node

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        cost, (x, y), path = heapq.heappop(pq)

        if (x, y) == goal:
            return cost, path

        # If we've already found a cheaper way to reach this node, skip it
        if (x, y) in visited and visited[(x, y)] <= cost:
            continue
        visited[(x, y)] = cost

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                # Total cost = current cost + cost of entering neighbor
                new_cost = cost + grid[nx, ny]
                heapq.heappush(pq, (new_cost, (nx, ny), path + [(nx, ny)]))

    return float('inf'), None

if __name__ == "__main__":
    # Create the weighted grid from the task
    # A wall of 9s forces the search to go around or find a high-cost gap.
    grid = np.array([
        [0, 1, 5, 1, 1], # Start is at 0 cost conceptually
        [1, 9, 9, 9, 1],
        [1, 1, 1, 9, 1],
        [9, 9, 1, 9, 1],
        [1, 1, 1, 1, 1]
    ])

    START_POS = (0, 0)
    GOAL_POS = (4, 4)

    print(f"--- Weighted Search Comparison on {grid.shape[0]}x{grid.shape[1]} Grid ---")
    print(f"Grid layout (Costs):")
    print(grid)
    
    # 1. Run BFS (Ignores Weights)
    bfs_cost, bfs_path = bfs_shortest_path(grid, START_POS, GOAL_POS)
    
    # 2. Run UCS (Respects Weights)
    ucs_cost, ucs_path = uniform_cost_search(grid, START_POS, GOAL_POS)

    # Comparison Results
    print("\n" + "="*45)
    print(f"{'Search Algorithm':<20} | {'Total Cost':<10} | {'Steps':<7}")
    print("-" * 45)
    print(f"{'BFS (Simple Steps)':<20} | {bfs_cost:<10} | {len(bfs_path) if bfs_path else 'N/A':<7}")
    print(f"{'UCS (Min Cost)':<20} | {ucs_cost:<10} | {len(ucs_path) if ucs_path else 'N/A':<7}")
    print("="*45)

    if bfs_path:
        visualize_grid(grid, bfs_path, "BFS: Shortest Steps (Ignores weight)")
    
    if ucs_path:
        visualize_grid(grid, ucs_path, "UCS: Lowest Cost (Respects weight)")

    print("\nObservation:")
    print("- BFS simply tries the fewest number of squares (steps).")
    print("- UCS avoids the cells with high cost (9s), even if it takes more steps.")
    print("- Notice how UCS 'snakes' through the 1s and avoids the wall of 9s.")
