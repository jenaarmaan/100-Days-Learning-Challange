# Day 31: Ontologies & Knowledge Graphs

## 1. One-line Definition
**Ontologies** define the structured concepts and relationships within a specific domain, while **knowledge graphs** represent this knowledge as a network of interconnected entities and real-world relations.

---

## 2. Problem it Solves
### Why this exists
As knowledge bases grow, simple systems like standard frames or semantic networks can become inconsistent. Different systems might call the same concept by different names, leading to a "Tower of Babel" problem in AI.

**Ontologies solve this by:**
- Providing **standardized vocabularies**.
- Creating **clear definitions** of concepts that different systems can share.
- Ensuring **interoperability** (allowing different AIs to speak the same "logic language").

### Example
- **Ontology:** Defines that `Dog` is a subclass of `Mammal`, and `Mammal` has properties like `lungs`.
- **Knowledge Graph:** Uses that definition to store facts like `Buddy` is a `Dog`. Because of the ontology, the system automatically knows `Buddy` has `lungs`.

---

## 3. Core Idea (Intuition)
- **Ontology = The Blueprint:** It defines the "rules of the world." It's abstract. (e.g., "Humans are mortal," "Dogs have owners.")
- **Knowledge Graph = The Data:** It populates the blueprint with real-world entities. It's concrete. (e.g., "Socrates is a Human," "Buddy is a Dog.")

### The "Triple" Format
Knowledge is often stored as **Subject-Predicate-Object** triples:
- `(Buddy, isA, Dog)`
- `(Buddy, owner, Alice)`

---

## 4. Components

### Ontology Components:
1.  **Classes:** Abstract categories (Person, City, Disease).
2.  **Properties:** Relationships (livesIn, treatedBy, subclassOf).
3.  **Constraints:** Rules (e.g., "An ID must be unique").

### Knowledge Graph Components:
1.  **Nodes:** Specific entities (Paris, Albert Einstein, COVID-19).
2.  **Edges:** The links connecting those nodes based on properties defined in the ontology.

---

## 5. Comparison: Ontology vs. Knowledge Graph

| Feature | Ontology | Knowledge Graph |
| :--- | :--- | :--- |
| **Purpose** | Define Structure & Rules | Store & Navigate Data |
| **Nature** | Abstract / Conceptual | Concrete / Instance-based |
| **Example** | "Every City is a Location" | "London is in the UK" |
| **Language** | OWL, RDF Schema | RDF Triples, Graph Databases |

---

## 6. Real-World Applications
- **Google Knowledge Graph:** Powers those info boxes you see in search results.
- **Recommendation Engines:** Understanding the relationships between a user's tastes and movie genres.
- **Healthcare:** Mapping symptoms to diseases and treatments globally.
- **Semantic Web:** Making web data readable by machines.

---

## 7. Coding Task: Simple Knowledge Graph
A Python implementation demonstrating triple storage, hierarchical inference (transitive logic), and a simple Q&A interface can be found in [knowledge_graph.py](./knowledge_graph.py).

### Running the implementation
```powershell
python knowledge_graph.py
```
---
