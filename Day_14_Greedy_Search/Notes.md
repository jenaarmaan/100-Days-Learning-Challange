# Day 14: Greedy Best-First Search

## 1. One-line definition (in your own words)

**Greedy Best-First Search is an informed search algorithm that expands the node that appears closest to the goal based solely on a heuristic estimate h(n).**

---

## 2. Problem it solves

### Why this exists

- Blind searches are too slow.
- We want faster goal-directed exploration.
- Sometimes speed is more important than optimality.

### What fails without it

- Large state spaces take too long to explore.
- Systems requiring fast decisions become inefficient.
- Real-time AI becomes impractical.

---

## 3. Core idea (intuition)

Greedy search chooses:

```text
f(n) = h(n)
```

It ignores cost so far and only considers estimated distance to goal.
It always moves toward what “looks” closest.

### Analogy

Trying to reach a mountain peak:

- You always walk in the direction that looks closest to the peak.
- You don’t track how much distance you've already walked.

### Diagram

```text
Start → A → B → Goal
         \
          C

If h(B) < h(C), explore B first.
```

---

## 4. How it works (high-level steps)

### Step 1

Define heuristic function h(n).

### Step 2

Insert start node into priority queue using h(n).

### Step 3

Expand node with smallest heuristic value.

---

## 5. Strengths

- Very fast in many cases.
- Simple to implement.
- Good for real-time systems.
- Often finds solution quickly.

---

## 6. Weaknesses / failure cases

- **Not optimal:** Does not guarantee the shortest path.
- **Local minima:** Can get trapped if the heuristic is misleading (e.g., walls).
- Strongly dependent on heuristic quality.

---

## 7. Where it is used in real systems

### FAANG example

- Quick path estimation in large maps.
- Ranking search results.
- Real-time decision engines.

### Startup example

- Fast robotics movement decisions.
- Game enemy AI.
- Quick recommendation ranking.

---

## 8. Keywords / terms to remember

- h(n)
- Informed search
- Priority queue
- Not optimal
- Heuristic-driven
- Local minima

---

## 9. 30–60 Minute Coding Task

### Goal

Implement Greedy Best-First Search and compare it to UCS.

### Task

- Use Manhattan heuristic.
- Implement greedy search.
- Compare path length and nodes expanded with UCS.
