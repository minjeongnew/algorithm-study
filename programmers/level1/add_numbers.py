def solution(numbers):
    answer = []
    l = len(numbers)
    for i in range(l):
        for j in range(i+1, l):
            answer.append(numbers[i]+numbers[j])

    return sorted(list(set(answer))) # set-> 중복 제거