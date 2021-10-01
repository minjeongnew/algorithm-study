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


def solution(n, costs):
    # 크루스칼 알고리즘
    mst = list()
    edges = list()
    parent = {x: x for x in range(n)}
    rank = {x: 0 for x in range(n)}
    for a, b, w in costs:
        edges.append([a, b, w])
        edges.append([b, a, w])
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        a, b, w = edge
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            mst.append(edge)
    return sum([x[2] for x in mst])


if __name__ == "__main__":
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(4, costs))