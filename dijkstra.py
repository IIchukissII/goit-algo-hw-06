import heapq


def dijkstra(graph, source):
    distances = {node: float("inf") for node in graph.nodes}
    distances[source] = 0
    queue = [(0, source)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = (
                current_distance + weight["weight"]
            )  # Отримати значення ваги з словника weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
