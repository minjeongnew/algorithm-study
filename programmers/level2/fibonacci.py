import sys
sys.setrecursionlimit(10**6)


f = [0, 1] + [0]*100000


def fibo(n):
    if n == 0:
        return f[0]
    if n == 1:
        return f[1]
    if f[n] > 0:
        return f[n]
    else:
        f[n] = (fibo(n-1) + fibo(n-2))%1234567
        return f[n]
