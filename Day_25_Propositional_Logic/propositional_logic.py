import itertools

# Logical functions
def AND(p, q):
    """Returns True if both p and q are True."""
    return p and q

def OR(p, q):
    """Returns True if at least one of p or q is True."""
    return p or q

def NOT(p):
    """Returns the negation of p."""
    return not p

def IMPLIES(p, q):
    """Returns True unless p is True and q is False (Logical Implication: P -> Q)."""
    return (not p) or q

def BICONDITIONAL(p, q):
    """Returns True if p and q have the same truth value (Logical Equivalence: P <-> Q)."""
    return p == q

def evaluate_truth_table(variables, expression_func, expression_label):
    """
    Generates and prints a truth table for a given logical expression.
    """
    # Generate all truth combinations (e.g., [(True, True), (True, False), ...])
    combinations = list(itertools.product([True, False], repeat=len(variables)))

    print(f"\nTruth Table for: {expression_label}")
    print("-" * (len(variables) * 10 + 10))
    
    # Print headers
    header = "  ".join([f"{var:<8}" for var in variables]) + "  RESULT"
    print(header)
    print("-" * len(header))

    for combo in combinations:
        # Create a mapping of variable name to its truth value
        val_map = dict(zip(variables, combo))
        
        # Evaluate the expression using the truth values
        result = expression_func(val_map)
        
        # Print the row
        row = "  ".join([f"{str(val):<8}" for val in combo]) + f"  {str(result)}"
        print(row)

if __name__ == "__main__":
    # Define our variables
    vars_list = ["P", "Q", "R"]

    # Expression: (P AND Q) -> R
    # We wrap it in a lambda or function that takes the truth assignment dictionary
    expr_1 = lambda d: IMPLIES(AND(d["P"], d["Q"]), d["R"])
    label_1 = "(P AND Q) -> R"

    evaluate_truth_table(vars_list, expr_1, label_1)

    # Secondary Expression Example: (P OR Q) AND (NOT R)
    expr_2 = lambda d: AND(OR(d["P"], d["Q"]), NOT(d["R"]))
    label_2 = "(P OR Q) AND (NOT R)"

    evaluate_truth_table(vars_list, expr_2, label_2)
    
    print("\nObservation:")
    print("Notice how 'IMPLIES' is only False when the antecedent (P AND Q) is True but the consequent (R) is False.")
