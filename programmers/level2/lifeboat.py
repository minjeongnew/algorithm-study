def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start, end = 0, len(people)-1
    while start <= end:
        answer +=1 # 80 70 70 50 10
        if people[start] + people[end] <= limit:
            end -= 1
        start += 1
    return answer


# 다른 방법
def solution2(people, limit):
    answer = len(people) # 전체 사람 수
    start, end = 0, len(people) - 1
    while start < end:
        if people[start] + people[end] <= limit:
            answer -= 1 # 짝이 지어지면 answer에서 -1하기
            end -= 1
        start += 1
    return answer

if __name__ == '__main__':
    p1, l1 = [70, 50, 80, 50], 100
    p2, l2 = [70, 80, 50], 100
    print(solution(p1, l1))
    print(solution(p2, l2))