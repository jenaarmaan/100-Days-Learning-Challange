# **C24. Planning Graphs**

TOPIC NAME:

## Topic: C24. Planning Graphs

---

## 1. One-line definition (in your own words)

**A Planning Graph is a layered structure that represents alternating levels of states and actions to efficiently analyze reachability and construct plans in classical planning problems.**

---

## 2. Problem it solves

### Why this exists

In classical planning, searching through the entire state space can be extremely expensive.

Problem:

- The number of possible states grows exponentially.
- Many actions may be irrelevant to the goal.
- Traditional search algorithms waste time exploring unnecessary branches.

Planning graphs solve this by:

- Structuring planning into **layers**
- Detecting **goal reachability early**
- Identifying **mutual exclusions (mutex)** between actions and states.

This dramatically improves planning efficiency.

---

### What fails without it

Without planning graphs:

- Planners must search blindly through state space.
- Impossible to efficiently reason about action interactions.
- Hard to detect impossible goals early.

Planning graphs provide **powerful heuristics and pruning mechanisms**.

---

## 3. Core idea (intuition)

A planning graph consists of alternating layers:

```text
State Layer (S0)
Action Layer (A0)
State Layer (S1)
Action Layer (A1)
State Layer (S2)
...
```

Each layer represents **what is possible at that step**.

- **State layers** contain possible facts.
- **Action layers** contain actions that can be applied.

---

### Example

Initial state:

```text
RobotAt(A)
BoxAt(B)
HandEmpty
```

Goal:

```text
BoxAt(A)
```

Planning graph expands like this:

```text
S0: Initial facts

A0: Possible actions

S1: Results of those actions

A1: New actions enabled

S2: New resulting states
```

The planner stops when:

```text
Goal appears in state layer without mutex conflicts
```

---

### Mutual Exclusion (Mutex)

Planning graphs track conflicts.

Two actions are **mutex** if:

- One deletes another’s effect
- One deletes the other's precondition
- They require mutually exclusive conditions

Mutex helps eliminate impossible plans early.

---

## 4. How it works (high-level steps)

### Step 1

Initialize **S0** with the initial state.

---

### Step 2

Add all actions whose **preconditions exist in S0**.

These form **A0**.

---

### Step 3

Apply effects of actions to produce **S1**.

---

### Step 4

Compute **mutex relations** between actions and states.

---

### Step 5

Repeat expansion until:

- Goal appears
- Graph levels stop changing (fixed point)

---

## 5. Strengths

- Efficient planning heuristics
- Detects unreachable goals early
- Handles action interactions
- Foundation of the **GraphPlan algorithm**

---

## 6. Weaknesses / failure cases

- Graph size grows quickly
- Mutex detection can be complex
- Still exponential for large domains

---

## 7. Where it is used in real systems

Planning graphs influenced many modern planners used in:

- Robotics planning systems
- Automated manufacturing
- Game AI planners
- Logistics optimization

They are also used to generate **heuristics for search planners**.

---

## 8. Keywords / terms to remember

- Planning graph
- State layer
- Action layer
- GraphPlan
- Mutex (mutual exclusion)
- Reachability analysis

---

## 9. 30–60 Minute Coding Task

### Goal

Implement a **simple planning graph expansion** that builds state and action layers.

This simplified version focuses on **layer construction**, not full GraphPlan.

---

### Problem Setup

Initial state:

```text
At(A)
BoxAt(B)
HandEmpty
```

Goal:

```text
BoxAt(A)
```

Actions:

```text
Move(A,B)
Move(B,A)
Pick(Box)
Drop(Box)
```
