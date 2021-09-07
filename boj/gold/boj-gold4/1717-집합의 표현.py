import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
# union-find 를 이용


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


parent = [i for i in range(n+1)]
for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')