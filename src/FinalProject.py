"""
Leonardo da Vinci Knowledge Graph: Mapping the Connections in His Notebooks
====================================
This project combines history, art, and computer science through graph theory.

| Author: Stefany Simplicio
| Date: 2025 December 02
"""


from leonardo_kg import LeonardoKnowledgeGraph
import matplotlib.pyplot as plt

def main():
    """Função principal para demonstrar a implementação inicial."""
    
    # Criar grafo
    kg = LeonardoKnowledgeGraph()
    
    # Carregar dados
    print("=== Carregando dados do Leonardo da Vinci ===")
    kg.load_concepts('data/leonardo_concepts.csv')
    kg.load_relationships('data/relationships.csv')
    
    # Estatísticas básicas
    print("\n=== Estatísticas do Grafo ===")
    stats = kg.get_basic_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Visualização básica
    print("\n=== Gerando visualização inicial ===")
    
    # Layout do grafo
    pos = nx.spring_layout(kg.graph, seed=42)
    
    # Cores por categoria
    category_colors = {
        'Arte': 'red',
        'Engenharia': 'blue', 
        'Anatomia': 'green',
        'Ciência': 'orange',
        'Matemática': 'purple',
        'Filosofia': 'brown'
    }
    
    # Plotar
    plt.figure(figsize=(12, 10))
    
    for category, color in category_colors.items():
        nodes = [n for n, attr in kg.graph.nodes(data=True) 
                if attr.get('category') == category]
        nx.draw_networkx_nodes(kg.graph, pos, 
                              nodelist=nodes,
                              node_color=color,
                              label=category,
                              node_size=500,
                              alpha=0.8)
    
    nx.draw_networkx_edges(kg.graph, pos, 
                          edge_color='gray',
                          alpha=0.5,
                          arrows=True,
                          arrowsize=10)
    
    # Labels dos nós
    labels = {node: attr['name'] for node, attr in kg.graph.nodes(data=True)}
    nx.draw_networkx_labels(kg.graph, pos, labels, font_size=8)
    
    plt.title("Grafo de Conhecimento de Leonardo da Vinci - Visualização Inicial")
    plt.legend(scatterpoints=1)
    plt.axis('off')
    plt.tight_layout()
    
    # Salvar figura
    plt.savefig('output/initial_graph.png', dpi=300, bbox_inches='tight')
    print("Visualização salva em 'output/initial_graph.png'")
    
    # Mostrar 10 conceitos com maior grau
    print("\n=== Top 10 Conceitos por Grau ===")
    degrees = dict(kg.graph.degree())
    sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:10]
    
    for node, degree in sorted_degrees:
        node_data = kg.graph.nodes[node]
        print(f"{node_data['name']} ({node_data['category']}): Grau {degree}")

if __name__ == "__main__":
    main()
