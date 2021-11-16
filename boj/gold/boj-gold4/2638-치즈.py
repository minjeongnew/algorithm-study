from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
len_cheese = 0
for x in graph:
    len_cheese += x.count(1)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check_4_sides(x, y):
    answer = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0: # 공기와 맞닿아있는면
                answer += 1
    return answer

from pprint import pprint
time = 0
q = deque()
q.append((0, 0))
while True:
    nq = deque()
    time += 1
    flag = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = -1
                    q.append((nx, ny))
                elif graph[nx][ny] > 0:
                    flag = False
                    graph[nx][ny] += 1
                    if graph[nx][ny] > 2:
                        nq.append((nx, ny))
                        graph[nx][ny] = -1
    # pprint(graph)
    q = nq
    if flag:
        break
print(time-1)

# 5 5
# 0 0 0 0 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 0 0 0 0