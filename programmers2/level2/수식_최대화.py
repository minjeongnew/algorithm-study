from itertools import permutations


def calc(exp, op, idx):
    if exp.isdigit():
        return str(exp)
    else:
        if op[idx] == "*":
            split_data = exp.split("*")
            tmp = []
            for x in split_data:
                tmp.append(calc(x, op, idx+1))
            return str(eval("*".join(tmp)))
        if op[idx] == "+":
            split_data = exp.split("+")
            tmp = []
            for x in split_data:
                tmp.append(calc(x, op, idx + 1))
            return str(eval("+".join(tmp)))
        if op[idx] == "-":
            split_data = exp.split("-")
            tmp = []
            for x in split_data:
                tmp.append(calc(x, op, idx + 1))
            return str(eval("-".join(tmp)))


def solution(expression):
    answer = 0
    operations = list(permutations(["*", "+", "-"], 3))
    for op in operations:
        result = abs(int(calc(expression, op, 0)))
        if answer < result:
            answer = result

    return answer


if __name__ == "__main__":
    e = "100-200*300-500+20"
    print(solution(e))