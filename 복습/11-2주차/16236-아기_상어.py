# gold 4
import sys
from collections import deque
from pprint import pprint


n = int(sys.stdin.readline())
shark_size = 2
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark_x, shark_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(shark_x, shark_y):
    q = deque()
    q.append((shark_x, shark_y, 0))
    v = [[-1]*n for _ in range(n)]
    v[shark_x][shark_y] = 0
    graph[shark_x][shark_y] = 0
    min_distance = float('inf')
    fishes = []
    while q:
        x, y, dist = q.popleft()
        for k in range(4):
            nx = x + directions[k][0]
            ny = y + directions[k][1]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                v[nx][ny] = 1
                if 0 < graph[nx][ny] < shark_size:
                    min_distance = dist
                    fishes.append((dist + 1, nx, ny))
                if dist + 1 <= min_distance:
                    q.append((nx, ny, dist + 1))

    if fishes:
        fishes.sort()
        print(fishes)
        return fishes[0]
    else:
        return -1

cnt = 0
time = 0
while True:
    result = bfs(shark_x, shark_y)
    if result == -1:
        break
    time += result[0]
    shark_x, shark_y = result[1], result[2]
    graph[shark_x][shark_y] = 0
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(time)