def solution(money):
    # 첫번째 집 들림
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = dp1[0]
    for idx in range(2, len(money) - 2):
        dp1[idx] = max(dp1[idx-1], dp1[idx-2] + money[idx])
    v1 = max(dp1)
    # 첫번째 집 안 들림
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    for idx in range(2, len(money) - 1):
        dp2[idx] = max(dp2[idx-1], dp2[idx-2] + money[idx])
    v2 = max(dp2)
    return max(v1, v2)