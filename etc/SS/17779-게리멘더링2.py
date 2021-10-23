n = int(input())
populations = [[0]*(n+1) for _ in range(n+1)]
total = 0
from pprint import pprint
for i in range(n):
    tmp = list(map(int, input().split()))
    total += sum(tmp)
    for j in range(n):
        populations[i+1][j+1] = tmp[j]
# print(populations)

board = [[0]*(n+1) for _ in range(n+1)]


def solve(x, y, d1, d2):
    tmp = [[0]*(n+1) for _ in range(n+1)]

    tmp[x][y] = 5
    for i in range(1, d1+1):
        tmp[x+i][y-i] = 5
    for i in range(1, d2+1):
        tmp[x+i][y+i] = 5
    for i in range(1, d2+1):
        tmp[x+d1+i][y-d1+i] = 5
    for i in range(1, d1+1):
        tmp[x+d2+i][y+d2-i] = 5

    people = [0] * 5
    # 1번 선거구
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if tmp[i][j] == 5:
                break
            else:
                tmp[i][j] = 1
                people[0] += populations[i][j]
    # 2번 선거구
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if tmp[i][j] == 5:
                break
            else:
                tmp[i][j] = 2
                people[1] += populations[i][j]
    # 3번 선거구
    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if tmp[i][j] == 5:
                break
            else:
                tmp[i][j] = 3
                people[2] += populations[i][j]

    # 4번 선거구
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if tmp[i][j] == 5:
                break
            else:
                tmp[i][j] = 4
                people[3] += populations[i][j]

    # 5번 선거구
    people[4] = total - sum(people)
    # pprint(tmp)
    # print(people)
    return max(people) - min(people)


answer = float('inf')
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if x + d1 + d2 <= n and 1 <= y-d1 < y and y - d1 < y + d2 <= n:
                    answer = min(answer, solve(x, y, d1, d2))
print(answer)