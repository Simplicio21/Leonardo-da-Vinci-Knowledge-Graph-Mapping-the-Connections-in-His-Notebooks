"""
Leonardo da Vinci Knowledge Graph: Mapping the Connections in His Notebooks
===========================================================================
Final Project for CSCI 310 - Graph Theory and Analysis

This project creates and analyzes a knowledge graph of Leonardo da Vinci's
interdisciplinary concepts, demonstrating graph algorithms and visualizations.

Author: Stefany Simplicio
Date: December 2025
"""

import sys
import os
import matplotlib.pyplot as plt

# Add current directory to Python path to import our modules
sys.path.insert(0, os.path.dirname(__file__))

# Import our modules
from leonardo_kg import LeonardoKnowledgeGraph
from graph_analysis import (
    visualize_graph_with_categories,
    visualize_centrality,
    visualize_communities,
    create_summary_plot
)


def main():
    """Main function to run the complete analysis."""
    
    print("=" * 70)
    print("LEONARDO DA VINCI KNOWLEDGE GRAPH ANALYSIS")
    print("=" * 70)
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    # Initialize graph
    print("\n📊 Initializing Knowledge Graph...")
    kg = LeonardoKnowledgeGraph()
    
    # Load data
    print("\n📂 Loading data...")
    try:
        # Go up one level to find data folder
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        concepts_path = os.path.join(data_dir, 'leonardo_concepts.csv')
        relationships_path = os.path.join(data_dir, 'relationships.csv')
        
        kg.load_concepts(concepts_path)
        kg.load_relationships(relationships_path)
        print("✅ Data loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        print("Please ensure the data files exist in the 'data/' directory.")
        print(f"Current directory: {os.getcwd()}")
        return
    
    # Get basic statistics
    print("\n📈 Graph Statistics:")
    print("-" * 40)
    stats = kg.get_basic_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Centrality Analysis
    print("\n🎯 Centrality Analysis")
    print("-" * 40)
    
    # Degree Centrality
    print("\n1. Degree Centrality (Top 10):")
    degree_centrality = kg.calculate_degree_centrality()
    top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
    for i, (node_id, score) in enumerate(top_degree, 1):
        node_name = kg.graph.nodes[node_id]['name']
        print(f"   {i:2}. {node_name:30} {score:.4f}")
    
    # Betweenness Centrality
    print("\n2. Betweenness Centrality (Top 10):")
    betweenness = kg.calculate_betweenness_centrality()
    top_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:10]
    for i, (node_id, score) in enumerate(top_betweenness, 1):
        node_name = kg.graph.nodes[node_id]['name']
        print(f"   {i:2}. {node_name:30} {score:.4f}")
    
    # PageRank
    print("\n3. PageRank (Top 10):")
    pagerank = kg.calculate_pagerank()
    top_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]
    for i, (node_id, score) in enumerate(top_pagerank, 1):
        node_name = kg.graph.nodes[node_id]['name']
        print(f"   {i:2}. {node_name:30} {score:.4f}")
    
    # Community Detection
    print("\n👥 Community Detection")
    print("-" * 40)
    communities = kg.detect_communities(method='louvain')
    print(f"Number of communities detected: {len(communities)}")
    
    # Show community information
    for i, community in enumerate(communities[:5], 1):  # Show first 5 communities
        community_names = [kg.graph.nodes[node_id]['name'] for node_id in community[:5]]
        print(f"\nCommunity {i} ({len(community)} nodes):")
        print(f"  Examples: {', '.join(community_names)}")
    
    # Shortest Path Analysis
    print("\n🛣️  Shortest Path Analysis")
    print("-" * 40)
    
    # Get some example nodes
    if kg.graph.nodes():
        nodes = list(kg.graph.nodes())
        if len(nodes) >= 4:
            # Find paths between some central nodes
            central_nodes = [node_id for node_id, _ in top_degree[:4]]
            
            for i in range(min(2, len(central_nodes))):
                for j in range(i+1, min(3, len(central_nodes))):
                    source = central_nodes[i]
                    target = central_nodes[j]
                    path = kg.find_shortest_path(source, target)
                    
                    if path:
                        source_name = kg.graph.nodes[source]['name']
                        target_name = kg.graph.nodes[target]['name']
                        print(f"\n{source_name} → {target_name}:")
                        print(f"  Path length: {len(path)-1} edges")
                        
                        # Show abbreviated path
                        if len(path) > 6:
                            path_display = (
                                f"{kg.graph.nodes[path[0]]['name']} → "
                                f"{kg.graph.nodes[path[1]]['name']} → ... → "
                                f"{kg.graph.nodes[path[-2]]['name']} → "
                                f"{kg.graph.nodes[path[-1]]['name']}"
                            )
                        else:
                            path_display = " → ".join([kg.graph.nodes[node]['name'] for node in path])
                        
                        print(f"  Path: {path_display}")
    
    # Minimum Spanning Tree
    print("\n🌳 Minimum Spanning Tree Analysis")
    print("-" * 40)
    mst_edges = kg.calculate_mst()
    print(f"Number of edges in MST: {len(mst_edges)}")
    print(f"MST contains {len(set().union(*mst_edges))} nodes")
    
    # Visualization
    print("\n🎨 Generating Visualizations...")
    print("-" * 40)
    
    # Adjust output paths to be relative to current directory
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    
    # 1. Graph by category
    visualize_graph_with_categories(kg.graph, os.path.join(output_dir, 'graph_by_category.png'))
    
    # 2. Centrality visualizations
    visualize_centrality(kg.graph, degree_centrality, 
                        "Degree Centrality", os.path.join(output_dir, 'degree_centrality.png'))
    
    visualize_centrality(kg.graph, pagerank,
                        "PageRank Centrality", os.path.join(output_dir, 'pagerank_centrality.png'))
    
    # 3. Community visualization
    visualize_communities(kg.graph, communities, os.path.join(output_dir, 'communities.png'))
    
    # 4. Create summary plot
    results = {
        'stats': stats,
        'top_pagerank': [(kg.graph.nodes[node_id]['name'], score) 
                         for node_id, score in top_pagerank],
        'top_betweenness': [(kg.graph.nodes[node_id]['name'], score) 
                           for node_id, score in top_betweenness],
        'communities': communities
    }
    create_summary_plot(results, os.path.join(output_dir, 'summary_analysis.png'))
    
    # Export to GEXF for external tools
    kg.export_to_gexf(os.path.join(output_dir, 'leonardo_graph.gexf'))
    
    # Final Summary
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE!")
    print("=" * 70)
    
    print("\n📋 Key Findings:")
    print("-" * 40)
    
    # Most central concept
    if top_degree:
        most_central_id, most_central_score = top_degree[0]
        most_central_name = kg.graph.nodes[most_central_id]['name']
        print(f"1. Most central concept: {most_central_name} (Degree: {most_central_score:.4f})")
    
    # Concept with highest betweenness
    if top_betweenness:
        highest_betweenness_id, highest_betweenness_score = top_betweenness[0]
        highest_betweenness_name = kg.graph.nodes[highest_betweenness_id]['name']
        print(f"2. Highest betweenness: {highest_betweenness_name} ({highest_betweenness_score:.4f})")
    
    # Concept with highest PageRank
    if top_pagerank:
        highest_pagerank_id, highest_pagerank_score = top_pagerank[0]
        highest_pagerank_name = kg.graph.nodes[highest_pagerank_id]['name']
        print(f"3. Highest PageRank: {highest_pagerank_name} ({highest_pagerank_score:.4f})")
    
    print(f"4. Number of communities: {len(communities)}")
    print(f"5. Graph density: {stats.get('Density', 0):.4f}")
    
    print("\n📁 Output Files Generated:")
    print("-" * 40)
    print(f"output/graph_by_category.png    - Graph colored by concept category")
    print(f"output/degree_centrality.png    - Node size based on degree centrality")
    print(f"output/pagerank_centrality.png  - Node size based on PageRank")
    print(f"output/communities.png         - Community detection visualization")
    print(f"output/summary_analysis.png    - Summary of all analyses")
    print(f"output/leonardo_graph.gexf     - Graph in GEXF format (for Gephi)")
    
    print("\n✅ Analysis complete! Check the 'output/' folder for visualizations.")


if __name__ == "__main__":
    main()
