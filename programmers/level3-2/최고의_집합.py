def solution(n, s):
    if n > s:
        return [-1]
    div = s // n
    mod = s % n
    answer = [div] * n
    idx = -1
    while mod:
        answer[idx] += 1
        idx -= 1
        mod -= 1
    return answer