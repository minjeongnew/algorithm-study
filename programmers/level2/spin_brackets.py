#
def check(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        elif stack[-1] == '(':
            if x == ')':
                stack.pop()
            else:
                stack.append(x)
        elif stack[-1] == '[':
            if x == ']':
                stack.pop()
            else:
                stack.append(x)
        elif stack[-1] == '{':
            if x == '}':
                stack.pop()
            else:
                stack.append(x)
    return False if stack else True


def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:]+s[:i]):
            answer += 1
    return answer