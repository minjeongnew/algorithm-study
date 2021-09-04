import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    if dp[i] == 0:
        dp[i] = 1
    for j in range(n):
        if a[i] > a[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

print(max(dp))
# LIS (DP)