# Day 28: Resolution & Unification

## 1. One-line Definition
**Resolution** is a rule-based method for proving logical statements by deriving contradictions, while **unification** is the process of matching logical expressions by finding valid substitutions for variables.

---

## 2. Problem it Solves
### Why this exists
Logical inference systems need a systematic way to prove statements automatically. Simple reasoning rules like *Modus Ponens* work for basic cases, but complex AI systems require a general-purpose proof method.

**Resolution provides:**
- A single powerful rule for logical deduction.
- A way to automatically prove theorems.
- A foundation for logic programming (like Prolog).

**Unification** allows the system to match variables with actual values, making resolution possible in first-order logic.

### Example
- **Knowledge Base:** All humans are mortal. John is a human.
- **Goal:** Is John mortal?
- **Resolution** proves this by showing that the opposite assumption (*John is not mortal*) leads to a contradiction.

---

## 3. Core Idea (Intuition)
Resolution works using **proof by contradiction** (Refutation).

### Steps:
1.  Convert knowledge into **Clause Form** (Conjunctive Normal Form - CNF).
2.  Assume the **negation** of the goal.
3.  Apply the **Resolution Rule** repeatedly.
4.  If a contradiction occurs (null clause $\square$) $\rightarrow$ the original goal is true.

---

## 4. Unification (The Key Enabler)
Unification determines how variables should be replaced to make two expressions identical.

### Example 1
- **Expr 1:** `Knows(John, x)`
- **Expr 2:** `Knows(y, Jane)`
- **Unifier:** `{y: John, x: Jane}`
- **Result:** Both become `Knows(John, Jane)`.

---

## 5. How Resolution Works (High-Level)

1.  **Convert to First-Order Logic:** $\forall x (Human(x) \implies Mortal(x))$
2.  **Convert to Clause Form:** $\neg Human(x) \lor Mortal(x)$
3.  **Add Negation of Goal:** Goal is $Mortal(John)$, so add $\neg Mortal(John)$.
4.  **Apply Resolution:**
    - Resolve $(\neg Human(x) \lor Mortal(x))$ with $(\neg Mortal(John))$
    - Unify $x$ with $John$.
    - Result: $\neg Human(John)$.
5.  **Conclude:** Resolve $\neg Human(John)$ with the fact $Human(John)$ $\rightarrow$ **Contradiction!** Goal is proven.

---

## 6. Strengths & Weaknesses

| Strengths | Weaknesses |
| :--- | :--- |
| Powerful automated reasoning | Computationally expensive |
| Foundation of modern theorem provers | Large search space in complex KBs |
| Works for First-Order Logic | Requires conversion to CNF |
| Only one inference rule needed | Can be slow for real-time systems |

---

## 7. Keywords to Remember
- **Resolution Rule:** The mechanics of cancelling out terms.
- **Clause Form (CNF):** A standard format for logic.
- **Unification:** Matching variables to constants or other variables.
- **Substitution:** The mapping of variables to values.
- **Refutation:** Proving by showing the negation is false.

---

## 8. Coding Task: Unification Algorithm
A Python implementation of the Unification algorithm can be found in [unification.py](./unification.py).

### Running the implementation
```powershell
python unification.py
```
