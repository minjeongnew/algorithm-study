def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(rank, parent, n1, n2):
    r1 = find(parent, n1)
    r2 = find(parent, n2)
    if rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r2] += 1


def solution(n, costs):
    mst = list()
    parent = {x: x for x in range(n)}
    rank = {x: 0 for x in range(n)}
    costs.sort(key=lambda x:x[2])
    for cost in costs:
        n1, n2, w = cost
        if find(parent, n1) != find(parent, n2):
            union(rank, parent, n1, n2)
            mst.append(cost)
    return sum([x[2] for x in mst])

if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))