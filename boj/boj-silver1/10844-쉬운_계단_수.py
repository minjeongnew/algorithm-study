import sys

# 1 -> 1, 2, 3, 4, 5, 6, 7, 8, 9
# 2 -> 10, 12, 21, 23, 32, 34,
# 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98

# 3 -> 10 + 1
# 12 + 1 or 3
n = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    # 계단 끝이 0으로 끝나는 경우
    dp[i][0] = dp[i-1][1]
    # 계단 끝이 9로 끝나는 경우
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
answer = sum(dp[n])
answer %= 1000000000
print(answer)