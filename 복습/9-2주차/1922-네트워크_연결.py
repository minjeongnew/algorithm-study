import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = {x+1:x+1 for x in range(n)}
graph = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))



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
    graph.sort(key=lambda x:x[2])
    for x in graph:
        a, b, c = x
        if find(a) != find(b):
            union(a, b)
            mst.append(x)
    return mst
result = kruskal()
print(sum([x[2] for x in result]))