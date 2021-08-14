def solution(n, s):
    # 원소 간 차이가 적을 수록 원소의 곱이 최대가 댐
    if n > s:
        return [-1]
    d = s // n
    mod = s % n
    answer = [d] * n
    idx = -1 # 리스트의 끝의 원소에서부터 1 증가
    while mod:
        answer[idx] += 1
        idx -= 1
        mod -= 1
    return answer