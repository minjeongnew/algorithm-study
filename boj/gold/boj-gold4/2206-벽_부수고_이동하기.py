import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 모든 벽(0)에 대해서 최단 경로의 경우의 수를 구함 -> 시간 초과
# v[x][y][w] -> w 이 0 인 경우 -> 벽을 뚫은 상태,
# 1 이면 벽을 뚫을 수 있음
# bfs를 돌면서 벽을 뚫을 수 있고 벽이라면 벽을 뚫고 +1 한다
# 아직 방문하지 않고 벽이 아니라면 +1


def bfs(graph):
    q = deque()
    q.append([0, 0, 1])
    v = [[[0] * 2 for _ in range(m)] for x in range(n)]
    v[0][0][1] = 1
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return v[x][y][w]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1:
                    v[nx][ny][0] = v[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and v[nx][ny][w] == 0:
                    q.append([nx, ny, w])
                    v[nx][ny][w] = v[x][y][w] + 1
    return -1


graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(bfs(graph))