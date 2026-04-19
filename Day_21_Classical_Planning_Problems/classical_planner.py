from collections import deque
import copy

# Define initial state
initial_state = {
    "RobotAt": "A",
    "BoxAt": "B",
    "Holding": False
}

goal_state = {
    "BoxAt": "A"
}

# Define actions
def move_to_a(state):
    if state["RobotAt"] != "A":
        new_state = copy.deepcopy(state)
        new_state["RobotAt"] = "A"
        return new_state
    return None

def move_to_b(state):
    if state["RobotAt"] != "B":
        new_state = copy.deepcopy(state)
        new_state["RobotAt"] = "B"
        return new_state
    return None

def pick(state):
    if state["RobotAt"] == state["BoxAt"] and not state["Holding"]:
        new_state = copy.deepcopy(state)
        new_state["Holding"] = True
        new_state["BoxAt"] = None
        return new_state
    return None

def drop(state):
    if state["Holding"]:
        new_state = copy.deepcopy(state)
        new_state["Holding"] = False
        new_state["BoxAt"] = state["RobotAt"]
        return new_state
    return None

def is_goal(state):
    return state["BoxAt"] == goal_state["BoxAt"]

def bfs_planner():
    # queue stores (current_state, plan_so_far)
    queue = deque([(initial_state, [])])
    visited = []

    while queue:
        state, plan = queue.popleft()

        if is_goal(state):
            return plan

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

        for action_name, action_func in actions:
            new_state = action_func(state)
            if new_state and new_state not in visited:
                queue.append((new_state, plan + [action_name]))

    return None

if __name__ == "__main__":
    plan = bfs_planner()
    if plan:
        print("Plan found:", " -> ".join(plan))
    else:
        print("No plan found.")

    # Let's also print what to observe as per instructions
    print("\n--- Observation ---")
    print("1. How states are generated: Each action creates a new state dictionary.")
    print("2. BFS guarantees the shortest plan.")
    print("3. Try changing the goal_state or initial_state to see how the plan adapts.")
