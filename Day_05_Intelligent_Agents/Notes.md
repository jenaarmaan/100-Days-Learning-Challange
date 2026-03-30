# Day 5: Intelligent Agents

## 1) One-line definition (in your own words)

An intelligent agent is an entity that perceives its environment, makes decisions, and acts rationally to achieve goals based on available information.

## 2) Problem it solves

### Why this exists

- Provides a structured framework for designing AI systems.
- Defines how AI perceives, decides, and acts.
- Helps evaluate whether an AI system behaves rationally.

### What fails without it

- AI systems lack decision-making clarity.
- No way to measure effectiveness.
- Difficult to model real-world interactions.

## 3) Core idea (intuition)

### Analogy

Think of a self-driving car:

- **Sensors** → Perception (camera, radar)
- **Decision system** → Reasoning
- **Controls** → Actions (steering, braking)
- **Goal** → Safe, efficient driving

**Rationality** means choosing the best action based on current knowledge and goals.

### Architecture

```text
Environment → Sensors → Agent → Actuators → Environment
                  ↓
              Decision Logic
```

## 4) How it works (high-level steps)

1. **Perception**: Agent perceives environment through sensors.
2. **Reasoning**: Processes information using rules, models, or learning.
3. **Action**: Selects and executes actions maximizing expected goal achievement.

## 5) Strengths

- Clear decision-making framework.
- Works across domains (robotics, ML, planning).
- Supports adaptive behavior.
- Enables performance evaluation.

## 6) Weaknesses / failure cases

- Rationality depends on available information.
- Imperfect sensors cause errors.
- Computational limits restrict optimal decisions.
- Environment uncertainty affects outcomes.

## 7) Where it is used in real systems

- **FAANG**: Recommendation systems, autonomous driving research, virtual assistants.
- **Startups**: Robotics automation, AI chatbots, trading algorithms.

## 8) Keywords / terms to remember

- Agent
- Environment
- Sensors
- Actuators
- Rationality
- Perception-action loop
- Utility maximization
