Usage Guide
===========

Basic Usage
-----------

To run the complete analysis:

.. code-block:: bash

   python src/FinalProject.py

This will:
1. Load the data from `data/` directory
2. Build the knowledge graph
3. Run all analyses
4. Generate visualizations in the `output/` directory

Command Line Options
--------------------

You can also import and use the modules directly:

.. code-block:: python

   from leonardo_kg import LeonardoKnowledgeGraph
   from graph_analysis import visualize_graph_with_categories
   
   # Create and load graph
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/leonardo_concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Get statistics
   stats = kg.get_basic_stats()
   print(stats)
   
   # Run analyses
   centrality = kg.calculate_degree_centrality()
   communities = kg.detect_communities()
   
   # Visualize
   visualize_graph_with_categories(kg.graph, 'output/my_graph.png')

Running Specific Analyses
-------------------------

**Centrality Analysis Only**

.. code-block:: python

   from leonardo_kg import LeonardoKnowledgeGraph
   
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/leonardo_concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Calculate all centrality measures
   degree = kg.calculate_degree_centrality()
   betweenness = kg.calculate_betweenness_centrality()
   pagerank = kg.calculate_pagerank()
   
   # Get top 10 concepts by PageRank
   top_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]
   for node_id, score in top_pagerank:
       print(f"{kg.graph.nodes[node_id]['name']}: {score:.4f}")

**Community Detection**

.. code-block:: python

   from leonardo_kg import LeonardoKnowledgeGraph
   
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/leonardo_concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Detect communities using Louvain method
   communities = kg.detect_communities(method='louvain')
   print(f"Found {len(communities)} communities")
   
   for i, community in enumerate(communities[:3], 1):
       print(f"\nCommunity {i} ({len(community)} nodes):")
       for node_id in community[:5]:  # Show first 5 nodes
           print(f"  - {kg.graph.nodes[node_id]['name']}")

**Shortest Path Analysis**

.. code-block:: python

   from leonardo_kg import LeonardoKnowledgeGraph
   
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/leonardo_concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Find shortest path between two concepts
   # First, find concept IDs
   concept_map = {data['name']: node_id for node_id, data in kg.graph.nodes(data=True)}
   
   source = concept_map.get('Proportion')
   target = concept_map.get('Human Anatomy')
   
   if source and target:
       path = kg.find_shortest_path(source, target)
       if path:
           print(f"Shortest path found ({len(path)-1} edges):")
           for node_id in path:
               print(f"  → {kg.graph.nodes[node_id]['name']}")

Generating Documentation
------------------------

To build the documentation locally:

.. code-block:: bash

   cd docs
   make html

The documentation will be available at `docs/_build/html/index.html`.

Running Tests
-------------

To run the test suite:

.. code-block:: bash

   python -m pytest tests/

Output Files
------------

The project generates the following output files:

* `output/graph_by_category.png` - Graph colored by concept category
* `output/degree_centrality.png` - Node size based on degree centrality
* `output/pagerank_centrality.png` - Node size based on PageRank
* `output/communities.png` - Community detection visualization
* `output/summary_analysis.png` - Summary of all analyses
* `output/leonardo_graph.gexf` - Graph in GEXF format (for Gephi)