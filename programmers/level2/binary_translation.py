def solution(s):
    turn = 0
    zeros = 0
    while True:
        if len(s) == 0:
            break
        turn += 1
        ones = s.count('1')
        zeros += len(s) - ones
        s = bin(len(ones))[2:]
    return [turn, zeros]