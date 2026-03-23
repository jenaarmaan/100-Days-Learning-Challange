import heapq

# Grid Settings
grid_size = 10
start = (0, 0)
goal = (9, 9)
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(x, y):
    return 0 <= x < grid_size and 0 <= y < grid_size

def manhattan(a, b):
    # h(n) = |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def ucs_search(start, goal):
    """
    Uniform Cost Search (No Heuristic)
    Priority = Current Cost g(n)
    Since all costs are 1, this behaves like BFS.
    """
    pq = []
    # (cost, current_node, path)
    heapq.heappush(pq, (0, start, [start]))
    visited = set()
    expanded_count = 0
    
    while pq:
        cost, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        expanded_count += 1
        visited.add(current)
        
        if current == goal:
            return path, expanded_count
            
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                heapq.heappush(pq, (cost + 1, (nx, ny), path + [(nx, ny)]))
                
    return None, expanded_count

def greedy_search(start, goal):
    """
    Greedy Best-First Search
    Priority = Heuristic h(n)
    """
    pq = []
    # (h(n), current_node, path)
    heapq.heappush(pq, (manhattan(start, goal), start, [start]))
    visited = set()
    expanded_count = 0
    
    while pq:
        _, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        expanded_count += 1
        visited.add(current)
        
        if current == goal:
            return path, expanded_count
            
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                heapq.heappush(pq, (manhattan((nx, ny), goal), (nx, ny), path + [(nx, ny)]))
                
    return None, expanded_count

if __name__ == "__main__":
    print(f"--- Grid Search Comparison: {start} to {goal} ---")
    
    # Run UCS
    path_ucs, expanded_ucs = ucs_search(start, goal)
    print("\n[Uniform Cost Search (Blind Search)]")
    print(f"Nodes Expanded: {expanded_ucs}")
    print(f"Path Length:    {len(path_ucs) if path_ucs else 'N/A'}")
    
    # Run Greedy
    path_greedy, expanded_greedy = greedy_search(start, goal)
    print("\n[Greedy Search (Heuristic-Informed)]")
    print(f"Nodes Expanded: {expanded_greedy}")
    print(f"Path Length:    {len(path_greedy) if path_greedy else 'N/A'}")
    
    print("\nObservation: Heuristics guide the search towards the goal, reducing the number of nodes explored.")
