import sys

answer = []


while True:
    stack = []
    cnt = 0
    s = sys.stdin.readline().rstrip()
    if '-' in s:
        break
    n = len(s)
    for i in range(n):
        if s[i] == "{":
            stack.append(s[i])
        elif stack and s[i] == "}":
            stack.pop()
        elif not stack and s[i] == "}":
            cnt += 1
            stack.append("{")
    answer.append(cnt+len(stack)//2)

for i, v in enumerate(answer):
    print("{}. {}".format(i+1, v))