import math


def solution(progresses, speeds):
    answer = []
    stack = []
    # 걸리는 시간
    for p, s in zip(progresses, speeds):
        t = math.ceil((100-p)/s)
        stack.append(t)

    front = 0
    for i in range(1, len(stack)):
        if stack[front] < stack[i]:
            stack.append(i-front)
            front = i
    answer.append(len(stack)-front)
    return answer