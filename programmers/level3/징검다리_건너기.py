def soultion(stones, k):
    cnt = 0
    answer = 0
    lt = 1
    rt = max(stones)
    while lt <= rt:
        blank_cnt = 0
        mid = (lt + rt) // 2 # 징검다리를 건너 수 있는 수
        for stone in stones:
            if stone - mid <= 0:
                blank_cnt += 1
            else:
                blank_cnt = 0
            if blank_cnt >= k:
                break
        if blank_cnt < k:
            lt = mid + 1
        else:
            answer = mid
            rt = mid - 1
    return answer