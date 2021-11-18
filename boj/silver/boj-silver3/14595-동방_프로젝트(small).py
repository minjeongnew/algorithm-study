import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
rooms = [0]*(n+1)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, y):
        rooms[i] = 1
    # print(rooms)
answer = 0
for x in rooms[1:]:
    if x == 0:
        answer += 1

print(answer)