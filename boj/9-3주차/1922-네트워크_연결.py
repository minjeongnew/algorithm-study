import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
parent = {node: node for node in range(1, n+1)}


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
    graph.sort(key=lambda x: x[2])
    for e in graph:
        a, b, w = e
        if find(a) != find(b):
            union(a, b)
            mst.append(e)
    return mst


result = kruskal()
print(sum([x[2] for x in result]))