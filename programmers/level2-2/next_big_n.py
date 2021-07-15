def solution(n):
    n1 = bin(n).count('1')
    st = n
    while True:
        st += 1
        if n1 == bin(st).count('1'):
            break
    return st