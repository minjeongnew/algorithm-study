from collections import deque

d = {0: (0, 1), 1: (1,0), 2: (-1, 0), 3: (0, -1)} # 오른쪽 위 아래 왼쪽

def solution(board):
    return min(bfs(board, (0, 0, 0, 0)), bfs(board, (0, 0, 1, 0)))


def bfs(board, start):
    start_x, start_y, start_head, start_cost = start
    q = deque()
    q.append(start)
    n = len(board)
    v = [[float('inf')*n for _ in range(n)]]
    v[start_x][start_y] = 0
    while q:
        x, y, cost, head = q.popleft()
        for k in range(4):
            nx = x + d[k]
            ny = y + d[k]
            if head == k:
                new_cost = cost + 100
            else:
                new_cost = cost + 600
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] < new_cost and board[nx][ny] == 0:
                q.append((nx, ny, k, new_cost))
                v[nx][ny] = new_cost
    return v[-1][-1]
