"""
Day 4 Task: Grid Navigation Problem Formulation
Modeling a simple search environment by defining states, actions, and constraints.
"""

import numpy as np

# 1. Define the Environment (The Grid)
# 0 = Empty, 1 = Obstacle
grid = np.zeros((5, 5))
grid[1, 1] = 1  # obstacle
grid[2, 2] = 1  # obstacle
grid[3, 3] = 1  # obstacle

# 2. Define Initial and Goal States
start_state = (0, 0)
goal_state = (4, 4)

# 3. Define Valid Actions
moves = [
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
    (-1, 0)   # Up
]

def get_next_states(current_pos):
    """
    Simulates state transitions based on valid actions and constraints.
    """
    valid_next_states = []
    
    for dx, dy in moves:
        # Calculate new position
        nx, ny = current_pos[0] + dx, current_pos[1] + dy
        
        # Check Constraints:
        # 1. Must be within grid boundaries
        # 2. Must not be an obstacle
        if 0 <= nx < 5 and 0 <= ny < 5:
            if grid[nx, ny] == 0:
                valid_next_states.append((nx, ny))
                
    return valid_next_states

def main():
    print("--- Day 4: AI Problem Formulation - Grid Navigation ---")
    print(f"Grid Size: 5x5")
    print(f"Start State: {start_state}")
    print(f"Goal State: {goal_state}")
    print("Obstacles at: (1,1), (2,2), (3,3)\n")

    # Test the formulation
    current = start_state
    print(f"Available moves from {current}: {get_next_states(current)}")

    # Move to (0,1) and check again
    test_pos = (1, 0)
    print(f"Available moves from {test_pos}: {get_next_states(test_pos)}")
    
    # Path simulation hint
    print("\n[Reflection]")
    print("This formulation provides the 'rules' of the game.")
    print("A search algorithm (like BFS or A*) can now use 'get_next_states' to find the path to the goal.")

if __name__ == "__main__":
    main()
