from collections import deque
import sys

# 왼쪽으로
# 0 북 1 동 2 남 3 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change_direction(d):
    return (d - 1) % 4


def back_direction(d):
    return (d - 2) % 4


def solve(r, c, d):
    q = deque()
    q.append((r, c, d))
    board[r][c] = 2
    cnt = 1
    while q:
        x, y, direction = q.popleft()
        for i in range(4):
            direction = change_direction(direction)
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                cnt += 1
                q.append((nx, ny, direction))
                break
            if i == 3:
                nx = x + dx[back_direction(direction)]
                ny = y + dy[back_direction(direction)]
                q.append((nx, ny, direction))
                if board[nx][ny] == 1:
                    return cnt


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(solve(r, c, d))