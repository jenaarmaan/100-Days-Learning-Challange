"""
Day 28: Unification Algorithm
A simple implementation of the unification algorithm for logical expressions.
Unification is the process of matching logical expressions by finding 
substitutions for variables.
"""

def is_variable(x):
    """
    Check if an expression element is a variable.
    By convention, variables start with a lowercase letter.
    """
    return isinstance(x, str) and x[0].islower()

def is_compound(x):
    """Check if an expression is a compound expression (list)."""
    return isinstance(x, list)

def unify(expr1, expr2, substitution=None):
    """
    Finds the Most General Unifier (MGU) for two expressions.
    Returns: A dictionary of substitutions or None if unification fails.
    """
    if substitution is None:
        substitution = {}

    # If both expressions are identical, return existing substitution
    if expr1 == expr2:
        return substitution
    
    # If expr1 is a variable, unify it with expr2
    if is_variable(expr1):
        return unify_variable(expr1, expr2, substitution)
    
    # If expr2 is a variable, unify it with expr1
    if is_variable(expr2):
        return unify_variable(expr2, expr1, substitution)

    # If both are compound expressions, unify their elements recursively
    if is_compound(expr1) and is_compound(expr2):
        if len(expr1) != len(expr2):
            return None
        
        # Unify first elements
        first_sub = unify(expr1[0], expr2[0], substitution)
        if first_sub is None:
            return None
            
        # Recursive unification of the rest with the new substitutions
        # This requires applying substitutions to the rest of the list
        return unify(expr1[1:], expr2[1:], first_sub)

    return None

def unify_variable(var, x, substitution):
    """Helper to unify a variable 'var' with an expression 'x'."""
    if var in substitution:
        return unify(substitution[var], x, substitution)
    
    # Optional: Occurs check would go here (to prevent infinite recursion if x contains var)
    # For simple logic, we keep it simple.
    
    if is_variable(x) and x in substitution:
        return unify(var, substitution[x], substitution)
    
    # Add new substitution
    new_substitution = substitution.copy()
    new_substitution[var] = x
    return new_substitution

def print_result(e1, e2, result):
    print("-" * 50)
    print(f"Expression 1: {e1}")
    print(f"Expression 2: {e2}")
    if result is not None:
        print(f"[SUCCESS] Unification Successful!")
        print(f"Unifier (Substitutions): {result}")
    else:
        print(f"[FAILED] Unification Failed.")

if __name__ == "__main__":
    print("--- Day 28: Unification Solver ---")
    
    # Standard Example
    e1 = ["Knows", "John", "x"]
    e2 = ["Knows", "y", "Jane"]
    print_result(e1, e2, unify(e1, e2))

    # Mini Extension 1
    e3 = ["P", "x", "x"]
    e4 = ["P", "y", "z"]
    print_result(e3, e4, unify(e3, e4))

    # Mini Extension 2
    e5 = ["P", "x", ["f", "y"]]
    e6 = ["P", "John", "z"]
    print_result(e5, e6, unify(e5, e6))

    # Mini Extension 3 (Fail Case)
    e7 = ["P", "John"]
    e8 = ["P", "Jane"]
    print_result(e7, e8, unify(e7, e8))
