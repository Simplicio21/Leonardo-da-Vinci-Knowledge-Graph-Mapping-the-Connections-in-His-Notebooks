LeonardoKnowledgeGraph Module
=============================

.. automodule:: leonardo_kg
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Classes
-------

.. autoclass:: LeonardoKnowledgeGraph
   :members:
   :special-members: __init__
   :inherited-members:
   
   .. rubric:: Methods
   
   .. automethod:: __init__
   .. automethod:: load_concepts
   .. automethod:: load_relationships
   .. automethod:: get_basic_stats
   .. automethod:: calculate_degree_centrality
   .. automethod:: calculate_betweenness_centrality
   .. automethod:: calculate_closeness_centrality
   .. automethod:: calculate_pagerank
   .. automethod:: detect_communities
   .. automethod:: find_shortest_path
   .. automethod:: calculate_mst
   .. automethod:: get_node_info
   .. automethod:: export_to_gexf

Examples
--------

**Creating and using the knowledge graph:**

.. code-block:: python

   from leonardo_kg import LeonardoKnowledgeGraph
   
   # Initialize the graph
   kg = LeonardoKnowledgeGraph()
   
   # Load data
   kg.load_concepts('data/leonardo_concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Get statistics
   stats = kg.get_basic_stats()
   print(f"Graph has {stats['Number of nodes']} nodes and {stats['Number of edges']} edges")
   
   # Calculate centrality
   centrality = kg.calculate_degree_centrality()
   top_node = max(centrality.items(), key=lambda x: x[1])
   print(f"Most central concept: {top_node[0]}")

**Finding shortest paths:**

.. code-block:: python

   # Find shortest path between two concepts
   path = kg.find_shortest_path('C1', 'C10')
   if path:
       print(f"Path found with {len(path)-1} edges")
       for node in path:
           print(f"  - {kg.graph.nodes[node]['name']}")

**Community detection:**

.. code-block:: python

   # Detect communities
   communities = kg.detect_communities(method='louvain')
   print(f"Found {len(communities)} communities")
   
   # Display each community
   for i, community in enumerate(communities):
       print(f"\nCommunity {i+1} ({len(community)} nodes):")
       for node in community[:3]:  # Show first 3 nodes
           print(f"  - {kg.graph.nodes[node]['name']}")