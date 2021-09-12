import sys

v, e = map(int, sys.stdin.readline().split())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]
parent = {x+1:x+1 for x in range(v)}
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
    l.sort(key=lambda x: x[2])

    for x in l:
        a, b, w = x
        if find(a) != find(b):
            union(a, b)
            mst.append(x)
    return mst

answer = kruskal()
print(sum([x[2] for x in answer]))