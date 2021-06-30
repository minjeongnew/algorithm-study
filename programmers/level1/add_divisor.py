def divsior(n):
    answer =0
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            if n//i != i:
                answer +=2
            else:
                answer +=1
    if answer%2==0:
        return True
    return False


def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        if divsior(x):
            answer+=x
        else:
            answer-=x

    return answer



# 제곱수의 약수의 개수는 혹수 임을 이용한 간단한 코딩
def solution2(left, right):
    answer =0
    for x in range(left, right+1):
        if int(x**0.5) == x**0.5:
            answer -= x
        else:
            answer += x

    return answer