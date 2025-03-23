import matplotlib.pyplot as plt
import networkx as nx
import time


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def add_edges(graph, node, pos, x=0, y=0, layer=1, spacing=1.5):
    """ Adiciona nós e arestas ao grafo para visualização """
    if node is not None:
        graph.add_node(node.val, pos=(x, y))
        if node.left:
            graph.add_edge(node.val, node.left.val)
            add_edges(graph, node.left, pos, x - spacing / layer, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            add_edges(graph, node.right, pos, x + spacing / layer, y - 1, layer + 1)


def draw_tree(root, path=[]):
    """ Desenha a árvore binária e destaca o caminho do percurso """
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, root, pos)

    plt.figure(figsize=(8, 5))
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="lightgray", edge_color="black")

    # Destaca o percurso in-order
    for i, val in enumerate(path):
        nx.draw_networkx_nodes(graph, pos, nodelist=[val], node_color="red")
        plt.title(f"Percorrendo: {val}")
        plt.pause(0.5)  # Tempo de pausa para visualizar cada nó
        plt.clf()
        nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="lightgray", edge_color="black")
        nx.draw_networkx_nodes(graph, pos, nodelist=path[:i + 1], node_color="red")

    # Exibe o caminho in-order na tela
    caminho_str = " ".join(map(str, path))
    plt.title("Caminho em ordem")
    plt.text(0, -1.5, caminho_str, fontsize=12, ha='center', bbox=dict(facecolor='white', edgecolor='black'))
    plt.show()


def in_order_traversal(root, path):
    """ Percorre a árvore em ordem e registra o caminho """
    if root:
        in_order_traversal(root.left, path)
        path.append(root.val)
        in_order_traversal(root.right, path)


# Criando a árvore binária
root = Node(55)
root.left = Node(30)
root.right = Node(80)
root.left.left = Node(20)
root.left.right = Node(35)
root.right.right = Node(90)
root.left.right.right = Node(45)
root.left.right.left = Node(32)

# Obtendo o percurso in-order
path = []
in_order_traversal(root, path)

# Desenhando a árvore e mostrando o percurso
draw_tree(root, path)
