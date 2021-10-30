from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dps = permutations(dungeons, len(dungeons))
    for di in dps:
        tmp = 0
        tmpk = k
        for x in di:
            if tmpk >= x[0]:
                tmp += 1
                tmpk -= x[1]
        if tmp > answer:
            answer = tmp
    return answer