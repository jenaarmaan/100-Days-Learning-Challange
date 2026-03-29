"""
AC-3 Algorithm for Arc Consistency
Goal: Enforce binary constraints (specifically A != B and B != C)
Variables: A, B, C
Initial Domains: {1, 2, 3}
"""

from collections import deque
from copy import deepcopy

# 1. Variables
variables = ['A', 'B', 'C']

# 2. Domains
domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# 3. Constraints (adjacency list for the constraint graph)
constraints = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

def constraint_satisfied(x, y):
    """
    Binary constraint checker: X != Y
    """
    return x != y

def revise(domains, xi, xj):
    """
    Revises the domain of xi such that for every value in Domain(xi), 
    there is at least one value in Domain(xj) that satisfies the constraint.
    Returns True if the domain was revised.
    """
    revised = False
    for x in domains[xi][:]:
        # If no value y in Domain(xj) satisfies the constraint with x
        if not any(constraint_satisfied(x, y) for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised

def ac3(domains):
    """
    Enforces arc consistency across all binary constraints using AC-3 algorithm.
    """
    # Initialize a queue with all arcs (Xi, Xj) in the CSP
    queue = deque()
    for xi in constraints:
        for xj in constraints[xi]:
            queue.append((xi, xj))

    print(f"Initial Queue Size: {len(queue)}")

    while queue:
        xi, xj = queue.popleft()
        
        if revise(domains, xi, xj):
            # If domain of xi is empty, the CSP is unsolvable
            if not domains[xi]:
                return False
            
            # Since domain of xi changed, re-check consistency for arcs pointing to xi
            # except the arc we just processed (xj -> xi)
            for xk in constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))
                    
    return True

if __name__ == "__main__":
    print("Initial Domains:", domains)
    
    # Example 1: Standard AC-3 run
    domains_copy = deepcopy(domains)
    result = ac3(domains_copy)
    print("\nRun 1 (Standard):")
    print("Arc Consistent:", result)
    print("Pruned Domains:", domains_copy)
    
    # Example 2: Forcing pruning by narrowing a domain
    print("\nRun 2 (Forced Pruning):")
    special_domains = deepcopy(domains)
    # If B can only be 1, and A != B, then A must lose 1.
    special_domains['B'] = [1]
    print(f"Modified Domain for B: {special_domains['B']}")
    
    result_2 = ac3(special_domains)
    print("Arc Consistent:", result_2)
    print("Pruned Domains (A should no longer have 1):", special_domains)
    
    # Example 3: Failure detection
    print("\nRun 3 (Failure Detection):")
    fail_domains = deepcopy(domains)
    # If A and B must both be 1 but A != B, AC-3 should fail.
    fail_domains['A'] = [1]
    fail_domains['B'] = [1]
    print(f"Modified Domains: A={fail_domains['A']}, B={fail_domains['B']}")
    
    result_3 = ac3(fail_domains)
    print("Arc Consistent:", result_3)
    if not result_3:
        print("AC-3 detected immediate failure!")
