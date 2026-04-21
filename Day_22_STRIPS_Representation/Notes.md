# **C22. STRIPS Representation**

TOPIC NAME:

## Topic: C22. STRIPS Representation

---

## 1. One-line definition (in your own words)

**STRIPS (Stanford Research Institute Problem Solver) is a formal language used to represent planning problems using actions defined by preconditions and effects.**

---

## 2. Problem it solves

### Why this exists

When solving planning problems, we need a structured way to describe:

- What the world currently looks like
- What actions are possible
- What changes after an action

Without a formal representation:

- Planning becomes ambiguous
- Hard to automate reasoning
- Impossible to generalize planning algorithms

STRIPS solves this by defining actions using:

```text
Preconditions
Add Effects
Delete Effects
```

---

### What fails without it

Without structured representation:

- Planning algorithms cannot reason about state transitions.
- Hard to track what changes in the environment.
- Action consequences become unclear.

STRIPS makes planning computable.

---

## 3. Core idea (intuition)

In STRIPS, the world is represented as a **set of logical facts**.

Example state:

```text
At(Robot, A)
BoxAt(B)
HandEmpty
```

An action has:

```text
Action: Pick(Box)

Preconditions:
    At(Robot, B)
    BoxAt(B)
    HandEmpty

Add Effects:
    Holding(Box)

Delete Effects:
    BoxAt(B)
    HandEmpty
```

After applying the action:

```text
Remove Delete Effects
Add Add Effects
```

This updates the world state.

---

## 4. How it works (high-level steps)

### Step 1

Represent world as logical facts.

Example:

```text
{At(Robot,A), BoxAt(B), HandEmpty}
```

### Step 2

Define actions using STRIPS format:

```text
Preconditions
Add list
Delete list
```

### Step 3

Planner checks:

```text
Are preconditions satisfied?
```

If yes → action is applicable.

### Step 4

Apply effects to update state.

### Step 5

Search for action sequence reaching the goal.

---

## 5. Strengths

- Clear symbolic representation
- Easy to reason about actions
- Standard in classical planning
- Enables automated planning algorithms

---

## 6. Weaknesses / failure cases

- Assumes deterministic actions
- Cannot handle uncertainty
- Cannot represent numeric changes easily
- State explosion for complex worlds

---

## 7. Where it is used in real systems

STRIPS-style planning influenced:

- Robotics planning systems
- NASA mission planning tools
- Automated manufacturing planning
- Game AI planners

Modern planners extend STRIPS with richer representations.

---

## 8. Keywords / terms to remember

- STRIPS
- Preconditions
- Add list
- Delete list
- State representation
- Action model
- Planning operators

---

## 9. 30–60 Minute Coding Task

### Goal

Implement a **simple STRIPS-style planner** that applies actions to reach a goal state.

---

### Problem Setup

Initial State

```text
At(A)
BoxAt(B)
HandEmpty
```

Goal

```text
BoxAt(A)
```

Actions

```text
Move(A,B)
Move(B,A)
Pick(Box)
Drop(Box)
```

Each action uses STRIPS format.
