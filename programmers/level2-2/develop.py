import math


def solution(progresses, speeds):
    answer = []
    works = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    print(works)
    front = 0
    for i in range(1, len(works)):
        if works[front] < works[i]:
            answer.append(i-front)
            front = i
    answer.append(len(works)-front)
    return answer


if __name__ == '__main__':
    p = [95, 90, 99, 99, 80, 99]
    s = [1, 1, 1, 1, 1, 1]
    print(solution(p, s))
    # 정답 [1, 3, 2]