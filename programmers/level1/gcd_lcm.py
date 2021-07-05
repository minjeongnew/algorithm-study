def gcd(x, y):
    k = min(x, y)
    for i in range(k+1, 0, -1):
        if x%i == 0 and y%i == 0:
            return i


def lcm(x, y):
    k = max(x, y)
    for i in range(k, x*y+1):
        if i%x == 0 and i%y ==0:
            return i


def solution(n, m):
    return [gcd(n,m), lcm(n,m)]