"""
Backtracking + Forward Checking for Map Coloring
Variables: A, B, C, D
Domains: {Red, Green, Blue}
Constraints:
- A != B
- A != C
- B != D
- C != D
"""

from copy import deepcopy

# 1. Variables
variables = ['A', 'B', 'C', 'D']

# 2. Domains
domains = {
    'A': ['Red', 'Green', 'Blue'],
    'B': ['Red', 'Green', 'Blue'],
    'C': ['Red', 'Green', 'Blue'],
    'D': ['Red', 'Green', 'Blue']
}

# 3. Constraints (represented as an adjacency list)
constraints = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def is_consistent(var, value, assignment):
    """
    Checks if assigning `value` to `var` is consistent with the current assignment
    """
    for neighbor in constraints[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def forward_check(var, value, domains, assignment):
    """
    Removes inconsistent values from the domains of neighboring unassigned variables.
    Returns the new domains if successful, or None if a domain is wiped out.
    """
    new_domains = deepcopy(domains)
    new_domains[var] = [value]

    for neighbor in constraints[var]:
        if neighbor not in assignment:
            # Remove `value` from the domain of unassigned neighbors
            new_domains[neighbor] = [
                v for v in new_domains[neighbor] if v != value
            ]
            # If a neighbor's domain becomes empty, forward checking fails
            if not new_domains[neighbor]:
                return None
    return new_domains

def backtrack(assignment, domains):
    """
    Backtracking search with Forward Checking
    """
    # Base case: if assignment is complete, return it
    if len(assignment) == len(variables):
        return assignment

    # Select an unassigned variable
    unassigned = [v for v in variables if v not in assignment][0]

    # Try assigning each value from its pruned domain
    for value in domains[unassigned]:
        if is_consistent(unassigned, value, assignment):
            # Apply Forward Checking to prune future domains
            new_domains = forward_check(unassigned, value, domains, assignment)
            if new_domains is not None:
                # Proceed with the assignment
                assignment[unassigned] = value
                result = backtrack(assignment, new_domains)
                if result:
                    return result
                # Backtrack: undo assignment
                del assignment[unassigned]

    return None

if __name__ == "__main__":
    initial_domains = domains  # Store the initial state
    solution = backtrack({}, initial_domains)
    
    print("Backtracking + Forward Checking Results:")
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution found.")
