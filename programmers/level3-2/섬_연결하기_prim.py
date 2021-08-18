from collections import defaultdict
import heapq
import sys


def prim(edges, start_node):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
    connected_nodes = set()
    connected_nodes.add(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapq.heapify(candidate_edge_list)
    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            mst.append((weight, n1, n2))
            connected_nodes.add(n2)
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edge_list, edge)
    return mst


def solution(n, costs):
    answer = sys.maxsize
    answers = []
    nodes = [i for i in range(n)]
    edges = []
    for n1, n2, weight in costs:
        edges.append((weight, n1, n2))
    for node in nodes:
        answers.append(prim(edges, node))
    for a in answers:
        answer = min(answer, sum([x[0] for x in a]))
    return answer


if __name__ == "__main__":
    n, c = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, c))