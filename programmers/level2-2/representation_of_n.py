def solution(n):
    ans = 0
    for i in range(1, n+1):
        s = 0
        for j in range(i, n+1):
            s += j
            if s == n:
                ans += 1
                break
            if s > n:
                break
    return ans