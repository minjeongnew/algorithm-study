# 문제 조건 -> numbers의 원소는 0 이상 '1000 이하'이다.

def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x:x*3, reverse=True)
    return ''.join(numbers)