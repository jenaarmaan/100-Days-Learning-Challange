# Day 20: Arc Consistency (AC-3 Algorithm)

## 1. One-line definition (in your own words)

**Arc Consistency is a constraint propagation technique that removes inconsistent values from variable domains by ensuring every value satisfies binary constraints with neighboring variables.**

---

## 2. Problem it solves

### Why this exists

Forward Checking only prunes domains after assignments.

Problem:

- It does not proactively enforce consistency between unassigned variables.
- Some inconsistencies remain hidden until deeper in the search tree.

Arc Consistency strengthens pruning by:

- Enforcing consistency across all variable pairs before and during search.

### What fails without it

- Domains may contain values that are doomed to fail.
- Search explores unnecessary branches.
- Constraint propagation is weak.

---

## 3. Core idea (intuition)

For a constraint between variables: `X → Y`

Arc consistency means:

> For every value in Domain(X), there exists at least one compatible value in Domain(Y).

If not:

- Remove that value from Domain(X).

### Example

If:

- `X ∈ {1, 2}`
- `Y ∈ {2}`
- Constraint: `X ≠ Y`

Check `X=2`:

- Y only has 2
- Violates constraint → Remove 2 from Domain(X)
- New: `X ∈ {1}`

### AC-3 Algorithm

- Maintain a queue of arcs.
- Repeatedly:
  - Pop an arc (X, Y)
  - Revise Domain(X)
  - If Domain(X) changed:
    - Add all neighboring arcs (Z, X) back to queue
- Continue until:
  - Queue empty → arc consistent
  - Or a domain becomes empty → failure

---

## 4. How it works (high-level steps)

1. **Initialize queue** with all arcs.
2. **While queue not empty**:
   - Remove arc (Xi, Xj)
   - Revise Xi domain
3. **If domain reduced**:
   - Add neighbors back into queue.
4. **Return** consistent domains.

---

## 5. Strengths

- Stronger pruning than forward checking.
- Detects failure early.
- Reduces search dramatically.
- Polynomial time preprocessing.

---

## 6. Weaknesses / failure cases

- Only works on binary constraints.
- Does not guarantee global consistency.
- Still exponential if search needed.

---

## 7. Where it is used in real systems

### FAANG example

- Scheduling engines
- Constraint solvers
- Configuration systems
- Timetabling software
- Industrial planning tools

Modern CSP solvers rely heavily on arc consistency.

---

## 8. Keywords / terms to remember

- Arc consistency
- Constraint propagation
- Domain revision
- Binary constraints
- AC-3 algorithm
- Domain pruning

---

## 9. Coding Task: AC-3 Implementation

### Goal

Implement the AC-3 algorithm to enforce arc consistency on a small CSP (variables A, B, C with domains {1, 2, 3} and constraints A ≠ B, B ≠ C) before backtracking. Observe how AC-3 prunes domains to reduce the search space.
