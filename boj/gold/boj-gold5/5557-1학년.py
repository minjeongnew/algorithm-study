import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0]*21 for _ in range(n-1)]
dp[0][nums[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            prev = j
            next = nums[i]
            if 0 <= prev + next <= 20:
                dp[i][prev+next] += dp[i-1][prev]
            if 0 <= prev - next <= 20:
                dp[i][prev - next] += dp[i - 1][prev]

print(dp[n-2][nums[-1]])