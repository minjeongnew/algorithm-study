def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(rank, parent, node_u, node_v):
    root1 = find(parent, node_u)
    root2 = find(parent, node_v)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(parent, rank, node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    rank = dict()
    parent = dict()
    for v in graph['vertices']:
        make_set(parent, rank, v)
    # 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()
    mst = list()
    for edge in edges:
        weight, node_u, node_v = edge
        if find(parent, node_u) != find(parent, node_v):
            union(rank, parent, node_u, node_v)
            mst.append(edge)
    return mst


if __name__ == "__main__":
    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'edges': [
            (7, 'A', 'B'),
            (5, 'A', 'D'),
            (7, 'B', 'A'),
            (8, 'B', 'C'),
            (9, 'B', 'D'),
            (7, 'B', 'E'),
            (8, 'C', 'B'),
            (5, 'C', 'E'),
            (5, 'D', 'A'),
            (9, 'D', 'B'),
            (7, 'D', 'E'),
            (6, 'D', 'F'),
            (7, 'E', 'B'),
            (5, 'E', 'C'),
            (7, 'E', 'D'),
            (8, 'E', 'F'),
            (9, 'E', 'G'),
            (6, 'F', 'D'),
            (8, 'F', 'E'),
            (11, 'F', 'G'),
            (9, 'G', 'E'),
            (11, 'G', 'F')
        ]
    }
    print(kruskal(graph))