# Day 10: Depth First Search (DFS)

## 1) One-line definition

Depth First Search (DFS) is a search algorithm that explores as far as possible along one branch of a state space before backtracking and exploring alternative branches.

## 2) Problem it solves

### Why this exists

- Systematic way to explore state spaces.
- Memory efficient for very deep trees.
- Essential for cycle detection, topological sorting, and solving puzzles where you must follow deep logic chains.

### What fails without it

- Random jumping around state spaces without a plan.
- Infinite loops in cyclic graphs if no visited check.
- High memory usage if BFS is always chosen for deep search trees.

## 3) Core Idea (Intuition)

### Analogy: Exploring a Maze

Standard "left-hand rule" in a maze is like DFS. You follow one path until you hit a wall, then backtrack to the last intersection and try a different direction.

### Diagram

![DFS Process Illustration](file:///d:/projects/100-Days-Learning-Challange/Day_10_DFS/dfs_visualization.png)

```text
     A
   /   \
  B     C
 / \
D   E

DFS Order: A → B → D → (Backtrack) → E → (Backtrack) → C
```

## 4) How it works (high-level steps)

1. **Push** the start node onto a **Stack** (LIFO).
2. While stack is not empty:
   - **Pop** current node.
   - If goal, return.
   - **Mark** as visited.
   - **Push** all unvisited neighbors onto the stack.

## 5) Strengths

- **Memory Efficiency**: Only needs to store the current path and siblings of nodes on the current path ($O(d)$ where $d$ is depth).
- **Deep Exploration**: Finds solutions quickly if they are hidden deep in the tree.
- **Cycle Detection**: Very natural fit for detecting cycles in graphs.

## 6) Weaknesses / failure cases

- **Not Optimal**: Does not guarantee the shortest path (as seen in today's task).
- **Infinite Paths**: Can get stuck in infinite branches if not careful.
- **Completeness**: May fail to find a goal in infinite-depth spaces if it chooses the wrong branch first.

## 7) Real-World Examples

- **Compilers**: Used in dependency resolution and syntax tree traversal.
- **Game AI**: Pathfinding in large open spaces where any path is better than none.
- **Networking**: Discovering connected components in massive social networks.

## 8) Keywords / terms to remember

- **Stack / Recursion**: The underlying data structure.
- **Backtracking**: Returning to a previous state when a branch ends.
- **LIFO**: Last In, First Out logic.

## 9) Coding Task: BFS vs DFS Comparison

### Task Overview

I implemented both BFS and DFS on an 8x8 grid with obstacles.

### Comparison Results

The comparison was conducted on an 8x8 grid with several obstacles (the same obstacles used in the Day 9 BFS task).

| Metric             | BFS (Queue) | DFS (Stack) |
| :----------------- | :---------- | :---------- |
| **Path Found?**    | Yes         | Yes         |
| **Path Length**    | 15          | 17          |
| **Nodes Explored** | 49          | 50          |

### Visualization Comparison

In my implementation:

- **BFS** found the shortest possible path (**15 steps**).
- **DFS** found a slightly longer path (**17 steps**) because it dived deep into one direction (following right/down moves) before exploring shorter routes.
- The **Nodes Explored** were similar in this small grid, but BFS tends to explore in a radial/wave pattern, whereas DFS snakes through.

### Reflections

- **BFS** explores all neighbors layer by layer, guaranteeing the shortest path in unweighted grids.
- **DFS** dives deep down one branch. It might find a path VERY different from the shortest one.
- In BFS, we visited more nodes generally if the goal is far, but BFS is systematic.
- If we reordered the 'moves' list in DFS (e.g., trying Left/Up first), we would get a completely different path.
