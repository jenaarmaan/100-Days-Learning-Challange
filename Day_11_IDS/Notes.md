# Day 11: Depth-Limited Search + Iterative Deepening (IDS)

## 1) One-line definition
Depth-Limited Search (DLS) restricts DFS to a fixed depth to prevent infinite exploration, while Iterative Deepening Search (IDS) repeatedly increases this limit until a solution is found, combining the memory efficiency of DFS with the completeness of BFS.

## 2) Problem it solves
**Why this exists**
- **DFS Failure**: DFS can get lost in infinite paths or very deep branches even if a solution is shallow.
- **BFS Failure**: BFS is complete and optimal but consumes exponential memory ($O(b^d)$) to store the frontier.
- **IDS Solution**: It finds the shallowest solution (like BFS) while using only linear memory (like DFS).

**What fails without it**
- Agents might wander infinitely in cyclical or large state spaces.
- High-memory dependency for simple pathfinding in massive trees.

## 3) Core Idea (Intuition)
### Analogy: Searching for your Phone
1. **Level 0**: Check your pocket (is it here?).
2. **Level 1**: Check the room you are in.
3. **Level 2**: Check all rooms on this floor.
4. **Level 3**: Search the entire building.
You gradually expand your search radius, ensuring you don't travel to the neighbor's house before checking your own desk.

### Diagram
![IDS Expanding Search Layers Illustration](file:///d:/projects/100-Days-Learning-Challange/Day_11_IDS/ids_visualization.png)

```
Level 0: [Start]
Level 1: [Start] → (A) → (B)
Level 2: [Start] → (A) → (C), (D) | [Start] → (B) → (E), (F)
... 
Each level increases the cutoff limit.
```

## 4) How it works
1. Start with `limit = 0`.
2. Run Depth-First Search. Stop if the goal is found OR if the current path length equals the `limit`.
3. If not found, increment `limit` and repeat.
4. Stop when the first solution is discovered.

## 5) Strengths
- **Complete**: Guarantees finding a solution if one exists (in finite branching factors).
- **Optimal (for unweighted)**: Finds the shallowest solution first.
- **Memory Efficient**: Uses only $O(bd)$ space, whereas BFS uses $O(b^d)$.

## 6) Weaknesses
- **Redundancy**: The upper levels of the tree are re-explored multiple times in each iteration.
- **Computational Overhead**: Slower than a single BFS if memory is not an issue.
- **Branching Factor**: If the branching factor is very high, the re-exploration overhead increases.

## 7) Real-World Examples
- **Game AI (Chess/Go)**: Searching move trees where depth must be limited due to time constraints (Iterative Deepening Depth-First Search).
- **Robotics**: Path planning where the configuration space is too large for BFS.
- **Web Crawlers**: Limiting how "deep" a crawler goes into a specific website domain.

## 8) Key Terms
- **Depth Limit**: The cutoff point for DLS.
- **Iterative Deepening**: The loop that manages the DLS calls.
- **Cutoff**: The result returned when a search stops due to the limit without finding the goal.

## 9) Coding Task: Iterative Deepening on 6x6 Grid
### Task Results
I implemented IDS on a 6x6 grid with obstacles at `(2,2)`, `(3,2)`, and `(4,4)`.

| Metric | Result |
| :--- | :--- |
| **Start / Goal** | (0, 0) → (5, 5) |
| **Solution Depth Found** | **10** |
| **Total Nodes Processed**| **2,089** (cumulative across all iterations) |
| **Memory Usage** | Minimal (Current path + local recursion) |

### Observation
- The goal was reached at depth 10, which is the Manhattan distance from (0,0) to (5,5).
- Even though we re-explore the base levels, the number of nodes at the deepest level dominates the search, making the overhead acceptable compared to the memory savings.
- Unlike the pure DFS from Day 10 (which might have wandered many more steps), IDS ensured we found the **shortest path** to the goal.
