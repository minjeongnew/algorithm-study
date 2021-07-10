from itertools import permutations


def prime(p, n):
    for i in range(2, n+1):
        if p[i]:
            for j in range(i*2, n+1, i):
                p[j] = False


def solution(n):
    nl = sorted(list(n), reverse=True)
    max_ = int(''.join(nl))
    p = [False, False] + [True]*(max_+1)
    prime(p, max_)
    r = []
    for i in range(1, len(nl)+1):
        tmp = list(permutations(nl, i))
        for j in tmp:
            r.append(''.join(j))
    r = list(set(map(int, r)))
    answer = 0
    print(r)
    for x in r:
        if p[x]:
            answer += 1
    return answer


if __name__ == '__main__':
    n = '011'
    print(solution(n))