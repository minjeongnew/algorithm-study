import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = []
parent = {}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((c, a, b))


def make_set(node):
    parent[node] = node


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    if r1 > r2:
        parent[r2] = r1
    else:
        parent[r1] = r2


def kruskal():
    mst = list()
    for i in range(1, n+1):
        make_set(i)
    graph.sort(key=lambda x:x[0])
    for x in graph:
        e, n1, n2 = x
        if find(n1) != find(n2):
            union(n1, n2)
            mst.append(x)
    return mst


mst = kruskal()
print(sum(x[0] for x in mst))