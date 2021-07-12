def solution(n, k):
    stack = []
    flag = 0
    for i in n:
        if flag != k:
            while stack and stack[-1] < i:
                if flag == k:
                    break
                stack.pop()
                flag += 1
            stack.append(i)
        else:
            stack.append(i)

    return ''.join(stack)[len(n)-k]


if __name__ == '__main__':
    n1, k1 = "1924", 2
    n2, k2 = "1231234", 3
    n3, k3 = "4177252841", 4

    print(solution(n1, k1))
    print(solution(n2, k2))
    print(solution(n3, k3))
