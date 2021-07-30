def solution(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b

    return a%1234567


if __name__ == '__main__':
    print(solution(4))