def solution(n):
    answer = ''
    while n > 0:
        remain = n % 3
        if remain == 0:
            answer += '4'
        else:
            answer += '124'[n % 3-1]
        n -= 1
        # 예) n=3 일 때 몫 이 1
        # 몫이 있으면 연산을 한 번 더 하게 됨
        n //= 3

    return answer[::-1]


if __name__ == '__main__':
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(9))