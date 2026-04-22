"""
Day 29: Knowledge Representation - Semantic Networks
A simple implementation of a Semantic Network using NetworkX.
Includes inheritance reasoning to follow 'is-a' chains.
"""

import networkx as nx

def create_knowledge_base():
    # Create directed graph
    G = nx.DiGraph()

    # Add relationships (subject, relation, object)
    knowledge = [
        ("Dog", "is-a", "Animal"),
        ("Cat", "is-a", "Animal"),
        ("Animal", "breathes", "Oxygen"),
        ("Dog", "sound", "Bark"),
        ("Cat", "sound", "Meow"),
        ("Husky", "is-a", "Dog"),
        ("Husky", "color", "White/Gray")
    ]

    # Add edges with relationship labels
    for subject, relation, obj in knowledge:
        G.add_edge(subject, obj, relation=relation)
    
    return G

def query_direct(G, subject):
    """Query only direct relationships from the node."""
    results = []
    if subject not in G:
        return results
        
    for neighbor in G.neighbors(subject):
        relation = G[subject][neighbor]['relation']
        results.append((subject, relation, neighbor))
    return results

def query_with_inheritance(G, subject):
    """
    Query relationships including inherited ones by following 'is-a' chains.
    """
    results = []
    if subject not in G:
        return results

    # Get direct facts
    direct_facts = query_direct(G, subject)
    results.extend(direct_facts)

    # Check for 'is-a' relationships and recurse
    for fact in direct_facts:
        if fact[1] == "is-a":
            parent = fact[2]
            # Inherit facts from parent (excluding the is-a link itself to avoid duplicates)
            parent_facts = query_with_inheritance(G, parent)
            for pf in parent_facts:
                # We don't necessarily want to say "Husky is-a Animal" here if we just want properties,
                # but for simplicity, we add everything not already present.
                if pf not in results:
                    results.append(pf)
    
    return results

def print_facts(subject, facts, title="Facts"):
    print(f"\n--- {title} about {subject} ---")
    if not facts:
        print("No facts found.")
    for fact in facts:
        # If it's an inherited fact, we might want to show the source, 
        # but here we just show the relationship.
        print(f"{fact[0]} --{fact[1]}--> {fact[2]}")

if __name__ == "__main__":
    kb = create_knowledge_base()

    # 1. Simple Query
    print("Testing Simple Query (Dog):")
    dog_facts = query_direct(kb, "Dog")
    print_facts("Dog", dog_facts, "Direct Facts")

    # 2. Inheritance Query (Husky)
    # A Husky is a Dog, and a Dog is an Animal.
    # Husky should inherit 'sound: Bark' and 'breathes: Oxygen'.
    print("\nTesting Inheritance Query (Husky):")
    husky_inherited = query_with_inheritance(kb, "Husky")
    print_facts("Husky", husky_inherited, "Inherited Facts")

    # 3. Inheritance Query (Dog)
    # Dog should inherit 'breathes: Oxygen' from Animal.
    print("\nTesting Inheritance Query (Dog):")
    dog_inherited = query_with_inheritance(kb, "Dog")
    print_facts("Dog", dog_inherited, "Inherited Facts")
