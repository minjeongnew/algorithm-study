def solution(array, commands):
    answer = []
    for x in commands:
        start = x[0]-1
        end = x[1]
        k = x[2]-1
        answer.append(sorted(array[start:end])[k])

    return answer