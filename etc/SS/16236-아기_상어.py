from collections import deque
from pprint import pprint


dx = [-1, 0, 1, 0] #
dy = [0, -1, 0, 1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
shark_size = 2
fish_cnt = 0
shark_x, shark_y = -1, -1
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark_x, shark_y = i, j
        if 1 <= board[i][j] <= 6:
            fish_cnt += 1

board[shark_x][shark_y] = 0
time = 0


def bfs(shark_x, shark_y):
    q = deque()
    q.append((shark_x, shark_y, 0))
    v = [[0]*n for _ in range(n)]
    v[shark_x][shark_y] = 1
    min_dist = float('inf')
    dist_list = []
    while q:
        x, y, dist = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                if board[nx][ny] <= shark_size:
                    v[nx][ny] = 1
                    if 0 < board[nx][ny] < shark_size:
                        min_dist = dist
                        dist_list.append((dist +1, nx, ny))
                    if dist + 1 <= min_dist:
                        q.append((nx, ny, dist+1))
    if dist_list:
        dist_list.sort()
        return dist_list[0] # 가장 가까운 물고기 거리, 그 다음 상어 위치 x, 그 다음 상어위치 y
    else:
        return 0

eat_cnt = 0
while fish_cnt:
    result = bfs(shark_x, shark_y)
    if result == 0:
        break
    shark_x, shark_y = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1
    if shark_size == eat_cnt:
        shark_size += 1
        eat_cnt = 0
    board[shark_x][shark_y] = 0
print(time)
