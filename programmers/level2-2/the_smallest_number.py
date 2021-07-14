def solution(a, b):
    a.sort()
    b.sort(reverse=True)
    answer = sum([i*j for i, j in zip(a, b)])
    return answer