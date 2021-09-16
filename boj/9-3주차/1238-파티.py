import sys
import heapq


n, m, x = map(int, sys.stdin.readline().split())
graph = {node: {} for node in range(1, n+1)}
for _ in range(m):
    a, b, v = map(int, sys.stdin.readline().split())
    graph[a][b] = v


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    hq = []
    heapq.heappush(hq, (distances[start], start))

    while hq:
        current_distance, current_node = heapq.heappop(hq)
        if distances[current_node] < current_distance:
            continue
        for new_node, new_distance in graph[current_node].items():
            distance = new_distance + distances[current_node]
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(hq, (distance, new_node))

    return distances


x_party = dijkstra(graph, x)
answer = 0
for node in graph:
    if node != x:
        tmp = dijkstra(graph, node)
        # print(node, tmp)
        if answer < tmp[x] + x_party[node]:
            answer = tmp[x] + x_party[node]
print(answer)