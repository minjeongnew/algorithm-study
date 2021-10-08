def solution(n):
    answer = 0
    bn = bin(n)[2:]
    ones = bn.count('1')
    # print(ones)
    # print(bn)
    while True:
        n += 1
        nbn = bin(n)[2:]
        if nbn.count('1') == ones:
            break
    return n