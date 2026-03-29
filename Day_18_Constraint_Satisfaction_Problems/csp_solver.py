"""
Simple CSP: 3-variable map coloring
Goal: Assign Red, Green, or Blue to A, B, and C such that:
- A != B
- B != C
- A != C
"""

# 1. Variables
variables = ['A', 'B', 'C']

# 2. Domains
domains = {
    'A': ['Red', 'Green', 'Blue'],
    'B': ['Red', 'Green', 'Blue'],
    'C': ['Red', 'Green', 'Blue']
}

# 3. Constraints
constraints = [
    ('A', 'B'),
    ('B', 'C'),
    ('A', 'C')
]

def is_valid(assignment, var, value):
    """
    Checks if assigning `value` to `var` is consistent with the current assignment
    """
    for (v1, v2) in constraints:
        if var == v1 and v2 in assignment and assignment[v2] == value:
            return False
        if var == v2 and v1 in assignment and assignment[v1] == value:
            return False
    return True

def backtrack(assignment):
    """
    Backtracking search algorithm
    """
    # Base case: if assignment is complete, return it
    if len(assignment) == len(variables):
        return assignment

    # Select an unassigned variable
    unassigned = [v for v in variables if v not in assignment][0]

    # Try assigning each value from its domain
    for value in domains[unassigned]:
        if is_valid(assignment, unassigned, value):
            assignment[unassigned] = value
            result = backtrack(assignment)
            if result:
                return result
            # Backtrack if assignment didn't lead to a solution
            del assignment[unassigned]

    return None

if __name__ == "__main__":
    solution = backtrack({})
    print("Map Coloring Results (A, B, C):")
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution found.")
