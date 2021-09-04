import sys

n = int(sys.stdin.readline())
cards = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (n+1)
# 1 -> 10
# 2 -> 10 + 10 or dp[2] -> 20
# 3 -> dp[2] + dp[1]  or dp[3] -> 28
# 4 -> dp[2] + dp[2] = 40 or dp[3] + dp[1] or dp[4]
# 5 -> dp[4] + dp[1] or dp[3] + dp[2] or dp[5]
# 6 -> dp[5] + dp[1] or dp[4] + dp[2] or dp[3] + dp[3] or dp[6]
dp[1] = cards[1]
if n > 1:
    dp[2] = max(dp[1] + dp[1], cards[2])
for i in range(3, n+1):
    dp[i] = cards[i]
    for j in range(1, n//2+1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[n])