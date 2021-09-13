# 에라토스테네체 -> 메모리 초과
# dfs
import sys

n = int(sys.stdin.readline())
primes = ['2', '3', '5', '7']


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def solve(x):
    if len(str(x)) == n: # 깊이
        print(x)
        return
    for i in range(10):
        tmp = int(x) * 10 + i
        if is_prime(tmp):
            solve(tmp)


for x in primes:
    solve(x)