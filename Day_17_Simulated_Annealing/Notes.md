# Day 17: Simulated Annealing

---

## 1. One-line definition

**Simulated Annealing is a probabilistic optimization algorithm that allows occasional "worse" moves to escape local optima.**

---

## 2. Problem it solves

**Hill Climbing** easily gets stuck in **local maxima** (small peaks that aren't the highest point). Simulated Annealing addresses this by introducing randomness and a "cooling" schedule.

---

## 3. Core idea

We sometimes accept a worse solution with a probability $P$:

$$P = e^{-\frac{\Delta E}{T}}$$

Where:
- $\Delta E$: The difference between the new state and the current state (negative if worse).
- $T$: **Temperature**, which gradually decreases (cools down) over time.

As $T$ decreases, the algorithm becomes more selective, eventually behaving like Hill Climbing.

---

## 4. Steps

1. **Start with high temperature ($T$):** The algorithm is more likely to accept worse moves (high exploration).
2. **Generate a random neighbor:** Move a small random distance from the current state.
3. **Better move?** Always accept.
4. **Worse move?** Accept probabilistically according to $P = e^{-\frac{\Delta E}{T}}$.
5. **Cool down:** Reduce $T$ slowly (e.g., $T \times 0.99$) and repeat.

---

## 5. Strengths

- **Escapes local maxima**: The randomness allows jumping out of shallow "valleys".
- **Robust for complex optimization**: Works well when the function has many small bumps.

---

## 6. Weaknesses

- **Parameter tuning**: Finding the right initial temperature and cooling rate is tricky.
- **Slower convergence**: Requires more iterations than simple hill climbing because of the exploration phase.

---

## 7. Real systems

- AI **Neural Architecture Search** (NAS).
- **Circuit design** and layout optimization.
- **Scheduling** complex shifts in factories or hospitals.

---

## 8. Keywords

- **Temperature**: Controls the probability of accepting worse moves.
- **Cooling schedule**: How $T$ is reduced over time.
- **Probabilistic acceptance**: The mechanism for escaping local optima.
- **Global optimization**: The goal of finding the best overall solution.

---

## 9. Coding Task: Function Optimization with Local Maxima

Optimize $f(x) = -x^2 + 4x + \sin(5x)$ using Simulated Annealing. This function is tricky because $\sin(5x)$ creates many local peaks!

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 + 4*x + np.sin(5*x)

def simulated_annealing(start_x, T=1.0, cooling_rate=0.99, iters=1000):
    x = start_x
    history = [x]
    
    for i in range(iters):
        # 1. Random move
        new_x = x + np.random.normal(0, 1)
        delta = f(new_x) - f(x)
        
        # 2. Acceptance check
        if delta > 0 or np.random.rand() < np.exp(delta / T):
            x = new_x
            
        # 3. Cool down
        T *= cooling_rate
        history.append(x)
        
    return x, history

# Run
x_initial = np.random.uniform(-10, 10)
final_x, path = simulated_annealing(x_initial)

print(f"Final x: {final_x:.4f}, Max f(x): {f(final_x):.4f}")
```
