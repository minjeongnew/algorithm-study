import sys
import heapq


V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = {node: {} for node in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w


def dijkstra(start):
    distances = {node: float('inf') for node in range(1, V+1)}
    distances[start] = 0
    hq = []
    heapq.heappush(hq, [distances[start], start])

    while hq:
        current_distance, current_destination = heapq.heappop(hq)
        if current_distance > distances[current_destination]:
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(hq, [distance, new_destination])
    return distances

answer = dijkstra(k)
for i in range(1, V+1):
    if answer[i] == float('inf'):
        print('INF')
    else:
        print(answer[i])