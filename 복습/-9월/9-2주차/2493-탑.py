import sys

n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []
for idx, top in enumerate(tops):
    while stack:
        if stack[-1][1] > top:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append((idx, top))
print(*answer)