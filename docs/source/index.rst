Leonardo da Vinci Knowledge Graph
=================================

Welcome to the documentation for the Leonardo da Vinci Knowledge Graph project.

.. image:: https://img.shields.io/badge/python-3.8%2B-blue
   :target: https://python.org
.. image:: https://img.shields.io/badge/graph-networkx-orange
   :target: https://networkx.org
.. image:: https://img.shields.io/badge/license-MIT-green
   :target: LICENSE

.. toctree::
   :maxdepth: 3
   :caption: Contents:
   
   overview
   installation
   usage
   api/leonardo_kg
   api/graph_analysis
   results
   contributing

Overview
--------

This project creates a knowledge graph from Leonardo da Vinci's notebooks to analyze 
how his ideas connected across different disciplines (art, engineering, anatomy, 
science, mathematics, and philosophy) using graph theory and network analysis.

Key Features:

* **65+ concepts** from Leonardo's notebooks
* **Graph algorithms**: Centrality, PageRank, Community Detection
* **Visualizations**: Interactive graphs, centrality plots, community structures
* **Analysis**: Shortest paths, Minimum Spanning Tree, betweenness analysis

Installation
------------

.. include:: installation.rst

Usage
-----

.. include:: usage.rst

API Documentation
----------------

.. toctree::
   :maxdepth: 2
   
   api/leonardo_kg
   api/graph_analysis

Results
-------

.. include:: results.rst

Contributing
------------

.. include:: contributing.rst

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`