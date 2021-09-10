import sys


parent = {}


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def make_set(node):
    parent[node] = node


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    if r1 == r2:
        return
    if r1 > r2:
        parent[r2] = r1
    else:
        parent[r1] = r2


n, m = map(int, sys.stdin.readline().split())
for i in range(1, n+1):
    make_set(i)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        union(b, c)
    elif a == 1:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')