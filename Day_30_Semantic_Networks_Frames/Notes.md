# Day 30: Semantic Networks & Frames

## 1. One-line Definition
**Semantic networks** and **frames** are knowledge representation methods that organize information as relationships (graphs) and structured object descriptions (schemas) to enable reasoning in AI systems.

---

## 2. Problem it Solves
### Why this exists
Basic logical representations can be hard to visualize and scale for real-world knowledge. AI needs more structured, human-like representations to handle:
- Relationships between concepts
- Object properties
- Hierarchies
- **Inheritance** of knowledge

### Example
Instead of complex logical predicates, we can represent a hierarchy:
`Dog` $\xrightarrow{\text{is-a}}$ `Animal` $\xrightarrow{\text{breathes}}$ `Oxygen`.
This makes it intuitive to infer that a `Dog` breathes `Oxygen`.

---

## 3. Core Idea (Intuition)
- **Semantic Networks (Graph-based):** Focus on how things are **connected**. Nodes are objects/concepts, and edges are relationships.
- **Frames (Object-based):** Focus on **internal structure**. Each concept is a record (like a class) containing attributes (**slots**) and values (**fillers**).

Together, they allow for a complete picture: Semantic networks show the big picture of connections, while Frames store the detailed specifications.

---

## 4. Semantic Networks (In Detail)
A semantic network is a graph where:
- **Nodes** = Concepts (e.g., Bird, Wings).
- **Edges** = Relationships (e.g., `is-a`, `has-part`, `can`).

### Key Concept: Inheritance
If $A$ `is-a` $B$, and $B$ has property $P$, then $A$ inherits property $P$ unless explicitly overridden. This significantly reduces redundancy in the knowledge base.

---

## 5. Frames (In Detail)
Frames are structured templates for objects.

### Structure:
- **Slots:** Attributes (e.g., `color`, `legs`, `diet`).
- **Fillers:** The values for these slots (e.g., `brown`, `4`, `omnivore`).
- **Default Values:** Values that are automatically assumed unless the specific instances provide a different filler (Overriding).

---

## 6. Comparison: Semantic Networks vs. Frames

| Feature | Semantic Networks | Frames |
| :--- | :--- | :--- |
| **Structure** | Graph | Structured record / Template |
| **Focus** | Inter-object relationships | Intra-object attributes |
| **Visualization** | Highly visual and intuitive | Systematic and modular |
| **Usage** | Global concept mapping | Detailed entity modeling |

---

## 7. Strengths & Weaknesses
### Strengths
- Human-like organization of knowledge.
- Native support for inheritance.
- Improves explainability (we can trace the inheritance path).

### Weaknesses
- Can become extremely complex in large systems.
- Potential ambiguity in relationship names without strict ontologies.
- Not ideal for representing uncertainty or fuzzy logic.

---

## 8. Coding Task: Combined Frames System
A Python implementation that merges Semantic Networks with Frames, supporting multiple inheritance and recursive property lookup, can be found in [frames_system.py](./frames_system.py).

### Running the implementation
```powershell
python frames_system.py
```
---
