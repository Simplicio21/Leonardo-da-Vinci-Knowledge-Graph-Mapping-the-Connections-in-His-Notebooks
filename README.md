🎨 Leonardo da Vinci Knowledge Graph: Mapping the Connections in His Notebooks
<div align="center">
https://img.shields.io/badge/python-3.12+-blue.svg
https://img.shields.io/badge/license-MIT-green.svg
https://img.shields.io/badge/docs-online-blue.svg

A computational graph analysis of interdisciplinary concepts in Leonardo da Vinci's notebooks

</div>
📊 About the Project
The Problem
Leonardo da Vinci was a Renaissance genius who studied multiple fields simultaneously: art, science, engineering, anatomy, and more. His notebooks contain thousands of interconnected ideas, but how can we systematically visualize and analyze these connections?

The Solution
This project creates a knowledge graph that maps Leonardo's key concepts and their relationships. Using graph theory algorithms, we can:

Identify the most important concepts

Discover communities of related ideas

Visualize how different knowledge domains connect

Why Graphs?
Graphs are perfect mathematical structures for representing complex relationships. In this project:

Nodes (vertices): Leonardo's concepts (e.g., "Proportion", "Anatomy")

Edges (links): Relationships between concepts (e.g., "influences", "related to")

🚀 Key Features
1. Centrality Analysis
Identifies the most important concepts using three different metrics:

Degree Centrality: Counts how many connections each concept has

Betweenness Centrality: Measures concepts that act as "bridges" between areas

PageRank: Google's algorithm that measures importance considering important connections

2. Community Detection
Uses the Louvain algorithm to group related concepts. For example:

Mathematics Community: Proportion, Geometry

Engineering Community: Mechanics, Hydrology, Flight

3. Interactive Visualizations
Generates multiple types of visualizations:

Graphs colored by category

Heat maps of importance

Community clustering

Minimum spanning tree

4. Path Analysis
Finds the shortest path between two concepts, revealing how seemingly unrelated ideas connect.

🛠️ Technologies Used
Technology	Role in the Project
NetworkX	Main library for creating and analyzing graphs
Matplotlib	Generation of visualizations and plots
Pandas	Handling notebook data
Python-Louvain	Community detection algorithm
SciPy	Numerical calculations for PageRank
Sphinx	Professional automated documentation
📁 Project Structure
text
Leonardo-da-Vinci-Knowledge-Graph/
├── src/                    # Main source code
│   ├── FinalProject.py     # Main execution script
│   ├── leonardo_kg.py      # Knowledge graph class
│   └── graph_analysis.py   # Analysis and visualization functions
├── data/                   # Structured data
│   ├── leonardo_concepts.csv     # Leonardo's concepts
│   └── relationships.csv          # Relationships between concepts
├── docs/                   # Sphinx documentation
├── output/                 # Automatically generated results
├── tests/                  # Unit tests
├── .github/workflows/      # GitHub automation
├── requirements.txt        # Project dependencies
└── README.md              # This file
📊 The Data
Concept Structure (leonardo_concepts.csv)
csv
id,name,category,description
C1,Proportion,Mathematics,"Mathematical proportions in art and architecture"
C2,Human Anatomy,Anatomy,"Study of the human body structure"
C3,Optics,Science,"Study of light and vision"
Relationship Structure (relationships.csv)
csv
source,target,relationship,weight
C1,C4,influences,2.0
C1,C9,related_to,1.5
Weights: Indicate relationship strength (1.0 = weak, 3.0 = strong)

🎯 How to Use
1. Installation
bash
# Clone the repository
git clone https://github.com/stefanysimplicio/Leonardo-da-Vinci-Knowledge-Graph-Mapping-the-Connections-in-His-Notebooks.git
cd Leonardo-da-Vinci-Knowledge-Graph-Mapping-the-Connections-in-His-Notebooks

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
2. Execution
bash
python src/FinalProject.py
The program automatically runs all analyses and generates:

Statistics in the terminal

5 graphical visualizations in the output/ folder

A GEXF file for analysis in Gephi

3. Expected Results
After running, you'll see in the terminal:

text
======================================================================
LEONARDO DA VINCI KNOWLEDGE GRAPH ANALYSIS
======================================================================

📊 Initializing Knowledge Graph...
📂 Loading data...
✅ Data loaded successfully!

📈 Graph Statistics:
----------------------------------------
Number of nodes: 10
Number of edges: 12
Density: 0.1333
Number of communities: 3

🎯 Centrality Analysis:
1. Degree Centrality (Top 3):
    1. Proportion (0.4444)
    2. Mechanics (0.4444)
    3. Optics (0.3333)

✅ Analysis complete! Check the 'output/' folder for visualizations.
📈 Results Explanation
1. Most Important Concepts
Our graph shows that:

Concept	Importance	Why?
Proportion	⭐⭐⭐⭐⭐	Links art and mathematics, with multiple connections
Mechanics	⭐⭐⭐⭐	Central to engineering and motion
Optics	⭐⭐⭐	Connects science and art through perspective
2. Detected Communities
Community 1 (Mathematics): Proportion, Geometry

Community 2 (Engineering): Anatomy, Mechanics, Hydrology, Flight

Community 3 (Art-Science): Optics, Perspective, Botany, Philosophy

3. Interesting Discoveries
Perspective connects art and science through optics

Philosophy appears as a "bridge" concept between domains

Flight heavily depends on mechanics and hydrology

🔍 Graph Algorithms Implemented
Algorithm	Function	What It Reveals
Degree Centrality	Counts direct connections	Local popularity
Betweenness Centrality	Counts paths through node	"Bridge" concepts
PageRank	Measures iterative importance	Global influence
Louvain	Detects communities	Natural groupings
Dijkstra	Finds shortest paths	Most direct connections
Kruskal	Minimum spanning tree	Essential structure
🎨 Generated Visualizations
1. Graph by Category (graph_by_category.png)
Different colors for each category (Mathematics, Art, Science, etc.)

Node size proportional to number of connections

2. Centrality Map (degree_centrality.png)
Larger nodes = more important

Warmer colors = higher centrality

3. Community Detection (communities.png)
Each community in a different color

Shows how concepts naturally cluster

4. PageRank Analysis (pagerank_centrality.png)
Based on Google's algorithm

Shows influence considering important connections

5. Graphical Summary (summary_analysis.png)
Combines all metrics in a single panel

Perfect for quick presentations

📚 Code Example: The Heart of the Project
python
# Simplified example of what happens in the project:

# 1. Create the graph
graph = NetworkX.DiGraph()

# 2. Add concepts as nodes
graph.add_node("Proportion", category="Mathematics")

# 3. Add relationships as edges
graph.add_edge("Proportion", "Perspective", weight=2.0)

# 4. Analyze importance
importance = nx.pagerank(graph)

# 5. Detect communities
communities = louvain_community(graph)

# 6. Visualize
visualize_graph(graph, "output/result.png")
🤔 Questions This Project Answers
"What are the most central concepts in Leonardo's notebooks?"
→ Answer: Proportion and Mechanics, based on centrality analysis.

"How do different knowledge domains connect?"
→ Answer: Through "bridge" concepts like Optics and Philosophy.

"Are there natural groupings of ideas?"
→ Answer: Yes, we detected 3 main communities.

"What's the shortest path between Art and Science?"
→ Answer: Art → Perspective → Optics → Science.

📊 Insights for Discussion
What the data reveals about Leonardo:
Systemic Thinking: Concepts connect across multiple disciplines

Art as Science: Perspective and Optics connect art and science

Human Engineering: Anatomy connected with mechanics shows vision of the body as a machine