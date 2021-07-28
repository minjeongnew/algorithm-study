def solution(n, money):
    dp = [1] + [0]*n
    for c in money:
        for p in range(c, n+1):
            if p >= c:
                dp[p] += dp[p-c]
    return dp[n]%1000000007