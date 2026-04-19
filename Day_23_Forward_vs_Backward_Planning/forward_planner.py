from collections import deque
import copy

# Initial state
initial_state = {
    "RobotAt": "A",
    "BoxAt": "B",
    "Holding": False
}

goal_state = {
    "BoxAt": "A"
}

# Action definitions
def move_to_a(state):
    """Moves the robot to location A if it's not already there."""
    if state["RobotAt"] != "A":
        new_state = copy.deepcopy(state)
        new_state["RobotAt"] = "A"
        return new_state
    return None

def move_to_b(state):
    """Moves the robot to location B if it's not already there."""
    if state["RobotAt"] != "B":
        new_state = copy.deepcopy(state)
        new_state["RobotAt"] = "B"
        return new_state
    return None

def pick(state):
    """The robot picks up the box if it is at the same location and hand is empty."""
    if state["RobotAt"] == state["BoxAt"] and not state["Holding"]:
        new_state = copy.deepcopy(state)
        new_state["Holding"] = True
        new_state["BoxAt"] = None
        return new_state
    return None

def drop(state):
    """The robot drops the box at its current location."""
    if state["Holding"]:
        new_state = copy.deepcopy(state)
        new_state["Holding"] = False
        new_state["BoxAt"] = state["RobotAt"]
        return new_state
    return None

def is_goal(state):
    """Checks if the goal condition (BoxAt A) is met."""
    return state["BoxAt"] == goal_state["BoxAt"]

def forward_planner():
    """Implements a forward (progression) planner using BFS."""
    # queue stores (current_state, plan_so_far)
    queue = deque([(initial_state, [])])
    visited = []

    while queue:
        state, plan = queue.popleft()

        if is_goal(state):
            return plan, len(visited)

        if state in visited:
            continue
        visited.append(state)

        # Possible actions
        actions = [
            ("move_to_a", move_to_a),
            ("move_to_b", move_to_b),
            ("pick", pick),
            ("drop", drop)
        ]

        for name, action_func in actions:
            new_state = action_func(state)
            if new_state and new_state not in visited:
                queue.append((new_state, plan + [name]))

    return None, len(visited)

if __name__ == "__main__":
    plan, states_explored = forward_planner()
    if plan:
        print("Plan found:", " -> ".join(plan))
        print(f"States explored: {states_explored}")
    else:
        print("No plan found.")

    print("\n--- Observation ---")
    print("1. Forward planning starts from the initial state and moves toward the goal.")
    print("2. Notice how 'states explored' grows as you add more possible actions or locations.")
    print("3. Backward planning would start from 'BoxAt: A' and deduce that 'drop' must be the last action.")
