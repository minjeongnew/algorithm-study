import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
dp = [1] + [0]*k
for c in coins:
    for i in range(1, k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]
print(dp[-1])