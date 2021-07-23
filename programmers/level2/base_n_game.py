import sys
sys.setrecursionlimit(10**6)


num_list = '0123456789ABCDEF'


def base_n(n, number):
    if number < n:
        return num_list[number]
    else:
        r = number % n
        return base_n(n, number//n) + num_list[r]


def solution(n, t, m, p):
    answer = ''
    flag = 0
    turn = 0
    n_list = []
    for i in range(t*m+1):
        tmp = base_n(n, i)
        for x in tmp:
            n_list.append(x)
    while True:
        if flag == t:
            break
        if turn % m + 1 == p:
            flag += 1
            answer += n_list[turn]
        turn += 1
    return answer
