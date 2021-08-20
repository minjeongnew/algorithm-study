def solution(sticker):
    # 첫번째 스티커 포함
    dp1 = [0] * len(sticker)
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, len(sticker)-2):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    v = max(dp1)

    # 첫번째 스티커 포함 안 함
    dp2 = [0] * len(sticker)
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)-1):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    v2 = max(dp2)
    return max(v1, v2)