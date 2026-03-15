"""
Day 5 Task: Rational Agent Simulation
Building an agent that selects actions based on expected reward/utility.
"""

import numpy as np

# 1. Setup the Environment
grid = np.zeros((5, 5))
grid[4, 4] = 10   # High Reward (Goal)
grid[2, 2] = -5   # Penalty (Trap)
grid[1, 1] = -2   # Small Penalty

# 2. Agent Configuration
current_position = [0, 0]
moves = [
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
    (-1, 0)   # Up
]

def choose_rational_action(pos):
    """
    RATIONALITY: Choose the move that yields the highest local reward.
    """
    best_move = None
    best_score = -np.inf

    for dx, dy in moves:
        nx, ny = pos[0] + dx, pos[1] + dy
        
        # Check boundary constraints
        if 0 <= nx < 5 and 0 <= ny < 5:
            score = grid[nx, ny]
            # Greedy rational choice
            if score > best_score:
                best_score = score
                best_move = (dx, dy)

    return best_move

def main():
    print("--- Day 5: Intelligent Agent Simulation ---")
    print("Agent starting at [0, 0]")
    
    pos = list(current_position)
    path = [tuple(pos)]

    # Simulate 10 steps of rational decision making
    for step in range(1, 11):
        move = choose_rational_action(pos)
        
        if move:
            pos[0] += move[0]
            pos[1] += move[1]
            path.append(tuple(pos))
            
            reward = grid[pos[0], pos[1]]
            print(f"Step {step}: Moved to {pos} | Local Reward: {reward}")
            
            # If we reached the high reward, let's stop
            if reward == 10:
                print("Goal reached!")
                break
        else:
            print("No valid moves available.")
            break

    print("\n[Final Report]")
    print(f"Final position: {pos}")
    print(f"Path taken: {path}")
    
    print("\n[Reflection]")
    print("The agent is 'locally' rational because it picks the best immediate move.")
    print("To be 'globally' rational, it would need a search algorithm or reinforcement learning")
    print("to look ahead beyond immediate neighbors.")

if __name__ == "__main__":
    main()
