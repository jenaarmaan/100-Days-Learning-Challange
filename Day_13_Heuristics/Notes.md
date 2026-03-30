# Day 13: Heuristics & Heuristic Design

## 1. One-line definition (in your own words)

**A heuristic is an estimate of the remaining cost from a current state to the goal, used to guide search algorithms toward solutions more efficiently.**

---

## 2. Problem it solves

### Why this exists

- Blind search (BFS, DFS, UCS) explores too many unnecessary states.
- Large state spaces become computationally expensive.
- We need “intelligent guessing” to reach goals faster.

### What fails without it

- Search becomes slow and memory-heavy.
- Algorithms explore irrelevant branches.
- Real-time systems (games, robotics, routing) become impractical.

---

## 3. Core idea (intuition)

A heuristic function:

```text
h(n) = estimated cost from node n to goal
```

Instead of blindly exploring, we:

- Estimate which states look closer to the goal.
- Prioritize those states.

Good heuristics dramatically reduce search space.

### Analogy

Using Google Maps:

- You don’t randomly try roads.
- You use straight-line distance to guess which direction is closer.

### Diagram

```text
Start → A → B → Goal
         \
          C → D

If h(B) < h(C),
Search prioritizes B branch.
```

---

## 4. How it works (high-level steps)

### Step 1

Define heuristic function h(n).

### Step 2

Use h(n) inside informed search algorithm (e.g., Greedy or A*).

### Step 3

Prioritize nodes with lower estimated total cost.

---

## 5. Strengths

- Dramatically reduces search time.
- Enables near-optimal solutions quickly.
- Essential for large-scale AI systems.
- Makes real-time AI feasible.

---

## 6. Weaknesses / failure cases

- Poor heuristic → bad performance.
- Overestimating heuristic → may lose optimality.
- Hard to design good heuristics.
- Domain-specific knowledge often required.

---

## 7. Where it is used in real systems

### FAANG example

- Navigation systems (shortest path estimation).
- Game AI pathfinding.
- Knowledge graph traversal ranking.

### Startup example

- Delivery route optimization.
- Robotics navigation.
- AI-based scheduling systems.

---

## 8. Keywords / terms to remember

- h(n)
- Admissible heuristic
- Consistent heuristic
- Overestimation
- Underestimation
- Informed search
- Evaluation function

---

## 9. 30–60 Minute Coding Task

### Goal

Understand heuristic impact by implementing Manhattan distance for grid pathfinding.

---

### Task

1. Create a grid world.
2. Define Manhattan distance heuristic:

   ```text
   h(n) = |x1 - x2| + |y1 - y2|
   ```

3. Compare:

   - Uniform Cost Search (no heuristic)
   - Greedy Search (uses only h(n))
4. Count number of nodes expanded.
