import math


def solution(n, k):
    answer = []
    ns = [i for i in range(1, n+1)]
    while n:
        f = math.factorial(n-1)
        answer.append(ns.pop((k-1)//f))
        n -= 1
        k %= f
    return answer
