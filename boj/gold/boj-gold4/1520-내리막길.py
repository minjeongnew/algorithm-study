import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
v = [[-1]*m for _ in range(n)]


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if v[x][y] == -1:
        v[x][y] = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] < graph[x][y]:
                    v[x][y] += dfs(nx, ny)
    return v[x][y]

print(dfs(0, 0))