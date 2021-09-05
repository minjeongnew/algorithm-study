import sys

s = sys.stdin.readline().rstrip()
exp_s = sys.stdin.readline().rstrip()
stack = []
for x in s:
    stack.append(x)
    if len(stack) >= len(exp_s) and ''.join(stack[-len(exp_s):]) == exp_s:
        idx = len(exp_s)
        while idx:
            stack.pop()
            idx -= 1

if not stack:
    print('FRULA')
else:
    print(''.join(stack))