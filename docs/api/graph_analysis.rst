Graph Analysis Module
=====================

.. automodule:: graph_analysis
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

visualize_graph_with_categories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: graph_analysis.visualize_graph_with_categories

**Example:**

.. code-block:: python

   from graph_analysis import visualize_graph_with_categories
   from leonardo_kg import LeonardoKnowledgeGraph
   
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   visualize_graph_with_categories(
       kg.graph, 
       'output/graph_by_category.png'
   )

visualize_centrality
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: graph_analysis.visualize_centrality

**Example:**

.. code-block:: python

   from graph_analysis import visualize_centrality
   from leonardo_kg import LeonardoKnowledgeGraph
   
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Calculate centrality
   pagerank = kg.calculate_pagerank()
   
   visualize_centrality(
       kg.graph,
       pagerank,
       "PageRank Centrality",
       "output/pagerank_centrality.png"
   )

visualize_communities
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: graph_analysis.visualize_communities

**Example:**

.. code-block:: python

   from graph_analysis import visualize_communities
   from leonardo_kg import LeonardoKnowledgeGraph
   
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Detect communities
   communities = kg.detect_communities()
   
   visualize_communities(
       kg.graph,
       communities,
       'output/communities.png'
   )

create_summary_plot
~~~~~~~~~~~~~~~~~~~

.. autofunction:: graph_analysis.create_summary_plot

**Example:**

.. code-block:: python

   from graph_analysis import create_summary_plot
   from leonardo_kg import LeonardoKnowledgeGraph
   
   kg = LeonardoKnowledgeGraph()
   kg.load_concepts('data/concepts.csv')
   kg.load_relationships('data/relationships.csv')
   
   # Get analysis results
   stats = kg.get_basic_stats()
   pagerank = kg.calculate_pagerank()
   communities = kg.detect_communities()
   
   # Prepare results dictionary
   results = {
       'stats': stats,
       'top_pagerank': sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10],
       'communities': communities
   }
   
   create_summary_plot(results, 'output/summary.png')