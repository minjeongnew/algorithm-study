from itertools import permutations


def calc(op, idx, exp):
    if exp.isdigit():
        return str(exp)
    if op[idx] == "*":
        split_data = exp.split("*")
        tmp = []
        for s in split_data:
            tmp.append(calc(op, idx+1, s))
        return str(eval("*".join(tmp)))
    if op[idx] == "+":
        split_data = exp.split("+")
        tmp = []
        for s in split_data:
            tmp.append(calc(op, idx+1, s))
        return str(eval("+".join(tmp)))
    if op[idx] == "-":
        split_data = exp.split("-")
        tmp = []
        for s in split_data:
            tmp.append(calc(op, idx+1, s))
        return str(eval("-".join(tmp)))


def solution(expression):
    answer = 0
    operations = list(permutations(['*', '+', '-'], 3))
    for op in operations:
        result = abs(int(calc(op, 0, expression)))
        if result > answer:
            answer = result
    return answer

if __name__ == '__main__':
    e = "100-200*300-500+20"
    print(solution(e))