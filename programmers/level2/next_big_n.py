# 이진수 변환시 1의 개수를 리턴해주는 함수
def bin_one(n):
    ans = 0
    while n:
        if n%2 == 1:
            ans += 1
        n //= 2
    return ans


def solution(n):
    next = n # n 다음 숫자
    n_ones = bin_one(n) # n 이진수 변환시 1의 개수
    while True:
        next += 1
        next_ones = bin_one(next)
        if n_ones == next_ones:
            return next

