import sys
from collections import deque


def bfs(graph):
    m, n = len(graph[0]), len(graph)
    v = [[-1]*(m+1) for _ in range(n+1)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and v[i][j] == -1:
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if graph[nx][ny] == 1 and v[nx][ny] == -1:
                            q.append((nx, ny))
                            v[nx][ny] = 1
                answer += 1
    return answer


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    board = [[0]*(m+1) for _ in range(n+1)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1
    print(bfs(board))

