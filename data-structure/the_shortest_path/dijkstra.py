import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} # 양의 무한대
    distances[start] = 0 # 시작값은 0
    q = []
    heapq.heappush(q, [distances[start], start]) # 시작 노드부터 탐색을 시작하기 위함

    while q:
        # 탐색할 노드, 거리
        current_distance, current_destination = heapq.heappop(q)

        # 기존의 거리보다 크다면 무시
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])

    return distances


if __name__ == '__main__':
    # 출발 노드와 도착 노드
    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }
    print(dijkstra(graph, 'A'))
