def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else:
            bn = bin(n)[2:]
            bn = '0' + bn
            # 오른쪽에서부터 첫 '0' 찾기
            idx = bn.rfind('0')
            bn_list = list(bn)
            bn_list[idx] = '1'
            bn_list[idx+1] = '0'
            answer.append(int(''.join(bn_list), 2))
    return answer


if __name__ == '__main__':
    ns = [2, 7]
    print(solution(ns))