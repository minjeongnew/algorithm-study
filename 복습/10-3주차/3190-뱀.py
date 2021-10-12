import sys
from collections import deque


directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def direction_change(d, c): # 위 오른쪽 아래 왼쪽
    if c == 'L':
        return (d-1) % 4
    elif c == 'D':
        return (d+1) % 4


def solve():
    d = 1
    time = 0
    x, y = 0, 0
    v = deque()
    v.append((x, y))
    while True:
        x = x + directions[d][0]
        y = y + directions[d][1]
        if 0 <= x < n and 0 <= y < n and board[x][y] != 2:
            if board[x][y] == 0:
                tail_x, tail_y = v.popleft()
                board[tail_x][tail_y] = 0
            board[x][y] = 2
            v.append((x, y))
            if time in times:
                d = direction_change(d, times[time])
            time += 1
        else:
            return time


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    board = [[0] * n for _ in range(n)]
    k = int(sys.stdin.readline())
    for _ in range(k):
        r, c = map(int, sys.stdin.readline().split())
        board[r - 1][c - 1] = 1
    l = int(sys.stdin.readline())
    times = {}
    for _ in range(l):
        t, d = map(str, sys.stdin.readline().split())
        times[int(t)] = d
    print(solve())