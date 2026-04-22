"""
Day 30: Semantic Networks & Frames
A knowledge representation system that combines Graph-based relationships
(Semantic Networks) with Slot-based object descriptions (Frames).
Includes support for single and multiple inheritance.
"""

# Frame storage mapping concepts to their slots (attributes) and fillers (values)
frames = {
    "LivingBeing": {
        "composed_of": "Cells",
        "alive": True
    },
    "Animal": {
        "is-a": ["LivingBeing"],
        "breathes": "Oxygen",
        "diet": "Required"
    },
    "Mammal": {
        "is-a": ["Animal"],
        "skin_covering": "Hair/Fur",
        "gives_birth": True
    },
    "Flyer": {
        "can_fly": True,
        "movement": "Flight"
    },
    "Dog": {
        "is-a": ["Mammal"],
        "sound": "Bark",
        "diet": "Omnivore"
    },
    "Cat": {
        "is-a": ["Mammal"],
        "sound": "Meow",
        "personality": "Independent"
    },
    "Bat": {
        "is-a": ["Mammal", "Flyer"],  # Example of Multiple Inheritance
        "sound": "Ultrasonic",
        "active_at": "Night"
    }
}

def get_property(entity, prop, visited=None):
    """
    Retrieve property with support for multiple inheritance.
    Uses Depth-First Search with a 'visited' set to avoid infinite loops.
    """
    if visited is None:
        visited = set()
    
    if entity not in frames or entity in visited:
        return None
    
    visited.add(entity)

    # 1. Check direct property in the current frame
    if prop in frames[entity]:
        return frames[entity][prop]

    # 2. Check inheritance ("is-a" slots)
    if "is-a" in frames[entity]:
        parents = frames[entity]["is-a"]
        for parent in parents:
            val = get_property(parent, prop, visited)
            if val is not None:
                return val

    return None

def ask_question(entity, prop):
    """A simple natural language-like query wrapper."""
    value = get_property(entity, prop)
    if value is not None:
        print(f"Q: What is the '{prop}' of {entity}?")
        print(f"A: {value}")
    else:
        print(f"Q: What is the '{prop}' of {entity}?")
        print(f"A: I don't know about that.")

if __name__ == "__main__":
    print("--- Day 30: Frames & Semantic Networks System ---")
    
    # Basic inheritance
    print("\n[Testing Single Inheritance]")
    ask_question("Dog", "sound")     # Direct
    ask_question("Dog", "breathes")  # Inherited from Animal
    ask_question("Cat", "gives_birth") # Inherited from Mammal

    # Deep inheritance
    print("\n[Testing Deep Inheritance]")
    ask_question("Dog", "composed_of") # Inherited from LivingBeing (Dog -> Mammal -> Animal -> LivingBeing)

    # Multiple inheritance
    print("\n[Testing Multiple Inheritance]")
    ask_question("Bat", "active_at") # Direct
    ask_question("Bat", "can_fly")   # Inherited from Flyer
    ask_question("Bat", "skin_covering") # Inherited from Mammal

    # Overriding (Default values)
    print("\n[Testing Property Overriding]")
    # Animal has diet: Required, but Dog specificies Omnivore
    ask_question("Animal", "diet")
    ask_question("Dog", "diet")
