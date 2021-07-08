from itertools import permutations


def prime(p, n):
    for i in range(2, n+1):
        if p[i]:
            for j in range(i*2, n+1, i):
                p[j] = False


def solution(numbers):
    answer = 0
    nl = sorted(list(numbers), reverse=True)
    # 가장 큰 수
    m = int(''.join(nl))
    p = [False, False] + [True]*m
    prime(p, m)

    a = []
    for i in range(1, len(numbers)+1):
        tmp = list(permutations(nl, i))
        for j in tmp:
            a.append(''.join(tmp))
    a = list(map(int, a))
    a = list(set(a))

    for x in a:
        if a[int(x)]:
            answer +=1
    return answer