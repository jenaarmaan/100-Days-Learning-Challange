# **D27. Logical Inference**

TOPIC NAME:

## Topic: D27. Logical Inference

---

## 1. One-line definition (in your own words)

**Logical inference is the process of deriving new conclusions from existing facts and rules using formal reasoning.**

---

## 2. Problem it solves

### Why this exists

A knowledge base in AI contains:

- **Facts**
- **Rules**

But these alone are not enough. AI systems must **derive new knowledge automatically**.

Logical inference enables a system to:

- Use existing rules
- Apply reasoning
- Generate new conclusions

---

### Example

Knowledge Base:

```text
All humans are mortal
Socrates is human
```

Logical inference allows the system to conclude:

```text
Socrates is mortal
```

---

### What fails without it

Without logical inference:

- Knowledge bases remain static
- AI cannot reason
- No conclusions can be derived from rules

Example:

```text
Human(Socrates)
∀x Human(x) → Mortal(x)
```

Without inference, the system **cannot derive**:

```text
Mortal(Socrates)
```

---

## 3. Core idea (intuition)

Logical inference works by applying **reasoning rules** to existing knowledge.

Two key components:

### Knowledge Base (KB)

Contains:

```text
Facts + Rules
```

Example:

```text
Human(Socrates)
Human(Plato)
∀x Human(x) → Mortal(x)
```

---

### Inference Engine

The inference engine applies reasoning methods such as:

- **Modus Ponens**
- **Resolution**
- **Unification**
- **Forward chaining**
- **Backward chaining**

---

### Inference Rule Example: Modus Ponens

Rule:

```text
If A → B
A is true
Therefore B is true
```

Example:

```text
Human(Socrates)
Human(x) → Mortal(x)
```

Conclusion:

```text
Mortal(Socrates)
```

---

## 4. How it works (high-level steps)

### Step 1 — Store knowledge

Example facts:

```text
Human(Socrates)
Human(Plato)
```

Rule:

```text
Human(x) → Mortal(x)
```

---

### Step 2 — Match rules to facts

The inference engine searches for:

```text
Human(x)
```

Matches:

```text
Human(Socrates)
Human(Plato)
```

---

### Step 3 — Apply rule

Apply:

```text
Human(x) → Mortal(x)
```

---

### Step 4 — Generate new knowledge

Result:

```text
Mortal(Socrates)
Mortal(Plato)
```

---

## 5. Types of logical inference

### Forward Chaining (Data-driven)

Starts with facts and derives new conclusions.

Example flow:

```text
Facts → Rules → New facts → More conclusions
```

Used in:

- Expert systems
- Rule engines

---

### Backward Chaining (Goal-driven)

Starts with a goal and checks if facts support it.

Example:

Goal:

```text
Mortal(Socrates)?
```

System checks:

```text
Human(Socrates)?
Rule: Human(x) → Mortal(x)
```

Used in:

- Prolog
- Theorem provers

---

### Resolution

A powerful inference rule used in automated theorem proving.
Converts formulas into **clause form** and derives contradictions to prove statements.

---

## 6. Strengths

- Enables automated reasoning
- Works with structured knowledge
- Foundation of expert systems
- Used in theorem proving and logic programming

---

## 7. Weaknesses / failure cases

- Computationally expensive for large knowledge bases
- Requires well-defined rules
- Not suitable for uncertain or probabilistic reasoning

For uncertainty, AI uses **probabilistic models** instead.

---

## 8. Keywords / terms to remember

- Knowledge base
- Inference engine
- Modus ponens
- Forward chaining
- Backward chaining
- Resolution
- Deductive reasoning
- Logical entailment

---

## 9. 30–60 Minute Coding Task

### Goal

Implement a **simple forward chaining inference engine** in Python.

The system will:

1. Store facts
2. Apply logical rules
3. Infer new facts automatically

---

### Example Knowledge Base

Facts:

```text
Human(Socrates)
Human(Plato)
```

Rule:

```text
Human(x) → Mortal(x)
```

Expected inference:

```text
Mortal(Socrates)
Mortal(Plato)
```

---

### Python Implementation

```python
# Simple Forward Chaining Inference Engine

# Facts stored as predicate -> list of objects
facts = {
    "Human": ["Socrates", "Plato"]
}

# Rules stored as (condition_predicate, result_predicate)
rules = [
    ("Human", "Mortal")
]

# Storage for inferred facts
inferred = {
    "Mortal": []
}

def forward_chaining(facts, rules, inferred):
    new_inference = True

    while new_inference:
        new_inference = False

        for condition, result in rules:
            if condition in facts:
                for obj in facts[condition]:
                    if result not in inferred:
                        inferred[result] = []
                        
                    if obj not in inferred[result]:
                        inferred[result].append(obj)
                        new_inference = True
    return inferred

results = forward_chaining(facts, rules, inferred)

print("Original Facts:")
for predicate, objects in facts.items():
    for obj in objects:
        print(f"{predicate}({obj})")

print("\nInferred Facts:")
for predicate, objects in results.items():
    for obj in objects:
        print(f"{predicate}({obj})")
```
