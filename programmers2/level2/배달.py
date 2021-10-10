import heapq


def solution(N, road, K):
    edges = {x+1: dict() for x in range(N)}
    for n1, n2, w in road:
        if n1 in edges[n2]:
            edges[n2][n1] = min(edges[n2][n1], w)
        else:
            edges[n2][n1] = w
        if n2 in edges[n1]:
            edges[n1][n2] = min(edges[n1][n2], w)
        else:
            edges[n1][n2] = w
    distances = {x+1: float('inf') for x in range(N)}
    start = 1
    distances[start] = 0
    hq = [[0, 1]]
    heapq.heapify(hq)
    while hq:
        current_cost, current_node = heapq.heappop(hq)
        if current_cost > distances[current_node]:
            continue
        for next_node, next_node_link_cost in edges[current_node].items():
            next_node_link_cost += current_cost
            if next_node_link_cost < distances[next_node]:
                distances[next_node] = next_node_link_cost
                heapq.heappush(hq, [next_node_link_cost, next_node])
    # print(distances)
    answer =0
    for x in distances.values():
        if x <= K:
            answer += 1
    return answer
