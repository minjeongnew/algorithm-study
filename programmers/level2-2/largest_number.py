def solution(n):
    n = list(map(str, n))
    n = sorted(n, key=lambda x:x*3, reverse=True)
    if n[0] == '0':
        return '0'

    return ''.join(n)


if __name__ == '__main__':
    n=[6, 10, 2]
    print(solution(n))
    n=[3, 30, 34, 5, 9]
    print(solution(n))
    n=[0,0,0,0]
    print(solution(n))