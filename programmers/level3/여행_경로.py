def solution(tickets):
    routes = {}
    for s, d in tickets:
        routes[s] = routes.get(s, []) + [d]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    answer = []
    while stack:
        current = stack[-1]
        if current not in routes or len(routes[current]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[current].pop())
    return answer[::-1]


if __name__ == '__main__':
    t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(t))