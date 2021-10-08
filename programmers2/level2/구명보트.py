def solution(people, limit):
    # 정렬, 그리디
    answer = 0
    start, end = 0, len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
    return answer