# Day 16: Local Search & Hill Climbing

---

## 1. One-line definition

**Hill Climbing is a local search algorithm that continuously moves to a better neighboring state until no improvement is possible.**

---

## 2. Problem it solves

- Used for optimization.
- Suitable when path doesn't matter.
- Used in large continuous spaces.

---

## 3. Core idea

Move toward increasing objective value.

Analogy: Climbing a hill blindfolded — always step upward.

---

## 4. Steps

1. Start at initial state.
2. Move to best neighbor.
3. Stop when no better neighbor.

---

## 5. Strengths

- Simple.
- Low memory.
- Fast.

---

## 6. Weaknesses / failure cases

- Local maxima (stuck on a peak that isn't the highest overall).
- Plateaus (flat areas where any move is the same).
- Not complete (may not find the global maximum).

---

## 7. Where it is used in real systems

- Hyperparameter tuning.
- Scheduling.
- Optimization engines.

---

## 8. Keywords

- **Local optimum**: A state better than its neighbors but not globally optimal.
- **Plateau**: A set of neighboring states with the same objective value.
- **Objective function**: The mathematical function we want to maximize/minimize.
- **Neighbor**: States reachable by a small change.

---

## 9. Coding Task: Function Optimization

Optimize a quadratic function using hill climbing.

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 + 4*x

def hill_climbing(start_x, step_size=0.1, max_iter=100):
    x = start_x
    history = [x]
    
    for _ in range(max_iter):
        neighbors = [x + step_size, x - step_size]
        next_x = max(neighbors, key=f)
        
        # Stop if no improvement
        if f(next_x) <= f(x):
            break
            
        x = next_x
        history.append(x)
        
    return x, history

# Initial state
x_start = np.random.uniform(-10, 10)
best_x, search_history = hill_climbing(x_start)

print(f"Initial x: {x_start:.4f}")
print(f"Best x: {best_x:.4f}")
print(f"Max value: {f(best_x):.4f}")
```
