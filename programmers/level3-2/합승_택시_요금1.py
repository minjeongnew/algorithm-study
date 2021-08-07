import heapq
import sys


def dijkstra(s, e):
    global graph, length
    v = [sys.maxsize] * (length+1)
    # cost와 노드 번호
    hq = [[0, s]]
    v[s] = 0
    heapq.heapify(hq)
    # bfs
    while hq:
        cost, node = heapq.heappop(hq)
        # 해당 노드를 방문하는데 기존 노드 방문 비용보다 크다면 무시
        if cost > v[node]:
            continue
        # 다음 방문 가능한 노드 찾기
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
    answer = sys.maxsize
    graph = [[] for _ in range(n+1)]
    for i, j, v in fares:
        # [node, v]
        graph[i].append([j, v])
        graph[j].append([i, v])
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return answer


if __name__ == '__main__':
    n, s, a, b = 6, 4, 6, 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))
    f2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    print(solution(7, 3, 4, 1, f2))