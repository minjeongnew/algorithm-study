import sys


def solve(a):
    answer = ''
    stack = []
    for x in a:
        if x.isalpha():
            answer += x
        elif x == "(":
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
        elif x == "*" or x == "/":
            while stack and (stack[-1] != '*' or stack[-1] != "/"):
                answer += stack.pop()
            stack.append(x)
        elif x == "+" or stack == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(x)

    while stack:
        answer += stack.pop()
    return answer

a = sys.stdin.readline()
print(solve(a))