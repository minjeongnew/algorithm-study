import heapq
import sys


def dijkstra(s, e):
    global graph, length
    v = [sys.maxsize] * (length + 1)
    v[s] = 0 # start node의 cost 0으로 설정하기
    hq = [[0, s]] # [cost, node]
    heapq.heapify(hq)
    while hq:
        cost, node = heapq.heappop(hq)
        if v[node] < cost:
            continue
        for g in graph[node]:
            new_node, new_cost = g
            new_cost += cost
            if new_cost < v[new_node]:
                v[new_node] = new_cost
                heapq.heappush(hq, [new_cost, new_node])
    return v[e]


def solution(n, s, a, b, fares):
    global graph, length
    length = n + 1
    graph = [[] for _ in range(n+1)]
    for i, j, c in fares:
        graph[i].append([j, c]) # [node, cost]
        graph[j].append([i, c])
    answer = sys.maxsize
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return answer


if __name__ == '__main__':
    n, s, a, b = 6, 4, 6, 2
    f = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, f))