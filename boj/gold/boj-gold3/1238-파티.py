import sys, heapq
# 다익스트라로 풀기


n, m, x = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a in graph:
        graph[a].append((b, c))
    else:
        graph[a] = [(b, c)]


def dijkstra(start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    hq = []
    heapq.heappush(hq, [distances[start], start])

    while hq:
        current_distance, current_destination = heapq.heappop(hq)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(hq, [distance, new_destination])

    return distances


dest = x
party = dijkstra(dest)
tmp = [dijkstra(i) for i in range(1, n+1)]
max_ = 0
for idx, start in enumerate(tmp):
    if idx != dest-1:
        max_ = max(max_, party[idx+1] + start[dest])
print(max_)
