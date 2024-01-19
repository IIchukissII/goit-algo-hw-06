import networkx as nx

# Створюємо граф
G = nx.Graph()

# Додаємо вершини до графу
G.add_nodes_from(range(1, 10))

# Додаємо ребра до графу
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 5)
G.add_edge(2, 6)
G.add_edge(3, 7)
G.add_edge(4, 8)
G.add_edge(4, 9)

# Виконуємо DFS
dfs_path = list(nx.dfs_preorder_nodes(G, source=1))

# Виконуємо BFS
bfs_path = list(nx.bfs_tree(G, source=1))

# Виводимо результати
print("DFS шлях:", dfs_path)
print("BFS шлях:", bfs_path)
