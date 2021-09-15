import sys
from collections import deque
from pprint import pprint


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().split())
coins = []
v = [[[[0]*m for _ in range(n)] for __ in range(m)] for ___ in range(n)]
# pprint(v)
board = []
for i in range(n):
    board.append( list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if board[i][j] == 'o':
            coins.append((i, j))


def visitable(x, y):
    return 0 <= x < n and 0 <= y < m


# print(coins)
q = deque()
q.append([coins[0], coins[1], 1])


def bfs():
    while q:
        c1, c2, cnt = q.popleft()
        if cnt > 10:
            break
        for k in range(4):
            nc1x = c1[0] + dx[k]
            nc1y = c1[1] + dy[k]
            nc2x = c2[0] + dx[k]
            nc2y = c2[1] + dy[k]
            if not visitable(nc1x, nc1y) and not visitable(nc2x, nc2y):
                continue
            if (not visitable(nc1x, nc1y) and visitable(nc2x, nc2y)) or (visitable(nc1x, nc1y) and not visitable(nc2x, nc2y)):
                return cnt
            if board[nc1x][nc1y] == '#':
                nc1x = c1[0]
                nc1y = c1[1]
            if board[nc2x][nc2y] == '#':
                nc2x = c2[0]
                nc2y = c2[1]
            if not v[nc1x][nc1y][nc2x][nc2y]:
                v[nc1x][nc1y][nc2x][nc2y] = 1
                q.append([(nc1x, nc1y), (nc2x, nc2y), cnt+1])
    return -1

# pprint(board)
print(bfs())