def solution(money):
    if len(money) <= 2:
        return max(money)
    # dp1: 0번째를 포함
    dp1 = [0 for _ in range(len(money))]
    dp1[0] = money[0]
    dp1[1] = dp1[0]
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    tmp1 = max(dp1)
    # dp2: 0번째 포함 x
    dp2 = [0 for _ in range(len(money))]
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    tmp2 = max(dp2)
    return max(tmp1, tmp2)

# print(dp1)
# print(dp2)
# [1, 1, 4, 0]
# [0, 2, 3, 3]