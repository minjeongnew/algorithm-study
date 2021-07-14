import sys
sys.setrecursionlimit(10**6)


f = [0, 1] + [0] * (100000)


def solution(n):
    if n == 0:
        return f[0]
    elif n == 1:
        return f[1]
    elif f[n] > 0:
        return f[n]
    else:
        f[n] = solution(n-2) + solution(n-1)
        return f[n]


if __name__ == '__main__':
    print(solution(5))