"""
Day 31: Ontologies & Knowledge Graphs
A simple Knowledge Graph system using (Subject, Relation, Object) triples.
Includes hierarchical inference and a simple natural language-like query interface.
"""

class KnowledgeGraph:
    def __init__(self):
        # Store triples as a list of tuples: (subject, relation, object)
        self.triples = []

    def add_triple(self, s, r, o):
        self.triples.append((s, r, o))

    def query_direct(self, entity):
        """Find all relationships where the entity is the subject."""
        return [t for t in self.triples if t[0] == entity]

    def query_reverse(self, obj):
        """Find all relationships where the entity is the object."""
        return [t for t in self.triples if t[2] == obj]

    def infer_hierarchy(self, entity):
        """
        Recursively find all 'isA' ancestors.
        Implements transitive reasoning.
        """
        ancestors = set()
        
        def traverse(e):
            for s, r, o in self.triples:
                if s == e and r == "isA":
                    if o not in ancestors:
                        ancestors.add(o)
                        traverse(o)
        
        traverse(entity)
        return ancestors

    def ask(self, question):
        """A simple NL query handler."""
        parts = question.lower().strip("?").split()
        
        # Example: "What is Buddy?"
        if parts[0] == "what" and parts[1] == "is":
            entity = parts[2].capitalize()
            ancestors = self.infer_hierarchy(entity)
            if not ancestors:
                # Check direct isA if recursion found nothing or provided entity is at top
                direct = [t[2] for t in self.query_direct(entity) if t[1] == "isA"]
                ancestors.update(direct)
                
            if ancestors:
                return f"{entity} is functionally a: {', '.join(ancestors)}"
            return f"I don't know what {entity} is."

        # Example: "Who owns Buddy?"
        if parts[0] == "who" and parts[1] == "owns":
            entity = parts[2].capitalize()
            # Reverse query for 'owner' or 'ownedBy'
            owners = [t[2] for t in self.query_direct(entity) if t[1] in ["owner", "ownedBy"]]
            if owners:
                return f"{entity} is owned by {', '.join(owners)}"
            return f"I don't know who owns {entity}."

        return "I don't understand that question yet."

if __name__ == "__main__":
    kg = KnowledgeGraph()
    
    # 1. Defining the Ontology (Blueprint)
    kg.add_triple("Dog", "isA", "Animal")
    kg.add_triple("Animal", "isA", "LivingBeing")
    kg.add_triple("Human", "isA", "LivingBeing")

    # 2. Populating the Knowledge Graph (Concrete Data)
    kg.add_triple("Buddy", "isA", "Dog")
    kg.add_triple("Buddy", "owner", "Alice")
    kg.add_triple("Buddy", "likes", "Bones")
    kg.add_triple("Alice", "isA", "Human")
    kg.add_triple("Alice", "livesIn", "Rome")

    print("--- Day 31: Ontologies & Knowledge Graphs ---")

    # Show direct facts
    print("\n[Direct facts about Buddy]")
    for t in kg.query_direct("Buddy"):
        print(f"Buddy --{t[1]}--> {t[2]}")

    # Show inference
    print("\n[Inferred 'isA' hierarchy for Buddy]")
    hierarchy = kg.infer_hierarchy("Buddy")
    for level in hierarchy:
        print(f"Buddy isA {level}")

    # Natural Language Queries
    print("\n[Natural Language Queries]")
    print(kg.ask("What is Buddy?"))
    print(kg.ask("Who owns Buddy?"))
    print(kg.ask("Who owns Cooper?")) # Unknown entity
