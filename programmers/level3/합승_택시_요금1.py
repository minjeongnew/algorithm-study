import sys
import heapq


def dijkstra(s, e):
    global graph, length
    # 방문한 노드를 최댓값으로 셋팅
    v = [sys.maxsize] * (length + 1)
    # start node는 0으로
    v[s] = 0
    # 우선순위 큐에 [cost, node]를 넣어준다
    hq = [[0, s]]
    heapq.heapify(hq)
    # bfs
    while hq:
        cost, node = heapq.heappop(hq)
        # 해당 노드를 방문하는데 드는 비용이 기존 최소 비용보다 큰 경우 무시
        if cost > v[node]:
            continue
        # 그 다음 방문 가능한 노드 탐색하기
        for g in graph[node]:
            new_node, new_cost = g
            # 기존 비용에 cost를 추가해 new cost
            new_cost += cost
            # 만약 새로운 비용이 기존 방문 노드를 방문하는데
            # 드는 비용이 작을 경우에만 진행
            if new_cost < v[new_node]:
                v[new_node] = new_cost
                heapq.heappush(hq, [new_cost, new_node])
    return v[e]


def solution(n, s, a, b, fares):
    global graph, length
    answer = sys.maxsize
    length = n + 1
    graph = [[] for _ in range(n+1)]
    for i, j, v in fares:
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