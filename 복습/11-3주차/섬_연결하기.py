def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, n1, n2):
    r1 = find(parent, n1)
    r2 = find(parent, n2)
    if rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r1] = r2
        if parent[r1] == parent[r2]:
            rank[r2] += 1


def solve(n, costs):
    mst = list()
    edges = list()
    parent = {i:i for i in range(n)}
    rank = {i:0 for i in range(n)}
    for a, b, w in costs:
        edges.append((w, a, b))
        edges.append((w, b, a))

    edges.sort(key=lambda x:x[2])
    for edge in edges:
        w, x, y = edge
        if find(parent, x) != find(parent, y):
            union(parent, rank, x, y)
            mst.append(edge)
    return sum(x[2] for x in mst)
