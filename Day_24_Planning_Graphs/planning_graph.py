import copy

# Initial state
initial_state = {"At_A", "BoxAt_B", "HandEmpty"}

# Action definitions
actions = {
    "Move_A_B": {
        "pre": {"At_A"},
        "add": {"At_B"},
        "del": {"At_A"}
    },
    "Move_B_A": {
        "pre": {"At_B"},
        "add": {"At_A"},
        "del": {"At_B"}
    },
    "Pick_Box": {
        "pre": {"At_B", "BoxAt_B", "HandEmpty"},
        "add": {"Holding"},
        "del": {"BoxAt_B", "HandEmpty"}
    },
    "Drop_Box": {
        "pre": {"At_A", "Holding"},
        "add": {"BoxAt_A", "HandEmpty"},
        "del": {"Holding"}
    }
}

def applicable_actions(state):
    """Finds all actions whose preconditions are met by the current state."""
    possible = []
    for name, action in actions.items():
        if action["pre"].issubset(state):
            possible.append(name)
    return possible

def build_planning_graph(initial_state, levels=3):
    """
    Builds state and action layers of a planning graph.
    Note: Highly simplified version (no mutex detection).
    """
    state_layers = [initial_state]
    action_layers = []

    current_state = copy.deepcopy(initial_state)

    for i in range(levels):
        # 1. Action Layer (Actions whose preconditions are in the previous state layer)
        possible_actions = applicable_actions(current_state)
        action_layers.append(possible_actions)

        # 2. State Layer (Union of previous state layer and all possible action effects)
        # In a real planning graph, state layer contains all literals that could be true
        next_state = copy.deepcopy(current_state)
        for action in possible_actions:
            next_state |= actions[action]["add"]

        state_layers.append(next_state)
        current_state = next_state

    return state_layers, action_layers

if __name__ == "__main__":
    states, actions_layers = build_planning_graph(initial_state, levels=4)

    print("--- Simplified Planning Graph Expansion ---")
    
    print("\nState Layers:")
    for i, s in enumerate(states):
        print(f"S{i}: {sorted(list(s))}")

    print("\nAction Layers:")
    for i, a in enumerate(actions_layers):
        print(f"A{i}: {a}")

    # Check for goal reachability
    goal = "BoxAt_A"
    for i, s in enumerate(states):
        if goal in s:
            print(f"\nGoal '{goal}' first appears in State Layer S{i}")
            break
    else:
        print(f"\nGoal '{goal}' not reachable within {len(actions_layers)} levels.")

    print("\n--- Observation ---")
    print("1. S0 is the initial world state.")
    print("2. A0 contains all actions whose preconditions are in S0.")
    print("3. S1 contains all facts from S0 plus the 'Add' effects of actions in A0.")
    print("4. This expansion continues until the goal appears or the graph levels off.")
