def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                return False
            elif stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    return len(stack) == 0