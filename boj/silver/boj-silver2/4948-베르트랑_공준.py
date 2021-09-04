import sys, math


primes = [True] * (123456*2 + 1)
def prime(n):
    end = int(math.sqrt(2*n+1))
    for i in range(2, end+1):
        if primes[i]:
            for j in range(i+i, 2*n + 1, i):
                primes[j] = False


def cnt(n):
    answer = 0
    for i in range(n+1, 2*n+1):
        if primes[i]:
            answer += 1
    return answer

a = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        a.append(n)
prime(max(a))
for x in a:
    print(cnt(x))