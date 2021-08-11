import heapq
import sys


def dijkstra(graph, s):
    hq = [[0, s]] # [cost, start_node]
    v = {node: sys.maxsize for node in graph}
    v[s] = 0
    heapq.heapify(hq)
    while hq:
        cost, node = heapq.heappop(hq)
        if cost > v[node]:
            continue
        for new_node, new_cost in graph[node].items():
            new_cost += cost
            if new_cost < v[new_node]:
                v[new_node] = new_cost
                heapq.heappush(hq, [new_cost, new_node])
    return v


if __name__ == '__main__':
    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }
    print(dijkstra(graph, 'A'))