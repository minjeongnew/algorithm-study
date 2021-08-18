def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(rank, parent, node_u, node_v):
    root_u = find(parent, node_u)
    root_v = find(parent, node_v)
    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_u] = root_v
        if rank[root_u] == rank[root_v]:
            rank[root_v] += 1


def make_set(parent, rank, node):
    parent[node] = node
    rank[node] = 0


def solution(n, costs):
    parent = {}
    rank = {}
    edges = []
    for i, j, cost in costs:
        edges.append([i, j, cost])
        edges.append([j, i, cost])
    edges.sort(key=lambda x:x[2]) # cost 기준 정렬
    nodes = [i for i in range(n)]
    for node in nodes:
        make_set(parent, rank, node)
    mst = list()
    answer = 0
    for edge in edges:
        node_u, node_v, cost = edge
        if find(parent, node_u) != find(parent, node_v):
            union(rank, parent, node_u, node_v)
            mst.append(edge)
            answer += cost
    return answer


if __name__ == "__main__":
    n, c = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, c))