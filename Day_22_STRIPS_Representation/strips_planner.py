from collections import deque
import copy

# Initial world state
initial_state = {
    "At_A": True,
    "At_B": False,
    "BoxAt_B": True,
    "BoxAt_A": False,
    "Holding": False,
    "HandEmpty": True
}

goal_state = {
    "BoxAt_A": True
}

# STRIPS-style actions
actions = {
    "Move_A_B": {
        "pre": ["At_A"],
        "add": ["At_B"],
        "del": ["At_A"]
    },
    "Move_B_A": {
        "pre": ["At_B"],
        "add": ["At_A"],
        "del": ["At_B"]
    },
    "Pick_Box": {
        "pre": ["At_B", "BoxAt_B", "HandEmpty"],
        "add": ["Holding"],
        "del": ["BoxAt_B", "HandEmpty"]
    },
    "Drop_Box": {
        "pre": ["At_A", "Holding"],
        "add": ["BoxAt_A", "HandEmpty"],
        "del": ["Holding"]
    }
}

def preconditions_met(state, action):
    """Check if all preconditions of an action are True in the current state."""
    return all(state.get(p, False) for p in action["pre"])

def apply_action(state, action):
    """Update state by removing 'del' effects and adding 'add' effects."""
    new_state = copy.deepcopy(state)

    for d in action["del"]:
        new_state[d] = False

    for a in action["add"]:
        new_state[a] = True

    return new_state

def goal_reached(state):
    """Check if the goal state is satisfied in the current state."""
    return all(state.get(g, False) for g in goal_state)

def planner():
    """BFS-based planner to find a sequence of STRIPS actions."""
    # queue stores (current_state, plan_so_far)
    queue = deque([(initial_state, [])])
    visited = []

    while queue:
        state, plan = queue.popleft()

        if goal_reached(state):
            return plan

        if state in visited:
            continue
        visited.append(state)

        for name, action in actions.items():
            if preconditions_met(state, action):
                new_state = apply_action(state, action)
                if new_state not in visited:
                    queue.append((new_state, plan + [name]))

    return None

if __name__ == "__main__":
    plan = planner()
    if plan:
        print("Plan found:", " -> ".join(plan))
    else:
        print("No plan found.")

    print("\n--- Observation ---")
    print("1. Preconditions control which actions are available at each state.")
    print("2. Add/Delete lists provide a clean way to update a logical world model.")
    print("3. BFS ensures we find the shortest path from initial to goal state.")
