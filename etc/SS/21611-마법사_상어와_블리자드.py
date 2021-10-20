from pprint import pprint
from collections import deque


# 상어 위치: (n//2, n//2)
directions = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ds = [list(map(int, input().split())) for _ in range(m)]
shark_x = (n+1)//2 -1
shark_y = (n+1)//2 -1
number = []
indexing = {}
index_board = [[0]*n for _ in range(n)]
# 번호 매기기
def init():
    # 왼쪽, 아래 // 오른쪽 위
    sx = shark_x
    sy = shark_y
    tmp_d = {1: (0, -1), 2: (1, 0), 3: (0, 1), 0: (-1, 0)}
    d = 1
    idx = 1
    depth = 1
    cnt = 0
    while sx > -1 and sy > -1:
        indexing[idx] = (sx, sy)
        index_board[sx][sy] = idx
        sx += tmp_d[d][0]
        sy += tmp_d[d][1]
        idx += 1
        cnt += 1
        if cnt == depth:
            if d in [0, 2]:
                depth += 1
            d = (d+1) % 4
            cnt = 0


def blizzard(d, s):
    # s: 거리
    global board
    dx, dy = directions[d]
    for i in range(1, s+1):
        nx = shark_x + dx*i
        ny = shark_y + dy*i
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny]:
                board[nx][ny] = 0

def move():
    global board
    start = 2 # 1번 인덱스는 상어니까
    end = 3
    while start < n*n and end <= n*n:
        while start < n*n:
            sx, sy = indexing[start]
            if board[sx][sy] == 0:
                break
            start += 1
        else:
            return
        if end <= start:
            end = start + 1
        while end <= n*n:
            ex, ey = indexing[end]
            if board[ex][ey]:
                break
            end += 1
        else:
            return
        board[sx][sy] = board[ex][ey]
        board[ex][ey] = 0


exploded_marbles = [0]*3
def explode():
    global board
    need_move = False
    start = 2
    end = 3
    same_cnt = 1
    while start < n*n and end <= n*n:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if board[sx][sy] == board[ex][ey]:
            same_cnt += 1
            end += 1
        else:
            if same_cnt >= 4:
                need_move = True
                for i in range(start, end):
                    bx, by = indexing[i]
                    exploded_marbles[board[bx][by]-1] += 1
                    board[bx][by] = 0
            same_cnt = 1
            start = end
            end = start + 1
    return need_move


def change():
    global board
    new_board = [[0]*n for _ in range(n)]
    start = 2
    end = 3
    same = 1
    idx = 2
    # A: 구슬 개수, B: 구슬 번호
    while start < n*n and end <= n*n:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if board[sx][sy] == board[ex][ey]:
            same += 1
            end += 1
        else:
            ix, iy = indexing[idx]
            new_board[ix][iy] = same
            ix, iy = indexing[idx+1]
            new_board[ix][iy] = board[sx][sy]
            idx += 2
            same = 1
            start = end
            end = start + 1
        if idx > n*n:
            break
    board = new_board


init()
# pprint(board)
# pprint(indexing)
for x in ds:
    d, s = x
    d -= 1
    blizzard(d, s)
    move()
    while explode():
        move()
        # pprint(board)
        # print(exploded_marbles)
    change()
    # pprint(board)
# print(exploded_marbles)
print(exploded_marbles[0]+2*exploded_marbles[1]+3*exploded_marbles[2])