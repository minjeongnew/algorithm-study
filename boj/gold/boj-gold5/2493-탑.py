import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
answer = []
stack = []
for idx, v in enumerate(top):
    while stack:
        if stack[-1][1] > v:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([idx, v])
print(*answer)