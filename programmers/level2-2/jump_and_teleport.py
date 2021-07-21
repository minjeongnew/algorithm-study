def solution(n):
    answer = 0
    while n:
        if n % 2:
            answer += 1
            n -= 1
        else:
            n //= 2

    return answer


if __name__ == '__main__':
    print(solution(5000))
