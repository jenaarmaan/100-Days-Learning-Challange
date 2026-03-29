# Day 18: Constraint Satisfaction Problems (CSP)

## 1. One-line definition (in your own words)
**A Constraint Satisfaction Problem (CSP) is a problem where we must assign values to variables such that all given constraints are satisfied.**

---

## 2. Problem it solves

### Why this exists
Many AI problems are not about finding a path, but about finding a *valid configuration*.

Examples:
- Scheduling exams
- Assigning time slots
- Sudoku
- Map coloring
- Resource allocation

### What fails without it
- Brute-force search becomes exponential.
- Invalid configurations are explored unnecessarily.
- Real-world planning and scheduling become inefficient.

---

## 3. Core idea (intuition)
A CSP is defined by three components:
1. Variables (X)
2. Domains (D)
3. Constraints (C)

We must:
> Assign a value from each variable’s domain so that all constraints hold.

### Example: Map Coloring
Variables: `WA, NT, SA`
Domain: `{Red, Green, Blue}`
Constraint: `Adjacent regions must have different colors.`

Solution:
`WA = Red, NT = Green, SA = Blue`

---

## 4. How it works (high-level steps)
1. **Define variables.**
2. **Define domain** for each variable.
3. **Define constraints** between variables.
4. **Use search** (often backtracking) to assign values while respecting constraints.

---

## 5. Strengths
- Structured representation.
- Efficient pruning possible.
- Works well for combinatorial problems.
- Clear mathematical formulation.

---

## 6. Weaknesses / failure cases
- Worst-case exponential complexity.
- Hard constraints may make problem unsolvable.
- Poor variable ordering leads to slow performance.

---

## 7. Where it is used in real systems

### FAANG example
- Task scheduling in data centers.
- Ad allocation constraints.
- Resource assignment in distributed systems.

### Startup example
- Delivery slot assignment.
- Interview scheduling platforms.
- Workforce planning tools.

---

## 8. Keywords / terms to remember
- Variables
- Domain
- Constraints
- Assignment
- Feasible solution
- Backtracking
- Constraint graph

---

## 9. Coding Task: Map Coloring Solver
Implement a simple CSP solver for the Map Coloring problem using backtracking for regions A, B, and C with colors Red, Green, and Blue.
