from collections import deque
import sys


def bfs(board, start):
    q = deque([start])
    n = len(board)
    v = [[sys.maxsize]*n for _ in range(n)]
    v[0][0] = 0
    # 방향, 위: 0, 오른쪽: 1, 아래: 2, 왼쪽:3
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, cost, head = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if head != i:
                new_cost = cost + 600
            else:
                new_cost = cost + 100
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and new_cost < v[nx][ny]:
                v[nx][ny] = new_cost
                q.append((nx, ny, new_cost, i))
    return v[-1][-1]


def solution(board):
    return min(bfs(board, (0, 0, 0, 1)), bfs(board, (0, 0, 0, 2)))


if __name__ == "__main__":
    b = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    print(solution(b))