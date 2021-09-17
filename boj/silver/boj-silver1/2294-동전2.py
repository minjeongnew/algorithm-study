import sys

n, k = map(int, sys.stdin.readline().split())
coins = sorted([int(sys.stdin.readline()) for _ in range(n)])
dp = [20001] * (k+1)
dp[0] = 0
for i in range(1, k+1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)

print(dp[k] if dp[k] != 20001 else -1)