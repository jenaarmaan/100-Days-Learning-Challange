# Day 29: Knowledge Representation Techniques

## 1. One-line Definition
**Knowledge Representation (KR)** techniques are methods used in AI to store facts, relationships, and rules about the world in a structured form that machines can understand and reason with.

---

## 2. Problem it Solves
### Why this exists
AI systems need **knowledge about the world** to make decisions. Raw data alone is not enough; machines must represent:
- **Objects** (e.g., "Socrates", "MyDog")
- **Relationships** (e.g., "is-a", "part-of")
- **Rules** (e.g., "If it rains, the ground is wet")
- **Events and Categories**

### Example
- **Human knowledge:** "A dog is an animal. Animals breathe. Dogs bark."
- **Inference:** An AI system should be able to infer that "Dogs breathe."

### Without KR
AI systems would struggle with reasoning, understanding structural relationships, and making complex decisions based on context. KR transforms **information into machine-understandable knowledge**.

---

## 3. Core Idea (Intuition)
Knowledge representation answers three key questions:
1.  **What knowledge should be stored?** (Facts, rules, categories)
2.  **How should it be stored?** (Logic, semantic networks, frames, ontologies)
3.  **How can AI reason with it?** (Inference engines, rule-based reasoning)

---

## 4. Main KR Techniques

### 1. Logical Representation
Uses formal logic (Propositional or First-Order) to represent knowledge.
- *Example:* `Human(Socrates)` AND `Human(x) → Mortal(x)` $\implies$ `Mortal(Socrates)`.

### 2. Semantic Networks
Represents knowledge using **graphs** where nodes are objects and edges are relationships.
- *Example:* `Dog` $\xrightarrow{\text{is-a}}$ `Animal` $\xrightarrow{\text{can}}$ `Breathe`.

### 3. Frames
Structured knowledge about objects, similar to **object-oriented classes**.
- *Example:* A `Dog` frame with slots for `type`, `sound`, `legs`.

### 4. Production Rules
Knowledge represented as **IF–THEN rules**. Common in expert systems.
- *Example:* `IF temperature > 38 THEN patient has fever`.

### 5. Ontologies
Define complex concepts and hierarchy within a domain. Used in knowledge graphs (like Google's) and the Semantic Web.

---

## 5. Characteristics of Good KR
- **Representational Adequacy:** Can it represent all the necessary knowledge?
- **Inferential Adequacy:** Can it derive new knowledge from existing facts?
- **Inferential Efficiency:** How fast can it reason?
- **Acquisitional Efficiency:** How easy is it to add new info?

---

## 6. Real-World Applications
- **Expert Systems:** Medical diagnosis (e.g., MYCIN).
- **Virtual Assistants:** Understanding context and intent.
- **Knowledge Graphs:** Powering search engines.
- **Robotics:** Planning actions and understanding environment.

---

## 7. Keywords to Remember
- Knowledge Base
- Semantic Networks
- Frames
- Production Rules
- Ontologies
- Inference Engine

---

## 8. Coding Task: Semantic Network
A Python implementation using `networkx` to represent a semantic network with inheritance reasoning can be found in [semantic_network.py](./semantic_network.py).

### Running the implementation
```powershell
python semantic_network.py
```
---
