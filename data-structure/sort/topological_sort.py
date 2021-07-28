
def topological_sort(graph):
    answer = []
    stack = []
    n = len(graph)
    v = [0 for _ in range(n)]
    for g in graph:
        if v[g] == 0:
            dfs(g, stack, v, graph)

    while len(stack):
        answer.append(stack.pop())
    return answer

def dfs(v, stack, visited, graph):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, stack, visited, graph)
    stack.append(v)


if __name__ == '__main__':
    graph = {0: [1, 2, 3], 1: [4], 2: [4, 5], 3: [], 4:[6], 5:[1], 6: []}
    print(topological_sort(graph))
