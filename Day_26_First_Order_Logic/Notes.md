# **D26. First-Order Logic (FOL)**

TOPIC NAME:

## Topic: D26. First-Order Logic

---

## 1. One-line definition (in your own words)

**First-Order Logic is a more expressive formal system than Propositional Logic that represents the world in terms of objects, relations, and quantifiers (All/Some).**

---

## 2. Problem it solves

### Why this exists

Propositional Logic is limited because it treats every statement as a single atomic unit. It cannot easily represent rules that apply to members of a group or relationships between specific objects.

**FOL allows us to express:**

- **Objects**: People, houses, numbers.
- **Relations**: "John is the father of Pete", "5 is greater than 3".
- **Properties**: "The apple is red".
- **Quantifiers**:
  - **Universal ($\forall$)**: "Every student likes AI".
  - **Existential ($\exists$)**: "Someone is in the room".

---

### What fails without it

Without FOL:

- You would need a separate proposition for every single fact (e.g., `Apple1IsRed`, `Apple2IsRed`).
- You cannot write general rules like "All humans are mortal".
- Reasoning about large sets of data becomes impossible.

---

## 3. Core idea (intuition)

FOL breaks a sentence down into:

1. **Constants**: Specific objects (e.g., `John`, `Mars`).
2. **Predicates**: Properties or relations (e.g., `IsRed(x)`, `Brother(x, y)`).
3. **Variables**: Placeholders for objects (e.g., `x`, `y`).
4. **Quantifiers**:

- **Universal ($\forall$)**: "For all..."
- **Existential ($\exists$)**: "There exists..."

---

### Example Expression

**English**: "Everyone who is a parent has a child."
**FOL**: $\forall x (Parent(x) \rightarrow \exists y ChildOf(y, x))$

---

## 4. How it works (high-level steps)

### Step 1: Define the Domain

Identify the "Universe of Discourse" (the set of all objects we are talking about).

### Step 2: Define Predicates and Constants

Establish the vocabulary (e.g., `Person(x)`, `John`).

### Step 3: Formalize Rules

Use quantifiers and logical connectives to represent general truths.

### Step 4: Inference

Use rules like **Universal Instantiation** (if it's true for everyone, it's true for John) to derive new facts.

---

## 5. Strengths

- Highly expressive and powerful.
- Can represent complex mathematical and real-world relationships.
- Standard for formal knowledge representation.

---

## 6. Weaknesses / failure cases

- Higher computational complexity for inference.
- Still cannot easily represent "fuzziness" or uncertainty (solved by **Probabilistic Logic**).
- Can lead to infinite loops in automated reasoning if not careful.

---

## 7. Where it is used in real systems

- **Knowledge Graphs**: Google Knowledge Graph, Wikidata.
- **Semantic Web**: Resource Description Framework (RDF).
- **Advanced Expert Systems**: Medical diagnostics.
- **Database Querying**: SQL is conceptually related to a subset of FOL.

---

## 8. Keywords / terms to remember

- Predicate
- Constant
- Quantifier ($\forall, \exists$)
- Arity
- Domain of discourse

---

## 9. 30–60 Minute Coding Task

### Goal

Implement a simple **First-Order Logic Knowledge Base** to represent a family tree and infer relationships like "Grandparent" using predicates.

---

### Python Implementation

```python
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
```
