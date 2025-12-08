"""
Graph Analysis Utilities
=======================
Helper functions for analyzing and visualizing the knowledge graph.
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from typing import Dict, List, Any
import numpy as np


def visualize_graph_with_categories(graph: nx.DiGraph, output_path: str = 'output/graph_by_category.png') -> None:
    """
    Visualize graph with nodes colored by category.
    
    Parameters
    ----------
    graph : nx.DiGraph
        The graph to visualize
    output_path : str
        Path to save the visualization
    """
    plt.figure(figsize=(14, 12))
    
    # Define category colors
    category_colors = {
        'Arte': '#FF6B6B',
        'Engenharia': '#4ECDC4', 
        'Anatomia': '#95E06C',
        'Ciência': '#FFD166',
        'Matemática': '#A882DD',
        'Filosofia': '#FFA9E7'
    }
    
    # Get positions
    pos = nx.spring_layout(graph, seed=42, k=0.9)
    
    # Draw nodes by category
    for category, color in category_colors.items():
        nodes = [n for n, attr in graph.nodes(data=True) 
                if attr.get('category') == category]
        if nodes:
            nx.draw_networkx_nodes(graph, pos, 
                                  nodelist=nodes,
                                  node_color=color,
                                  label=category,
                                  node_size=400,
                                  alpha=0.8)
    
    # Draw edges
    nx.draw_networkx_edges(graph, pos, 
                          edge_color='gray',
                          alpha=0.3,
                          arrows=True,
                          arrowsize=10,
                          connectionstyle="arc3,rad=0.1")
    
    # Add labels for important nodes
    degrees = dict(graph.degree())
    important_nodes = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:15]
    labels = {node: graph.nodes[node]['name'] for node, _ in important_nodes}
    nx.draw_networkx_labels(graph, pos, labels, font_size=9)
    
    plt.title("Leonardo da Vinci Knowledge Graph by Category", fontsize=16, fontweight='bold')
    plt.legend(loc='upper left')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Category visualization saved to {output_path}")


def visualize_centrality(graph: nx.DiGraph, centrality_scores: Dict[str, float], 
                        title: str, output_path: str) -> None:
    """
    Visualize graph with node size based on centrality scores.
    
    Parameters
    ----------
    graph : nx.DiGraph
        The graph to visualize
    centrality_scores : dict
        Dictionary of centrality scores
    title : str
        Title for the visualization
    output_path : str
        Path to save the visualization
    """
    plt.figure(figsize=(14, 12))
    
    # Get positions
    pos = nx.spring_layout(graph, seed=42, k=0.9)
    
    # Normalize centrality scores for node sizes
    max_score = max(centrality_scores.values()) if centrality_scores.values() else 1
    node_sizes = [centrality_scores.get(node, 0) * 5000 / max_score + 100 
                  for node in graph.nodes()]
    
    # Draw graph
    nx.draw_networkx_nodes(graph, pos, 
                          node_size=node_sizes,
                          node_color='#4285F4',
                          alpha=0.7)
    
    nx.draw_networkx_edges(graph, pos,
                          edge_color='gray',
                          alpha=0.2,
                          arrows=False)
    
    # Label top nodes
    top_nodes = sorted(centrality_scores.items(), key=lambda x: x[1], reverse=True)[:10]
    top_labels = {node: graph.nodes[node]['name'] for node, _ in top_nodes}
    nx.draw_networkx_labels(graph, pos, top_labels, font_size=10, font_weight='bold',
                           bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Centrality visualization saved to {output_path}")


def visualize_communities(graph: nx.DiGraph, communities: List[List[str]], 
                         output_path: str = 'output/communities.png') -> None:
    """
    Visualize graph with communities.
    
    Parameters
    ----------
    graph : nx.DiGraph
        The graph to visualize
    communities : list of lists
        List of communities
    output_path : str
        Path to save the visualization
    """
    plt.figure(figsize=(14, 12))
    
    # Get positions
    pos = nx.spring_layout(graph, seed=42, k=0.9)
    
    # Create color map for communities
    colors = cm.rainbow(np.linspace(0, 1, len(communities)))
    
    # Draw each community with different color
    for i, community in enumerate(communities):
        nx.draw_networkx_nodes(graph, pos,
                              nodelist=community,
                              node_color=[colors[i]],
                              node_size=300,
                              alpha=0.8,
                              label=f'Community {i+1}')
    
    # Draw edges
    nx.draw_networkx_edges(graph, pos,
                          edge_color='gray',
                          alpha=0.2,
                          arrows=False)
    
    # Label community representatives
    labels = {}
    for i, community in enumerate(communities[:5]):  # Label first 5 communities
        if community:
            # Get the node with highest degree in community
            community_degrees = [(node, graph.degree(node)) for node in community]
            top_node = max(community_degrees, key=lambda x: x[1])[0]
            labels[top_node] = f"C{i+1}: {graph.nodes[top_node]['name'][:15]}..."
    
    nx.draw_networkx_labels(graph, pos, labels, font_size=9, font_weight='bold',
                           bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.title(f"Community Detection ({len(communities)} Communities)", fontsize=16, fontweight='bold')
    plt.legend(loc='upper left')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Community visualization saved to {output_path}")


def create_summary_plot(results: Dict[str, Any], output_path: str = 'output/summary.png') -> None:
    """
    Create a summary plot of analysis results.
    
    Parameters
    ----------
    results : dict
        Dictionary containing analysis results
    output_path : str
        Path to save the summary plot
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Top concepts by PageRank
    ax = axes[0, 0]
    top_pagerank = results.get('top_pagerank', [])
    if top_pagerank:
        names = [item[0] for item in top_pagerank[:8]]
        scores = [item[1] for item in top_pagerank[:8]]
        bars = ax.barh(range(len(names)), scores, color='#4285F4')
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels([n[:20] + '...' if len(n) > 20 else n for n in names])
        ax.invert_yaxis()
        ax.set_xlabel('PageRank Score')
        ax.set_title('Top Concepts by PageRank')
    
    # Plot 2: Top concepts by Betweenness
    ax = axes[0, 1]
    top_betweenness = results.get('top_betweenness', [])
    if top_betweenness:
        names = [item[0] for item in top_betweenness[:8]]
        scores = [item[1] for item in top_betweenness[:8]]
        bars = ax.barh(range(len(names)), scores, color='#34A853')
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels([n[:20] + '...' if len(n) > 20 else n for n in names])
        ax.invert_yaxis()
        ax.set_xlabel('Betweenness Centrality')
        ax.set_title('Top Concepts by Betweenness')
    
    # Plot 3: Community sizes
    ax = axes[1, 0]
    communities = results.get('communities', [])
    if communities:
        sizes = [len(comm) for comm in communities]
        colors = cm.rainbow(np.linspace(0, 1, len(sizes)))
        ax.bar(range(1, len(sizes) + 1), sizes, color=colors)
        ax.set_xlabel('Community ID')
        ax.set_ylabel('Number of Nodes')
        ax.set_title(f'Community Sizes (Total: {len(communities)})')
    
    # Plot 4: Graph statistics
    ax = axes[1, 1]
    ax.axis('off')
    stats = results.get('stats', {})
    if stats:
        stats_text = f"""Graph Statistics:
        
Nodes: {stats.get('Number of nodes', 'N/A')}
Edges: {stats.get('Number of edges', 'N/A')}
Density: {stats.get('Density', 0):.4f}
Avg Degree: {stats.get('Average degree', 0):.2f}
Connected: {stats.get('Is weakly connected', False)}
Communities: {len(communities)}"""
        
        ax.text(0.1, 0.5, stats_text, fontsize=12, 
                verticalalignment='center', fontfamily='monospace')
        ax.set_title('Graph Summary')
    
    plt.suptitle('Leonardo da Vinci Knowledge Graph - Analysis Summary', 
                fontsize=18, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Summary plot saved to {output_path}")