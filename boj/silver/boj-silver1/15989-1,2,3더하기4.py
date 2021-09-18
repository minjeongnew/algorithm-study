import sys
# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 4 -> 1111 112 13 22
# 5 -> 11111 1112 113 122 23 -> 5
# 6 =>
n = int(sys.stdin.readline())
nlist = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0]*10001
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
for i in range(4, 10001):
    dp[i] = dp[i-1] + dp[i-2] - dp[i-3]
    if i % 3 == 0:
        dp[i] += 1
for x in nlist:
    print(dp[x])