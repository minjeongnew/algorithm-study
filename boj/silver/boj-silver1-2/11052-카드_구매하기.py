n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = cards[i]
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
print(dp[n])

