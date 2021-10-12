from itertools import permutations


def calc(op, idx, exp):
    answer = []
    if exp.isdigit():
        return str(exp)
    if op[idx] == "*":
        tmp = exp.split("*")
        for x in tmp:
            result = calc(op, idx+1, x)
            answer.append(result)
        return str(eval('*'.join(answer)))
    elif op[idx] == "+":
        tmp = exp.split("+")
        for x in tmp:
            result = calc(op, idx+1, x)
            answer.append(result)
        return str(eval("+".join(answer)))
    elif op[idx] == "-":
        tmp = exp.split("-")
        for x in tmp:
            result = calc(op, idx+1, x)
            answer.append(result)
        return str(eval("-".join(answer)))


def solution(expression):
    operation = list(permutations(["*", "+", "-"], 3))
    answers = []
    for op in operation:
        answers.append(abs(int(calc(op, 0, expression))))
    return max(answers)


if __name__ == "__main__":
    print(solution("100-200*300-500+20"))