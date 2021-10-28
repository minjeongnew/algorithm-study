import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

stack = []
cnt = 0
answer = 0
for i in range(m):
    if s[i] == "I":
        stack.append(i)

for i in range(1, len(stack)):
    if stack[i] - stack[i-1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= n:
        answer += 1
print(answer)
