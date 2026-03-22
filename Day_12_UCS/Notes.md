# Day 12: Uniform Cost Search (UCS)

## 1) One-line definition
Uniform Cost Search (UCS) is an evaluation-based search algorithm that expands the node with the lowest cumulative path cost from the start, ensuring the cheapest path is found first in weighted graphs.

## 2) Problem it solves
**Why this exists**
- In many real-world problems, actions have different costs (e.g., fuel, time, tolls).
- BFS treats all edges as equal (weight = 1).
- UCS adapts to varying weights, expanding nodes by **cost** rather than **depth**.

**What fails without it**
- Simple BFS would confidently return a short path with 3 steps that costs $1000, while ignoring a longer path with 10 steps that costs only $10.

## 3) Core Idea (Intuition)
### Analogy: Road Trip
Imagine driving from City A to City B. You have two options:
- **Shortcut**: 50km but has $50 in tolls.
- **Scenic Route**: 100km but has $0 in tolls.
BFS would pick the Shortcut. UCS would pick the Scenic Route because the total "cost" is lower.

### Diagram
![UCS Cost-Aware Expansion Illustration](file:///d:/projects/100-Days-Learning-Challange/Day_12_UCS/ucs_visualization.png)

```
    (A) --[5]--> (B) --[5]--> (C)
     |                         ^
    [2]                       [10]
     |                         |
    (D) -----------------------/

BFS chooses A -> D -> C (2 steps, cost 12)
UCS chooses A -> B -> C (2 steps, cost 10)
```

## 4) How it works
1. **Initialize**: Use a **Priority Queue** (Min-Heap).
2. **Push**: Add the start node with cost = 0.
3. **Loop**:
   - **Pop** the node with the **lowest cumulative cost** $g(n)$.
   - If goal, return path.
   - **Explore neighbors**: For each neighbor, calculate `new_cost = current_cost + edge_cost`.
   - **Update**: If we found a cheaper way to reach the neighbor, update its cost in the queue.

## 5) Strengths
- **Optimal**: Guaranteed to find the least costly path if all step costs $\ge \epsilon > 0$.
- **Complete**: Will find the goal in finite graphs.
- **Dijkstra Connection**: UCS is essentially Dijkstra's algorithm but stops as soon as the goal is reached.

## 6) Weaknesses
- **Search Space**: Can explore a massive number of nodes if a low-cost path leads away from the goal.
- **No Heuristics**: It explores based only on the past ($g(n)$), not the future (this leads to A* later!).
- **Memory**: Needs to store all explored nodes and the frontier.

## 7) Real-World Examples
- **Google Maps**: Basic route calculation based on travel time (cost).
- **Packet Routing**: Sending data through the network with the lowest latency.
- **Database Querying**: Choosing the "cheapest" execution plan for a SQL query.

## 8) Key Terms
- **Priority Queue**: The backbone of UCS.
- **g(n)**: The total cost from start to node $n$.
- **Optimal Path**: The cheapest route, regardless of step count.

## 9) Coding Task: BFS vs UCS on 5x5 Weighted Grid
### Results Comparison
| Metric | BFS (Shortest Steps) | UCS (Lowest Cost) |
| :--- | :--- | :--- |
| **Path Cost** | 12 | **8** |
| **Number of Steps**| 9 | 9 |

### Observations
In my test grid, both algorithms took 9 steps, but **UCS** chose a route that snaked through 1-cost cells, successfully avoiding the high-cost (9) "walls." **BFS** blindly took a path with a 5-cost cell because it was the most direct route in terms of steps.

- **BFS** optimized for **Distance**.
- **UCS** optimized for **Price**.
