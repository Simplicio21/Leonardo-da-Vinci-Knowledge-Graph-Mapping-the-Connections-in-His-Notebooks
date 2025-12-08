Project Overview
================

The Leonardo da Vinci Knowledge Graph project aims to map and analyze the 
interdisciplinary connections found in Leonardo da Vinci's notebooks using 
graph theory and network analysis techniques.

Motivation
----------

Leonardo da Vinci was a true Renaissance man, working across multiple 
disciplines. This project seeks to understand how his ideas in different 
fields were interconnected using computational methods.

Objectives
----------

1. **Data Collection**: Extract and organize key concepts from Leonardo's work
2. **Graph Construction**: Build a knowledge graph with concepts as nodes and 
   relationships as edges
3. **Analysis**: Apply graph algorithms to discover patterns and insights
4. **Visualization**: Create clear visual representations of the knowledge graph
5. **Documentation**: Provide comprehensive documentation for reproducibility

Methodology
-----------

1. **Data Sources**: Concepts extracted from Leonardo's known notebooks and works
2. **Graph Structure**: Directed graph with weighted edges
3. **Algorithms Used**:
   - Centrality measures (Degree, Betweenness, PageRank)
   - Community detection (Louvain method)
   - Shortest path analysis
   - Minimum Spanning Tree
4. **Visualization**: NetworkX with Matplotlib for static visualizations

Graph Structure
---------------

The knowledge graph is structured as follows:

* **Nodes**: Concepts from Leonardo's work (e.g., "Proportion", "Human Anatomy")
* **Edges**: Relationships between concepts (e.g., "influences", "relates to")
* **Attributes**: 
  - Node attributes: name, category, description
  - Edge attributes: relationship type, weight