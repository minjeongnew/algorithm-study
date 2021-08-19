def solution(sticker):
    ls = len(sticker)
    # 0번째 포함
    dp1 = [0 for _ in range(ls)]
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    # 마지막 원소 포함 x
    for i in range(2, ls-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    v1 = max(dp1)
    # 0번째 포함 x
    dp2 = [0 for _ in range(ls)]
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, ls):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    v2 = max(dp2)
    return max(v1, v2)