import networkx as nx
import random
import matplotlib.pyplot as plt
from tabulate import tabulate
from dijkstra import dijkstra


# Створюємо порожній граф
G = nx.Graph()

# Додаємо вершини до графу
G.add_nodes_from(range(1, 10))

# Додаємо ребра до графу з вагами від 5 до 9
for u in range(1, 10):
    for v in range(u + 1, 10):
        weight = random.randint(5, 9)
        G.add_edge(u, v, weight=weight)

# Виводимо результати у вигляді таблиці
results = []
results.append(["", ""])
results.append(["Кількість вершин:", G.number_of_nodes()])
results.append(["Кількість ребер:", G.number_of_edges()])

degree_table = []
for node in G.nodes:
    degree_table.append(["Ступінь вершини", node, G.degree[node]])
results.extend(degree_table)

weight_table = []
for u, v, data in G.edges(data=True):
    weight_table.append(["Вага ребра", f"({u}, {v})", data["weight"]])
results.extend(weight_table)

print(tabulate(results, headers=["", "", ""], tablefmt="pipe"))

print("==" * 20 + "Завдання 2" + "==" * 20)
# Виконуємо DFS
dfs_path = list(nx.dfs_preorder_nodes(G, source=1))

# Виконуємо BFS
bfs_path = list(nx.bfs_tree(G, source=1))

# Виводимо результати
print("DFS шлях:", dfs_path)
print("BFS шлях:", bfs_path)

print("==" * 20 + "Завдання 3" + "==" * 20)

# Знаходимо найкоротші шляхи від кожної вершини до всіх інших
shortest_paths = {}
for node in G.nodes:
    shortest_paths[node] = dijkstra(G, node)

# Формуємо таблицю матриці найкоротших шляхів
table = []
header = [""] + list(G.nodes)  # Створюємо заголовок таблиці

for i, node in enumerate(G.nodes):
    row = [node]
    for j, target in enumerate(G.nodes):
        if node != target:
            distance = shortest_paths[node][target]
            row.append(distance)
        else:
            row.append(0)  # Встановлюємо 0 на діагоналі
    table.append(row)

# Виводимо таблицю з відповідним форматуванням
table_str = tabulate(table, headers=header, tablefmt="grid")

# Відокремлюємо перший рядок і перший стовпець порожнім символом
table_lines = table_str.split("\n")
table_lines[0] = (
    table_lines[0][:6] + "|" + table_lines[0][6:]
)  # Відокремлюємо перший рядок

for i in range(1, len(table_lines)):
    table_lines[i] = (
        table_lines[i][:6] + "|" + table_lines[i][6:]
    )  # Відокремлюємо перший стовпець

# Об'єднуємо рядки таблиці знову
table_str = "\n".join(table_lines)

print(table_str)


# Виводимо графік
pos = nx.spring_layout(G)  # Визначаємо позиції вершин для відображення графа
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    node_color="lightblue",
    edge_color="gray",
    width=1,
    alpha=0.7,
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
