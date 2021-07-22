def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else:
            bn = '0' + bin(n)[2:]
            # 오른쪽에서부터 0 찾기
            idx = bn.rfind(bn)
            bn = list(bn)
            bn[idx] = '1'
            bn[idx] = '0'
            answer.append(int(''.join(bn), 2))
    return answer