# Day 32: Probability Theory Basics

## 1. One-line Definition

**Probability theory** is the mathematical framework for quantifying uncertainty, measuring how likely events are to occur, and enabling rational reasoning under incomplete information.

---

## 2. Problem it Solves

### Why this exists

In the real world, outcomes are rarely deterministic (100% certain). Systems face uncertainty in various ways:

- **Noise in sensor measurements** (e.g., LiDAR in self-driving cars).
- **Incomplete observations** (e.g., diagnosing a disease without knowing all patient history).
- **Inherent randomness** (e.g., stock market changes, user ad clicks).

Without probability, AI systems would rely on rigid, rule-based systems that break under noisy, real-world data. Probability provides a robust way to make decisions in uncertain environments.

### Example

When flipping a fair coin:

- **Possible outcomes:** Heads ($H$) or Tails ($T$).
- **Probability distribution:** $P(H) = 0.5$, $P(T) = 0.5$.

Knowing these odds, an AI agent can compute risk, evaluate expected value, and make optimal decisions.

---

## 3. Core Idea (Intuition)

Probability is a number between `0` and `1` (or 0% to 100%) representing our confidence in an event's occurrence:

- **0:** Impossible event.
- **1:** Certain event.

### Key Intuition: The Law of Large Numbers

As the number of times an experiment is repeated increases, the **empirical (observed) probability** converges closer to the **theoretical (true) probability**. This is why simulations with more trials yield more accurate results.

---

## 4. Basic Concepts

1. **Experiment:** A repeatable process with an uncertain outcome (e.g., rolling a six-sided die).
2. **Sample Space ($S$):** The set of all possible outcomes. For a six-sided die, $S = \{1, 2, 3, 4, 5, 6\}$.
3. **Event ($A$):** A subset of the sample space (e.g., rolling an even number: $A = \{2, 4, 6\}$).
4. **Probability of an Event ($P(A)$):**
   $$P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes in } S}$$
   For rolling an even number: $P(A) = \frac{3}{6} = 0.5$.

---

## 5. Types of Probability

1. **Classical Probability:** Based on physical symmetries and equally likely outcomes (e.g., theoretical coin flips).
2. **Empirical (Frequentist) Probability:** Estimated by conducting experiments and observing frequencies:
   $$P(A) \approx \frac{\text{Observed frequency of } A}{\text{Total trials}}$$
3. **Subjective (Bayesian) Probability:** Quantifies a degree of belief or credibility based on prior evidence and experience.

---

## 6. Important Rules

- **Complement Rule:** $P(\text{not } A) = 1 - P(A)$
- **Addition Rule:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Multiplication Rule (Independent Events):** $P(A \cap B) = P(A) \times P(B)$
- **Conditional Probability:** $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ (The probability of event $A$ occurring, given that event $B$ has already occurred).

---

## 7. Why Probability Matters in AI/ML

Probability is the bedrock of modern Machine Learning:

- **Classification:** Predicts the probability of a class, e.g., $P(\text{Spam} \mid \text{Words in email})$.
- **Generative Models:** Modeling probability distributions to generate text, images, or audio (e.g., Diffusion models, LLMs).
- **Reinforcement Learning:** Estimating the likelihood of state transitions in uncertain environments (Markov Decision Processes).

---

## 8. Strengths & Limitations

### Strengths

- Gracefully handles noise and missing data.
- Provides a rigorous mathematical framework for decision-making.
- Enables models to express confidence (or lack thereof) in predictions.

### Limitations

- Often requires simplifying assumptions (e.g., the Naive Bayes assumption of independence).
- Calculating joint probabilities over many variables can be computationally expensive.
- Subject to misinterpretation (e.g., conflating correlation with causation).

---

## 9. Keywords to Remember

- **Sample Space**
- **Event**
- **Empirical Probability**
- **Conditional Probability**
- **Independence**
- **Law of Large Numbers**
- **Joint Probability**

---

## 10. Coding Task: Probability Simulation

A Python implementation demonstrating empirical probability, biased coin tosses, conditional/joint probability, and convergence visualization can be found in [probability_simulation.py](./probability_simulation.py).

### Running the implementation

To run the simulation:

```powershell
python probability_simulation.py
```

This will run the empirical simulations and generate a convergence plot saved as `probability_convergence.png`.
