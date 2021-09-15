import sys

v, e = map(int, sys.stdin.readline().split())
parent = {node:node for node in range(1, v+1)}
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    if r1 == r2:
        return
    if r1 > r2:
        parent[r2] = r1
    else:
        parent[r1] = r2


def kruskal():
    mst = list()
    graph.sort(key=lambda x:x[2])
    for g in graph:
        a, b, v = g
        if find(a) != find(b):
            union(a, b)
            mst.append(g)
    return mst


result = kruskal()
print(sum([x[2] for x in result]))