import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
graph = []
q = deque() # bfs 를 위한
v = [] # 방문 기록 체크
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j
q.append((rx, ry, bx, by, 0)) # rx, ry, bx, by, depth
v.append((rx, ry, bx, by))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move(x, y, dx, dy):
    cnt = 0 # 빨간구슬과 파란구슬이 한 번 기울였을 때 몇 칸 움직이는지
    # 다음 움직일 칸이 벽이면 안되고 현재 위치한 칸이 구멍이 아닐 경우
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs():
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        if graph[bx][by] != 'O':
            if graph[rx][ry] == 'O':
                print(depth)
                return
            for i in range(4):
                nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
                nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in v:
                    q.append((nrx, nry, nbx, nby, depth+1))
                    v.append((nrx, nry, nbx, nby))
    print(-1)
bfs()