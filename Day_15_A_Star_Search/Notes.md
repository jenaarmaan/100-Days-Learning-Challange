# Day 15: A* Search Algorithm

## 1. One-line definition (in your own words)

**A* is an informed search algorithm that combines path cost (g) and heuristic estimate (h) to find the optimal path efficiently.**

---

## 2. Problem it solves

### Why this exists

- **Greedy** is fast but not optimal (it ignores $g(n)$).
- **UCS** is optimal (it uses $g(n)$) but slow (it ignores $h(n)$).
- **A*** balances both to achieve speed and optimality.

### What fails without it

- Either suboptimal solutions are found (Greedy).
- Or excessive computation is spent on irrelevant states (UCS).

---

## 3. Core idea (intuition)

A* uses the evaluation function:

```text
f(n) = g(n) + h(n)
```

Where:

- **g(n)** = Cost already incurred to reach node $n$ (Exploration).
- **h(n)** = Estimated cost from node $n$ to the goal (Exploitation).

By minimizing $f(n)$, the algorithm expands nodes that are likely to lead to the most efficient path.

### Analogy

Planning a cross-country trip:

- You track how many miles you've already driven ($g$).
- You also look at the GPS for the estimated miles remaining ($h$).
- You choose the route that minimizes the sum of both ($f$).

---

## 4. How it works (high-level steps)

### Step 1

Initialize a priority queue with the start node, using $f(start) = h(start)$.

### Step 2

Expand the node with the smallest $f(n)$ value.

### Step 3

For each neighbor, calculate its $g(n)$ and $f(n)$. If a shorter path to the neighbor is found, update its values and add to the queue.

---

## 5. Strengths

- **Optimal:** Guarantees the shortest path if the heuristic is *admissible* (never overestimates).
- **Efficient:** Expands fewer nodes than BFS/UCS by using domain knowledge.
- **Versatile:** Widely used in GPS, robotics, and game AI.

---

## 6. Weaknesses / failure cases

- **Memory intensive:** Must store all visited states and their costs.
- **Heuristic dependence:** Performance varies based on how well $h(n)$ approximates the real cost.

---

## 7. Where it is used in real systems

### FAANG example

- Google Maps routing.
- Game pathfinding (e.g., characters moving in StarCraft or League of Legends).
- Robotics navigation (SLAM).

### Startup example

- Drone navigation pathing.
- Delivery route optimization.
- Warehouse robotics (e.g., Amazon/Kiva bots).

---

## 8. Keywords / terms to remember

- **f(n)**: Total evaluation function.
- **g(n)**: Cost so far.
- **h(n)**: Heuristic estimate.
- **Admissible**: $h(n) \le h^*(n)$ (never overestimates actual cost).
- **Consistent**: Triangle inequality satisfied by the heuristic.

---

## 9. 30–60 Minute Coding Task

### Goal

Implement A* using Manhattan heuristic and observe its balanced search behavior.

### Task

Implement A* search on a grid and compare the number of nodes expanded against UCS and Greedy Search.
