import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        gap = graph[i][j]
        # 오른쪽으로
        if j + gap < n:
            dp[i][j+gap] += dp[i][j]
        # 아래로
        if i + gap < n:
            dp[i+gap][j] += dp[i][j]
print(dp[-1][-1])