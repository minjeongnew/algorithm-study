import sys


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c = map(int, sys.stdin.readline().split())
graph = [list(map(lambda x:ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(r)]
v = [0] * 26


def dfs(x, y, cnt):
    global answer
    answer = answer if answer > cnt else cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c and v[graph[nx][ny]] == 0:
            v[graph[nx][ny]] = 1
            dfs(nx, ny, cnt+1)
            v[graph[nx][ny]] = 0

answer = 0
v[graph[0][0]] = 1
dfs(0, 0, 1)
print(answer)
