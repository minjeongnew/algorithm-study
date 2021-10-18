import sys
from collections import deque


d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n, m, energy = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
passenger_departure = dict()
taxi_x, taxi_y = map(int, sys.stdin.readline().split())
taxi_x -= 1
taxi_y -= 1
for _ in range(m):
    px, py, dx, dy = map(int, sys.stdin.readline().split())
    passenger_departure[(px-1, py-1)] = (dx-1, dy-1)


def bfs1(start_x, start_y):
    q = deque()
    q.append((start_x, start_y, 0)) # 시작x, 시작y, 거리
    v = [[0]*n for _ in range(n)]
    v[start_x][start_y] = 1
    dist_list = []
    min_dist = float('inf')
    if (start_x, start_y) in passenger_departure:
        return (0, start_x, start_y)
    while q:
        x, y, distance = q.popleft()
        # print(x, y, dist)
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) in passenger_departure and (nx, ny) == (start_x, start_y):
                    dist_list.append((0, nx, ny))
                    v[nx][ny] = 1
                    return (0, nx, ny)
                if v[nx][ny] == 0 and board[nx][ny] != 1:
                    v[nx][ny] = 1
                    if (nx, ny) in passenger_departure.keys():
                        min_dist = distance
                        dist_list.append((distance+1, nx, ny))
                    if distance + 1 <= min_dist:
                        q.append((nx, ny, distance+1))

    if dist_list:
        dist_list.sort()
        return dist_list[0]
    return 0


def bfs2(passenger_x, passenger_y):
    departure_x, departure_y = passenger_departure[(passenger_x, passenger_y)]
    q = deque()
    q.append((passenger_x, passenger_y))  # 시작x, 시작y, 거리
    v = [[-1] * n for _ in range(n)]
    v[passenger_x][passenger_y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == -1 and board[nx][ny] != 1:
                v[nx][ny] = v[x][y] + 1
                q.append((nx, ny))
                if (nx, ny) == (departure_x, departure_y):
                    return (v[nx][ny], departure_x, departure_y)
    if v[departure_x][departure_y] == -1:
        return 0

def solve(m, sx, sy, energy):
    while m:
        m -= 1
        tmp = bfs1(sx, sy)
        if tmp == 0:
            return -1
        dist, nnx, nny = tmp
        # print('dist, nx, ny', dist, nnx, nny)
        energy -= dist
        # print(energy)
        if energy < 0:
            return -1
        tmp2 = bfs2(nnx, nny)
        if tmp2 == 0:
            return -1
        dist2, ddx, ddy = tmp2
        # print('dist2, dx, dy', dist2, ddx, ddy)
        energy -= dist2
        # print(energy)
        if energy < 0:
            return -1
        energy += (dist2*2)
        sx, sy = ddx, ddy
        del passenger_departure[(nnx, nny)]
        # print(energy)

    return energy
print(solve(m, taxi_x,taxi_y, energy))
