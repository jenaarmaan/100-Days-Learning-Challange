# Day 19: Backtracking + Forward Checking

## 1. One-line definition (in your own words)
**Backtracking is a depth-first search strategy for CSPs that assigns variables incrementally and backtracks when constraints are violated, while Forward Checking prunes future variable domains after each assignment to prevent conflicts early.**

---

## 2. Problem it solves

### Why this exists
Basic CSP backtracking:
- Assigns values sequentially.
- Detects failure only after a constraint is violated.

Problem:
- It may go deep into invalid branches before realizing inconsistency.

Forward Checking improves this by:
- Removing inconsistent values from neighboring variable domains immediately.
- Detecting dead-ends earlier.

### What fails without it
- Excessive unnecessary search.
- Late detection of constraint violations.
- Exponential blow-up in medium-sized CSPs.

---

## 3. Core idea (intuition)

### Plain Backtracking
1. Pick an unassigned variable.
2. Try a value.
3. Check constraints with assigned variables.
4. If failure → backtrack.

### Forward Checking Adds:
After assigning `X = value`, we:
- Look at all unassigned neighbors of X.
- Remove values from their domains that conflict.
- If any domain becomes empty → immediate backtrack.

### Intuition Analogy: Scheduling Interviews
If `Alice = Monday 10AM`, then remove Monday 10AM from:
- Bob’s domain
- Charlie’s domain

If Bob now has no available time slots → backtrack immediately.

---

## 4. How it works (high-level steps)
1. **Select unassigned variable.**
2. **Try a value** from its domain.
3. **Apply Forward Checking**: Remove inconsistent values from neighbors.
4. **If any domain becomes empty** → undo assignment.
5. **Continue recursively.**

---

## 5. Strengths
- Prunes search space early.
- Detects failure sooner than plain backtracking.
- Dramatically improves performance.
- Easy to implement on top of backtracking.

---

## 6. Weaknesses / failure cases
- Still exponential in worst case.
- Does not enforce full consistency (unlike AC-3).
- Extra bookkeeping overhead.

---

## 7. Where it is used in real systems

### Large-scale systems
- Workforce scheduling
- Constraint-based timetabling
- Resource allocation engines

### Applied AI
- Puzzle solvers (Sudoku, crosswords)
- Configuration systems
- Planning under constraints

---

## 8. Keywords / terms to remember
- Backtracking search
- Domain pruning
- Constraint propagation
- Forward checking
- Early failure detection
- Search tree pruning

---

## 9. Coding Task: Backtracking + Forward Checking (Map Coloring)
Implement a CSP solver using Backtracking and Forward Checking for a map with variables A, B, C, D and constraints:
- A ≠ B
- A ≠ C
- B ≠ D
- C ≠ D
Using colors: {Red, Green, Blue}
