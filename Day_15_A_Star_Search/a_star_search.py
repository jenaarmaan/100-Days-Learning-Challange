import heapq

# Configuration
grid_size = 10
start = (0, 0)
goal = (9, 9)
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# A slightly complex wall to test all three algorithms
obstacles = {(4, i) for i in range(2, 10)} | {(7, i) for i in range(0, 8)}

def manhattan(a, b):
    # h(n) = |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_valid(x, y):
    return 0 <= x < grid_size and 0 <= y < grid_size and (x, y) not in obstacles

def ucs_search(start, goal):
    """UCS: No heuristic, just g(n). Guaranteed Optimal."""
    pq = []
    # (g_n, current, path)
    heapq.heappush(pq, (0, start, [start]))
    visited = {}
    expanded = 0
    
    while pq:
        g, current, path = heapq.heappop(pq)
        
        if current in visited and visited[current] <= g:
            continue
        
        visited[current] = g
        expanded += 1
        
        if current == goal:
            return path, expanded
            
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny):
                heapq.heappush(pq, (g + 1, (nx, ny), path + [(nx, ny)]))
                
    return None, expanded

def greedy_search(start, goal):
    """Greedy Search: Only h(n). Fast but Not Optimal."""
    pq = []
    # (h_n, current, path)
    heapq.heappush(pq, (manhattan(start, goal), start, [start]))
    visited = set()
    expanded = 0
    
    while pq:
        _, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        visited.add(current)
        expanded += 1
        
        if current == goal:
            return path, expanded
            
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                heapq.heappush(pq, (manhattan((nx, ny), goal), (nx, ny), path + [(nx, ny)]))
                
    return None, expanded

def a_star_search(start, goal):
    """A* Search: g(n) + h(n). Guaranteed Optimal & Faster than UCS."""
    pq = []
    # (f_n, current, path, g_n)
    heapq.heappush(pq, (manhattan(start, goal), start, [start], 0))
    visited = {} # current -> shortest g_n found so far
    expanded = 0
    
    while pq:
        f, current, path, g = heapq.heappop(pq)
        
        if current in visited and visited[current] <= g:
            continue
            
        visited[current] = g
        expanded += 1
        
        if current == goal:
            return path, expanded
            
        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny):
                new_g = g + 1
                new_f = new_g + manhattan((nx, ny), goal)
                heapq.heappush(pq, (new_f, (nx, ny), path + [ (nx, ny) ], new_g))
                
    return None, expanded

if __name__ == "__main__":
    print(f"--- Algorithm Comparison: {start} to {goal} ---")
    
    # 1. UCS
    p_ucs, e_ucs = ucs_search(start, goal)
    print(f"\n[UCS (Optimal, Blind)]")
    print(f"Nodes Expanded: {e_ucs}")
    print(f"Path Length:    {len(p_ucs) if p_ucs else 'N/A'}")
    
    # 2. Greedy Search
    p_greedy, e_greedy = greedy_search(start, goal)
    print(f"\n[Greedy (Fast, Sub-optimal)]")
    print(f"Nodes Expanded: {e_greedy}")
    print(f"Path Length:    {len(p_greedy) if p_greedy else 'N/A'}")
    
    # 3. A* Search
    p_astar, e_astar = a_star_search(start, goal)
    print(f"\n[A* (Optimal, Efficient)]")
    print(f"Nodes Expanded: {e_astar}")
    print(f"Path Length:    {len(p_astar) if p_astar else 'N/A'}")
    
    print("\n--- Summary ---")
    print(f"A* achieves the same path length as UCS ({len(p_astar)}) but with significantly fewer node expansions ({e_astar} vs {e_ucs}).")
    print(f"In cases with obstacles, Greedy may find a path length longer than {len(p_astar)}.")
