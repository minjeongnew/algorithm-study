# 크루스칼 알고리즘 사용할거임
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(rank, parent, n1, n2):
    r1 = parent[n1]
    r2 = parent[n2]
    if rank[r1] > rank[r2]:
        rank[r2] = r1
    else:
        rank[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r1] += 1


def make_set(parent, rank, node):
    parent[node] = node
    rank[node] = 0


def solution(n, costs):
    parent = {}
    rank = {}
    edges = []
    for i, j, weight in costs:
        edges.append([i, j, weight])
        edges.append([j, i, weight])
    edges.sort(key=lambda x: x[2]) # weight 기준 정렬하기
    ns = [i for i in range(n)]
    for x in ns:
        make_set(parent, rank, x)
    mst = []
    answer = 0
    for edge in edges:
        n1, n2, weight = edge
        if find(parent, n1) != find(parent, n2):
            union(rank, parent, n1, n2)
            mst.append(edge)
            answer += edge[2]

    return answer