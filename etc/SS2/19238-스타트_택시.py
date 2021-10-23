from pprint import pprint
from collections import deque
n, m, energy = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1
customers = dict()
starts = []
destinations = []
for i in range(m):
    start_x, start_y, destination_x, destination_y = map(int, input().split())
    customers[(start_x-1, start_y-1)] = (destination_x-1, destination_y-1)
    board[start_x-1][start_y-1] = 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 가장 가까운 승객 찾기
def bfs1(sx, sy):
    q = deque()
    q.append((sx, sy, 0))
    v = [[0]*n for _ in range(n)]
    distance_list = []
    min_distance = float('inf')
    if (sx, sy) in customers.keys():
        return 0, sx, sy
    while q:
        x, y, distance = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and v[nx][ny] == 0:
                v[nx][ny] = 1
                if board[nx][ny] == 2:
                    min_distance = distance
                    distance_list.append((distance+1, nx, ny))
                if distance + 1 <= min_distance:
                    q.append((nx, ny, distance+1))
    if distance_list:
        distance_list.sort()
        return distance_list[0]
    else:
        return -1

# 목적지 거리
def bfs2(sx, sy):
    dest_x, dest_y = customers[(sx, sy)]
    q = deque()
    q.append((sx, sy, 0))
    v = [[0]*n for _ in range(n)]
    if sx == dest_x and sy == dest_y:
        return 0
    while q:
        x, y, dist = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and v[nx][ny] == 0:
                if nx == dest_x and ny == dest_y:
                    return dist+1, nx, ny
                q.append((nx, ny, dist+1))
                v[nx][ny] = 1
    return -1


for _ in range(m):
    result = bfs1(taxi_x, taxi_y)
    if result == -1:
        energy = -1
        break
    energy -= result[0]
    if energy < 0:
        energy = -1
        break
    taxi_x, taxi_y = result[1], result[2]
    board[taxi_x][taxi_y] = 0
    result2 = bfs2(taxi_x, taxi_y)
    if result2 == -1:
        energy = -1
        break
    energy -= result2[0]
    if energy < 0:
        energy = -1
        break
    energy += (result2[0]*2)
    del customers[(taxi_x, taxi_y)]
    taxi_x, taxi_y = result2[1], result2[2]
print(energy)