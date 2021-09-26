import math


def solution(progresses, speeds):
    answer = []
    days = []
    for p, s in zip(progresses, speeds):
        tmp = math.ceil((100-p)/s)
        days.append(tmp)
    front = 0
    for i in range(1, len(days)):
        if days[front] < days[i]:
            answer.append(i-front)
            front = i
    answer.append(len(days)-front)

    return answer