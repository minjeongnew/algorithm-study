import sys
sys.setrecursionlimit(10**6)


t = [0, 1, 2, 3] + [0] * 60000


def solution(n):
    if t[n]:
        return t[n] % 1000000007
    else:
        t[n] = solution(n-2) + solution(n-1)
        return t[n] % 1000000007


def solution2(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
        print(a,b)
    return a % 1000000007


if __name__ == '__main__':
    n = 5
    print(solution2(n))