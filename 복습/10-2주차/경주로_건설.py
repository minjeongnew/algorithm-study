from collections import deque

# 0: 아래, 1: 오른쪽, 2: 위, 3: 왼쪽
d = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def bfs(graph, start):
    x, y, head, cost = start
    n = len(graph)
    v = [[float('inf')]*n for _ in range(n)]
    v[x][y] = 0
    q = deque()
    q.append(start)
    while q:
        a, b, head, cost = q.popleft()
        for k in range(4):
            nx = a + d[k][0]
            ny = b + d[k][1]
            if k == head:
                new_cost = cost + 100
            else:
                new_cost = cost + 600
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and v[nx][ny] > new_cost:
                v[nx][ny] = new_cost
                q.append((nx, ny, k, new_cost))
    # print(v)
    return v[-1][-1]


def solution(graph):
    return min(bfs(graph, (0, 0, 0, 0)), bfs(graph, (0, 0, 1, 0)))


if __name__ == "__main__":
    graph = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    print(solution(graph))