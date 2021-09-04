import sys

n = int(input())
tmp = list(map(int, sys.stdin.readline().split()))
p = [[tall+1, value] for tall, value in enumerate(tmp)]
answer = [0]*(n)
for tall, value in p:
    cnt = 0
    for i in range(n):
        if answer[i] == 0 and cnt == value:
            answer[i] = tall
            break
        elif answer[i] == 0:
            cnt += 1

print(*answer)

