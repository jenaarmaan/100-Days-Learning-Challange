class FamilyKnowledgeBase:
    """
    A simple representation of First-Order Logic predicates and inference.
    """
    def __init__(self):
        # Facts represented as lists/dicts
        self.parent_relation = [] # (parent, child)
        self.gender = {}          # {name: 'M' or 'F'}

    def add_parent(self, parent, child):
        """Adds a parent-child relationship (Predicate: Parent(p, c))."""
        self.parent_relation.append((parent, child))

    def set_gender(self, name, g):
        """Sets the gender of a person (Predicate: Male(n) or Female(n))."""
        self.gender[name] = g

    def is_father(self, x, y):
        """
        Infers Fatherhood.
        Predicate: Father(x, y) <-> Parent(x, y) AND Male(x)
        """
        return (x, y) in self.parent_relation and self.gender.get(x) == 'M'

    def is_grandfather(self, x, z):
        """
        Infers Grandfatherhood using a placeholder variable 'y'.
        Predicate: Grandfather(x, z) <-> EXISTS y (Father(x, y) AND Parent(y, z))
        """
        # Find all y such that x is father of y
        potential_middle_links = [child for parent, child in self.parent_relation if parent == x and self.gender.get(x) == 'M']
        
        for y in potential_middle_links:
            # Check if y is parent of z
            if (y, z) in self.parent_relation:
                return True
        return False

if __name__ == "__main__":
    kb = FamilyKnowledgeBase()

    # Define Constants and Facts
    kb.set_gender("Abe", "M")
    kb.set_gender("Homer", "M")
    kb.set_gender("Marge", "F")
    
    kb.add_parent("Abe", "Homer")
    kb.add_parent("Homer", "Bart")
    kb.add_parent("Homer", "Lisa")
    kb.add_parent("Marge", "Bart")

    print("--- Family Logic Inference (First-Order Logic) ---")
    
    # Simple Predicate Check
    print(f"Is Abe the father of Homer? {kb.is_father('Abe', 'Homer')}")
    print(f"Is Marge the father of Bart? {kb.is_father('Marge', 'Bart')}")
    
    # Existential Inference
    print(f"Is Abe the grandfather of Bart? {kb.is_grandfather('Abe', 'Bart')}")
    print(f"Is Abe the grandfather of Lisa? {kb.is_grandfather('Abe', 'Lisa')}")
    print(f"Is Homer the grandfather of Bart? {kb.is_grandfather('Homer', 'Bart')}")
