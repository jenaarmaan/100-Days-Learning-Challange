"""
Day 8: State Space Representation
Task: Model a simple grid navigation problem and explore reachable states.
"""

import numpy as np

def visualize_grid(grid_size, visited_states):
    """Simple text visualization of the grid and visited states."""
    print("\nGrid Visualization (X = Visited, . = Unvisited):")
    for r in range(grid_size):
        row_str = ""
        for c in range(grid_size):
            if (r, c) in visited_states:
                row_str += " X "
            else:
                row_str += " . "
        print(row_str)
    print()

def get_neighbors(state, grid_size):
    """
    State Transitions function.
    Given a state (x, y), returns all possible next states.
    """
    moves = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1), # Left
        (-1, 0)  # Up
    ]
    
    neighbors = []
    x, y = state
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        # Check if the new state is within the grid boundaries
        if 0 <= nx < grid_size and 0 <= ny < grid_size:
            neighbors.append((nx, ny))
    return neighbors

def explore_state_space(grid_size, start_pos):
    """
    Explores the entire state space starting from a given initial state.
    Uses Depth First Search (DFS) to find all reachable states.
    """
    print(f"--- Exploring State Space for {grid_size}x{grid_size} Grid ---")
    print(f"Initial State: {start_pos}")
    
    visited = set()
    stack = [start_pos]
    
    # Counter for transitions attempted
    transitions_count = 0

    while stack:
        current_state = stack.pop()
        
        if current_state not in visited:
            visited.add(current_state)
            
            # Generate transitions (actions)
            neighbors = get_neighbors(current_state, grid_size)
            transitions_count += len(neighbors)
            
            # Add new states to the stack
            stack.extend(neighbors)

    print(f"Total Reachable States: {len(visited)}")
    print(f"Total Transitions Attempted: {transitions_count}")
    
    # Observe state space explosion
    # For a grid of size N, there are N^2 states.
    print(f"Theoretical Max States (N^2): {grid_size**2}")
    
    return visited

if __name__ == "__main__":
    # Test with a small grid
    GRID_SIZE = 5
    START = (0, 0)
    
    reachable = explore_state_space(GRID_SIZE, START)
    visualize_grid(GRID_SIZE, reachable)
    
    print("Reachable states list:")
    print(sorted(list(reachable)))
    
    # Scenario: Obstacles (Reducing the state space)
    # If we added obstacles, some states would become unreachable.
    # This is how real-world state spaces are often constrained.
    
    print("\nReflecting on State Space Explosion:")
    print("- A 4x4 grid has 16 states.")
    print("- A 10x10 grid has 100 states.")
    print("- A 100x100 grid has 10,000 states.")
    print("- A 3D cube grid of 100x100x100 has 1,000,000 states!")
    print("This exponential growth is why we need efficient search algorithms.")
