from collections import deque
from pprint import pprint
n, q = map(int, input().split())
N = 2**n
# 얼음들 양
board = [list(map(int, input().split())) for _ in range(N)]
levels = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def go():
    global board
    for level in levels:
        new_board = [[0]*N for _ in range(N)]
        for i in range(0, N, 2**level):
            for j in range(0, N, 2**level):
                for k in range(2**level):
                    for l in range(2**level):
                        new_board[i+l][2**level+j-1-k] = board[i+k][j+l]
                        # print(k+i, l+j, '->', i+l, 2**level+j-1-k)
        board =[[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and new_board[nx][ny] > 0:
                        cnt+= 1
                if new_board[i][j] > 0:
                    if cnt < 3:
                        board[i][j] = new_board[i][j] - 1
                    else:
                        board[i][j] = new_board[i][j]

# 얼음 덩어리 면적 세기
def bfs():
    answers = [(0, 0)]
    ice_sum = 0
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ice_sum += board[i][j]
            if board[i][j] and v[i][j] == 0:
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                area = board[i][j]
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and board[nx][ny] != 0:
                            v[nx][ny] = 1
                            cnt += 1
                            area += board[nx][ny]
                            q.append((nx, ny))
                answers.append((area, cnt))
    # print(answers)
    return ice_sum, sorted(answers, reverse=True)[0][1]

go()
answer = bfs()
print(answer[0])
print(answer[1])