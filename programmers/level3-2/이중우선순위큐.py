import heapq


def solution(operations):
    q = []
    for op in operations:
        if op == 'D -1':
            if q:
                heapq.heappop(q)
        elif op == 'D 1':
            if q:
                q.pop(-1)
        else:
            t1, n1 = map(str, op.split())
            heapq.heappush(q, int(n1))
    q.sort()
    if len(q) == 0:
        return [0, 0]
    elif len(q) == 1:
        return [q[0]]*2
    else:
        return [q[-1], q[0]]