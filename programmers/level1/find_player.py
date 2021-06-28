from collections import Counter


# 파이썬 collections 모듈의 Counter 클래스 사용하면 리스트끼리 빼기가 가능

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)

    return list(dict(answer).keys())[0]



# 2
# 내장 함수 zip 사용

# 각 객체가 담고 있는 원소를 tuple 형태로 차례로 접근 가능하게 함
# a = ['1', '2', '3']
# b = ['4', '5', '6']
# for i in zip(a, b):
#     print(i)
# 출력
# ('1', '4')
# ('2', '5')
# ('3', '6')


def solution2(par, com):
    par.sort() # 리스트 내장 함수 sort()
    com.sort()

    for p, c in zip(par, com):
        if p!=c:
            return p
    return par[-1]


