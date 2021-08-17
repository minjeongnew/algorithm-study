import sys
from collections import deque


def bfs(board, start):
    q = deque([start])
    ln = len(board)
    v = [[sys.maxsize]*ln for _ in range(ln)]
    v[0][0] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, cost, head = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if head != idx:
                new_cost = cost + 600
            else:
                new_cost = cost + 100
            if 0 <= nx < ln and 0 <= ny < ln and v[nx][ny] > new_cost and board[nx][ny] == 0:
                v[nx][ny] = new_cost
                q.append((nx, ny, new_cost, idx))
    return v[-1][-1]


def solution(board):
    return min(bfs(board, (0,0,0,1)), bfs(board, (0,0,0,2)))


if __name__ == "__main__":
    b = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    print(solution(b))