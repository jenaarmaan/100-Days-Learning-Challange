import heapq

# Settings
grid_size = 10
start = (0, 0)
goal = (9, 9)
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Obstacles - a wall that might trip up a simple greedy approach
obstacles = {(4, i) for i in range(8)}  # A wall blocking the direct path

def manhattan(a, b):
    # h(n) = |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_valid(x, y):
    return 0 <= x < grid_size and 0 <= y < grid_size and (x, y) not in obstacles

def ucs_search(start, goal):
    """Uniform Cost Search (Blind Search) - Guarantees Optimal Path"""
    pq = []
    # (cost_g, current_node, path)
    heapq.heappush(pq, (0, start, [start]))
    visited = set()
    expanded = 0
    
    while pq:
        g, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        expanded += 1
        visited.add(current)
        
        if current == goal:
            return path, expanded
            
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                heapq.heappush(pq, (g + 1, (nx, ny), path + [(nx, ny)]))
                
    return None, expanded

def greedy_search(start, goal):
    """Greedy Best-First Search (Informed Search) - Very Fast, but Not Always Optimal"""
    pq = []
    # (h_n, current_node, path)
    heapq.heappush(pq, (manhattan(start, goal), start, [start]))
    visited = set()
    expanded = 0
    
    while pq:
        _, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        expanded += 1
        visited.add(current)
        
        if current == goal:
            return path, expanded
            
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                heapq.heappush(pq, (manhattan((nx, ny), goal), (nx, ny), path + [(nx, ny)]))
                
    return None, expanded

if __name__ == "__main__":
    print(f"--- Pathfinding: {start} to {goal} ---")
    print(f"Wall obstacles present at x=4.")
    
    # Run UCS
    path_ucs, expand_ucs = ucs_search(start, goal)
    print("\n[Uniform Cost Search (Blind)]")
    print(f"Nodes Expanded: {expand_ucs}")
    print(f"Path Length:    {len(path_ucs)}")
    
    # Run Greedy
    path_greedy, expand_greedy = greedy_search(start, goal)
    print("\n[Greedy Best-First Search (Heuristic)]")
    print(f"Nodes Expanded: {expand_greedy}")
    print(f"Path Length:    {len(path_greedy)}")
    
    if len(path_greedy) > len(path_ucs):
        print("\nNotice: Greedy search found a LONGER path than UCS because it ignores the cost so far and only considers the heuristic estimate to the goal.")
    else:
        print("\nNotice: Both algorithms found the same path length, but Greedy Search likely expanded far fewer nodes.")
