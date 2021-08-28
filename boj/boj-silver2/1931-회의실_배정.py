import sys

n = int(sys.stdin.readline())
meeting_rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
meeting_rooms = sorted(meeting_rooms, key=lambda x:(x[1], x[0]))
answer = 1
current = meeting_rooms[0]
for i in range(1, len(meeting_rooms)):
    if current[1] <= meeting_rooms[i][0]:
        answer += 1
        current = meeting_rooms[i]
print(answer)