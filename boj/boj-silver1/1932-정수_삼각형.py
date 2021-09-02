import sys
from pprint import pprint


n = int(sys.stdin.readline())
t = []
for i in range(n):
    tmp = [0] + list(map(int, sys.stdin.readline().split())) + [0] * (n-i-1)
    t.append(tmp)
for i in range(1, n):
    for j in range(1, n+1):
        t[i][j] += max(t[i-1][j], t[i-1][j-1])
print(max(t[-1]))
