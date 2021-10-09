# gold5
import sys
from collections import deque


dx = [-1, 0, 1, 0] # 위 0 오른쪽 1 아래 2 왼쪽 3
dy = [0, 1, 0, -1]


def direction_change(d, c):
    if c == "L":
        d = (d-1) % 4
    elif c == "D":
        d = (d+1) % 4
    return d


def solve():
    time = 1
    x, y = 0, 0
    v = deque()
    v.append((x, y))
    board[x][y] = 2
    direction = 1 # 오른쪽
    while True:
        x += dx[direction]
        y += dy[direction]
        if 0 <= x < n and 0 <= y < n and board[x][y] != 2:
            if board[x][y] == 0: # 사과 아닌 그냥 빈칸
                tail_x, tail_y = v.popleft()
                board[tail_x][tail_y] = 0
            board[x][y] = 2
            v.append((x, y))
            if time in times:
                direction = direction_change(direction, times[time])
            time += 1
        else: # 벽 또는 자기 몸통
            return time

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    board = [[0]*n for _ in range(n)]
    k = int(sys.stdin.readline())
    for _ in range(k):
        r, c = map(int, sys.stdin.readline().split())
        board[r-1][c-1] = 1
    l = int(sys.stdin.readline())
    times = dict()
    for _ in range(l):
        x, c = map(str, sys.stdin.readline().split())
        times[int(x)] = c

    print(solve())