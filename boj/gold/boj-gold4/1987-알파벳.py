import sys
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
q = deque()
q.append([0, 0, graph[0][0]])
answer = 0
while q:
    x, y, a = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in a:
            q.append([nx, ny, a+graph[nx][ny]])
            answer = max(answer, len(a)+1)
print(answer)