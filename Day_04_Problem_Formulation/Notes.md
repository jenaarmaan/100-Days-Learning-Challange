# Day 4: AI Problem Formulation

### 1) One-line definition (in your own words)
AI problem formulation is the process of clearly defining a task in terms of states, actions, goals, and constraints so an AI system can systematically solve it.

### 2) Problem it solves
**Why this exists**
- AI systems need structured problem definitions before applying algorithms.
- Converts vague real-world tasks into solvable computational models.
- Enables efficient search, optimization, and learning.

**What fails without it**
- Algorithms become ineffective or misapplied.
- Ambiguous goals lead to incorrect outputs.
- Poor performance due to undefined constraints or states.

### 3) Core idea (intuition)
**Analogy**
Planning a road trip:
- **Initial state** → Current location
- **Goal state** → Destination
- **Actions** → Routes you can take
- **Constraints** → Time, fuel, traffic

Without defining these, navigation becomes chaotic.

**Structure**
```
Initial State → Actions → State Transitions → Goal State
        ↑                               ↓
     Constraints and Environment Rules
```

### 4) How it works (high-level steps)
1. **Define the initial state**: Identify the starting point or current situation.
2. **Specify possible actions**: Map out all valid moves and how they change the state (transitions).
3. **Define goal state and constraints**: State the objective and the boundaries (rules) for a valid solution.

### 5) Strengths
- Clarifies problem structure.
- Enables algorithm selection.
- Improves solution efficiency.
- Makes AI systems reproducible.

### 6) Weaknesses / failure cases
- Incorrect abstraction leads to poor solutions.
- Over-simplification ignores important factors.
- Complex environments are difficult to model fully.

### 7) Where it is used in real systems
- **FAANG**: Route optimization (Google Maps), recommendation engines, logistics planning.
- **Startups**: Delivery route optimization, customer segmentation, automated scheduling.

### 8) Keywords / terms to remember
- State space
- Initial state
- Goal state
- Actions
- Constraints
- Search problem
- Optimization formulation
