def binary(n, val): # 이진수 str 만들기
    ans = [0]*n
    i = n - 1
    while i>=0:
        ans[i] = str(val%2)
        val//=2
        i-=1
    return ''.join(ans)


def cmp(v1, v2): # 두 수 비교 해 비밀지도 원소 구하기
    if v1!=v2:
        return '#'
    else:
        if v1 == '1':
            return '#'
        return ' '


def solution(n, arr1, arr2):
    answer = []

    for x, y in zip(arr1, arr2):
        x, y = binary(n, x), binary(n, y)
        tmp = ''
        for i, j in zip(x, y):
            tmp += cmp(i, j)
        answer.append(tmp)
    return answer


# 다른 사람 풀이
# bin 내장 함수
# rjust

def solution2(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:]) # | 비트 연산
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)

    return answer