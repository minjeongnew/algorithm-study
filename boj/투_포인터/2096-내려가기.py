# 골드4
# 메모리 줄이는 방법
import sys


n = int(sys.stdin.readline())
dp = [[0]*3 for _ in range(2)]
dp2 = [[0]*3 for _ in range(2)]

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    dp[1][0] = max(dp[0][0], dp[0][1]) + tmp[0]
    dp[1][1] = max(dp[0][0], dp[0][1], dp[0][2]) + tmp[1]
    dp[1][2] = max(dp[0][1], dp[0][2]) + tmp[2]

    dp2[1][0] = min(dp2[0][0], dp2[0][1]) + tmp[0]
    dp2[1][1] = min(dp2[0][0], dp2[0][1], dp2[0][2]) + tmp[1]
    dp2[1][2] = min(dp2[0][1], dp2[0][2]) + tmp[2]

    dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]
    dp2[0][0], dp2[0][1], dp2[0][2] = dp2[1][0], dp2[1][1], dp2[1][2]
print(max(dp[1]), min(dp2[1]))