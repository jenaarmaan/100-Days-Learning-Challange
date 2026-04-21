# Simple Forward Chaining Inference Engine

def forward_chaining(facts, rules, inferred_container):
    """
    Applies forward chaining to infer new facts from existing facts and rules.
    
    Args:
        facts (dict): Original knowledge base facts {predicate: [objects]}.
        rules (list): Logical rules list of tuples (condition_predicate, result_predicate).
        inferred_container (dict): Dictionary to store newly derived facts.
        
    Returns:
        dict: The updated container of inferred facts.
    """
    new_inference_found = True

    while new_inference_found:
        new_inference_found = False

        # Check each rule
        for condition, result in rules:
            # Combine original facts and already inferred facts as potential triggers
            current_known_predicates = {**facts, **inferred_container}
            
            if condition in current_known_predicates:
                for obj in current_known_predicates[condition]:
                    # Ensure the result predicate exists in our storage
                    if result not in inferred_container:
                        inferred_container[result] = []
                    
                    # If this fact hasn't been inferred yet, add it
                    if obj not in inferred_container[result]:
                        inferred_container[result].append(obj)
                        new_inference_found = True
                        print(f"  [Inferred] {result}({obj})")

    return inferred_container

if __name__ == "__main__":
    # --- Example 1: Socrates and Plato ---
    print("--- Scenario 1: Basic Human Mortality ---")
    
    # Facts stored as predicate -> list of objects
    kb_facts = {
        "Human": ["Socrates", "Plato"]
    }

    # Rules stored as (condition_predicate, result_predicate)
    # Means: IF Human(x) THEN Mortal(x)
    kb_rules = [
        ("Human", "Mortal")
    ]

    # Container for discovered knowledge
    inferred_facts = {}

    print("Initial Facts:")
    for pred, objs in kb_facts.items():
        for o in objs: print(f"  {pred}({o})")

    print("\nStarting Inference...")
    results = forward_chaining(kb_facts, kb_rules, inferred_facts)

    print("\nFinal State of Inferred Knowledge:")
    for pred, objs in results.items():
        for o in objs: print(f"  {pred}({o})")


    # --- Scenario 2: Mini Extensions ---
    print("\n" + "="*40)
    print("--- Scenario 2: Extended Rules ---")
    
    ext_facts = {
        "Student": ["Alice", "Bob"],
        "Cat": ["Tom", "Garfield"]
    }
    
    ext_rules = [
        ("Student", "Studies"),
        ("Cat", "Animal"),
        ("Animal", "Mortal") # Recursive rule
    ]
    
    ext_inferred = {}
    
    print("Initial Facts:")
    for pred, objs in ext_facts.items():
        for o in objs: print(f"  {pred}({o})")
        
    print("\nStarting Extended Inference...")
    ext_results = forward_chaining(ext_facts, ext_rules, ext_inferred)
    
    print("\nAll Derived Knowledge:")
    for pred, objs in ext_results.items():
        for o in objs: print(f"  {pred}({o})")
