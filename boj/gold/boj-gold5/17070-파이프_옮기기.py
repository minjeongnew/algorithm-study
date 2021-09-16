import sys
# from collections import deque
# bfs -> 시간초과

n = int(sys.stdin.readline())
pipes = {1:[(0, 1), (1, 1)],
         2:[(1, 0), (1, 1)],
         3:[(0, 1), (1, 0), (1, 1)]}
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp =[[[0]*n for _ in range(n)] for __ in range(3)]
dp[0][0][1] = 1


for i in range(2, n):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
    for j in range(2, n):
        # 대각선
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[2][i][j] = dp[2][i-1][j-1] + dp[1][i-1][j-1] + dp[0][i-1][j-1]
        if board[i][j] == 0:
            # 가로
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
print(sum([dp[0][n-1][n-1], dp[1][n-1][n-1], dp[2][n-1][n-1]]))