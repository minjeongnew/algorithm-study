import heapq
from collections import defaultdict


def prim(start_node, edges):
    mst = list()
    adjacent_edge = defaultdict(list)
    connected_nodes = set(start_node)
    for weight, n1, n2 in edges:
        adjacent_edge[n1].append((weight, n1, n2))
        adjacent_edge[n2].append((weight, n2, n1))
    candidate_edge_list = adjacent_edge[start_node]
    heapq.heapify(candidate_edge_list)
    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            mst.append((weight, n1, n2))
            connected_nodes.add(n2)
            for edge in adjacent_edge[n2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edge_list, edge)
    return mst


if __name__ == "__main__":
    edges = [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (5, 'C', 'E'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (11, 'F', 'G')
    ]
    print(prim('A', edges))