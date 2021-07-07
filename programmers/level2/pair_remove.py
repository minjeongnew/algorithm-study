def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    return 1 if len(stack) == 0 else 0


def solution2(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else len(stack) > 0:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    return 1 if len(stack) == 0 else 0
