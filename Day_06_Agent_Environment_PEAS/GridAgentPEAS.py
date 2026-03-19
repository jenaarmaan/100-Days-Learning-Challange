import numpy as np
import time

# --- Day 6: Agent-Environment Interaction & PEAS Simulation ---

"""
PEAS Definition:
- Performance: Reach goal with minimum steps (efficiency).
- Environment: 5x5 Grid with an obstacle at (3,3) and goal at (4,4).
- Actuators: Move (Up, Down, Left, Right).
- Sensors: Current grid position (x, y).
"""

# 1. ENVIRONMENT DEFINITION
GRID_SIZE = 5
grid = np.zeros((GRID_SIZE, GRID_SIZE))
grid[3, 3] = -1   # Obstacle
GOAL = (4, 4)     # Goal position

# 2. AGENT DEFINITION
class GridAgent:
    def __init__(self, start_pos=[0, 0]):
        self.position = list(start_pos)
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (dx, dy)
        self.steps = 0

    def get_sensors(self):
        # The agent's sensor returns its current grid position
        return tuple(self.position)

    def select_action(self, goal, obstacle_pos=(3, 3)):
        # Simple heuristic: move towards the goal while avoiding obstacles
        best_move = None
        best_dist = float('inf')

        # Perception: Agent "sees" current position through sensors
        current_pos = self.get_sensors()

        for dx, dy in self.moves:
            nx, ny = current_pos[0] + dx, current_pos[1] + dy
            
            # Check environment constraints: valid move
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) != obstacle_pos:
                # Calculate distance to goal (Performance measurement proxy)
                dist = abs(goal[0] - nx) + abs(goal[1] - ny)
                if dist < best_dist:
                    best_dist = dist
                    best_move = (dx, dy)
        
        return best_move

    def execute_action(self, move):
        # Actuators: Move the agent
        if move:
            self.position[0] += move[0]
            self.position[1] += move[1]
            self.steps += 1
            return True
        return False

# 3. INTERACTION LOOP (Simulation)
def run_simulation():
    agent = GridAgent(start_pos=[0, 0])
    print(f"Agent starting at {agent.position}")
    print(f"Goal is at {GOAL}")
    print(f"Obstacle is at (3, 3)")
    print("-" * 20)

    while agent.get_sensors() != GOAL and agent.steps < 20:
        # Sensor feedback
        current_status = agent.get_sensors()
        
        # Agent decides on action
        move = agent.select_action(GOAL)
        
        # Actuator interaction
        if not agent.execute_action(move):
            print("Agent is stuck!")
            break
            
        # Visualization (optional)
        print(f"Step {agent.steps}: Moved to {agent.position}")
        
        # (Optional) Display grid
        display_grid = np.full((GRID_SIZE, GRID_SIZE), ".", dtype=str)
        display_grid[3, 3] = "X" # Obstacle
        display_grid[GOAL] = "G" # Goal
        display_grid[tuple(agent.position)] = "A" # Agent
        
        for row in display_grid:
            print(" ".join(row))
        print("-" * 20)
        time.sleep(0.3)

    # 4. PERFORMANCE MEASUREMENT
    if agent.get_sensors() == GOAL:
        print(f"Goal reached successfully!")
        print(f"Total steps taken (Performance): {agent.steps}")
    else:
        print("Agent failed to reach the goal within the step limit.")

if __name__ == "__main__":
    run_simulation()
