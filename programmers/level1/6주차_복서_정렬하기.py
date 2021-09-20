def solution(weights, head2head):
    answer = []
    n = len(weights)
    for x in range(n):
        h = [i for i in range(n) if weights[x] < weights[i]] # 몸무게 더 나가는 사람들
        w = len([i for i in h if head2head[x][i] == "W"])
        r = 0 if head2head[x].count('N') == n else head2head[x].count('W') /(n-head2head[x].count('N'))
        answer.append((x+1, weights[x], r, w))
    answer.sort(key=lambda x: (-x[2], -x[3], -x[1], x[0]))
    return [-x[0] for x in answer]