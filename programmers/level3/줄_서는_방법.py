import math


def solution(n, k):
    nl = [i for i in range(1, n+1)]
    answer = []
    while n:
        f = math.factorial(n-1)
        answer.append(nl.pop(k-1)//f)
        n -= 1
        k %= f
    return answer