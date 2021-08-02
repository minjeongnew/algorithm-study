def solution(price, money, count):
    answer = sum([i*price for i in range(1, count+1)])
    return answer - money if answer > money else 0


if __name__ == '__main__':
    print(solution(3, 20, 4))