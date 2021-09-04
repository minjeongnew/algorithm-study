import sys

t = int(sys.stdin.readline())
ns = []
max_n = 0
for _ in range(t):
    n = int(sys.stdin.readline())
    ns.append(n)
    if max_n < n:
        max_n = n
dp = [0, 1, 1] + [0]*(max_n-2)
for i in range(3, max_n+1):
    dp[i] = dp[i-3] + dp[i-2]
for n in ns:
    print(dp[n])
