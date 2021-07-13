def solution(number, k):
    stack = []
    flag = 0
    for i in number:
        if flag != k:
            while stack and stack[-1] < i:
                if flag == k:
                    break
                stack.pop()
                flag += 1
            stack.append(i)
        else:
            stack.append(i)
    return ''.join(stack)[:len(number)-k]


if __name__ == '__main__':
    n = '4177252841'
    k = 4
    print(solution(n, k))