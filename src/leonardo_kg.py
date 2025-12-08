"""
Leonardo da Vinci Knowledge Graph Module
========================================
This module contains the main graph class for analyzing Leonardo's concepts.
"""

import networkx as nx
import pandas as pd
from typing import Dict, List, Tuple, Optional, Any
import community as community_louvain  # python-louvain


class LeonardoKnowledgeGraph:
    """
    A knowledge graph representing Leonardo da Vinci's interdisciplinary concepts.
    
    This class builds and analyzes a directed graph of concepts from
    Leonardo's notebooks, with methods for centrality analysis,
    community detection, and visualization.
    
    Attributes
    ----------
    graph : nx.DiGraph
        The directed graph containing concepts and relationships
    """
    
    def __init__(self):
        """Initialize an empty directed graph."""
        self.graph = nx.DiGraph()
        print("Leonardo Knowledge Graph initialized")
    
    def load_concepts(self, filepath: str) -> None:
        """
        Load concepts from a CSV file and add them as nodes.
        
        Parameters
        ----------
        filepath : str
            Path to the CSV file containing concepts.
            Expected columns: id, name, category, description
        """
        try:
            df = pd.read_csv(filepath)
            
            for _, row in df.iterrows():
                self.graph.add_node(
                    row['id'],
                    name=row['name'],
                    category=row['category'],
                    description=row['description']
                )
            print(f"Loaded {len(df)} concepts from {filepath}")
        except FileNotFoundError:
            print(f"Error: File {filepath} not found")
            raise
    
    def load_relationships(self, filepath: str) -> None:
        """
        Load relationships from a CSV file and add them as edges.
        
        Parameters
        ----------
        filepath : str
            Path to the CSV file containing relationships.
            Expected columns: source, target, relationship, weight
        """
        try:
            df = pd.read_csv(filepath)
            
            for _, row in df.iterrows():
                self.graph.add_edge(
                    row['source'],
                    row['target'],
                    relationship=row['relationship'],
                    weight=row['weight']
                )
            print(f"Loaded {len(df)} relationships from {filepath}")
        except FileNotFoundError:
            print(f"Error: File {filepath} not found")
            raise
    
    def get_basic_stats(self) -> Dict[str, Any]:
        """
        Get basic statistics about the graph.
        
        Returns
        -------
        dict
            Dictionary containing graph statistics
        """
        stats = {
            "Number of nodes": self.graph.number_of_nodes(),
            "Number of edges": self.graph.number_of_edges(),
            "Density": nx.density(self.graph),
            "Is directed": nx.is_directed(self.graph),
            "Number of weakly connected components": nx.number_weakly_connected_components(self.graph),
        }
        
        # Calculate average degree
        if self.graph.number_of_nodes() > 0:
            degrees = [d for _, d in self.graph.degree()]
            stats["Average degree"] = sum(degrees) / len(degrees)
        
        # Check connectivity
        if nx.is_directed(self.graph):
            stats["Is weakly connected"] = nx.is_weakly_connected(self.graph)
        
        return stats
    
    def calculate_degree_centrality(self) -> Dict[str, float]:
        """
        Calculate degree centrality for all nodes.
        
        Returns
        -------
        dict
            Dictionary mapping node ID to degree centrality score
        """
        return nx.degree_centrality(self.graph)
    
    def calculate_betweenness_centrality(self) -> Dict[str, float]:
        """
        Calculate betweenness centrality for all nodes.
        
        Returns
        -------
        dict
            Dictionary mapping node ID to betweenness centrality score
        """
        return nx.betweenness_centrality(self.graph, normalized=True)
    
    def calculate_closeness_centrality(self) -> Dict[str, float]:
        """
        Calculate closeness centrality for all nodes.
        
        Returns
        -------
        dict
            Dictionary mapping node ID to closeness centrality score
        """
        return nx.closeness_centrality(self.graph)
    
    def calculate_pagerank(self, alpha: float = 0.85) -> Dict[str, float]:
        """
        Calculate PageRank for all nodes.
        
        Parameters
        ----------
        alpha : float, optional
            Damping parameter (default=0.85)
            
        Returns
        -------
        dict
            Dictionary mapping node ID to PageRank score
        """
        return nx.pagerank(self.graph, alpha=alpha)
    
    def detect_communities(self, method: str = 'louvain') -> List[List[str]]:
        """
        Detect communities in the graph.
        
        Parameters
        ----------
        method : str, optional
            'louvain' or 'greedy' (default='louvain')
            
        Returns
        -------
        list of lists
            List of communities, each containing node IDs
        """
        if method == 'louvain':
            try:
                # Convert to undirected for Louvain
                undirected_graph = self.graph.to_undirected()
                partition = community_louvain.best_partition(undirected_graph)
                
                # Organize nodes by community
                communities_dict = {}
                for node, community_id in partition.items():
                    if community_id not in communities_dict:
                        communities_dict[community_id] = []
                    communities_dict[community_id].append(node)
                
                return list(communities_dict.values())
            except Exception as e:
                print(f"Louvain method failed: {e}. Falling back to greedy modularity.")
                return self.detect_communities('greedy')
        
        elif method == 'greedy':
            # Greedy modularity communities
            undirected_graph = self.graph.to_undirected()
            communities = list(nx.algorithms.community.greedy_modularity_communities(
                undirected_graph))
            return [list(community) for community in communities]
    
    def find_shortest_path(self, source: str, target: str) -> Optional[List[str]]:
        """
        Find shortest path between two nodes.
        
        Parameters
        ----------
        source : str
            Source node ID
        target : str
            Target node ID
            
        Returns
        -------
        list or None
            List of node IDs in the path, or None if no path exists
        """
        try:
            return nx.shortest_path(self.graph, source=source, target=target)
        except nx.NetworkXNoPath:
            return None
    
    def calculate_mst(self) -> List[Tuple[str, str]]:
        """
        Calculate Minimum Spanning Tree (MST) for the graph.
        
        Returns
        -------
        list of tuples
            List of edges in the MST
        """
        # Convert to undirected and use weights
        undirected_graph = nx.Graph()
        for u, v, data in self.graph.edges(data=True):
            undirected_graph.add_edge(u, v, weight=data.get('weight', 1.0))
        
        mst = nx.minimum_spanning_tree(undirected_graph)
        return list(mst.edges())
    
    def get_node_info(self, node_id: str) -> Dict[str, Any]:
        """
        Get information about a specific node.
        
        Parameters
        ----------
        node_id : str
            Node ID
            
        Returns
        -------
        dict
            Dictionary with node information
        """
        if node_id not in self.graph:
            raise ValueError(f"Node {node_id} not found in graph")
        
        info = self.graph.nodes[node_id].copy()
        info['degree'] = self.graph.degree(node_id)
        info['in_degree'] = self.graph.in_degree(node_id)
        info['out_degree'] = self.graph.out_degree(node_id)
        info['neighbors'] = list(self.graph.neighbors(node_id))
        
        return info
    
    def export_to_gexf(self, filepath: str) -> None:
        """
        Export the graph to GEXF format for external visualization.
        
        Parameters
        ----------
        filepath : str
            Path where to save the GEXF file
        """
        nx.write_gexf(self.graph, filepath)
        print(f"Graph exported to {filepath}")