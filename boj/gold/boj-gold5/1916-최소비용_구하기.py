import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = {i:{} for i in range(1, n+1)}
for _ in range(m):
    a, b, v = map(int, sys.stdin.readline().split())
    graph[a][b] = v
a, b = map(int, sys.stdin.readline().split())

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    hq = []
    heapq.heappush(hq, [distances[start], start])
    while hq:
        current_distance, current_node = heapq.heappop(hq)

        if distances[current_node] < current_distance:
            continue
        for new_node, new_distance in graph[current_node].items():
            distance = new_distance + current_distance
            if distances[new_node] > distance:
                distances[new_node] = distance
                heapq.heappush(hq, [distance, new_node])
    return distances[b]
print(dijkstra(graph, a))




