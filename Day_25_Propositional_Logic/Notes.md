# **D25. Propositional Logic**

TOPIC NAME:

## Topic: D25. Propositional Logic

---

## 1. One-line definition (in your own words)

**Propositional Logic is a formal system that represents knowledge using simple true/false statements combined with logical operators.**

---

## 2. Problem it solves

### Why this exists

AI systems need a way to **represent facts about the world** and **reason about them logically**.

Example reasoning:

```text
If it rains → the ground becomes wet
It is raining
Therefore → the ground is wet
```

Propositional logic provides a structured framework for:

- Representing facts
- Combining statements
- Performing logical inference

---

### What fails without it

Without logical representation:

- AI cannot reason about facts formally.
- Knowledge becomes ambiguous.
- Systems cannot derive new conclusions.

Propositional logic enables **automated reasoning**.

---

## 3. Core idea (intuition)

A **proposition** is a statement that is either:

```text
True
False
```

Examples:

```text
P: It is raining
Q: The ground is wet
R: The road is slippery
```

These can be combined using **logical operators**.

---

### Common Logical Operators

| Operator | Symbol | Meaning |
| --- | --- | --- |
| AND | ∧ | Both must be true |
| OR | ∨ | At least one true |
| NOT | ¬ | Negation |
| IMPLIES | → | If P then Q |
| BICONDITIONAL | ↔ | P if and only if Q |

---

### Example Expression

```text
P → Q
```

Meaning:

```text
If P is true then Q must be true
```

Example:

```text
Rain → WetGround
```

---

### Truth Tables

Logical expressions can be evaluated using truth tables.

Example:

```text
P ∧ Q
```

| P | Q | Result |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

---

## 4. How it works (high-level steps)

### Step 1

Represent knowledge as **propositions**.

Example:

```text
Rain
WetGround
```

---

### Step 2

Combine propositions using **logical operators**.

Example:

```text
Rain → WetGround
```

---

### Step 3

Apply logical inference rules.

Example:

```text
Rain
Rain → WetGround
----------------
WetGround
```

---

### Step 4

Evaluate truth using logic rules or truth tables.

---

## 5. Strengths

- Simple and precise
- Easy to implement
- Enables automated reasoning
- Foundation for AI logic systems

---

## 6. Weaknesses / failure cases

- Cannot represent relationships between objects
- Cannot express quantities
- Limited expressiveness

These limitations lead to **First Order Logic**, which is more powerful.

---

## 7. Where it is used in real systems

Propositional logic appears in:

- Rule-based expert systems
- Knowledge-based AI
- Logic programming
- Automated theorem proving
- Digital circuit design

It is the **foundation of symbolic AI reasoning**.

---

## 8. Keywords / terms to remember

- Proposition
- Logical operators
- Truth values
- Logical expression
- Truth table
- Inference

---

## 9. 30–60 Minute Coding Task

### Goal

Implement a **simple propositional logic evaluator** using Python.

The program will evaluate logical expressions using truth tables.

---

### Example Expression

```text
(P AND Q) → R
```

We will test this expression for different truth assignments.

---

### Python Implementation

```python
import itertools

# Logical functions
def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def NOT(p):
    return not p

def IMPLIES(p, q):
    return (not p) or q

# Variables
variables = ["P", "Q", "R"]

# Generate all truth combinations
combinations = list(itertools.product([True, False], repeat=len(variables)))

print("Truth Table for (P AND Q) -> R\n")

print(f"{'P':<8} {'Q':<8} {'R':<8} {'RESULT':<8}")
print("-" * 35)

for combo in combinations:
    P, Q, R = combo
    
    # Evaluate (P AND Q) -> R
    result = IMPLIES(AND(P, Q), R)
    
    print(f"{str(P):<8} {str(Q):<8} {str(R):<8} {str(result):<8}")
```

---

### Expected Output (Example)

```text
P        Q        R        RESULT  
-----------------------------------
True     True     True     True    
True     True     False    False   
True     False    True     True    
...
```

---

### What to Observe

- How logical expressions behave under different truth values.
- How implication behaves differently from AND/OR.
- Modify the expression (e.g., `(P OR Q) AND NOT R`) and regenerate the truth table.
