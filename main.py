import networkx as nx
import random
import matplotlib.pyplot as plt
from tabulate import tabulate
from dijkstra import dijkstra

print("==" * 20 + "Завдання 1" + "==" * 20)

G = nx.Graph()

G.add_nodes_from(range(1, 10))

for u in range(1, 10):
    for v in range(u + 4, 10):
        weight = random.randint(5, 9)
        G.add_edge(u, v, weight=weight)

results = [["", ""], ["Кількість вершин:", G.number_of_nodes()], ["Кількість ребер:", G.number_of_edges()]]

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

dfs_path = list(nx.dfs_preorder_nodes(G, source=1))

bfs_path = list(nx.bfs_tree(G, source=1))

# результати
print("DFS шлях:", dfs_path)
print("BFS шлях:", bfs_path)

print("""\n Шляхи відрізняються, так як:\n\
- \033[1mПошук у глибину (DFS)\033[0m  виконується шляхом відвідування вершини, \
а потім рекурсивного відвідування всіх сусідніх вершин, які ще не були відвідані.\n
- \033[1mПошук у ширину (BFS)\033[0m відрізняється від DFS тим, що він відвідує всі вершини на певному рівні перед тим, \
  як перейти до наступного рівня. \n""")

print("==" * 20 + "Завдання 3" + "==" * 20)

# Знаходимо найкоротші шляхи від кожної вершини до всіх інших
shortest_paths = {}
for node in G.nodes:
    shortest_paths[node] = dijkstra(G, node)


table = []
header = [""] + list(G.nodes)

for i, node in enumerate(G.nodes):
    row = [node]
    for j, target in enumerate(G.nodes):
        if node != target:
            distance = shortest_paths[node][target]
            row.append(distance)
        else:
            row.append(0)  # Встановлюємо 0 на діагоналі
    table.append(row)


table_str = tabulate(table, headers=header, tablefmt="grid")

table_lines = table_str.split("\n")
table_lines[0] = table_lines[0][:6] + "+" + table_lines[0][6:]


for i in range(1, len(table_lines)):
    if i % 2 == 1:
        table_lines[i] = table_lines[i][:6] + "|" + table_lines[i][6:]
    else:
        table_lines[i] = table_lines[i][:6] + "+" + table_lines[i][6:]

table_str = "\n".join(table_lines)

print(table_str)

print("""\nВ даній таблиці наведено найкоротші шляхи від кожної вершини до всіх інших, де перший рядок і \
перша колонка індексуються вершиною, а в комірках на перетині - найкоротші шляхи знайдені за використанням\
алгоритму Dijkstra.\n""")


pos = nx.spring_layout(G, k=0.3, iterations=20)
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
