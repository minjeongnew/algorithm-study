# silver 3
import sys
n = int(sys.stdin.readline())
ts = []
ps = []
dp = [0]*(n+1)
for i in range(n):
    ti, pi = map(int, sys.stdin.readline().split())
    ts.append(ti)
    ps.append(pi)


for i in range(n-1, -1, -1):
    if ts[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(ps[i] + dp[i+ts[i]], dp[i+1])

print(dp[0])