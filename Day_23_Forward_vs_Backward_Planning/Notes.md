# **C23. Forward vs Backward Planning**

TOPIC NAME:

**C23. Forward vs Backward Planning**

---

## 1. One-line definition (in your own words)

**Forward planning searches from the initial state toward the goal, while backward planning starts from the goal and works backward to determine which actions could have produced it.**

---

## 2. Problem it solves

### Why this exists

In classical planning, we must determine **how to search the space of possible plans**.

Two main strategies exist:

- **Forward Planning (Progression)**
- **Backward Planning (Regression)**

Both aim to find an action sequence reaching the goal but approach the problem from different directions.

Choosing the right approach can significantly reduce search complexity.

---

### What fails without it

Without structured planning strategies:

- The search space becomes extremely large.
- The planner may explore irrelevant actions.
- Goal reasoning becomes inefficient.

Forward and backward planning provide systematic ways to explore possible plans.

---

## 3. Core idea (intuition)

### Forward Planning

Start with the **initial state**.

Repeatedly apply actions whose **preconditions are satisfied**.

```
Initial State
      ↓
Action 1
      ↓
Action 2
      ↓
Action 3
      ↓
Goal State
```

This is similar to **state-space search**.

---

### Backward Planning

Start with the **goal state**.

Ask:

> What action could have produced this goal?
> 

Then replace the goal with the **preconditions of that action**.

```
Goal
 ↑
Action that produces goal
 ↑
Preconditions
 ↑
Previous action
 ↑
Initial state
```

---

### Intuition Example

Goal:

```
BoxAt(A)
```

Backward planner asks:

```
Which action produces BoxAt(A)?
```

Answer:

```
Drop(Box)
```

Then new subgoal becomes:

```
Holding(Box)
At(A)
```

Planner continues reasoning backward.

---

## 4. How it works (high-level steps)

### Forward Planning

1. Start with initial state.
2. Find applicable actions.
3. Apply action → new state.
4. Continue until goal satisfied.

---

### Backward Planning

1. Start with goal conditions.
2. Find actions that produce the goal.
3. Replace goal with action preconditions.
4. Continue until conditions match initial state.

---

## 5. Strengths

### Forward Planning

- Simple and intuitive
- Works well when branching factor is small
- Easy to implement

### Backward Planning

- Focuses only on relevant actions
- Reduces unnecessary exploration
- Often more efficient for complex goals

---

## 6. Weaknesses / failure cases

### Forward Planning

- May explore many irrelevant states
- State explosion in large environments

### Backward Planning

- Requires reasoning about goal dependencies
- Harder to implement
- Not ideal when many actions can achieve the same effect

---

## 7. Where it is used in real systems

Forward and backward planning appear in:

- Robotics task planners
- Automated workflow systems
- Game AI planning systems
- Logistics planning engines

Many modern planners combine both strategies.

---

## 8. Keywords / terms to remember

- Forward planning
- Backward planning
- Progression planning
- Regression planning
- State-space search
- Goal regression

---

# 9. 30–60 Minute Coding Task

### Goal

Implement a **simple forward planner** and compare it conceptually with backward reasoning.

---

### Problem Setup

World state:

```
RobotAt(A)
BoxAt(B)
Holding(False)
```

Goal:

```
BoxAt(A)
```

Actions:

```
Move(A,B)
Move(B,A)
Pick(Box)
Drop(Box)
```
